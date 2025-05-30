from unittest import TestCase
import emailable
import time

class TestClient(TestCase):
  def setUp(self):
    self.client = emailable.Client('test_7aff7fc0142c65f86a00')
    time.sleep(0.5)

  def test_verify_returns_response(self):
    response = self.client.verify('johndoe+tag@emailable.com')
    self.assertIsInstance(response, emailable.Response)

  def test_verification_role(self):
    response = self.client.verify('role@example.com')
    self.assertTrue(response.role)

  def test_verification_deliverable(self):
    response = self.client.verify('deliverable@example.com')
    self.assertEqual(response.state, 'deliverable')

  def test_verification_tag(self):
    response = self.client.verify('johndoe+tag@emailable.com')
    self.assertEqual(response.tag, 'tag')

  def test_verification_name_and_gender(self):
    response = self.client.verify('johndoe+tag@emailable.com')
    # name and gender checks only get run for certain verification states
    if response.state in ['deliverable', 'risky', 'unknown']:
      self.assertEqual(response.first_name, 'John')
      self.assertEqual(response.last_name, 'Doe')
      self.assertEqual(response.full_name, 'John Doe')
      self.assertEqual(response.gender, 'male')
    else:
      self.assertIsNone(response.first_name)
      self.assertIsNone(response.last_name)
      self.assertIsNone(response.full_name)
      self.assertIsNone(response.gender)

  def test_batch_creation(self):
    response = self.client.batch(
      ['evan@emailable.com', 'jarrett@emailable.com']
    )
    self.assertIsNotNone(response.id)

  def test_batch_creation_with_params(self):
    with self.assertRaises(emailable.error.ClientError):
      self.client.batch(
        ['evan@emailable.com', 'jarrett@emailable.com'],
        {'url': 'test@example.org', 'simulate': 'generic_error'}
      )

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
