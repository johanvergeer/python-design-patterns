from typing_extensions import Protocol


class DragonSlayingStrategy(Protocol):
    def execute(self):
        ...


class ProjectileStrategy(DragonSlayingStrategy):
    def execute(self):
        print(
            "You shoot the dragon with the magical crossbow and it falls dead on the ground!"
        )


class SpellStrategy(DragonSlayingStrategy):
    def execute(self):
        print(
            "You cast the spell of disintegration and the dragon vaporizes in a pile of dust!"
        )


class MeleeStrategy(DragonSlayingStrategy):
    def execute(self):
        print("With your Excalibur you sever the dragon's head!")


class DragonSlayer:
    def __init__(self, strategy: DragonSlayingStrategy):
        self._strategy = strategy

    def change_strategy(self, strategy: DragonSlayingStrategy):
        self._strategy = strategy

    def go_to_battle(self):
        self._strategy.execute()


if __name__ == "__main__":
    print("Green dragon spotted ahead!")
    slayer = DragonSlayer(MeleeStrategy())
    slayer.go_to_battle()

    print("Red dragon emerges.")
    slayer.change_strategy(ProjectileStrategy())
    slayer.go_to_battle()

    print("Black dragon lands before you.")
    slayer.change_strategy(SpellStrategy())
    slayer.go_to_battle()
