
from typing import TYPE_CHECKING

from openapi_pydantic.compat import PYDANTIC_V2

from .arazzo import Arazzo as Arazzo
from .components import Components as Components
from .criterion import Criterion as Criterion
from .criterion_expression import CriterionExpression as CriterionExpression
from .failure_action import FailureAction as FailureAction
from .info import Info as Info
from .json_schema import JsonSchema as JsonSchema
from .parameter import Parameter as Parameter
from .payload_replacement import PayloadReplacement as PayloadReplacement
from .request_body import RequestBody as RequestBody
from .reusable import Reusable as Reusable
from .source_description import SourceDescription as SourceDescription
from .step import Step as Step
from .success_action import SuccessAction as SuccessAction
from .workflow import Workflow as Workflow

if TYPE_CHECKING:
    pass
elif PYDANTIC_V2:
    # resolve forward references
    ...
else:
    # resolve forward references
    ...

__ALL__ = [
    "Arazzo",
    "Components",
    "CriterionExpression",
    "Criterion",
    "FailureAction",
    "Info",
    "JSONSchema",
    "Parameter",
    "PayloadReplacement",
    "RequestBody",
    "Reusable",
    "SourceDescription",
    "Step",
    "SuccessAction",
    "Workflow",
]
