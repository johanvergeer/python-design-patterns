from typing import Callable


def projectile_strategy():
    print(
        "You shoot the dragon with the magical crossbow and it falls dead on the ground!"
    )


def melee_strategy():
    print("With your Excalibur you sever the dragon's head!")


def spell_strategy():
    print(
        "You cast the spell of disintegration and the dragon vaporizes in a pile of dust!"
    )


class DragonSlayer:
    def __init__(self, strategy: Callable):
        self._strategy = strategy

    def change_strategy(self, strategy: Callable):
        self._strategy = strategy

    def go_to_battle(self):
        self._strategy()


if __name__ == "__main__":
    print("Green dragon spotted ahead!")
    slayer = DragonSlayer(melee_strategy)
    slayer.go_to_battle()

    print("Red dragon emerges.")
    slayer.change_strategy(projectile_strategy)
    slayer.go_to_battle()

    print("Black dragon lands before you.")
    slayer.change_strategy(spell_strategy)
    slayer.go_to_battle()
