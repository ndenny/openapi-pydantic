from typing import List, Literal, Optional

from pydantic import BaseModel, Field

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
                "type": "jsonpath",
            }
        ],
    }
]


class SuccessAction(BaseModel):
    """A single success action which describes an action to take upon success of a workflow step."""

    name: str
    """
    The name of the success action
    """

    type: Literal["goto", "end"]
    """
    The type of action to take
    """

    workflowId: Optional[str] = None
    """
    The workflowId referencing an existing workflow within the Arazzo description to
    transfer to upon success of the step
    """

    stepId: Optional[str] = None
    """
    The stepId to transfer to upon success of the step
    """

    criteria: Optional[List[Criterion]] = Field(default=None, unique_items=True)
    """
    A list of assertions to determine if this action SHALL be executed
    """

    # TODO add validation that goto actions have workflowId or stepId

    if PYDANTIC_V2:
        model_config = ConfigDict(
            extra="allow",
            json_schema_extra={"examples": _examples},
        )

    else:

        class Config:
            extra = Extra.allow
            schema_extra = {"examples": _examples}
