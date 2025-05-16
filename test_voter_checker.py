import unittest
from voter_checker import (is_eligible_to_vote, is_not_eligible_to_vote)


class TestVoterEligibility(unittest.TestCase):

    def test_valid_voter(self):
        self.assertTrue(is_eligible_to_vote(18, True))

    def test_underage_voter(self):
        self.assertTrue(is_not_eligible_to_vote(15))
