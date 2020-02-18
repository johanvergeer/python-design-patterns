from abc import ABC, abstractmethod


class Weapon(ABC):
    @abstractmethod
    def use(self) -> None:
        ...


class Sword(Weapon):
    def use(self) -> None:
        print("Swinging the sword.")


class Bow(Weapon):
    def use(self) -> None:
        print("Shooting an arrow")


class Orc:
    def attack(self, weapon: Weapon) -> None:
        weapon.use()


if __name__ == "__main__":
    azog = Orc()
    sword = Sword()

    azog.attack(sword)
