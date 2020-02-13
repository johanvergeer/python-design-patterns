from abc import ABC, abstractmethod


class StealingMethod(ABC):
    @abstractmethod
    def _pick_target(self) -> str:
        ...

    @abstractmethod
    def _confuse_target(self, target: str):
        ...

    @abstractmethod
    def _steal_the_item(self, target: str):
        ...

    def steal(self):
        target = self._pick_target()
        print(f"The target has been chosen as {target}.")
        self._confuse_target(target)
        self._steal_the_item(target)


class SubtleMethod(StealingMethod):
    def _pick_target(self) -> str:
        return "shop keeper"

    def _confuse_target(self, target: str):
        print(f"Approach the {target} with tears running and hug him!")

    def _steal_the_item(self, target: str):
        print(f"While in close contact grab the {target}'s wallet.")


class HitAndRunMethod(StealingMethod):
    def _pick_target(self) -> str:
        return "old goblin woman"

    def _confuse_target(self, target: str):
        print(f"Approach the {target} from behind.")

    def _steal_the_item(self, target: str):
        print("Grab the handbag and run away fast!")


class HalflingThief:
    def __init__(self, method: StealingMethod):
        self.__method = method

    def steal(self):
        self.__method.steal()

    def change_method(self, method: StealingMethod):
        self.__method = method


if __name__ == "__main__":
    print("Using the hit and run method")
    print("----------------------------")
    thief = HalflingThief(HitAndRunMethod())
    thief.steal()

    print()
    print("Switching to a subtle method")
    print("----------------------------")
    thief.change_method(SubtleMethod())
    thief.steal()
