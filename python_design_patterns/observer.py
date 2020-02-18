import itertools
from enum import Enum
from typing import Set

from typing_extensions import Protocol


class WeatherType(Enum):
    SUNNY = 1
    RAINY = 2
    WINDY = 3
    COLD = 4


weather_types = itertools.cycle([t_ for t_ in WeatherType])


class WeatherObserver(Protocol):
    """Observer interface"""

    def update(self, weather_type: WeatherType):
        """Changes the weather""" ""
        ...


class Weather:
    def __init__(self):
        self._observers: Set[WeatherObserver] = set()
        self._current_weather = next(weather_types)

    def add_observer(self, observer: WeatherObserver):
        """Adds an observer"""
        self._observers.add(observer)

    def remove_observer(self, observer: WeatherObserver):
        """Removes an observer"""
        self._observers.remove(observer)

    def time_passes(self):
        """Makes time pass for the weather"""

        self._current_weather = next(weather_types)

        self._notify_observers()

    def _notify_observers(self):
        for obs in self._observers:
            obs.update(self._current_weather)


class Hobbits(WeatherObserver):
    def update(self, weather_type: WeatherType):
        messages = {
            WeatherType.SUNNY: "The happy hobbits bade in the warm sun.",
            WeatherType.COLD: "The hobbits are shivering in the cold weather.",
            WeatherType.RAINY: "The hobbits look for cover from the rain.",
            WeatherType.WINDY: "The hobbits hold their hats tightly in the windy weather.",
        }

        print(messages[weather_type])


class Orcs(WeatherObserver):
    def update(self, weather_type: WeatherType):
        messages = {
            WeatherType.SUNNY: "The sun hurts the orcs' eyes.",
            WeatherType.COLD: "The orcs are freezing cold.",
            WeatherType.RAINY: "The orcs are dripping wet.",
            WeatherType.WINDY: "The orc smell almost vanishes in the wind.",
        }

        print(messages[weather_type])


if __name__ == "__main__":
    weather = Weather()
    weather.add_observer(Hobbits())
    weather.add_observer(Orcs())

    weather.time_passes()
    weather.time_passes()
    weather.time_passes()
    weather.time_passes()
