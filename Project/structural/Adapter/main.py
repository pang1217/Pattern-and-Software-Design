# Target interface
class MediaPlayer:
    def play(self, audio_type, file_name):
        pass

# Adaptee interface 
class AdvancedMediaPlayer:
    def play_video(self, file_name):
        pass

# Adaptee class 1 
class MP4Player(AdvancedMediaPlayer):
    def play_video(self, file_name):
        print("Playing MP4 video file:", file_name)

# Adaptee class 2
class MKVPlayer(AdvancedMediaPlayer):
    def play_video(self, file_name):
        print("Playing MKV video file:", file_name)

# Adapter
class MediaPlayerAdapter(MediaPlayer):
    def __init__(self, advanced_media_player):
        self.advanced_media_player = advanced_media_player

    def play(self, audio_type, file_name):
        if audio_type.lower() == "mp4" or audio_type.lower() == "mkv":
            self.advanced_media_player.play_video(file_name)
        else:
            print("Invalid media type:", audio_type)

# Client code
if __name__ == "__main__":
    mp4_player = MediaPlayerAdapter(MP4Player())
    mp4_player.play("mp4", "movie.mp4")

    mkv_player = MediaPlayerAdapter(MKVPlayer())
    mkv_player.play("mkv", "video.mkv")
