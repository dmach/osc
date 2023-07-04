# This file is partially auto-generated. Place any additional code below the 'AUTO-GENERATED' separator.


from typing import Optional
from typing import Tuple

from . import xmlmodel
from . import choices


class ConfigurationSchedulers(xmlmodel.Model):
    TAG_NAME = "schedulers"

    archs: Optional[Tuple[str]] = xmlmodel.TextNodeListField(
        "arch",
        choices=choices.BUILD_ARCH,
        optional=True,
    )

# AUTO-GENERATED: The code above is auto-generated. Place any additional code below this line.
