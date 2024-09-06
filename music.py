# Система управління музичною колекцією:
# Створіть клас "Пісня" з атрибутами: назва, виконавець, альбом, рік випуску, жанр, тривалість.
# Розробіть клас "Плейлист", який містить список пісень та має назву. Потім створіть клас "МузичнаБібліотека",
# який використовує словник для зберігання всіх пісень (ключ - унікальний ідентифікатор пісні) 
# та список для зберігання плейлистів.

class Song:
    def __init__(self, name, author, album, year, genre, time):
        self.name = name
        self.author = author 
        self.album = album 
        self.year = year
        self.genre = genre 
        self.time = time 
    
    def __str__(self):
        return f"{self.name} - {self.author} ({self.album} {self.year} {self.genre} {self.time})"
    
class Playlist: 
    def __init__(self, name, songs):
        self.name = name
        self.songs = songs
    def __str__(self):
        return(f"[{self.name}]: {[str(song) for song in self.songs]}")

class MyLibrary:
    def __init__(self):
        self.songs = {}
        self.playlists = []
    def __str__(self):
        songs_str = '\n'.join([f"{song_id}:{str(song)}" for song_id, song in self.songs.items()])
        playlist_str = '\n'.join([str(playlist) for playlist in self.playlists])
        return f"{songs_str}\n{playlist_str}"
    
song1 = Song("Overcompensate", "Twenty One Pilots", "Clancy", 2024, "Pop", "3:56")
song2 = Song("Backslide", "Joseph", "Clancy", 2024, "Pop", "3:00")
song3 = Song("Vignette", "Twenty One Pilots", "Clancy", 2024, "Pop", "3:22")
song4 = Song("Lavish", "Joseph", "Clancy", 2024, "Pop", "2:38")


playlist1 = Playlist("Liked", songs=[song1,song3])

Library = MyLibrary()

Library.songs["1"] = song1
Library.songs["2"] = song2
Library.songs["3"] = song3
Library.songs["4"] = song4



Library.playlists.append(playlist1)

print(Library)
