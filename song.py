"""
6. SONG CHALLENGE:

A playlist is considered a repeating playlist if any of the songs
contain a reference to a previous song in the playlist. Otherwise, the playlist
will end with the last song which points to None.

Implement a function is_repeating_playlist that returns true
if a playlist is repeating or false if it is not.


For example, the following code prints "True" as both songs point to each other.

first = Song("Hello")
second = Song("Eye of the tiger")
third = Song("Third Eye")

first.next_song(second);
second.next_song(third);
third.next_song(first)

print(first.is_repeating_playlist())
should return True
"""


class Song:
    def __init__(self, name):
        self.name = name
        self.next = None

    def next_song(self, song):
        self.next = song

    def is_repeating_playlist(self):
        """
        :returns: (bool) True if the playlist is repeating, False if not.
        """
         # YOUR CODE GOES HERE
        played_song = [self.name]
        nextSong = self.next
        while True:
            if nextSong != None:
                if nextSong.name in played_song:
                    return True
                else:
                    played_song.append(nextSong.name)
                    nextSong = nextSong.next
            else:
                return False


first = Song("Hello")
second = Song("Eye of the tiger")
third = Song("Third Eye")

first.next_song(second);
second.next_song(third);
third.next_song(first)

print(first.is_repeating_playlist())
# This should return True
