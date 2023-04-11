from apispec import APISpec
import json

spec = APISpec(
    title="LifeFoundry",
    version="1.0.0",
    openapi_version="3.0.2",
    info=dict(description="A minimal test API doc"),
)


spec.components.schema(
    "Service",
    {
        "properties": {
        "id": {"type": "integer", "format": "int64"},
        "name": {"type": "string"},
    }
    },
)

spec.path(
    path="/service/{service_id}",
    operations=dict(
        get=dict(
            responses={"200": {"content": {"application/json": {"schema": "Service"}}}}
        )
    ),
)

with open("./openAPI.json", "w") as outfile:
    json.dump(spec.to_dict(), outfile)