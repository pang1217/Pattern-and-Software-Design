class Detail :
    def __init__(self, artist, album, releaseYear, genre) -> None:
        self.__artist = artist
        self.__album = album
        self.__releaseYear = releaseYear
        self.__genre = genre
        
    def playSong(self, title) :
        print(f'Now playing {title} - {self.__artist} album {self.__album}({self.__releaseYear})')

class DetailFactory :
    def __init__(self) -> None:
        self.container = {} # Dictionary

    def getDetail(self, artist, album, release_year, genre):
        key = (artist, album, release_year, genre)
        if key not in self.container:
            self.container[key] = Detail(artist, album, release_year, genre)
        return self.container[key] 

class Song :
    def __init__(self, title, detail : Detail) :
        self.__title = title
        self.__detail = detail
        
    def playSong(self):
        # print(f'Now playing {self.__title}')
        self.__detail.playSong(self.__title)

class Playlist :
    def __init__(self) -> None:
        self.songs = []
        
    def addSong(self, title, artist, album, releaseYear, genre) :
        detail = DetailFactory().getDetail(artist, album, releaseYear, genre)
        self.songs.append(Song(title, detail))
    
    def playSong(self) :
        for song in self.songs :
            song.playSong()


if __name__ == '__main__' :
    pepperMintTown = Playlist()
    pepperMintTown.addSong(title='One Way Ticket', artist='My Life As Ali Thomas', album='Peppermint Town', releaseYear='2021', genre='Indie Rock')
    pepperMintTown.addSong(title='Dream Lover', artist='My Life As Ali Thomas', album='Peppermint Town', releaseYear='2021', genre='Indie Rock')
    pepperMintTown.addSong(title='Dear All My Universe', artist='My Life As Ali Thomas', album='Peppermint Town', releaseYear='2021', genre='Indie Rock')
    pepperMintTown.playSong()
