from dataclasses import dataclass
from enum import Enum
from typing import Optional


class Armor(Enum):
    CLOTHES = "clothes"
    LEATHER = "leather"
    CHAIN_MAIL = "chain mail"
    PLATE_MAIL = "plate mail"


class HairColor(Enum):
    WHITE = "white"
    BLOND = "blond"
    RED = "red"
    BROWN = "brown"
    BLACK = "black"


class HairType(Enum):
    BALD = "bald"
    SHORT = "short"
    CURLY = "curly"
    LONG_STRAIGHT = "long straight"
    LONG_CURLY = "long curly"


class Profession(Enum):
    WARRIOR = "warrior"
    THIEF = "thief"
    MAGE = "mage"
    PRIEST = "priest"


class Weapon(Enum):
    DAGGER = "dagger"
    SWORD = "sword"
    AXE = "axe"
    WARHAMMER = "warhammer"
    BOW = "bow"


@dataclass
class Hero:
    name: str
    profession: Profession
    hair_type: Optional[HairType]
    hair_color: Optional[HairColor]
    weapon: Optional[Weapon]
    armor: Optional[Armor]

    def __repr__(self) -> str:
        """
        Why did I use a list instead of naively appending to a string: https://waymoot.org/home/python_string/
        """
        desc = [f"This is a {self.profession.value} named {self.name}"]

        if any([self.hair_type, self.hair_color]):
            desc.append("with")
        if self.hair_color:
            desc.append(self.hair_color.value)
        if self.hair_type:
            desc.append(self.hair_type.value)

            if self.hair_type == HairType.BALD:
                desc.append("head")
            else:
                desc.append("hair")
        if self.armor:
            desc.append(f"wearing {self.armor.value}")
        if self.weapon:
            desc.append(f"wielding {self.weapon.value}")

        return " ".join(desc)


class HeroBuilder:
    def __init__(self, name: str, profession: Profession):
        self.name: str = name
        self.profession: Profession = profession

        self.hair_type: Optional[HairType] = None
        self.hair_color: Optional[HairColor] = None
        self.armor: Optional[Armor] = None
        self.weapon: Optional[Weapon] = None

    def with_hair_type(self, hair_type: HairType) -> "HeroBuilder":
        self.hair_type = hair_type
        return self

    def with_hair_color(self, hair_color: HairColor) -> "HeroBuilder":
        self.hair_color = hair_color
        return self

    def with_armor(self, armor: Armor) -> "HeroBuilder":
        self.armor = armor
        return self

    def with_weapon(self, weapon: Weapon) -> "HeroBuilder":
        self.weapon = weapon
        return self

    def build(self) -> Hero:
        return Hero(
            self.name,
            self.profession,
            self.hair_type,
            self.hair_color,
            self.weapon,
            self.armor,
        )


if __name__ == "__main__":
    hero = (
        HeroBuilder("Legolas", Profession.WARRIOR)
        .with_armor(Armor.CLOTHES)
        .with_hair_color(HairColor.BLOND)
        .with_hair_type(HairType.LONG_STRAIGHT)
        .with_weapon(Weapon.BOW)
        .build()
    )

    print(str(hero))
