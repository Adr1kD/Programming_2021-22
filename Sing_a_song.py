class Song(object):
    def __init__(self, song1):
        self.song1=song1
    def sing_me_a_song(self, song1):
        song1=song1.split(" ")
        for x in song1:
            print (x)

class Get(Song):
    def __init__(self, song):
        song1 = ""
        for x in range(len(song)):
            song1 = song1 + song[x]
        print(song1)
        print(type(song1))
        return super().sing_me_a_song(song1)
