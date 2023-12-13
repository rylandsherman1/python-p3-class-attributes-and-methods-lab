class Song:
    # Class attributes
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        # Instance attributes
        self.name = name
        self.artist = artist
        self.genre = genre

        # Increment the count of songs
        Song.add_song_to_count()

        # Add the genre to the genres list and update genre_count
        self.add_to_genres()

        # Add the artist to the artists list and update artist_count
        self.add_to_artists()

    @classmethod
    def add_song_to_count(cls):
        cls.count += 1

    def add_to_genres(self):
        if self.genre not in Song.genres:
            Song.genres.append(self.genre)

        if self.genre in Song.genre_count:
            Song.genre_count[self.genre] += 1
        else:
            Song.genre_count[self.genre] = 1

    def add_to_artists(self):
        if self.artist not in Song.artists:
            Song.artists.append(self.artist)

        if self.artist in Song.artist_count:
            Song.artist_count[self.artist] += 1
        else:
            Song.artist_count[self.artist] = 1

    @classmethod
    def add_to_genre_count(cls):
        # Update genre_count based on the songs created so far
        for song in cls.genres:
            if song.genre in cls.genre_count:
                cls.genre_count[song.genre] += 1
            else:
                cls.genre_count[song.genre] = 1

    @classmethod
    def add_to_artist_count(cls):
        # Update artist_count based on the songs created so far
        for song in cls.artists:
            if song.artist in cls.artist_count:
                cls.artist_count[song.artist] += 1
            else:
                cls.artist_count[song.artist] = 1
