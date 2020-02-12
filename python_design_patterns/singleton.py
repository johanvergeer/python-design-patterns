"""
Singleton pattern ensures that the class can have only one existing instance per Java
classloader instance and provides global access to it.

One of the risks of this pattern is that bugs resulting from setting a singleton up in a
distributed environment can be tricky to debug, since it will work fine if you debug with a
single classloader. Additionally, these problems can crop up a while after the implementation of
a singleton, since they may start out synchronous and only become async with time, so you it may
not be clear why you are seeing certain changes in behaviour.

There are many ways to implement the Singleton. The first one is the eagerly initialized
instance in :class:`IvoryTower`. Eager initialization implies that the implementation is thread
safe. If you can afford giving up control of the instantiation moment, then this implementation
will suit you fine.
"""

from typing import Optional, cast


class IvoryTower:
    """Singleton class example"""

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
