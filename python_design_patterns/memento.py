"""
The Memento pattern is a software design pattern that provides the ability to restore an object
to its previous state (undo via rollback).

<p>The Memento pattern is implemented with three objects: the originator, a caretaker and a
memento. The originator is some object that has an internal state. The caretaker is going to do
something to the originator, but wants to be able to undo the change. The caretaker first asks
the originator for a memento object. Then it does whatever operation (or sequence of operations)
it was going to do. To roll back to the state before the operations, it returns the memento
object to the originator. The memento object itself is an opaque object (one which the caretaker
cannot, or should not, change). When using this pattern, care should be taken if the originator
may change other objects or resources - the memento pattern operates on a single object.

In this example the object (:class:`Star`) gives out a "memento" (:class:`StarMemento`) that
contains the state of the object. Later on the memento can be set back to the object restoring
the state.
"""

from dataclasses import dataclass
from enum import Enum
from typing import cast

from typing_extensions import Protocol


class StarMemento(Protocol):
    """External interface to memento."""

    ...


class StarType(Enum):
    """Types of stars"""

    SUN = "sun"
    RED_GIANT = "red giant"
    WHITE_DWARF = "white dwarf"
    SUPERNOVA = "supernova"
    DEAD = "dead star"
    UNDEFINED = ""


class Star:
    """Star uses "mementos" to store and restore state."""

    def __init__(self, start_type: StarType, start_age: int, start_mass: int):
        self.star_type: StarType = start_type
        self.age_years: int = start_age
        self.mass_tons: int = start_mass

    def time_passes(self):
        """Makes time pass for the star."""

        old_new = {
            StarType.SUN: StarType.RED_GIANT,
            StarType.RED_GIANT: StarType.WHITE_DWARF,
            StarType.WHITE_DWARF: StarType.SUPERNOVA,
            StarType.SUPERNOVA: StarType.DEAD,
        }

        self.star_type = old_new.get(self.star_type, StarType.DEAD)

        if self.star_type == StarType.DEAD:
            self.age_years *= 2
            self.mass_tons = 0
        else:
            self.age_years *= 2
            self.mass_tons *= 8

    def get_memento(self) -> StarMemento:
        """Gets a :class:`StarMemento` from the current state"""
        return Star.StarMementoInternal(self.star_type, self.age_years, self.mass_tons)

    def set_memento(self, memento: StarMemento):
        """Sets values on start from :class:StarMemento"""
        state = cast(Star.StarMementoInternal, memento)
        self.star_type = state.star_type
        self.age_years = state.age_years
        self.mass_tons = state.mass_tons

    def __str__(self):
        return f"{self.star_type.value}, age: {self.age_years} years, mass: {self.mass_tons} tons."

    @dataclass
    class StarMementoInternal(StarMemento):
        """:class:`StarMemento` implementation."""

        star_type: StarType
        age_years: int
        mass_tons: int


if __name__ == "__main__":
    states = []

    star = Star(StarType.SUN, 1_0000_000, 500_000)
    print(star)
    states.append(star.get_memento())

    star.time_passes()
    print(star)
    states.append(star.get_memento())

    star.time_passes()
    print(star)
    states.append(star.get_memento())

    star.time_passes()
    print(star)
    states.append(star.get_memento())

    star.time_passes()
    print(star)
    states.append(star.get_memento())

    while len(states) > 0:
        star.set_memento(states.pop())
        print(star)
