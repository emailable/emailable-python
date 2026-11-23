from unittest import TestCase
from unittest.mock import Mock, patch
import requests
import emailable

OK = Mock(status_code=200)
OK.json.return_value = {}

@patch('emailable.client.requests.request', return_value=OK)
class TestTimeout(TestCase):

  def test_default_timeouts(self, request):
    emailable.Client('key').account()
    self.assertEqual(request.call_args[1]['timeout'], (30, 60))

  @patch.object(emailable.Client, 'open_timeout', 5)
  @patch.object(emailable.Client, 'read_timeout', 45)
  def test_configured_timeouts(self, request):
    emailable.Client('key').account()
    self.assertEqual(request.call_args[1]['timeout'], (5, 45))

  @patch.object(emailable.Client, 'open_timeout', None)
  def test_open_timeout_cannot_be_none(self, request):
    with self.assertRaises(ValueError):
      emailable.Client('key').account()
    request.assert_not_called()

  @patch.object(emailable.Client, 'read_timeout', None)
  def test_read_timeout_cannot_be_none(self, request):
    with self.assertRaises(ValueError):
      emailable.Client('key').account()
    request.assert_not_called()

  def test_verify_timeout_is_not_request_timeout(self, request):
    emailable.Client('key').verify('evan@emailable.com', timeout=25)
    self.assertEqual(request.call_args[1]['params']['timeout'], 25)
    self.assertEqual(request.call_args[1]['timeout'], (30, 60))

  def test_timeout_raises_client_error(self, request):
    request.side_effect = requests.exceptions.ReadTimeout('read timed out')
    with self.assertRaisesRegex(emailable.ClientError, 'read timed out'):
      emailable.Client('key').account()
    self.assertEqual(request.call_count, 1)
