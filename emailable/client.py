import requests
from .response import Response
from .error import (ClientError, AuthError, PaymentRequiredError,
                    ResourceNotFoundError, RateLimitExceededError,
                    ServerUnavailableError)

class Client:

  def __init__(self, api_key=None):
    self.api_key = api_key
    self.base_url = 'https://api.emailable.com/v1/'

  def verify(self,
             email,
             smtp=True,
             accept_all=False,
             timeout=None,
             api_key=None,
             access_token=None):
    options = {
      'params': {
        'email': email,
        'smtp': str(smtp).lower(),
        'accept_all': str(accept_all).lower(),
        'timeout': timeout
      }
    }

    url = self.base_url + 'verify'
    return self.__request('get', url, options, api_key or access_token)

  def batch(self, emails, params={}, api_key=None, access_token=None):
    options = {
      'params': {
        **params
      },
      'json': {
        'emails': emails
      }
    }
    url = self.base_url + 'batch'
    return self.__request('post', url, options, api_key or access_token)

  def batch_status(self,
                   batch_id,
                   simulate=None,
                   api_key=None,
                   access_token=None):
    options = {
      'params': {
        'id': batch_id,
        'simulate': simulate
      }
    }

    url = self.base_url + 'batch'
    return self.__request('get', url, options, api_key or access_token)

  def account(self, api_key=None, access_token=None):
    url = self.base_url + 'account'
    return self.__request('get', url, {}, api_key or access_token)

  def __request(self, method, url, options, key_or_token):
    response = None
    options['headers'] = { 
      'Authorization': f'Bearer {key_or_token or self.api_key}'
    }
    try:
      response = requests.request(method, url, **options)
      response.raise_for_status()
      return Response(response)
    except requests.exceptions.RequestException as e:
      self.__handle_error(e, response)

  def __handle_error(self, e, response):
    status_code = response.status_code if response is not None else None
    message = response.json()['message'] if response is not None else None
    if status_code == 401 or status_code == 403:
      raise AuthError(message)
    elif status_code == 402:
      raise PaymentRequiredError(message)
    elif status_code == 404:
      raise ResourceNotFoundError(message)
    elif status_code == 429:
      raise RateLimitExceededError(message)
    elif status_code == 503:
      raise ServerUnavailableError(message)
    else:
      raise ClientError(status_code, message)
