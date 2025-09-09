from pydantic import BaseModel

from openapi_pydantic.compat import PYDANTIC_V2, ConfigDict, Extra

_examples = [
    {"target": "/petId", "value": "$inputs.pet_id"},
    {"target": "/quantity", "value": 10},
]


class PayloadReplacement(BaseModel):
    """Describes a location within a payload (e.g., a request body) and a value to set
    within the location.
    """

    target: str
    """
    A JSON Pointer or XPath Expression which MUST be resolved against the request body
    """

    value: str
    """
     The value set within the target location
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
