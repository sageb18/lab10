class Reactor:
    """Singleton class for the reactor system."""
    
    _instance = None
    _initialized = False

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        if not Reactor._initialized:
            self._power = 100
            self._temperature = 30
            Reactor._initialized = True

    @property
    def power(self):
        return self._power

    @property
    def temperature(self):
        return self._temperature

    def consume_power(self, amt):
        """Consumes power from the reactor. Ensures that power does not go below 0%."""

        self._power = max(0, self._power - amt)

    def generate_power(self):
        """Generates power for the reactor. Ensures that power does not exceed 100%."""

        self._power = min(100, self._power + 20)
        self._temperature = min(100, self._temperature + 10)

    def cool(self,amt):
        """Cools down the reactor. Ensures that temperature does not go below 0%."""

        self._temperature = max(0, self._temperature - amt)

    def heat(self, amt):
        """Heats up the reactor. Ensures that temperature does not exceed 100%."""

        self._temperature = min(100, self._temperature + amt)