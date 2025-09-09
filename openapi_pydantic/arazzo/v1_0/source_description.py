from typing import Literal

from pydantic import BaseModel, Field

from openapi_pydantic.compat import PYDANTIC_V2, ConfigDict, Extra

from .uri_reference import UriReference

_examples = [
    {
        "name": "petStoreDescription",
        "url": "https://github.com/swagger-api/swagger-petstore/blob/master/src/main/resources/openapi.yaml",
        "type": "openapi"
    }
]

class SourceDescription(BaseModel):
    """A description of the source of the API definition."""

    name: str = Field(format='^[A-Za-z0-9_\\-]+$')
    """
    **REQUIRED**. The name of the source.
    """

    url: UriReference
    """
    **REQUIRED**. The URL of the source.
    """

    type: Literal["openapi", "arazzo"]
    """
    The type of the source (e.g., `openapi`, `arazzo`).
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
