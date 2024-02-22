class Command :
    def execute(self) :
        pass
    
class Speaker :
    def on(self, msg) :
        print(f"Speaker On in : {msg}")
        
    def off(self, msg) :
        print(f"Speaker Off in : {msg}")
        
    def volumeUp(self, msg) :
        print(f"Speaker Volume Up in : {msg}")
        
    def volumeDown(self, msg) :
        print(f"Speaker Volume Down in : {msg}")
        
class SpeakerOn (Command) :
    def __init__(self, speaker, msg):
        self.speaker = speaker
        self.msg = msg
    
    def execute(self):
        self.speaker.on(self.msg)
        
class SpeakerOff(Command) :
    def __init__(self, speaker, msg):
        self.speaker = speaker
        self.msg = msg
    
    def execute(self):
        self.speaker.off(self.msg)
        
class SpeakerVolumeDown(Command) :
    def __init__(self, speaker, msg):
        self.speaker = speaker
        self.msg = msg
    
    def execute(self):
        self.speaker.volumeUp(self.msg)
        
class SpeakerVolumeUp(Command) :
    def __init__(self, speaker, msg):
        self.speaker = speaker
        self.msg = msg
    
    def execute(self):
        self.speaker.volumeDown(self.msg)
        
class Remote :
    def setCommand(self, c) :
        self.command = c
    
    def execute(self):
        self.command.execute()
    
if __name__ == '__main__' :
    remote = Remote()
    speaker = Speaker()
    
    remote.setCommand(SpeakerOn(speaker, "Bedroom"))
    remote.execute()
    remote.setCommand(SpeakerVolumeUp(speaker, "Bedroom"))
    remote.execute()
    remote.setCommand(SpeakerVolumeDown(speaker, "Bedroom"))
    remote.execute()
    remote.setCommand(SpeakerOff(speaker, "Bedroom"))
    remote.execute()