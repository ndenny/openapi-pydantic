from typing import Optional

from pydantic import BaseModel

from openapi_pydantic.compat import PYDANTIC_V2, ConfigDict, Extra

from .failure_action import FailureAction
from .json_schema import JsonSchema
from .parameter import Parameter
from .success_action import SuccessAction

_examples = [


]


class Components(BaseModel):
    inputs: Optional[dict[str, JsonSchema]]  # Schema Object
    parameters: Optional[dict[str, Parameter]]
    successActions: Optional[dict[str, SuccessAction]]
    failureActions: Optional[dict[str, FailureAction]]

    if PYDANTIC_V2:
        model_config = ConfigDict(
            extra="allow",
            json_schema_extra={"examples": _examples},
        )

    else:

        class Config:
            extra = Extra.allow
            schema_extra = {"examples": _examples}
