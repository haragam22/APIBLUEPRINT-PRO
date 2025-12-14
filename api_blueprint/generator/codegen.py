import os

def _generate_errors_file(out_dir: str):
    content = """# Step 3.2: Error Class Generator
class APIError(Exception):
    pass

class ClientError(APIError):
    pass

class ServerError(APIError):
    pass

class RateLimitError(APIError):
    pass
"""
    with open(os.path.join(out_dir, "errors.py"), "w") as f:
        f.write(content)

def _generate_retry_policy(out_dir: str):
    content = """# Step 3.3: Retry / Backoff Generator
import time
import random
import requests
from .errors import APIError, ClientError, ServerError, RateLimitError

def requests_with_retry(method, url, **kwargs):
    max_retries = 3
    base_delay = 1.0
    
    for attempt in range(max_retries + 1):
        try:
            response = requests.request(method, url, **kwargs)
            
            if 200 <= response.status_code < 300:
                return response
                
            if response.status_code == 429:
                raise RateLimitError(f"429 Too Many Requests: {response.text}")
            elif 500 <= response.status_code < 600:
                raise ServerError(f"{response.status_code} Server Error: {response.text}")
            elif 400 <= response.status_code < 500:
                # Do not retry 4xx (except 429 which is handled above)
                raise ClientError(f"{response.status_code} Client Error: {response.text}")
                
            return response
            
        except (ServerError, RateLimitError) as e:
            if attempt == max_retries:
                raise e
                
            # Exponential backoff + jitter
            delay = (base_delay * (2 ** attempt)) + random.uniform(0, 1)
            time.sleep(delay)
            
        except requests.exceptions.RequestException as e:
            # Network errors
            if attempt == max_retries:
                raise APIError(f"Network error: {str(e)}")
            time.sleep(1)

    return None
"""
    with open(os.path.join(out_dir, "retry_policy.py"), "w") as f:
        f.write(content)

def _generate_kestra_template(out_dir: str):
    content = """# Step 3.4: Kestra Template Generator
id: api_blueprint_workflow
namespace: com.example.api

tasks:
  - id: api_call
    type: io.kestra.plugin.core.http.Request
    uri: "https://example.com/api"
    method: POST
    retry:
      type: constant
      interval: PT1S
      maxAttempt: 5
"""
    with open(os.path.join(out_dir, "kestra_template.yaml"), "w") as f:
        f.write(content)

def _generate_tests(spec: dict, out_dir: str):
    tests_dir = os.path.join(out_dir, "tests")
    os.makedirs(tests_dir, exist_ok=True)
    
    # Create empty init
    with open(os.path.join(tests_dir, "__init__.py"), "w") as f:
        pass

    for ep in spec["endpoints"]:
        suffix = ep["path"].replace("/", "_").strip("_")
        fname = f"test_{suffix}.py"
        func_name = f"post_{suffix}" if "post" in ep["method"].lower() else f"call_{suffix}"
        
        with open(os.path.join(tests_dir, fname), "w") as f:
            f.write("import pytest\n")
            f.write("import requests_mock\n")
            f.write("from .. import api_client\n\n")
            
            f.write("@pytest.fixture\n")
            f.write("def mock_api():\n")
            f.write("    with requests_mock.Mocker() as m:\n")
            f.write("        yield m\n\n")
            
            f.write(f"def test_{func_name}_success(mock_api):\n")
            f.write(f"    endpoint = 'https://example.com{ep['path']}'\n")
            f.write(f"    mock_api.{ep['method'].lower()}(endpoint, json={{'status': 'ok'}}, status_code=200)\n")
            f.write(f"    payload = {{}}\n")
            f.write(f"    response = api_client.{func_name}(payload)\n")
            f.write(f"    assert response.status_code == 200\n")
            f.write(f"    assert mock_api.called\n\n")

            f.write(f"def test_{func_name}_retry(mock_api):\n")
            f.write(f"    endpoint = 'https://example.com{ep['path']}'\n")
            f.write(f"    mock_api.{ep['method'].lower()}(endpoint, [\n")
            f.write(f"        {{'status_code': 500}},\n")
            f.write(f"        {{'status_code': 200}}\n")
            f.write(f"    ])\n")
            f.write(f"    payload = {{}}\n")
            f.write(f"    response = api_client.{func_name}(payload)\n")
            f.write(f"    assert response.status_code == 200\n")
            f.write(f"    assert mock_api.call_count == 2\n")

def generate_sdk(spec: dict, out_dir: str):
    os.makedirs(out_dir, exist_ok=True)
    
    # Create package init
    with open(os.path.join(out_dir, "__init__.py"), "w") as f:
        pass
    
    # Generate helper files
    _generate_errors_file(out_dir)
    _generate_retry_policy(out_dir)
    _generate_kestra_template(out_dir)
    _generate_tests(spec, out_dir)

    # Generate API Client
    fname = "api_client.py"
    path = os.path.join(out_dir, fname)

    with open(path, "w") as f:
        f.write("from .retry_policy import requests_with_retry\n")
        f.write("from .errors import APIError, ClientError, ServerError, RateLimitError\n\n")
        
        for ep in spec["endpoints"]:
            # Basic function name derivation
            suffix = ep["path"].replace("/", "_").strip("_")
            func_name = f"post_{suffix}" if "post" in ep["method"].lower() else f"call_{suffix}"
            
            f.write(f"def {func_name}(payload):\n")
            f.write("    # Step 3.3: Uses retry wrapper\n")
            f.write(f"    return requests_with_retry('{ep['method']}', 'https://example.com{ep['path']}', json=payload)\n\n")
