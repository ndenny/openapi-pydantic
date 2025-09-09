from typing import Literal, Optional, Union

from pydantic import BaseModel

from openapi_pydantic.compat import PYDANTIC_V2, ConfigDict, Extra

from .criterion_expression import CriterionExpression

_examples = [
    {"condition": "$statusCode == 200"},
    {"context": "$statusCode", "condition": "^200$", "type": "regex"},
    {
        "context": "$response.body",
        "condition": "$[?count(@.pets) > 0]",
        "type": "jsonpath",
    },
]


class Criterion(BaseModel):
    """An object used to specify the context, conditions, and condition types
    that can be used to prove or satisfy assertions specified in Step Object successCriteria,
    Success Action Object criteria, and Failure Action Object criteria
    """

    context: Optional[str] = None
    """
    A runtime expression used to set the context for the condition to be applied on
    """

    condition: str
    """
    The condition to apply
    """

    type: Optional[
        Union[Literal["simple", "regex", "jsonpath", "xpath"], CriterionExpression]
    ] = "simple"
    """
    The type of condition to be applied
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
