from abc import ABC
from enum import Enum


class WeaponType(Enum):
    SHORT_SWORD = "short sword"
    SPEAR = "spear"
    AXE = "axe"
    UNDEFINED = ""


class Weapon(ABC):
    def __init__(self, weapon_type):
        self._weapon_type = weapon_type

    @property
    def weapon_type(self) -> WeaponType:
        return self._weapon_type


class ElfWeapon(Weapon):
    def __str__(self) -> str:
        return f"Elven {self.weapon_type.value}"


class OrcWeapon(Weapon):
    def __str__(self) -> str:
        return f"Orcish {self.weapon_type.value}"


elven_weapons = {weapon_type: ElfWeapon(weapon_type) for weapon_type in WeaponType}


def manufacture_elven_weapon(weapon_type: WeaponType) -> Weapon:
    return elven_weapons[weapon_type]


orc_weapons = {weapon_type: OrcWeapon(weapon_type) for weapon_type in WeaponType}


def manufacture_orc_weapon(weapon_type: WeaponType) -> Weapon:
    return orc_weapons[weapon_type]


if __name__ == "__main__":
    weapon = manufacture_elven_weapon(WeaponType.SPEAR)
    print(weapon)

    weapon = manufacture_orc_weapon(WeaponType.AXE)
    print(weapon)
