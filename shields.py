from system import System
from reactor import Reactor

class Shields(System):
    """Station's shield system."""
    
    def __init__(self):
        """Initializes the shields with 50%."""
        self._shields = 50

    @property
    def shields(self):
        """Returns the shield level of the shield system."""
        return self._shields

    def damage(self, amt):
        """Damages the shield system. Ensures that shields do not go below 0%."""
        self._shields = max(0, self._shields - amt)
    
    def repair(self):
        """Repairs the shield system if sufficient power is available. Ensures that shields do not exceed 100%."""
        
        r = Reactor()
        if r.power >= 20:
            r.consume_power(20)
            r.heat(5)

            self._shields = min(100, self._shields + 25)
            return "Shields have been improved."

        return "Insufficient reactor power!"