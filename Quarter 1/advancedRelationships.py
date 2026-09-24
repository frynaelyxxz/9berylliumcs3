class Music:
    def __init__(self, title, singer, album, duration, number_of_streams):
        self.title = title
        self.singer = singer
        self.album = album
        self.duration = duration
        self.number_of_streams = number_of_streams

    def displayTitle(self):
        print(f"{self.title}")

    def displaySinger(self):
        print(f"{self.singer}")

    def displayAlbum(self):
        print(f"{self.album}")

    def displayDuration(self):
        print(f"{self.duration}")
        
    def displayStreams(self):
        print(f"{self.number_of_streams}")

    def addNumberOfStreams(self, amt):
        self.number_of_streams += amt
        
class PremiumMusic(Music):
    def __init__(self, title, singer, album, duration, number_of_streams, subscription_type):
        super().__init__(title, singer, album, duration, number_of_streams)
        self.subscription_type = subscription_type

    def displaySubscriptionType(self):
        print(f"{self.subscription_type}")
        
class AUDIO_PLAYER:
    def __init__(self, current_track, is_playing, volume, queue_position):
         self.current_track = current_track
         self.is_playing = is_playing
         self.volume = volume
         self.queue_position = queue_position 

    def play(self):
        self.is_playing = True
        print(f"Now playing: {self.current_track}")
        
    def pause(self):
        self.is_playing = False
        print("Playback paused")
    
    def setVolume(self, level):
        self.volume = level

# --- FIXED INDENTATION PIPELINE ---
if __name__ == "__main__":
    print("===Test 1 - Inheritance===")
    premium_song = PremiumMusic(
        title="Oceans & Engines", 
        singer="NIKI", 
        album="Nicole", 
        duration="5:36", 
        number_of_streams=5000, 
        subscription_type="Premium"
    )
    
    print("Child object (PremiumMusic) accessing parent attributes directly:")
    print(f"Parent Song Title: {premium_song.title}")
    print(f"Parent Song Artist: {premium_song.singer}")
    print(f"Parent Song Duration: {premium_song.duration}")
    print("Parent Method Call (displayTitle):")
    premium_song.displayTitle()
    print()
    
    print("===Test 2 - Composition===")
    player = AUDIO_PLAYER(current_track="Heather", is_playing=False, volume=50, queue_position=1)
    print("AUDIO_PLAYER object accessing its own attributes:")
    print(f"Current Track: {player.current_track}")
    print(f"Is Playing: {player.is_playing}")
    print(f"Volume: {player.volume}")
    print(f"Queue Position: {player.queue_position}")
    print()

    print("===Test 3 - Dependency===")
    player.play()
    print()