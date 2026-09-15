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
        
song1 = Music("Oceans & Engines", "NIKI", "Nicole", "5:36", 5000)
song2 = Music("Heather", "Conan Gray", "Kid Krow", "3:18", 10000)

print("Initial number of streams:")
print("Song 1:")
song1.displayStreams()
print("Song 2:")
song2.displayStreams()

song2.addNumberOfStreams(20000)

print("Updated number of streams:")
print("Song 1:")
song1.displayStreams()
print("Song 2:")
song2.displayStreams()


class AUDIO_PLAYER:
    def __init__(self,current_track, is_playing, volume, queue_position):
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
        print(f"Volume set to: {self.volume}%")
        
    def skip(self, next_track):
        print(f"Skipping...Left queue position {self.queue_position}")
        self.current_track = next_track
        self.queue_position
        print(f"Now playing: {self.current_track}(Position{self.queue_position})")

# Create a player object
player = AUDIO_PLAYER(current_track = "Oceans & Engines", is_playing=False, volume=50, queue_position=1)

print("---Initial Player Actions---")
player.play()
player.setVolume(49)

print("---pausing & skipping---")
player.pause()
# Skip to the next song in line
player.skip(next_track="Heather")