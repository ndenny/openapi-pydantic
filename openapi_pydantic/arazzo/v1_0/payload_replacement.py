from typing import Any

from pydantic import BaseModel

from openapi_pydantic.compat import PYDANTIC_V2, ConfigDict, Extra

_examples = [
    {
        "target": "/petId",
        "value": "$inputs.pet_id"
    },
    {
        "target": "/quantity",
        "value": 10
    }
]


class PayloadReplacement(BaseModel):

    target: str
    value: Any

    if PYDANTIC_V2:
        model_config = ConfigDict(
            extra="allow",
            json_schema_extra={"examples": _examples},
        )

    else:

        class Config:
            extra = Extra.allow
            schema_extra = {"examples": _examples}
