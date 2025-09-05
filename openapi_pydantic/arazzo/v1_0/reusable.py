from typing import Optional

from pydantic import BaseModel

from openapi_pydantic.compat import PYDANTIC_V2, ConfigDict, Extra

_examples = [

  {
    "reference": "$components.successActions.notify"
  },
  {
    "reference": "$components.parameters.page",
    "value": 1
  }
]


class Reusable(BaseModel):
    reference: str
    value: Optional[str]

    if PYDANTIC_V2:
        model_config = ConfigDict(
            extra="allow",
            json_schema_extra={"examples": _examples},
        )

    else:

        class Config:
            extra = Extra.allow
            schema_extra = {"examples": _examples}
