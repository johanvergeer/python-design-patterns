from typing import Protocol


class RowingBoat(Protocol):
    def row(self):
        ...


class FishingBoat:
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
