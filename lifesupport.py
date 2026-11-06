from system import System
from reactor import Reactor

class LifeSupport(System):
    """Station's oxygen life support system.

    Attributes:
        oxygen (int): the percentage of safe levels of oxygen (0-100).
    """

    def __init__(self):
        """Initializes the life support with 80% oxygen."""
        self._oxygen = 80

    @property
    def oxygen(self):
        """Returns the oxygen level of the life support system."""
        return self._oxygen

    def consume(self, amt):
        """Consumes oxygen from the life support system. Ensures that oxygen does not go below 0%."""
        self._oxygen = max(0, self._oxygen - amt)
    
    def repair(self):
        """Repairs the life support system if sufficient power is available. Ensures that oxygen does not exceed 100%."""
        
        r = Reactor()
        if r.power >= 15:
            r.consume_power(15)
            r.heat(5)

            self._oxygen = min(100, self._oxygen + 20)
            return "Life Support has been improved."

        return "Insufficient reactor power!"