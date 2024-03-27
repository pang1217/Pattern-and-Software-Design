class Mediator:
    def notify(self, sender, event):
        pass

class MusicPlayerMediator (Mediator):
    def __init__(self, playlist, player, display):
        self.playlist = playlist
        self.player = player
        self.display = display

    def songSelected(self, song):
        self.player.playSong(song)
        self.display.showSongInfo(song)

    def playbackStarted(self):
        self.display.updateStatus("Playing")

    def playbackPaused(self):
        self.display.updateStatus("Paused")

    def notify(self, sender, event):
        print(f'===> {self.__class__.__name__} received notification from {sender.__class__.__name__} for event {event}')
        if event == "songSelected":
            self.songSelected(sender.selectedSong)

        elif event == "playbackStarted":
            self.playbackStarted()

        elif event == "playbackPaused":
            self.playbackPaused()
            
        elif event == "songChanged":
            self.songSelected(sender.selectedSong)    
            
class Colleague:
    def __init__(self, mediator):
        self.mediator = mediator

class PlayList(Colleague):
    def __init__(self, mediator):
        super().__init__(mediator)
        self.selectedSong = None

    def selectSong(self, song):
        self.selectedSong = song
        self.mediator.notify(self, "songSelected")
        
    def changeSong(self, song):
        self.selectedSong = song
        self.mediator.notify(self, "songChanged")

class Player(Colleague):
    def playSong(self, song):
        self.mediator.notify(self, "playbackStarted")
        
    def pausePlayback(self):
        self.mediator.notify(self, "playbackPaused")

class Display(Colleague):
    def showSongInfo(self, song):
        print(f'Displaying song information {song}')

    def updateStatus(self, status):
        print(f'Updating status {status}')


if __name__ == '__main__':
    playlist = PlayList(None)  
    player = Player(None)  
    display = Display(None)  

    # Create the Mediator and associate it with the Colleagues
    mediator = MusicPlayerMediator(playlist, player, display)
    playlist.mediator = mediator
    player.mediator = mediator
    display.mediator = mediator

    playlist.selectSong("Song 1")  
    print()
    player.pausePlayback()

    print()
    playlist.changeSong('Song 2')
    