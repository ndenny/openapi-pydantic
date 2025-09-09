from typing import Optional

from pydantic import BaseModel

from openapi_pydantic.compat import PYDANTIC_V2, ConfigDict, Extra

from .failure_action import FailureAction
from .json_schema import JsonSchema
from .output_key import OutputKey
from .parameter import Parameter
from .success_action import SuccessAction

_examples = []


class Components(BaseModel):
    """Holds a set of reusable objects for different aspects of the Arazzo Specification."""

    inputs: Optional[dict[OutputKey, JsonSchema]] = None
    """
    An object to hold reusable JSON Schema 2020-12 schemas to be referenced from workflow inputs
    """

    parameters: Optional[dict[OutputKey, Parameter]] = None
    """
    An object to hold reusable Parameter Objects
    """

    successActions: Optional[dict[OutputKey, SuccessAction]] = None
    """
    An object to hold reusable Success Actions Objects
    """

    failureActions: Optional[dict[OutputKey, FailureAction]] = None
    """
    An object to hold reusable Failure Actions Objects
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
