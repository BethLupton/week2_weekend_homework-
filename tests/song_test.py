import unittest
from src.song import Song

class TestSong(unittest.TestCase):

    def setUp(self):
        self.song = Song("Train in Vain", "The Clash")

    def test_song_has_title(self):
        self.assertEqual("Train in Vain", self.song.title)
                                       
    def test_song_has_artist(self):
        self.assertEqual("The Clash", self.song.artist)    
