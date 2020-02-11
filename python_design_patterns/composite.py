from abc import ABC
from typing import List


class LetterComposite(ABC):
    def __init__(self):
        self._children: List[LetterComposite] = []

    def add(self, letter: "LetterComposite"):
        self._children.append(letter)

    def count(self):
        return len(self._children)

    def print_this_before(self):
        pass

    def print_this_after(self):
        pass

    def print(self):
        self.print_this_before()

        for letter in self._children:
            letter.print()

        self.print_this_after()


class Letter(LetterComposite):
    def __init__(self, char: str):
        assert len(char) == 1

        super().__init__()

        self._char = char

    def print_this_before(self):
        print(self._char, end="")


class Word(LetterComposite):
    @staticmethod
    def from_letters(*letters: Letter):
        word = Word()
        for letter in letters:
            word.add(letter)

        return word

    @staticmethod
    def from_characters(*characters: str):
        word = Word()
        for char in characters:
            word.add(Letter(char))
        return word

    def print_this_before(self):
        print(" ", end="")


class Sentence(LetterComposite):
    def __init__(self, *words: Word):
        super(Sentence, self).__init__()

        for word in words:
            self.add(word)

    def print_this_after(self):
        print(".")


class Messenger:
    def message_from_orcs(self) -> LetterComposite:
        words = [
            Word.from_characters("W", "h", "e", "r", "e"),
            Word.from_characters("t", "h", "e", "r", "e"),
            Word.from_characters("i", "s"),
            Word.from_characters("a"),
            Word.from_characters("w", "h", "i", "p"),
            Word.from_characters("t", "h", "e", "r", "e"),
            Word.from_characters("i", "s"),
            Word.from_characters("a"),
            Word.from_characters("w", "a", "y"),
        ]

        return Sentence(*words)

    def message_from_elves(self) -> LetterComposite:
        words = [
            Word.from_characters("M", "u", "c", "h"),
            Word.from_characters("w", "i", "n", "d"),
            Word.from_characters("p", "o", "u", "r", "s"),
            Word.from_characters("f", "r", "o", "m"),
            Word.from_characters("y", "o", "u", "r"),
            Word.from_characters("m", "o", "u", "t", "h"),
        ]

        return Sentence(*words)


if __name__ == "__main__":
    messenger = Messenger()

    print("Message from the Orcs:")
    messenger.message_from_orcs().print()

    print("Messages from the elves:")
    messenger.message_from_elves().print()
