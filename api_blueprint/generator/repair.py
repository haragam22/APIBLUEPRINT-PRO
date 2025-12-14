from datetime import datetime

def repair_schema(spec: dict) -> dict:
    for ep in spec["endpoints"]:
        repairs = []

        if "timestamp" not in ep["body"]:
            ep["body"]["timestamp"] = {
                "type": "string",
                "format": "iso8601",
                "default": datetime.utcnow().isoformat()
            }
            repairs.append("Added timestamp (ISO8601)")

        if "{id}" in ep["path"] or "vehicle" in ep["path"]:
            if "vehicle_id" not in ep["body"]:
                ep["body"]["vehicle_id"] = {
                    "type": "string",
                    "required": True,
                    "source": "path"
                }
                repairs.append("Inferred vehicle_id from endpoint path")

        ep["repairs_applied"] = repairs

    return spec
