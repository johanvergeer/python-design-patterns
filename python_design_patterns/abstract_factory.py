"""
The Abstract Factory pattern provides a way to encapsulate a group of individual factories that
have a common theme without specifying their concrete classes. In normal usage, the client
software creates a concrete implementation of the abstract factory and then uses the generic
interface of the factory to create the concrete objects that are part of the theme. The client
does not know (or care) which concrete objects it gets from each of these internal factories,
since it uses only the generic interfaces of their products. This pattern separates the details
of implementation of a set of objects from their general usage and relies on object composition,
as object creation is implemented in methods exposed in the factory interface.

The essence of the Abstract Factory pattern is a factory interface (:class:`KingdomFactory`)
and its implementations ( :class:`ElfKingdomFactory`, :class:`OrcKingdomFactory`). The example uses
both concrete implementations to create a king, a castle and an army.
"""

from abc import ABC, abstractmethod
from enum import Enum

# region Kings


class King(ABC):
    @property
    @abstractmethod
    def description(self) -> str:
        ...


class ElfKing(King):
    @property
    def description(self) -> str:
        return "This is the Elven king!"


class OrcKing(King):
    @property
    def description(self) -> str:
        return "This is the Orc king!"


# endregion

# region Castles


class Castle(ABC):
    @property
    @abstractmethod
    def description(self) -> str:
        ...


class ElfCastle(Castle):
    @property
    def description(self) -> str:
        return "This is the Elven castle!"


class OrcCastle(Castle):
    @property
    def description(self) -> str:
        return "This is the Orc castle!"


# endregion

# region Armies


class Army(ABC):
    @property
    @abstractmethod
    def description(self) -> str:
        ...


class ElfArmy(Army):
    @property
    def description(self) -> str:
        return "This is the Elven army!"


class OrcArmy(Army):
    @property
    def description(self) -> str:
        return "This is the Orc army!"


# endregion

# region Kingdom Factories


class KingdomFactory(ABC):
    @abstractmethod
    def create_castle(self) -> Castle:
        ...

    @abstractmethod
    def create_army(self) -> Army:
        ...

    @abstractmethod
    def create_king(self) -> King:
        ...


class ElfKingdomFactory(KingdomFactory):
    def create_castle(self) -> Castle:
        return ElfCastle()

    def create_army(self) -> Army:
        return ElfArmy()

    def create_king(self) -> King:
        return ElfKing()


class OrcKingdomFactory(KingdomFactory):
    def create_castle(self) -> Castle:
        return OrcCastle()

    def create_army(self) -> Army:
        return OrcArmy()

    def create_king(self) -> King:
        return OrcKing()


# endregion


class KingdomType(Enum):
    ELF = 1
    ORC = 2


def create_kingdom_factory(kingdom_type: KingdomType) -> KingdomFactory:
    factories = {
        KingdomType.ORC: OrcKingdomFactory(),
        KingdomType.ELF: ElfKingdomFactory(),
    }

    return factories[kingdom_type]


if __name__ == "__main__":
    print("Elf kingdom")

    elf_kingdom = create_kingdom_factory(KingdomType.ELF)
    print(elf_kingdom.create_castle().description)
    print(elf_kingdom.create_army().description)
    print(elf_kingdom.create_king().description)

    print()
    print("Orc kingdom")
    orc_kingdom = create_kingdom_factory(KingdomType.ORC)
    print(orc_kingdom.create_castle().description)
    print(orc_kingdom.create_army().description)
    print(orc_kingdom.create_king().description)
