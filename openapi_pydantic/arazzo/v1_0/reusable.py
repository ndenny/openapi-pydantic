from pydantic import BaseModel

from openapi_pydantic.arazzo.v1_0.parameter import ValueTypes
from openapi_pydantic.compat import PYDANTIC_V2, ConfigDict, Extra

_examples = [
    {"reference": "$components.successActions.notify"},
    {"reference": "$components.parameters.page", "value": 1},
]

ValueTypes = str | int | float | bool | dict | list | None


class Reusable(BaseModel):
    """A simple object to allow referencing of objects contained within the Components Object"""

    reference: str
    """
    A runtime expression used to reference the desired object
    """

    value: ValueTypes = None
    """
    Sets a value of the referenced parameter
    """

    if PYDANTIC_V2:
        model_config = ConfigDict(
            extra="allow",
            json_schema_extra={"examples": _examples},
        )

    else:

        class Config:
            extra = Extra.allow
            schema_extra = {"examples": _examples}
