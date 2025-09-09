from typing import List, Optional

from pydantic import BaseModel, Field

from openapi_pydantic.compat import PYDANTIC_V2, ConfigDict, Extra

from .payload_replacement import PayloadReplacement

_examples = [
    {
        "contentType": "application/json",
        "payload": """
            "petOrder": {
                "petId": "{$inputs.pet_id}",
                "couponCode": "{$inputs.coupon_code}",
                "quantity": "{$inputs.quantity}",
                "status": "placed",
                "complete": false
            }
        """,
    },
    {
        "contentType": "application/json",
        "payload": {
            "petOrder": {
                "petId": "{$inputs.pet_id}",
                "couponCode": "{$inputs.coupon_code}",
                "quantity": "{$inputs.quantity}",
                "status": "placed",
                "complete": False,
            }
        },
    },
    {
        "contentType": "application/json",
        "payload": "$inputs.petOrderRequest",
    },
    {
        "contentType": "application/xml",
        "payload": """
            <petOrder>
                <petId>{$inputs.pet_id}</petId>
                <couponCode>{$inputs.coupon_code}</couponCode>
                <quantity>{$inputs.quantity}</quantity>
                <status>placed</status>
                <complete>false</complete>
            </petOrder>
        """,
    },
    {
        "contentType": "application/x-www-form-urlencoded",
        "payload": {
            "client_id": "$inputs.clientId",
            "grant_type": "$inputs.grantType",
            "redirect_uri": "$inputs.redirectUri",
            "client_secret": "$inputs.clientSecret",
            "code": "$steps.browser-authorize.outputs.code",
            "scope": "$inputs.scope",
        },
    },
    {
        "contentType": "application/x-www-form-urlencoded",
        "payload": "client_id={$inputs.clientId}&grant_type={$inputs.grantType}&redirect_uri={$inputs.redirectUri}&client_secret={$inputs.clientSecret}&code={$steps.browser-authorize.outputs.code}&scope={$inputs.scope}",  # noqa: E501
    },
]

PayloadTypes = str | dict | list | int | float | bool | None


class RequestBody(BaseModel):
    """The request body to pass to an operation as referenced by operationId or operationPath."""

    contentType: str
    """
    The Content-Type for the request content
    """

    payload: PayloadTypes

    replacements: Optional[List[PayloadReplacement]] = Field(
        default=None, unique_items=True
    )
    """
    A list of locations and values to set within a payload
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
