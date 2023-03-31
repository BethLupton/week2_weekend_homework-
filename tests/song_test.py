import unittest
from src.song import Song
from src.guest import Guest

class TestSong(unittest.TestCase):

    def setUp(self):
        self.song1 = Song("The Walk", "The Cure")
        self.song2 = Song("Train in Vain", "The Clash")
        