import re

import json

def parse_input(text: str) -> dict:
    spec = {"endpoints": []}

    # Try parsing as JSON first (OpenAPI/Swagger)
    try:
        data = json.loads(text)
        if "paths" in data:
            for path, methods in data["paths"].items():
                for method, details in methods.items():
                    if method.lower() in ["get", "post", "put", "delete"]:
                        spec["endpoints"].append({
                            "method": method.upper(),
                            "path": path,
                            "raw_text": json.dumps(details) # Keep context for inference
                        })
            return spec
    except json.JSONDecodeError:
        pass

    # Fallback to Regex for text/markdown
    matches = re.findall(r"(GET|POST|PUT|DELETE)\s+(/[a-zA-Z0-9/_\-{}]+)", text)
    for method, path in matches:
        spec["endpoints"].append({
            "method": method,
            "path": path,
            "raw_text": text
        })

    return spec
