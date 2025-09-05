from typing import List, Optional

from pydantic import BaseModel

from openapi_pydantic.compat import PYDANTIC_V2, ConfigDict, Extra

from .criterion import Criterion

_examples = [
    {
        "name": "JoinWaitingList",
        "type": "goto",
        "stepId": "joinWaitingListStep",
        "criteria": [
            {
                "context": "$response.body",
                "condition": "$[?count(@.pets) > 0]",
                "type": "jsonpath"
            }
        ]
    }
]

class SuccessAction(BaseModel):

    name: str

    type: str

    workflowId: Optional[str]

    stepId: Optional[str]

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
