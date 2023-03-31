class Room:
    def __init__(self, guests, songs, fee, capacity):
        self.guests = guests
        self.songs = songs
        self.fee = fee
        self.capacity = capacity

    def guest_count(self):
        return len(self.guests)

    def check_in_guest(self, guest):
        self.guests.append(guest)

    def check_out_guest(self, guest):
        self.guests.remove.check_in_guest(guest)
  

    # def song_count(self):
    #     return len(self.songs)

    # def add_song(self, song):
    #     self.songs.append(song)
