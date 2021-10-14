from unittest import TestCase
import emailable
import time

class TestClient(TestCase):
  def setUp(self):
    self.client = emailable.Client('test_7aff7fc0142c65f86a00')
    self.response = self.client.verify('johndoe+tag@emailable.com')
    time.sleep(0.25)

  def test_invalid_api_key(self):
    client = emailable.Client('test_7aff7fc0141c65f86a00')
    self.assertRaises(
      emailable.AuthError,
      client.verify,
      'evan@emailable.com'
    )

  def test_missing_api_key(self):
    self.client.api_key = None
    self.assertRaises(
      emailable.AuthError,
      self.client.verify,
      'evan@emailable.com'
    )

  def test_verify_returns_response(self):
    self.assertIsInstance(self.response, emailable.Response)

  def test_verification_role(self):
    response = self.client.verify('role@example.com')
    self.assertTrue(response.role)

  def test_verification_deliverable(self):
    response = self.client.verify('deliverable@example.com')
    self.assertEqual(response.state, 'deliverable')

  def test_verification_tag(self):
    self.assertEqual(self.response.tag, 'tag')

  def test_verification_name_and_gender(self):
    # name and gender checks only get run for certain verification states
    if self.response.state in ['deliverable', 'risky', 'unknown']:
      self.assertEqual(self.response.first_name, 'John')
      self.assertEqual(self.response.last_name, 'Doe')
      self.assertEqual(self.response.full_name, 'John Doe')
      self.assertEqual(self.response.gender, 'male')
    else:
      self.assertIsNone(self.response.first_name)
      self.assertIsNone(self.response.last_name)
      self.assertIsNone(self.response.full_name)
      self.assertIsNone(self.response.gender)

  def test_batch_creation(self):
    response = self.client.batch(
      ['evan@emailable.com', 'jarrett@emailable.com']
    )
    self.assertIsNotNone(response.id)

  def test_batch_status(self):
    response = self.client.batch(
      ['evan@emailable.com', 'jarrett@emailable.com']
    )
    response = self.client.batch_status(response.id)
    self.assertIsNotNone(response.emails)
    self.assertIsNotNone(response.id)
    self.assertIsNotNone(response.reason_counts)
    self.assertIsNotNone(response.total_counts)

  def test_account(self):
    response = self.client.account()
    self.assertIsNotNone(response.owner_email)
    self.assertIsNotNone(response.available_credits)
