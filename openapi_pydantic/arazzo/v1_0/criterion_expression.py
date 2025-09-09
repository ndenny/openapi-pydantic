from typing import Literal

from pydantic import BaseModel

from openapi_pydantic.compat import PYDANTIC_V2, ConfigDict, Extra

_examples = [
    {"type": "jsonpath", "version": "draft-goessner-dispatch-jsonpath-00"},
    {"type": "xpath", "version": "xpath-30"},
]


class CriterionExpression(BaseModel):
    """An object used to describe the type and version of an expression used within a Criterion Object."""

    type: Literal["jsonpath", "xpath"]
    """
    The type of condition to be applied
    """

    version: Literal[
        "draft-goessner-dispatch-jsonpath-00", "xpath-10", "xpath-20", "xpath-30"
    ]
    """
    A short hand string representing the version of the expression type
    """

    # TODO only allow xpath types for xpath and jsonpath types for jsonpath

    if PYDANTIC_V2:
        model_config = ConfigDict(
            extra="allow",
            json_schema_extra={"examples": _examples},
        )

    else:

        class Config:
            extra = Extra.allow
            schema_extra = {"examples": _examples}
