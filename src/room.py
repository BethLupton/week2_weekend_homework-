class Room:
    def __init__(self, guests, songs, fee, capacity):
        self.guests = guests
        self.songs = songs
        self.fee = fee
        self.capacity = capacity

    def guest_count(self):
        return len(self.guests)

    def check_in_guest(self, guest):
        if guest.pay_fee(self.fee):
            self.guests.append(guest)

    def check_in_guests(self, new_guests):
        if self.guest_count() + len(new_guests) <= self.capacity:
            for new_guest in new_guests:
                self.check_in_guest(new_guest)

    def check_out_guest(self, guest):
        self.guests.remove(guest)
  
    def song_count(self):
        return len(self.songs)

    def add_song(self, song):
        self.songs.append(song)
