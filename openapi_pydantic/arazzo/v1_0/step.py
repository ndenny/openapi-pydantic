from typing import Dict, List, Optional, Union

from pydantic import BaseModel, Field

from openapi_pydantic.compat import PYDANTIC_V2, ConfigDict, Extra

from .criterion import Criterion
from .failure_action import FailureAction
from .output_key import OutputKey
from .parameter import Parameter
from .request_body import RequestBody
from .reusable import Reusable
from .success_action import SuccessAction

_examples = [
    {
        "stepId": "loginStep",
        "description": "This step demonstrates the user login step",
        "operationId": "loginUser",
        "parameters": [
            {"name": "username", "in": "query", "value": "$inputs.username"},
            {"name": "password", "in": "query", "value": "$inputs.password"},
        ],
        "successCriteria": [{"condition": "$statusCode == 200"}],
        "outputs": {
            "tokenExpires": "$response.header.X-Expires-After",
            "rateLimit": "$response.header.X-Rate-Limit",
        },
    }
]


class Step(BaseModel):
    """Describes a single workflow step which MAY be a call to an
    API operation (OpenAPI Operation Object or another Workflow Object)
    """

    description: Optional[str] = None
    """
    A description of the step.
    [CommonMark syntax](https://spec.commonmark.org/) MAY be used for rich text
    representation.
    """

    stepId: str
    """**REQUIRED**. Unique string to represent the step. The stepId MUST be unique
    amongst all steps described in the workflow"""

    operationId: Optional[str] = None
    """
    The name of an existing, resolvable operation, as defined with a unique
    operationId and existing within one of the sourceDescriptions. The
    referenced operation will be invoked by this workflow step.
    """

    operationPath: Optional[str] = None
    """
    A reference to a Source Description Object combined with a JSON Pointer to
    reference an operation.
    """

    workflowId: Optional[str] = None
    """
    The workflowId referencing an existing workflow within the Arazzo
    Description.
    """

    parameters: Optional[List[Union[Parameter, Reusable]]] = None
    """
    A list of parameters that MUST be passed to an operation or workflow
    as referenced by operationId, operationPath, or workflowId.
    """

    requestBody: Optional[RequestBody] = None
    """
    The request body to pass to an operation as referenced by operationId or
    operationPath
    """

    successCriteria: Optional[List[Criterion]] = Field(
        default=None, unique_items=True, min_items=1
    )
    """
    A list of assertions to determine the success of the step
    """

    onSuccess: Optional[List[Union[SuccessAction, Reusable]]] = Field(
        default=None, unique_items=True
    )
    """
    An array of success action objects that specify what to do upon step success
    """

    onFailure: Optional[List[Union[FailureAction, Reusable]]] = Field(
        default=None, unique_items=True
    )
    """
    An array of failure action objects that specify what to do upon step failure
    """

    outputs: Optional[Dict[OutputKey, str]]
    """
    A map between a friendly name and a dynamic output value defined using a runtime
    expression
    """

    # TODO validation
    # @model_validator(mode='after')
    def check_one_of_workflow_or_op_set(self):
        """Ensures that exactly one of operationId, operationPath, or workflowId set."""
        if self.operationId:
            if self.operationPath or self.workflowId:
                raise ValueError(
                    "If operationId is set, operationPath and workflowId must not be set."
                )
        elif self.operationPath:
            if self.operationId or self.workflowId:
                raise ValueError(
                    "If operationPath is set, operationId and workflowId must not be set."
                )
        elif self.workflowId:
            if self.operationId or self.operationPath:
                raise ValueError(
                    "If workflowId is set, operationId and operationPath must not be set."
                )
        else:
            raise ValueError(
                "One of operationId, operationPath, or workflowId must be set."
            )
        return self

    # TODO validation 2 - if operationId or operationPath is set, parameters must
    # have "in" set.

    if PYDANTIC_V2:
        model_config = ConfigDict(
            extra="allow",
            json_schema_extra={"examples": _examples},
        )

    else:

        class Config:
            extra = Extra.allow
            schema_extra = {"examples": _examples}
