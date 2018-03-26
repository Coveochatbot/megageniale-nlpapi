import unittest
from model.entity import Entity


class TestEntity(unittest.TestCase):

    def test_new_intent(self):
        intent_name = "Une intention"
        intent = Entity(intent_name, 1)
        self.assertEqual(intent_name, intent.name)
        self.assertEqual(1, intent.confidence)

    if __name__ == '__main__':
        unittest.main()