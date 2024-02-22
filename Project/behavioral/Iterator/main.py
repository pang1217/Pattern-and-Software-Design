class IMedia : 
    def getType(self) : 
        pass
    def getMedia(self) :
        pass
    
class Movie(IMedia):
    def __init__(self, title, type) -> None:
        self.title = title
        self.type = type.lower()
        
    def getMedia(self):
        return f"Movie title : {self.title} type : {self.type}"
    
    def getType(self):
        return self.type
    
class Song(IMedia):
    def __init__(self, title, type) -> None:
        self.title = title
        self.type = type.lower()
        
    def getMedia(self):
        return f"Song title : {self.title} type : {self.type}"
    
    def getType(self):
        return self.type

# Collection
class MediaCollection() :
    def createIterator():
        pass
    
    def createNewMediaIterator():
        pass
    
    def createPopularMediaIterator():
        pass

class MovieCollection(MediaCollection) :
    def __init__(self):
      self.movie = []
    
    def add(self, m):
        self.movie.append(m)
        
    def createIterator(self) :
        return AllMediaIterator(self.movie)
    
    def createNewMediaIterator(self):
        return NewMediaIterator(self.movie)
    
    def createPopularMediaIterator(self):
        return PopularMediaIterator(self.movie)
    
class SongCollection(MediaCollection) :
    def __init__(self):
      self.song = []
    
    def add(self, s):
        self.song.append(s)
        
    def createIterator(self) :
        return AllMediaIterator(self.song)
    
    def createNewMediaIterator(self):
        return NewMediaIterator(self.song)
    
    def createPopularMediaIterator(self):
        return PopularMediaIterator(self.song)

# Iterator 
class IMediaIterator :
    def getNext():
        pass
    
    def hasMore():
        pass
    
class AllMediaIterator(IMediaIterator) :
    def __init__(self, mediaCollection) -> None:
        self.media = mediaCollection
        self.currentIndex = 0
    
    def getNext(self) -> IMedia :
        media = self.media[self.currentIndex]
        self.currentIndex += 1
        return media
    
    def hasMore(self):
        return self.currentIndex < len(self.media)
    
class NewMediaIterator (IMediaIterator):
    def __init__(self, mediaCollection) -> None:
        self.media = [media for media in mediaCollection if media.getType() == 'new']
        self.currentIndex = 0
    
    def getNext(self) -> IMedia :
        media = self.media[self.currentIndex]
        self.currentIndex += 1
        return media
    
    def hasMore(self):
        return self.currentIndex < len(self.media)

class PopularMediaIterator (IMediaIterator):
    def __init__(self, mediaCollection) -> None:
        self.media = [media for media in mediaCollection if media.getType() == 'popular']
        self.currentIndex = 0
    
    def getNext(self) -> IMedia :
        media = self.media[self.currentIndex]
        self.currentIndex += 1
        return media
    
    def hasMore(self):
        return self.currentIndex < len(self.media)

def showMedia(it : IMediaIterator) :
    while it.hasMore() :
        print(it.getNext().getMedia())

if __name__ == '__main__' :
    print('-- Movie')
    movies = MovieCollection()
    movies.add(Movie("Harry Potter", "popular"))
    movies.add(Movie("Dune", "new"))
    movies.add(Movie("The Marvels", "new"))
    movies.add(Movie("Deadpool 2", "new"))
    movies.add(Movie("Lord Of the ring", "Popular"))
    movies.add(Movie("The Matrix", "PoPular"))
    
    print("-- Movie All Media Iterator")
    showMedia(movies.createIterator())
    print("-- Movie New Media Iterator")
    showMedia(movies.createNewMediaIterator())
    print("-- Movie Popular Media Iterator")
    showMedia(movies.createPopularMediaIterator())
    
    print('=' * 25, "\n-- Song")
    songs = SongCollection()
    songs.add(Song("Umbrella", "popular"))
    songs.add(Song("Weird World", "new"))
    songs.add(Song("Nightwalker", "new"))
    songs.add(Song("End of Time", "new"))
    songs.add(Song("What's Up", "Popular"))
    songs.add(Song("500 Miles", "PoPular"))
    
    print("-- Song All Media Iterator")
    showMedia(songs.createIterator())
    print("-- Song New Media Iterator")
    showMedia(songs.createNewMediaIterator())
    print("-- Song Popular Media Iterator")
    showMedia(songs.createPopularMediaIterator())