"""
The Facade design pattern is often used when a system is very complex or difficult to understand
because the system has a large number of interdependent classes or its source code is
unavailable. This pattern hides the complexities of the larger system and provides a simpler
interface to the client. It typically involves a single wrapper class which contains a set of
members required by client. These members access the system on behalf of the facade client and
hide the implementation details.

In this example the Facade is (:class:DwarvenGoldmineFacade) and it provides a simpler
interface to the goldmine subsystem.
"""
from abc import ABC, abstractmethod
from enum import Enum
from typing import List


class DwarvenMineWorker(ABC):
    """DwarvenMineWorker is one of the goldmine subsystems."""

    @property
    @abstractmethod
    def name(self) -> str:
        ...

    @abstractmethod
    def work(self):
        ...

    def go_to_sleep(self):
        print(f"{self.name} goes to sleep.")

    def wake_up(self):
        print(f"{self.name} wakes up.")

    def go_home(self):
        print(f"{self.name} goes home.")

    def go_to_mine(self):
        print(f"{self.name} goes to the min.")

    def action(self, *actions: "DwarvenMineWorker.Action"):
        actions_map = {
            DwarvenMineWorker.Action.GO_TO_SLEEP: self.go_to_sleep,
            DwarvenMineWorker.Action.WAKE_UP: self.wake_up,
            DwarvenMineWorker.Action.GO_HOME: self.go_home,
            DwarvenMineWorker.Action.GO_TO_MINE: self.go_to_mine,
            DwarvenMineWorker.Action.WORK: self.work,
        }

        for action in actions:
            actions_map[action]()

    class Action(Enum):
        """Actions performed by a dwarven mine worker"""

        GO_TO_SLEEP = 1
        WAKE_UP = 2
        GO_HOME = 3
        GO_TO_MINE = 4
        WORK = 5


class DwarvenTunnelDigger(DwarvenMineWorker):
    """DwarvenTunnelDigger is one of the goldmine subsystems."""

    @property
    def name(self) -> str:
        return "Dwarven tunnel digger"

    def work(self):
        print(f"{self.name} creates another promising tunnel.")


class DwarvenGoldDigger(DwarvenMineWorker):
    """DwarvenGoldDigger is one of the goldmine subsystems."""

    @property
    def name(self) -> str:
        return "Dwarf gold digger"

    def work(self):
        print(f"{self.name} digs for gold.")


class DwarvenCartOperator(DwarvenMineWorker):
    """DwarvenCartOperator is one of the goldmine subsystems."""

    @property
    def name(self) -> str:
        return "Dwarf cart operator"

    def work(self):
        print(f"{self.name} moves gold chunks out of the mine.")


class DwarvenGoldMineFacade:
    """DwarvenGoldmineFacade provides a single interface through which users can operate the subsystems.

    This makes the goldmine easier to operate and cuts the dependencies from the goldmine user to the subsystems."""

    def __init__(self):
        self._workers = [
            DwarvenGoldDigger(),
            DwarvenCartOperator(),
            DwarvenTunnelDigger(),
        ]

    def start_new_day(self):
        self._perform_actions(
            self._workers,
            DwarvenMineWorker.Action.WAKE_UP,
            DwarvenMineWorker.Action.GO_TO_MINE,
        )

    def dig_out_gold(self):
        self._perform_actions(self._workers, DwarvenMineWorker.Action.WORK)

    def end_day(self):
        self._perform_actions(
            self._workers,
            DwarvenMineWorker.Action.GO_HOME,
            DwarvenMineWorker.Action.GO_TO_SLEEP,
        )

    @staticmethod
    def _perform_actions(
        workers: List[DwarvenMineWorker], *actions: DwarvenMineWorker.Action
    ):
        for worker in workers:
            worker.action(*actions)


if __name__ == "__main__":
    facade = DwarvenGoldMineFacade()
    facade.start_new_day()
    facade.dig_out_gold()
    facade.end_day()
