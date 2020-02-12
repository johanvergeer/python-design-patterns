"""
The intention of the Builder pattern is to find a solution to the telescoping constructor
anti-pattern. The telescoping constructor anti-pattern occurs when the increase of object
constructor parameter combination leads to an exponential list of constructors. Instead of using
numerous constructors, the builder pattern uses another object, a builder, that receives each
initialization parameter step by step and then returns the resulting constructed object at once.

The Builder pattern has another benefit. It can be used for objects that contain flat data
(html code, SQL query, X.509 certificate...), that is to say, data that can't be easily edited.
This type of data cannot be edited step by step and must be edited at once. The best way to
construct such an object is to use a builder class.

In this example we have the Builder pattern variation as described by Joshua Bloch in
`Effective Java 2nd Edition`_.

We want to build :class:`Hero` objects, but its construction is complex because of the many
parameters needed. To aid the user we introduce :class:`HeroBuilder` class.
:class:`HeroBuilder` takes the minimum parameters to build  :class:`Hero` object in its constructor.
After that additional configuration for the  :class:`Hero` object can be done
using the fluent :class:`HeroBuilder` interface.
When configuration is ready the :meth:`HeroBuilder.build` method is called to receive the final  :class:`Hero` object.

.. _Effective Java 2nd Edition: https://www.amazon.com/Effective-Java-2nd-Joshua-Bloch/dp/0321356683
"""

from dataclasses import dataclass
from enum import Enum
from typing import Optional


class Armor(Enum):
    """Armors"""

    CLOTHES = "clothes"
    LEATHER = "leather"
    CHAIN_MAIL = "chain mail"
    PLATE_MAIL = "plate mail"


class HairColor(Enum):
    """Hair colors"""

    WHITE = "white"
    BLOND = "blond"
    RED = "red"
    BROWN = "brown"
    BLACK = "black"


class HairType(Enum):
    """Hair types"""

    BALD = "bald"
    SHORT = "short"
    CURLY = "curly"
    LONG_STRAIGHT = "long straight"
    LONG_CURLY = "long curly"


class Profession(Enum):
    """Professions"""

    WARRIOR = "warrior"
    THIEF = "thief"
    MAGE = "mage"
    PRIEST = "priest"


class Weapon(Enum):
    """Weapons"""

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
    """Builder to create a new :class:`Hero`"""

    def __init__(self, name: str, profession: Profession):
        self._name: str = name
        self._profession: Profession = profession

        self._hair_type: Optional[HairType] = None
        self._hair_color: Optional[HairColor] = None
        self._armor: Optional[Armor] = None
        self._weapon: Optional[Weapon] = None

    def with_hair_type(self, hair_type: HairType) -> "HeroBuilder":
        self._hair_type = hair_type
        return self

    def with_hair_color(self, hair_color: HairColor) -> "HeroBuilder":
        self._hair_color = hair_color
        return self

    def with_armor(self, armor: Armor) -> "HeroBuilder":
        self._armor = armor
        return self

    def with_weapon(self, weapon: Weapon) -> "HeroBuilder":
        self._weapon = weapon
        return self

    def build(self) -> Hero:
        """Builds the :class:`Hero` using the given values"""
        return Hero(
            self._name,
            self._profession,
            self._hair_type,
            self._hair_color,
            self._weapon,
            self._armor,
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
