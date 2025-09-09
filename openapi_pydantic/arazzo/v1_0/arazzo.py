from typing import List, Literal, Optional

from pydantic import BaseModel, Field

from openapi_pydantic.compat import PYDANTIC_V2, ConfigDict, Extra

from .components import Components
from .info import Info
from .source_description import SourceDescription
from .workflow import Workflow


class Arazzo(BaseModel):
    """This is the root document object of the Arazzo document."""

    arazzo: Literal["1.0.0", "1.0.1"]
    """
    **REQUIRED**. This string MUST be the version number of the Arazzo Specification
    that the Arazzo Description uses. The arazzo field MUST be used by tooling to
    interpret the Arazzo Description.
    """

    info: Info
    """
    **REQUIRED**. Provides metadata about the workflows contain within the Arazzo
    Description. The metadata MAY be used by tooling as required.
    """

    sourceDescriptions: List[SourceDescription] = Field(min_items=1, unique_items=True)
    """
    **REQUIRED**. A list of source descriptions (such as an OpenAPI description) this
    Arazzo Description SHALL apply to. The list MUST have at least one entry.
    """

    workflows: List[Workflow] = Field(min_items=1, unique_items=True)
    """
    **REQUIRED**. A list of workflows. The list MUST have at least one entry.
    """

    components: Optional[Components] = None
    """
    An element to hold various schemas for the Arazzo Description.
    """

    """
    This object /MAY/ be extended with Specification Extensions.
    """
    if PYDANTIC_V2:
        model_config = ConfigDict(
            extra="allow",
        )

    else:

        class Config:
            extra = Extra.allow
