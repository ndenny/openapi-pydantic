from typing import List, Optional

from pydantic import BaseModel

from openapi_pydantic.compat import PYDANTIC_V2, ConfigDict, Extra

from .criterion import Criterion

_examples = [
    {
        "name": "retryStep",
        "type": "retry",
        "retryAfter": 1,
        "retryLimit": 5,
        "criteria": [
            {
                "condition": "$statusCode == 503"
            }
        ]
    }
]

class FailureAction(BaseModel):

    name: str

    type: str

    workflowId: Optional[str]

    stepId: Optional[str]

    retryAfter: Optional[int | float]

    retryLimit: Optional[int]

    criteria: Optional[List[Criterion]]


    if PYDANTIC_V2:
        model_config = ConfigDict(
            extra="allow",
            json_schema_extra={"examples": _examples},
        )

    else:

        class Config:
            extra = Extra.allow
            schema_extra = {"examples": _examples}
