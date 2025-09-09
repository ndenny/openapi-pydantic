from typing import Literal, Optional

from pydantic import BaseModel, Field

from openapi_pydantic.compat import PYDANTIC_V2, ConfigDict, Extra

_examples = [
    {"name": "username", "in": "query", "value": "$inputs.username"},
    {"name": "X-Api-Key", "in": "header", "value": "$inputs.x-api-key"},
]

ValueTypes = str | int | float | bool | dict | list | None


class Parameter(BaseModel):
    """Describes a single step parameter."""

    name: str
    """
    The name of the parameter
    """

    param_in: Optional[Literal["query", "header", "path", "cookie"]] = Field(
        default=None, alias="in"
    )
    """
    The named location of the parameter
    """

    value: ValueTypes
    """
    The value to pass in the parameter
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
