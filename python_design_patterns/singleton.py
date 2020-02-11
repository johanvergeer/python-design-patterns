from typing import Optional, cast


class IvoryTower:
    _instance: Optional["IvoryTower"] = None

    def __new__(cls, *args, **kwargs):
        if cls._instance:
            return cls._instance

        cls._instance = cast(
            "IvoryTower", super(IvoryTower, cls).__new__(cls, *args, **kwargs)
        )
        return cls._instance

    def __str__(self):
        return f"The id of this Ivory Tower is {id(self)}"


if __name__ == "__main__":
    tower_1 = IvoryTower()
    tower_2 = IvoryTower()

    print(tower_1)
    print(tower_2)
