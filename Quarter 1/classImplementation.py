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