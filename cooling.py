from system import System
from reactor import Reactor

class Cooling(System):
    """Station's reactor cooling system."""

    def repair(self):
        """Cools the reactor by 25 if sufficient power is available. Consumes 10 power.
        Returns:
            A string describing whether the repair was successful.
        """
        r = Reactor()
        if r.power >= 10:
            r.consume_power(10)
            r.cool(25)
            return "Cooling systems have been improved."
        return "Insufficient reactor power!"
