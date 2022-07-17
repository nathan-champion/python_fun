class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics
    
    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

happy_bday = Song(["Happy birthday to you",
                   "I don't want to get sued",
                   "So I'll stop right there"])

bulls_on_parade = Song(["They rally around tha family",
                        "With pockets full of shells"])

numbers = Song([1, 2, 3, 4, 5])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()
bop2 = Song(bulls_on_parade.lyrics)
bill = ["EIEIO", "Old Bill had a taxidermist"]
billsong = Song(bill)
numbers.sing_me_a_song()
bop2.sing_me_a_song()
billsong.sing_me_a_song()