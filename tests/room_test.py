import unittest
from src.room import Room
from src.guest import Guest
from src.song import Song


class TestRoom(unittest.TestCase):
    def setUp(self):
        self.song1 = Song("The Walk", "The Cure")
        self.song2 = Song("Train in Vain", "The Clash")
        self.song3 = Song("This Must Be the Place", "Talking Heads")
        self.song4 = Song("Honey Sweet", "Blossoms")
        self.guest1 = Guest("Beth", 125, self.song1)
        self.guest2 = Guest("Errin", 200, self.song4)
        self.guest3 = Guest("Hannah", 75, self.song2)
        self.room1 = Room([], [], 20, 2)
        self.room2 = Room([], [self.song1], 50, 6)
        self.room3 = Room([self.guest3], [self.song1], 110, 15)

        self.karaoke_bar = {
            "name": "Maggie's Mosh Pit",
            "rooms": [
                self.room1,
                self.room2,
                self.room3
            ]
        }

    def test_to_check_in_guest(self):
        self.room1.check_in_guest(self.guest1)
        self.assertEqual(1, self.room1.guest_count())


    def test_to_check_out_guest(self):
        self.room1.check_out_guest(self.guest1)
        self.assertEqual(1, self.room1.check_out_guest)

    # def test_to_add_song_to_room(self):
    #     self.room1.add_song(self.song1)
    #     self.assertEqual(1, self.room1.song_count())

# def test_to_remove_song(self):


# def test_to_find_guests_fave_song(self):
# def test_room_does_have_capacity(self):
# def test_room_does_not_have_capacity(self):
