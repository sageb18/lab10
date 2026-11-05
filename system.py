import abc

class System(abc.ABC):
    """Abstract interface for the ship system."""
    
    @abc.abstractmethod
    def repair(self):
        """Repairs the system."""
        pass