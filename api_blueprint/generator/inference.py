def infer_schema(spec: dict) -> dict:
    for ep in spec["endpoints"]:
        body = {}

        if "voltage" in ep["raw_text"]:
            body["voltage"] = {"type": "float"}

        if "engine_temp" in ep["raw_text"]:
            body["engine_temp"] = {
                "type": "float",
                "note": "assume Celsius"
            }

        ep["body"] = body
        ep["confidence"] = 0.7
        
        # Step 3.1: Error Code Extraction
        errors = []
        if "429" in ep["raw_text"]:
            errors.append("429")
        if "500" in ep["raw_text"] or "5xx" in ep["raw_text"]:
            errors.append("500")
        if "400" in ep["raw_text"] or "4xx" in ep["raw_text"]:
            errors.append("400")
            
        ep["errors"] = errors

    return spec
