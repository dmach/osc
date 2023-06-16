import xml.sax.saxutils
from xml.etree import ElementTree as ET


def escape(string):
    """
    Escape the string so it's safe to use in XML and xpath.
    """
    entities = {
        "\"": "&quot;",
        "'": "&apos;",
    }
    if isinstance(string, bytes):
        return xml.sax.saxutils.escape(string.decode("utf-8"), entities=entities).encode("utf-8")
    return xml.sax.saxutils.escape(string, entities=entities)


def unescape(string):
    """
    Decode XML entities in the string.
    """
    entities = {
        "&quot;": "\"",
        "&apos;": "'",
    }
    if isinstance(string, bytes):
        return xml.sax.saxutils.unescape(string.decode("utf-8"), entities=entities).encode("utf-8")
    return xml.sax.saxutils.unescape(string, entities=entities)


def indent(root):
    """
    Indent XML so it looks pretty after printing or saving to file.
    """
    if hasattr(ET, "indent"):
        # ElementTree supports indent() in Python 3.9 and newer
        ET.indent(root)
    else:
        _indent_compat(root)


def _indent_compat(elem, level=0):
    """
    Indent XML on Python < 3.9.
    """
    i = "\n" + level * "  "
    if isinstance(elem, ET.ElementTree):
        elem = elem.getroot()
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + "  "
        for e in elem:
            _indent_compat(e, level + 1)
            if not e.tail or not e.tail.strip():
                e.tail = i + "  "
        if not e.tail or not e.tail.strip():
            e.tail = i
    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = i
