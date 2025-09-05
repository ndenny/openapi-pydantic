from typing import Literal

from pydantic import BaseModel

from openapi_pydantic.compat import PYDANTIC_V2, ConfigDict, Extra

_examples = [
    {
        "name": "petStoreDescription",
        "url": "https://github.com/swagger-api/swagger-petstore/blob/master/src/main/resources/openapi.yaml",
        "type": "openapi"
    }
]

class SourceDescription(BaseModel):
    """A description of the source of the API definition."""

    name: str
    """
    **REQUIRED**. The name of the source.
    """

    url: str
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
