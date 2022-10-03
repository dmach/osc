import errno
import os
import shutil
import subprocess

import behave


def makedirs(path):
    try:
        os.makedirs(path)
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise


def run(cmd, shell=True, cwd=None, env=None):
    """
    Run a command.
    Return exitcode, stdout, stderr
    """

    proc = subprocess.Popen(
        cmd,
        shell=shell,
        cwd=cwd,
        env=env,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        encoding="utf-8",
        universal_newlines=True,
        errors="surrogateescape",
    )

    stdout, stderr = proc.communicate()
    return proc.returncode, stdout, stderr


def check_exit_code(context):
    # check if the previous command finished successfully
    # or if the exit code was tested in a scenario
    if not getattr(context, "cmd", None):
        return

    if context.cmd_exitcode_checked:
        return

    the_exit_code_is(context, 0)


def run_in_context(context, cmd, can_fail=False, **run_args):
    check_exit_code(context)

    context.cmd = cmd

    if hasattr(context.scenario, "working_dir") and 'cwd' not in run_args:
        run_args['cwd'] = context.scenario.working_dir

    if hasattr(context.scenario, "PATH"):
        env = os.environ.copy()
        path = context.scenario.PATH
        env["PATH"] = path.replace("$PATH", env["PATH"])
        run_args["env"] = env

    if context.config.userdata.get("DEBUG", False):
        print(f"DEBUG: command: {cmd}")

    context.cmd_exitcode, context.cmd_stdout, context.cmd_stderr = run(cmd, **run_args)
    context.cmd_exitcode_checked = False

    if context.config.userdata.get("DEBUG", False):
        print(f"DEBUG: exit code: {context.cmd_exitcode}")
        print(f"DEBUG: stdout: {context.cmd_stdout}")
        print(f"DEBUG: stderr: {context.cmd_stderr}")

    if not can_fail and context.cmd_exitcode != 0:
        raise AssertionError('Running command "%s" failed: %s' % (cmd, context.cmd_exitcode))


@behave.step("stdout contains \"{text}\"")
def step_impl(context, text):
    if re.search(text.format(context=context), context.cmd_stdout):
        return
    raise AssertionError("Stdout doesn't contain: %s" % text)


@behave.step("stderr contains \"{text}\"")
def step_impl(context, text):
    if re.search(text.format(context=context), context.cmd_stderr):
        return
    raise AssertionError("Stderr doesn't contain: %s" % text)


@behave.step("stdout is")
def step_impl(context):
    expected = context.text.format(context=context).rstrip().split('\n')
    found = context.cmd_stdout.rstrip().split('\n')

    if found == expected:
        return

    expected_str = "\n".join(expected)
    found_str = "\n".join(found)
    raise AssertionError(f"Stdout is not:\n{expected_str}\n\nActual stdout:\n{found_str}")


@behave.step('I set working directory to "{path}"')
def step_impl(context, path):
    path = path.format(context=context)
    context.scenario.working_dir = path


@behave.step('I set PATH to "{path}"')
def step_impl(context, path):
    path = path.format(context=context)
    context.scenario.PATH = path


@behave.step('I copy file "{source}" to "{destination}"')
def step_impl(context, source, destination):
    # substitutions
    source = source.format(context=context)
    destination = destination.format(context=context)

    # if destination is a directory, append the source filename
    if destination.endswith("/"):
        destination = os.path.join(destination, os.path.basename(source))

    # copy file without attributes
    makedirs(os.path.dirname(destination))
    shutil.copyfile(source, destination)


@behave.step('file "{path}" exists')
def step_impl(context, path):
    path = path.format(context=context)
    if not os.path.isfile(path):
        raise AssertionError(f"File doesn't exist: {path}")


@behave.step('file "{path}" does not exist')
def step_impl(context, path):
    path = path.format(context=context)
    if os.path.isfile(path):
        raise AssertionError(f"File exists: {path}")


@behave.step('file "{one}" is identical to "{two}"')
def step_impl(context, one, two):
    one = one.format(context=context)
    two = two.format(context=context)
    data_one = open(one, "r").read()
    data_two = open(two, "r").read()
    if data_one != data_two:
        raise AssertionError(f"Files differ: {one} != {two}")


@behave.step('directory "{path}" exists')
def step_impl(context, path):
    path = path.format(context=context)
    if not os.path.isdir(path):
        raise AssertionError(f"Directory doesn't exist: {path}")


@behave.step('directory "{path}" does not exist')
def step_impl(context, path):
    path = path.format(context=context)
    if os.path.isdir(path):
        raise AssertionError(f"Directory exists: {path}")


@behave.step('I create file "{path}" with perms "{mode}"')
def step_impl(context, path, mode):
    path = path.format(context=context)
    mode = int(mode, 8)
    content = context.text.format(context=context).rstrip()

    makedirs(os.path.dirname(path))
    open(path, "w").write(content)
    os.chmod(path, mode)


@behave.step("the exit code is {exitcode}")
def the_exit_code_is(context, exitcode):
    if context.cmd_exitcode != int(exitcode):
        raise AssertionError(f"Command has exited with code {context.cmd_exitcode}: {context.cmd}")
    context.cmd_exitcode_checked = True


@behave.step('directory listing of "{path}" is')
def step_impl(context, path):
    path = path.format(context=context)
    expected = context.text.format(context=context).rstrip().split('\n')
    expected = [i for i in expected if i.strip()]
    found = os.listdir(path)

    expected = set(expected)
    found = set(found)

    if found == expected:
        return

    extra = sorted(set(found) - set(expected))
    missing = sorted(set(expected) - set(found))

    msg = []
    if extra:
        msg.append("Unexpected files found on disk:")
        for fn in extra:
            msg.append(f"  {fn}")
    if missing:
        msg.append("Files missing on disk:")
        for fn in missing:
            msg.append(f"  {fn}")

    msg = "\n".join(msg)

    raise AssertionError(f"Directory listing does not match:\n{msg}")


@behave.step('directory tree in "{path}" is')
def step_impl(context, path):
    path = path.format(context=context)
    path = os.path.abspath(path)
    expected = context.text.format(context=context).rstrip().split('\n')
    expected = [i for i in expected if i.strip()]

    found = []
    for root, dirs, files in os.walk(path):
        for fn in files:
            file_abspath = os.path.join(root, fn)
            file_relpath = file_abspath[len(path) + 1:]
            found.append(file_relpath)
#    found = os.listdir(path)

    expected = set(expected)
    found = set(found)

    if found == expected:
        return

    extra = sorted(set(found) - set(expected))
    missing = sorted(set(expected) - set(found))

    msg = []
    if extra:
        msg.append("Unexpected files found on disk:")
        for fn in extra:
            msg.append(f"  {fn}")
    if missing:
        msg.append("Files missing on disk:")
        for fn in missing:
            msg.append(f"  {fn}")

    msg = "\n".join(msg)

    raise AssertionError(f"Directory listing does not match:\n{msg}")
