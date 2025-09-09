from typing import Annotated

from pydantic import Field

OutputKey = Annotated[
    str,
    Field(
        pattern=r'^[a-zA-Z0-9\.\-_]+$'
    )
]
