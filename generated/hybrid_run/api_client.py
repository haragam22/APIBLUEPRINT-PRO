from .retry_policy import requests_with_retry
from .errors import APIError, ClientError, ServerError, RateLimitError

def post_pet_{petId}_uploadImage(payload):
    # Step 3.3: Uses retry wrapper
    return requests_with_retry('POST', 'https://example.com/pet/{petId}/uploadImage', json=payload)

def post_pet(payload):
    # Step 3.3: Uses retry wrapper
    return requests_with_retry('POST', 'https://example.com/pet', json=payload)

def call_pet(payload):
    # Step 3.3: Uses retry wrapper
    return requests_with_retry('PUT', 'https://example.com/pet', json=payload)

def call_pet_findByStatus(payload):
    # Step 3.3: Uses retry wrapper
    return requests_with_retry('GET', 'https://example.com/pet/findByStatus', json=payload)

def call_pet_findByTags(payload):
    # Step 3.3: Uses retry wrapper
    return requests_with_retry('GET', 'https://example.com/pet/findByTags', json=payload)

def call_pet_{petId}(payload):
    # Step 3.3: Uses retry wrapper
    return requests_with_retry('GET', 'https://example.com/pet/{petId}', json=payload)

def post_pet_{petId}(payload):
    # Step 3.3: Uses retry wrapper
    return requests_with_retry('POST', 'https://example.com/pet/{petId}', json=payload)

def call_pet_{petId}(payload):
    # Step 3.3: Uses retry wrapper
    return requests_with_retry('DELETE', 'https://example.com/pet/{petId}', json=payload)

def call_store_inventory(payload):
    # Step 3.3: Uses retry wrapper
    return requests_with_retry('GET', 'https://example.com/store/inventory', json=payload)

def post_store_order(payload):
    # Step 3.3: Uses retry wrapper
    return requests_with_retry('POST', 'https://example.com/store/order', json=payload)

def call_store_order_{orderId}(payload):
    # Step 3.3: Uses retry wrapper
    return requests_with_retry('GET', 'https://example.com/store/order/{orderId}', json=payload)

def call_store_order_{orderId}(payload):
    # Step 3.3: Uses retry wrapper
    return requests_with_retry('DELETE', 'https://example.com/store/order/{orderId}', json=payload)

def post_user_createWithList(payload):
    # Step 3.3: Uses retry wrapper
    return requests_with_retry('POST', 'https://example.com/user/createWithList', json=payload)

def call_user_{username}(payload):
    # Step 3.3: Uses retry wrapper
    return requests_with_retry('GET', 'https://example.com/user/{username}', json=payload)

def call_user_{username}(payload):
    # Step 3.3: Uses retry wrapper
    return requests_with_retry('PUT', 'https://example.com/user/{username}', json=payload)

def call_user_{username}(payload):
    # Step 3.3: Uses retry wrapper
    return requests_with_retry('DELETE', 'https://example.com/user/{username}', json=payload)

def call_user_login(payload):
    # Step 3.3: Uses retry wrapper
    return requests_with_retry('GET', 'https://example.com/user/login', json=payload)

def call_user_logout(payload):
    # Step 3.3: Uses retry wrapper
    return requests_with_retry('GET', 'https://example.com/user/logout', json=payload)

def post_user_createWithArray(payload):
    # Step 3.3: Uses retry wrapper
    return requests_with_retry('POST', 'https://example.com/user/createWithArray', json=payload)

def post_user(payload):
    # Step 3.3: Uses retry wrapper
    return requests_with_retry('POST', 'https://example.com/user', json=payload)

