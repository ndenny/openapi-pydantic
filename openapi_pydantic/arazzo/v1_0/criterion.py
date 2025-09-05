from typing import Optional, Union

from pydantic import BaseModel

from openapi_pydantic.compat import PYDANTIC_V2, ConfigDict, Extra

from .criterion_expression import CriterionExpression

_examples = [
    {
        "condition": "$statusCode == 200"
    },
    {
        "context": "$statusCode",
        "condition": "^200$",
        "type": "regex"
    },
    {
        "context": "$response.body",
        "condition": "$[?count(@.pets) > 0]",
        "type": "jsonpath"
    }
]


class Criterion(BaseModel):

    context: Optional[str]
    condition: str
    type: Optional[Union[str, CriterionExpression]]

    if PYDANTIC_V2:
        model_config = ConfigDict(
            extra="allow",
            json_schema_extra={"examples": _examples},
        )

    else:

        class Config:
            extra = Extra.allow
            schema_extra = {"examples": _examples}
