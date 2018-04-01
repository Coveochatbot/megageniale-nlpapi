import unittest
from nose.tools import raises
from api.config import config


class TestConfig(unittest.TestCase):

    def test_get_dialogflow_secret_success(self):
        self.assertEqual('file.json', config.get('dialogflow_secret'))

    def test_get_project_id_success(self):
        self.assertEqual('whisperproject', config.get('project_id'))

    def test_get_language_success(self):
        self.assertEqual('en-US', config.get('language'))

    @raises(AttributeError)
    def test_invalid_config_key(self):
        self.assertRaises(AttributeError, config.get('key_invalid'))

    if __name__ == '__main__':
        unittest.main()
