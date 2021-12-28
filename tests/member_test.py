import unittest
from models.member import Member
from models.membership import Membership

membership = Membership("Free", 0, 0)

class TestMember(unittest.TestCase):
    
    def setUp(self):
        self.member = Member("Jack", "Cogan", membership)
        
    def member_has_membership(self):
        expected = membership
        actual = self.member.membership
        self.assertEqual(expected, actual)