import unittest
from nose.tools import raises
from api.config import config


class TestConfig(unittest.TestCase):

    def test_get_api_key_success(self):
        self.assertEqual('404', config.get('api_key'))

    @raises(AttributeError)
    def test_invalid_config_key(self):
        self.assertRaises(AttributeError, config.get('key_invalid'))

    if __name__ == '__main__':
        unittest.main()
