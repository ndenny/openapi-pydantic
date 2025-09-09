from typing import List, Literal, Optional

from pydantic import BaseModel, Field

from openapi_pydantic.compat import PYDANTIC_V2, ConfigDict, Extra

from .criterion import Criterion

_examples = [
    {
        "name": "retryStep",
        "type": "retry",
        "retryAfter": 1,
        "retryLimit": 5,
        "criteria": [{"condition": "$statusCode == 503"}],
    }
]


class FailureAction(BaseModel):
    """A single failure action which describes an action to take upon failure of a workflow step."""

    name: str
    """
    The name of the failure action
    """

    type: Literal["retry", "goto", "end"]
    """
    The type of action to take
    """

    workflowId: Optional[str] = None
    """
    The workflowId referencing an existing workflow within the Arazzo description to
    transfer to upon failure of the step
    """

    stepId: Optional[str] = None
    """
    The stepId to transfer to upon failure of the step
    """

    retryAfter: Optional[int | float] = Field(default=None, ge=0)
    """
    A non-negative decimal indicating the seconds to delay after the step failure before
    another attempt SHALL be made
    """

    retryLimit: Optional[int] = Field(default=None, ge=0)
    """
    A non-negative integer indicating how many attempts to retry the step MAY be
    attempted before failing the overall step
    """

    criteria: Optional[List[Criterion]] = Field(default=None, unique_items=True)
    """
    A list of assertions to determine if this action SHALL be executed
    """

    # TODO add validation that goto actions have workflowId or stepId
    # TODO add validation that retry actions have retryAfter and optionally retryLimit

    if PYDANTIC_V2:
        model_config = ConfigDict(
            extra="allow",
            json_schema_extra={"examples": _examples},
        )

    else:

        class Config:
            extra = Extra.allow
            schema_extra = {"examples": _examples}
