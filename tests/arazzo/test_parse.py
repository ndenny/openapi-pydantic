from typing import Literal

import pytest

from openapi_pydantic.arazzo import v1_0
from openapi_pydantic.arazzo.parser import parse_obj


@pytest.mark.parametrize("version", ["1.0.0", "1.0.1"])
def test_parse_arazzo_obj_1_0(
    version: Literal["1.0.0", "1.0.1"],
) -> None:
    result = parse_obj(
        {
            "arazzo": version,
            "info": {"title": "foo", "version": "0.1.0"},
            "sourceDescriptions": [
                {
                    "name": "source-name",
                    "type": "openapi",
                    "url": "https://example.com/openapi.json",
                }
            ],
            "workflows": [
                {
                    "workflowId": "workflow-name",
                    "name": "workflow-name",
                    "description": "A description of the workflow",
                    "steps": [
                        {
                            "stepId": "loginStep",
                            "description": "This step demonstrates the user login step",
                            "operationId": "loginUser",
                            "parameters": [
                                {
                                    "name": "username",
                                    "param_in": "query",
                                    "value": "$inputs.username",
                                },
                                {
                                    "name": "password",
                                    "param_in": "query",
                                    "value": "$inputs.password",
                                },
                            ],
                            "successCriteria": [{"condition": "$statusCode == 200"}],
                            "outputs": {
                                "tokenExpires": "$response.header.X-Expires-After",
                                "rateLimit": "$response.header.X-Rate-Limit",
                            },
                        }
                    ],
                }
            ],
            "components": None,
        }
    )

    assert result == v1_0.Arazzo(
        arazzo=version,
        info=v1_0.Info(title="foo", version="0.1.0"),
        sourceDescriptions=[
            v1_0.SourceDescription(
                name="source-name",
                type="openapi",
                url="https://example.com/openapi.json",
            )
        ],
        workflows=[
            v1_0.Workflow(
                workflowId="workflow-name",
                name="workflow-name",
                description="A description of the workflow",
                steps=[
                    v1_0.Step(
                        stepId="loginStep",
                        description="This step demonstrates the user login step",
                        operationId="loginUser",
                        parameters=[
                            v1_0.Parameter(
                                name="username",
                                param_in="query",
                                value="$inputs.username",
                            ),
                            v1_0.Parameter(
                                name="password",
                                param_in="query",
                                value="$inputs.password",
                            ),
                        ],
                        successCriteria=[
                            v1_0.Criterion(condition="$statusCode == 200")
                        ],
                        outputs={
                            "tokenExpires": "$response.header.X-Expires-After",
                            "rateLimit": "$response.header.X-Rate-Limit",
                        },
                    )
                ],
            )
        ],
        components=None,
    )
