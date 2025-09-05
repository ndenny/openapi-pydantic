
from pydantic import BaseModel

from openapi_pydantic.compat import PYDANTIC_V2, ConfigDict, Extra

_examples = [
    {
        "type": "jsonpath",
        "version": "draft-goessner-dispatch-jsonpath-00"
    },
    {
        "type": "xpath",
        "version": "xpath-30"
    }
]


class CriterionExpression(BaseModel):

    type: str

    version: str

    if PYDANTIC_V2:
        model_config = ConfigDict(
            extra="allow",
            json_schema_extra={"examples": _examples},
        )

    else:

        class Config:
            extra = Extra.allow
            schema_extra = {"examples": _examples}
