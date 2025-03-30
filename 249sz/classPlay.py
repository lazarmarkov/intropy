import time
import random

class Playlist:
    def __init__(self):
        self.playlist = {}

    def add_song(self, song_id, song_name, artist, duration):
        self.playlist[song_id] = {"song_name":song_name, "artist": artist, "duration": duration}

    def move_song(self, song_id, new_position):
        items = list(self.playlist.items())
        for pair in items:
            if pair[0] == song_id:
                items.remove(pair)
                items.insert(new_position, pair)
                break

        # Rebuild the dictionary
        self.playlist = dict(items)

    def remove_song(self, song_id):
        del self.playlist[song_id]

    def get_playlist_info(self):
        song_num = 1
        for song in self.playlist:
            song_time = time.strftime("%M:%S",time.gmtime(self.playlist[song]["duration"]))
            print(f"{song_num}. {self.playlist[song]["song_name"]} - {self.playlist[song]["artist"]} ({song_time})")
            song_num += 1

    def get_total_duration(self):
        total_duration = 0
        for song in self.playlist:
            total_duration += self.playlist[song]["duration"]

        total_time = time.strftime("%M:%S",time.gmtime(total_duration))
        print(f"Total duration: {total_time}")

    def shuffle_playlist(self):
        list_shuffle = list(self.playlist.items())
        random.shuffle(list_shuffle)
        self.playlist = dict(list_shuffle)

    def clear_playlist(self):
        self.playlist.clear()