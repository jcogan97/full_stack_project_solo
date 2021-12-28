import unittest
from models.membership import Membership

class TestMembership(unittest.TestCase):
    
    def setUp(self):
        self.membership = Membership("Free", 0, 0)
        self.membership2 = Membership("Silver", 10, 3)
        
    def test_membership_has_free_classes(self):
        expected = 3
        actual = self.membership2.free_classes
        self.assertEqual(expected, actual)