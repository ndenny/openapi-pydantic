from typing import Dict, List, Optional, Union

from pydantic import BaseModel, Field

from openapi_pydantic.compat import PYDANTIC_V2, ConfigDict, Extra

from .failure_action import FailureAction
from .json_schema import JsonSchema
from .output_key import OutputKey
from .parameter import Parameter
from .reusable import Reusable
from .step import Step
from .success_action import SuccessAction

_examples = [
    {
        "workflowId": "loginUser",
        "summary": "Login User",
        "description": "This workflow lays out the steps to login a user",
        "inputs": {
            "type": "object",
            "properties": {
                "username": {"type": "string"},
                "password": {"type": "string"},
            },
        },
        "steps": [
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
        ],
        "outputs": {"tokenExpires": "$steps.loginStep.outputs.tokenExpires"},
    }
]

# 2. Define a TypeAdapter to validate individual keys later.
# output_key_validator = TypeAdapter(OutputKey)


class Workflow(BaseModel):
    """Describes the steps to be taken to achieve an objective.

    This may involve calling multiple APIs or performing a series of actions.
    """

    workflowId: str
    """
    **REQUIRED**. Unique string to represent the workflow. The id MUST be unique amongst
    all workflows described in the Arazzo Description.**
    """

    summary: Optional[str] = None
    """
    A summary of the purpose or objective of the workflow.
    """

    description: Optional[str] = None
    """
    A short description of the API.
    [CommonMark syntax](https://spec.commonmark.org/) MAY be used for rich text
    representation.
    """

    inputs: Optional[JsonSchema] = None
    """
    A JSON Schema 2020-12 object representing the input parameters used by this
    workflow.
    """

    dependsOn: Optional[List[str]] = Field(default=None, unique_items=True)
    """
    A list of workflow IDs that must be completed successfully before this workflow
    can be executed.
    """

    steps: List[Step] = Field(min_items=1, unique_items=True)
    """
    **REQUIRED**. An ordered list of steps where each step represents a call to an API
    operation or to another workflow.
    """

    successActions: Optional[List[Union[SuccessAction, Reusable]]] = Field(
        default=None, unique_items=True
    )
    """
    A list of success actions that are applicable for all steps described under this
    workflow.
    """

    failureActions: Optional[List[Union[FailureAction, Reusable]]] = Field(
        default=None, unique_items=True
    )
    """
    A list of failure actions that are applicable for all steps described under this
    workflow.
    """

    outputs: Optional[Dict[OutputKey, str]] = None
    """
    A map between a friendly name and a dynamic output value. The name MUST use keys
    that match the regular expression: `^[a-zA-Z0-9\\.\\-_]+$`.
    """

    parameters: Optional[List[Union[Parameter, Reusable]]] = Field(
        default=None, unique_items=True
    )
    """
    A list of parameters that are applicable for all steps described under this
    workflow.
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
