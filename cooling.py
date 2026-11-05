from system import System
from reactor import Reactor

class Cooling(System):
    """Cooling system for the reactor."""

    def repair(self):
        r = Reactor()
        if r.power >= 10:
            r.consume_power(10)
            r.cool(25)
            return "Cooling systems have been improved."
        return "Insufficient reactor power!"