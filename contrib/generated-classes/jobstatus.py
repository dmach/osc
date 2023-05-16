from typing import List
from typing import Type

from . import _base
from .build_arch import BuildArch


class Jobstatus(_base.ApiEndPointBase):
    pass

    _attributes: List[str] = ['code', 'result', 'details']
    _elements: List[str] = ['starttime', 'endtime', 'lastduration', 'workerid', 'hostarch', 'arch', 'uri', 'jobid', 'job', 'attempt']

    _code_is_optional: bool = True

    @property
    def code(self) -> str:
        return self._get_attribute("code")

    @code.setter
    def code(self, value: str):
        self._set_attribute("code", value)

    @code.deleter
    def code(self):
        self._delete_attribute("code")

    _result_is_optional: bool = True

    @property
    def result(self) -> str:
        """
        This attribute is present, if the package finished building. Then the
        status of the build result is available via it.
        """
        return self._get_attribute("result")

    @result.setter
    def result(self, value: str):
        self._set_attribute("result", value)

    @result.deleter
    def result(self):
        self._delete_attribute("result")

    _details_is_optional: bool = True

    @property
    def details(self) -> str:
        return self._get_attribute("details")

    @details.setter
    def details(self, value: str):
        self._set_attribute("details", value)

    @details.deleter
    def details(self):
        self._delete_attribute("details")
# {'optional': '1', 'doc': 'The unix time at which the build started.'}

    _starttime_is_optional: bool = True

    @property
    def starttime(self) -> str:
        """
        The unix time at which the build started.
        """
        return self._get_element("starttime")

    @starttime.setter
    def starttime(self, value: str):
        self._set_element("starttime", value)

    @starttime.deleter
    def starttime(self):
        self._delete_element("starttime")
# {'optional': '1', 'doc': 'The unix time at which the build finished.'}

    _endtime_is_optional: bool = True

    @property
    def endtime(self) -> str:
        """
        The unix time at which the build finished.
        """
        return self._get_element("endtime")

    @endtime.setter
    def endtime(self, value: str):
        self._set_element("endtime", value)

    @endtime.deleter
    def endtime(self):
        self._delete_element("endtime")
# {'optional': '1', 'doc': 'Time in seconds that the last build took.'}

    _lastduration_is_optional: bool = True

    @property
    def lastduration(self) -> str:
        """
        Time in seconds that the last build took.
        """
        return self._get_element("lastduration")

    @lastduration.setter
    def lastduration(self, value: str):
        self._set_element("lastduration", value)

    @lastduration.deleter
    def lastduration(self):
        self._delete_element("lastduration")
# {'optional': '1', 'doc': 'ID of the worker that is running this build'}

    _workerid_is_optional: bool = True

    @property
    def workerid(self) -> str:
        """
        ID of the worker that is running this build
        """
        return self._get_element("workerid")

    @workerid.setter
    def workerid(self, value: str):
        self._set_element("workerid", value)

    @workerid.deleter
    def workerid(self):
        self._delete_element("workerid")
# {'optional': '1', 'doc': 'Native architecture of the worker', 'ref': 'build-arch'}

    _hostarch_wrapper_class: Type = BuildArch
    _hostarch_is_optional: bool = True

    @property
    def hostarch(self) -> BuildArch:
        """
        Native architecture of the worker
        """
        return self._get_element("hostarch")

    @hostarch.setter
    def hostarch(self, value: BuildArch):
        self._set_element("hostarch", value)

    @hostarch.deleter
    def hostarch(self):
        self._delete_element("hostarch")
# {'optional': '1', 'doc': 'Architecture of the build', 'ref': 'build-arch'}

    _arch_wrapper_class: Type = BuildArch
    _arch_is_optional: bool = True

    @property
    def arch(self) -> BuildArch:
        """
        Architecture of the build
        """
        return self._get_element("arch")

    @arch.setter
    def arch(self, value: BuildArch):
        self._set_element("arch", value)

    @arch.deleter
    def arch(self):
        self._delete_element("arch")
# {'optional': '1', 'doc': 'internal URI to reachh the worker'}

    _uri_is_optional: bool = True

    @property
    def uri(self) -> str:
        """
        internal URI to reachh the worker
        """
        return self._get_element("uri")

    @uri.setter
    def uri(self, value: str):
        self._set_element("uri", value)

    @uri.deleter
    def uri(self):
        self._delete_element("uri")
# {'optional': '1', 'doc': 'internal md5 of this build job'}

    _jobid_is_optional: bool = True

    @property
    def jobid(self) -> str:
        """
        internal md5 of this build job
        """
        return self._get_element("jobid")

    @jobid.setter
    def jobid(self, value: str):
        self._set_element("jobid", value)

    @jobid.deleter
    def jobid(self):
        self._delete_element("jobid")
# {'optional': '1', 'doc': 'internal name of this build job'}

    _job_is_optional: bool = True

    @property
    def job(self) -> str:
        """
        internal name of this build job
        """
        return self._get_element("job")

    @job.setter
    def job(self, value: str):
        self._set_element("job", value)

    @job.deleter
    def job(self):
        self._delete_element("job")
# {'optional': '1', 'doc': 'number of attempts to build the job'}

    _attempt_is_optional: bool = True

    @property
    def attempt(self) -> str:
        """
        number of attempts to build the job
        """
        return self._get_element("attempt")

    @attempt.setter
    def attempt(self, value: str):
        self._set_element("attempt", value)

    @attempt.deleter
    def attempt(self):
        self._delete_element("attempt")
