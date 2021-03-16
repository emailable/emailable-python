class ClientError(Exception):
  pass

class AuthError(ClientError):
  pass

class PaymentRequiredError(ClientError):
  pass

class ResourceNotFoundError(ClientError):
  pass

class RateLimitExceededError(ClientError):
  pass

class ServerUnavailableError(ClientError):
  pass
