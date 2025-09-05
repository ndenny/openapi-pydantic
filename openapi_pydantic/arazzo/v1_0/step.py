
from typing import Dict, List, Optional, Union

from pydantic import BaseModel

from openapi_pydantic.compat import PYDANTIC_V2, ConfigDict, Extra

from .criterion import Criterion
from .failure_action import FailureAction
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
            {
                "name": "username",
                "in": "query",
                "value": "$inputs.username"
            },
            {
                "name": "password",
                "in": "query",
                "value": "$inputs.password"
            }
        ],
        "successCriteria": [
            {
                "condition": "$statusCode == 200"
            }
        ],
        "outputs": {
            "tokenExpires": "$response.header.X-Expires-After",
            "rateLimit": "$response.header.X-Rate-Limit"
        }
    }
]

class Step(BaseModel):

    description: Optional[str]
    """
    A description of the step.
    [CommonMark syntax](https://spec.commonmark.org/) MAY be used for rich text
    representation.
    """

    stepId: str
    """**REQUIRED**. Unique string to represent the step. The stepId MUST be unique
    amongst all steps described in the workflow"""

    operationId: Optional[str]
    """
    The name of an existing, resolvable operation, as defined with a unique
    operationId and existing within one of the sourceDescriptions. The
    referenced operation will be invoked by this workflow step.
    """

    operationPath: Optional[str]
    """
    A reference to a Source Description Object combined with a JSON Pointer to
    reference an operation.
    """

    workflowId: Optional[str]
    """
    The workflowId referencing an existing workflow within the Arazzo
    Description.
    """

    parameters: Optional[List[Union[Parameter, Reusable]]]
    """
    A list of parameters that MUST be passed to an operation or workflow
    as referenced by operationId, operationPath, or workflowId.
    """

    requestBody: Optional[RequestBody]

    successCriteria: Optional[List[Criterion]]

    onSuccess: Optional[List[Union[SuccessAction, Reusable]]]

    onFailure: Optional[List[Union[FailureAction, Reusable]]]

    outputs: Optional[Dict[str, str]]

    if PYDANTIC_V2:
        model_config = ConfigDict(
            extra="allow",
            json_schema_extra={"examples": _examples},
        )

    else:

        class Config:
            extra = Extra.allow
            schema_extra = {"examples": _examples}
