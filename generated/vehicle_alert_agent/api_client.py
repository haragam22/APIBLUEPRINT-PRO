from .retry_policy import requests_with_retry
from .errors import APIError, ClientError, ServerError, RateLimitError

def post_vehicles_alert(payload):
    # Step 3.3: Uses retry wrapper
    return requests_with_retry('POST', 'https://example.com/vehicles/alert', json=payload)

