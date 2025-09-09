from typing import Optional

from pydantic import BaseModel

from openapi_pydantic.compat import PYDANTIC_V2, ConfigDict, Extra

_examples = [
    {
        "title": "A pet purchasing workflow",
        "summary": "This Arazzo Description showcases the workflow for how to"
        " purchase apet through a sequence of API calls",
        "description": "This Arazzo Description walks you through the workflow"
        " and steps of `searching` for, `selecting`, and `purchasing` an"
        " available pet.",
        "version": "1.0.1"
    }
]

class Info(BaseModel):
    """The object provides metadata about API workflows.

    ... in this Arazzo Document.
    """

    title: str
    """
    **REQUIRED**. A human readable title of the Arazzo Description.
    """

    summary: Optional[str] = None
    """
    A short summary of the Arazzo Description.
    """

    description: Optional[str] = None
    """
    A description of the purpose of the workflows defined.
    [CommonMark syntax](https://spec.commonmark.org/) MAY be used for rich text
    representation.
    """

    version: str
    """
    **REQUIRED**. The version of the Arazzo document
    (which is distinct from the [Arazzo Specification version](#arazzoVersion)).
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
