import lyricsgenius as lg


class Genius:
    def __init__(self):
        self.API = "kUgGcvfZUd5sUqXwC4oHIvYwrp73VUHP3uFZ9cBkv2NcxTOhwfogwaYt0CNOvL8i"
        self.genius = lg.Genius(self.API, skip_non_songs=True, excluded_terms=["(Remix)", "(Live)"],
                                remove_section_headers=True)

    def get_lyrics(self, artist_name, song_name):
        artist = self.genius.search_artist(artist_name, max_songs=1)
        # searching for artist

        song = artist.song(song_name)
        # searching for song

        lyrics = song.lyrics
        # getting lyrics

        return lyrics
        # returning results

    # def get_albums(self, artist_name):
    #     artist = self.genius.search_artist(artist_name)

