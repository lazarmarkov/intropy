from classPlay import Playlist

playlist = Playlist()

playlist.add_song("S1", "Bohemian Rhapsody", "Queen", 354)
playlist.add_song("S2", "Yesterday", "The Beatles", 125)
playlist.add_song("S3", "Hotel California", "Eagles", 391)

playlist.add_song("S8", "Dream On", "Aerosmith", 267)
playlist.add_song("S5", "Sweet Child O' Mine", "Guns N' Roses", 302)
playlist.add_song("S6", "Breathe", "Pink Floyd", 187)
# playlist.get_playlist_info()

print("-----Initial Playlist-----")
playlist.get_playlist_info()
print()

print("-----Moving S3 song on top-----")
playlist.move_song("S3",0)
playlist.get_playlist_info()
print()

print("-----Remove S2-----")
playlist.remove_song("S2")
playlist.get_playlist_info()
print()

print("-----Get total duration----")
playlist.get_total_duration()
print()

print("-----Shuffle Playlist-----")
playlist.shuffle_playlist()
playlist.get_playlist_info()
print()

print("-----Shuffle Playlist again-----")
playlist.shuffle_playlist()
playlist.get_playlist_info()
print()

print("-----Clear Playlist-----")
playlist.clear_playlist()

