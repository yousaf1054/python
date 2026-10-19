class Playlist:
    def __init__(self):
        self.songs = []

    def Add_song(self, song):
        self.songs.append(song)

    def __len__(self):
        return len(self.songs)

    def __repr__(self):
        return f"playlist(songs={self.songs})"


palylist = Playlist()

palylist.Add_song("song a")
palylist.Add_song("song b")
palylist.Add_song("song c")
print(len(palylist))
print(repr(palylist))
