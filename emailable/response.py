class Response:

  def __init__(self, response):
    self.status_code = response.status_code
    for key, value in response.json().items():
      setattr(self, key, value)
