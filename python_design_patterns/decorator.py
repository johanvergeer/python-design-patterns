"""
The Decorator pattern is a more flexible alternative to subclassing. The Decorator class
implements the same interface as the target and uses composition to "decorate" calls to the
target. Using the Decorator pattern it is possible to change the behavior of the class during
runtime.

In this example we show how the simple :class:`SimpleTroll` first attacks and then flees the
battle. Then we decorate the :class:`SimpleTroll` with a :class:`ClubbedTroll` and perform the
attack again. You can see how the behavior changes after the decoration.

Notes:
    This example doesn't use `PEP318 decorators`_ because they change the behavior
    at design time, while the decorator pattern allows us to change the behavior
    at runtime.

.. _PEP318 decorators: https://www.python.org/dev/peps/pep-0318/
"""
from typing_extensions import Protocol


class Troll(Protocol):
    """Protocol for trolls"""

    def attack(self):
        ...

    @property
    def attack_power(self) -> int:
        ...

    def flee_battle(self):
        ...


class SimpleTroll(Troll):
    """:py:class:`SimpleTroll` implements :py:class:`Troll` directly"""

    def attack(self):
        print("The troll tries to grab you!")

    @property
    def attack_power(self) -> int:
        return 10

    def flee_battle(self):
        print("The troll shrieks in horror and runs away!")


class ClubbedTroll(Troll):
    """Decorator that adds a club for a :py:class:`Troll`"""

    def __init__(self, decorated: Troll):
        self.decorated = decorated

    def attack(self):
        self.decorated.attack()
        print("The troll swings at you with a club!")

    @property
    def attack_power(self) -> int:
        return self.decorated.attack_power + 1

    def flee_battle(self):
        self.decorated.flee_battle()


if __name__ == "__main__":
    print("A simple looking troll approaches.")
    troll = SimpleTroll()
    troll.attack()
    troll.flee_battle()
    print(f"Simple troll power {troll.attack_power}.")

    print()
    print("A troll with huge club surprises you.")
    clubbed_troll = ClubbedTroll(troll)
    clubbed_troll.attack()
    clubbed_troll.flee_battle()
    print(f"Clubbed troll power {clubbed_troll.attack_power}")
