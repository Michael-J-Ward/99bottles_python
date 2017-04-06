class Bottles:

    NoMore = staticmethod(lambda verse: (
        "No more bottles of beer on the wall, " +
        "no more bottles of beer.\n" +
        "Go to the store and buy some more, " +
        "99 bottles of beer on the wall.\n"
    ))

    LastOne = staticmethod(lambda verse: (
        "1 bottle of beer on the wall, " +
        "1 bottle of beer.\n" +
        "Take it down and pass it around, " +
        "no more bottles of beer on the wall.\n"
    ))

    Penultimate = staticmethod(lambda verse: (
        "2 bottles of beer on the wall, " +
        "2 bottles of beer.\n" +
        "Take one down and pass it around, " +
        "1 bottle of beer on the wall.\n"
    ))

    Default = staticmethod(lambda verse: (
        f"{verse.number} bottles of beer on the wall, " +
        f"{verse.number} bottles of beer.\n" +
        "Take one down and pass it around, " +
        f"{verse.number - 1} bottles of beer on the wall.\n"
    ))

    def song(self):
        return self.verses(99, 0)

    def verses(self, start, finish):
        return "\n".join(self.verse(n) for n in range(start, finish - 1, -1))

    def verse(self, number):
        return self.verse_for(number).text()

    def verse_for(self, number):
        templates = {
            0: Verse(0, self.NoMore),
            1: Verse(1, self.LastOne),
            2: Verse(2, self.Penultimate),
        }
        return templates.get(number, Verse(number, self.Default))


class Verse:

    def __init__(self, number, lyrics):
        self.number = number
        self.lyrics = lyrics

    def text(self):
        return self.lyrics(self)
