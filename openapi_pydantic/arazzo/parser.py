from typing import TYPE_CHECKING, Any, Union

from pydantic import BaseModel, Field

from openapi_pydantic.compat import PYDANTIC_V2

from .v1_0 import Arazzo as Arazzov1_0

Arazzov1 = Union[Arazzov1_0]

if TYPE_CHECKING:

    def parse_obj(data: Any) -> Arazzov1:
        """Parse a raw object into an Arazzo model with version inference."""
        ...

elif PYDANTIC_V2:
    from pydantic import RootModel

    class _Arazzo(RootModel):
        # Once v1_1 - add discriminator="arazzo")
        root: Arazzov1 = Field()

    def parse_obj(data: Any) -> Arazzov1:
        """Parse a raw object into an Arazzo model with version inference."""
        return _Arazzo.model_validate(data).root

else:

    class _Arazzo(BaseModel):
        # Once v1_1 - add discriminator="arazzo")
        __root__: Arazzov1 = Field()

    def parse_obj(data: Any) -> Arazzov1:
        """Parse a raw object into an Arazzo model with version inference."""
        return _Arazzo.parse_obj(data).__root__
