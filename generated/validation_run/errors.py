# Step 3.2: Error Class Generator
class APIError(Exception):
    pass

class ClientError(APIError):
    pass

class ServerError(APIError):
    pass

class RateLimitError(APIError):
    pass
