# target interface
class MediaPlayer :
    def play(self, file) :
        pass
    
# mp4 adapter
class MP4Adapter (MediaPlayer):
    def __init__(self, file) -> None:
        self.mp4_player = file
        
    def play(self, file) :
        self.mp4_player.play_mp4(file)
        
class MP4Adaptee :
    def play_mp4 (self, file) :
        print(f'Playing mp4 file : {file}')
        
class MPVAdapter (MediaPlayer):
    def __init__(self, file) -> None:
        self.mpv_player = file
        
    def play(self, file) :
        self.mpv_player.play_mpv(file)
        
# mpv adapter
class MPVAdaptee :
    def play_mpv (self, file) :
        print(f'Playing mpv file : {file}')
        
if __name__ == '__main__' :
    mp4_player = MP4Adaptee()
    mpv_player = MPVAdaptee()
    
    # adapter
    mp4_adapter = MP4Adapter(mp4_player)
    mpv_adapter = MPVAdapter(mpv_player)
    
    mp4_adapter.play("file.mp4")
    mpv_adapter.play("file.mpv")
    
    
    # adaptees = [MP4Adaptee(), MPVAdaptee()]
    # adapters = [MediaAdapter(adaptee) for adaptee in adaptees]
    # for adapter in adapters:
    #     adapter.play("file.mp4")
    