# Step 3.3: Retry / Backoff Generator
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
