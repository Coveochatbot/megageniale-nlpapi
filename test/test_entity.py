import unittest
from model.entity import Entity


class TestEntity(unittest.TestCase):

    def test_new_intent(self):
        intent = Entity("An entity")
        self.assertEqual("An entity", intent.name)

    if __name__ == '__main__':
        unittest.main()
