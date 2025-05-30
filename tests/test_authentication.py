from unittest import TestCase
import emailable

class TestAuthentication(TestCase):

  def setUp(self):
    self.api_key = 'test_7aff7fc0142c65f86a00'
    self.email = 'evan@emailable.com'
    self.emails = ['evan@emailable.com', 'jarrett@emailable.com']

  def test_invalid_api_key_authentication(self):
    client = emailable.Client('test_7aff7fc0141c65f86a00')
    self.assertRaises(
      emailable.AuthError,
      client.verify,
      'evan@emailable.com'
    )

  def test_missing_api_key_authentication(self):
    client = emailable.Client()
    self.assertRaises(
      emailable.AuthError,
      client.verify,
      'evan@emailable.com'
    )

  def test_global_api_key_authentication(self):
    client = emailable.Client(self.api_key)
    self.assertIsNotNone(client.verify(self.email).domain)
    batch_id = client.batch(self.emails).id
    self.assertIsNotNone(batch_id)
    self.assertIsNotNone(client.batch_status(batch_id).id)
    self.assertIsNotNone(client.account().available_credits)

  def test_request_time_api_key_authentication(self):
    client = emailable.Client()
    self.assertIsNotNone(client.verify(self.email, api_key=self.api_key).domain)
    batch_id = client.batch(self.emails, api_key=self.api_key).id
    self.assertIsNotNone(batch_id)
    self.assertIsNotNone(client.batch_status(batch_id, api_key=self.api_key).id)
    self.assertIsNotNone(client.account(api_key=self.api_key).available_credits)
