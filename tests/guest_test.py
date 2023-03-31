import unittest
from src.guest import Guest
from src.song import Song

class TestGuest(unittest.TestCase):

    def setUp(self):
        self.song1 = Song("The Walk", "The Cure")
        self.guest1 = Guest("Beth", 125, self.song1)

    def test_guest_has_name(self):
        self.assertEqual('Beth', self.guest1.name)

    def test_guest_has_fav_song(self):
        self.assertEqual(self.song1.title, self.guest1.fave_song.title)

    def test_how_much_guest_has_in_wallet(self):
        self.assertEqual(125, self.guest1.wallet)

    def test_guest_pays_fee_has_money(self):
        paid = self.guest1.pay_fee(125)
        self.assertEqual(True, paid)
        
    def test_guest_pays_fee_does_not_have_money(self):
        paid = self.guest1.pay_fee(126)
        self.assertEqual(False, paid)