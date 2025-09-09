from openapi_pydantic.arazzo.v1_0 import Arazzo
from openapi_pydantic.compat import PYDANTIC_V2


def test_arazzo_v1_0() -> None:
    with open("tests/data/arazzo_v1.0.0.json") as f:
        if PYDANTIC_V2:
            validate = getattr(Arazzo, "model_validate_json")  # noqa: B009
        else:
            validate = getattr(Arazzo, "parse_raw")  # noqa: B009
        open_api = validate(f.read())
    assert open_api
