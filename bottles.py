class Bottles:

    def song(self):
        return self.verses(99, 0)

    def verses(self, start, end):
        return "\n".join(self.verse(i) for i in range(start, end - 1, -1))

    def verse(self, number):
        verse_0 = (
            "No more bottles of beer on the wall, " +
            "no more bottles of beer.\n" +
            "Go to the store and buy some more, " +
            "99 bottles of beer on the wall.\n"
        )
        verse_1 = (
           "1 bottle of beer on the wall, " +
           "1 bottle of beer.\n" +
           "Take it down and pass it around, " +
           "no more bottles of beer on the wall.\n"
        )
        verse_2 = (
           "2 bottles of beer on the wall, " +
           "2 bottles of beer.\n" +
           "Take one down and pass it around, " +
           "1 bottle of beer on the wall.\n"
        )
        default = (
           f"{number} bottles of beer on the wall, " +
           f"{number} bottles of beer.\n" +
           "Take one down and pass it around, " +
           f"{number-1} bottles of beer on the wall.\n"
        )
        CASES = {
            0: verse_0,
            1: verse_1,
            2: verse_2,
        }
        return CASES.get(number, default)

