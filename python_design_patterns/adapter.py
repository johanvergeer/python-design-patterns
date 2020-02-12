"""
An adapter helps two incompatible interfaces to work together. This is the real world definition
for an adapter. Interfaces may be incompatible but the inner functionality should suit the need.
The Adapter design pattern allows otherwise incompatible classes to work together by converting
the interface of one class into an interface expected by the clients.

There are two variations of the Adapter pattern: The class adapter implements the adaptee's
interface whereas the object adapter uses composition to contain the adaptee in the adapter
object. This example uses the object adapter approach.

The Adapter (:class:`FishingBoatAdapter`) converts the interface of the adaptee class
(:class:`FishingBoat`) into a suitable one expected by the client (:class:`RowingBoat`).

The story of this implementation is this: Pirates are coming! we need a :class:`RowingBoat` to flee!
We have a :class:`FishingBoat` and our captain. We have no time to make up a new ship!
We need to reuse this :class:`FishingBoat`. The captain needs a rowing boat which he can operate.
The spec is in :class:`RowingBoat`. We will use the Adapter pattern to reuse :class:`FishingBoat`.
"""

from typing import Protocol


class RowingBoat(Protocol):
    def row(self):
        ...


class FishingBoat:
    """A boat to go fishing"""
    def sail(self):
        print("The fishing boat is sailing")


class Captain:
    def __init__(self, rowing_boat: RowingBoat):
        self.rowing_boat = rowing_boat

    def row(self):
        self.rowing_boat.row()


class FishingBoatAdapter(RowingBoat):
    def __init__(self):
        self.fishing_boat = FishingBoat()

    def row(self):
        self.fishing_boat.sail()


if __name__ == "__main__":
    captain = Captain(FishingBoatAdapter())

    captain.row()
