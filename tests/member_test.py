import unittest
from models.member import Member
from models.membership import Membership

membership = Membership("Free", 0, 0)

class TestMember(unittest.TestCase):
    
    def setUp(self):
        self.member = Member("Jack", "Cogan", membership)
        
    def test_member_has_membership(self):
        expected = membership
        actual = self.member.membership
        self.assertEqual(expected, actual)
        
    def test_member_has_name(self):
        expected = "Jack"
        actual = self.member.first_name
        self.assertEqual(expected, actual)