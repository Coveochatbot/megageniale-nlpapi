import unittest
from model.intent import Intent

class TestIntent(unittest.TestCase):

    def test_new_intent(self):
        intent_name = "Une intention"
        intent = Intent(intent_name)
        self.assertEqual(intent_name, intent.name)

    if __name__ == '__main__':
        unittest.main()
