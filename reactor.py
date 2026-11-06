class Reactor:
    """Singleton class representing the space station's shared power supply.

    Attributes:
        power (int): the amount of power generated (0-100).
        temperature (int): the reactor's temperature (0-100).
    """

    _instance = None
    _initialized = False

    def __new__(cls):
        """Constructs the Reactor if it hasn't been constructed yet, otherwise returns the existing instance."""
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        """Initializes the power to 100 and temperature to 30 if the Reactor hasn't been initialized yet."""
        if not Reactor._initialized:
            self._power = 100
            self._temperature = 30
            Reactor._initialized = True

    @property
    def power(self):
        """Returns the reactor's power level."""
        return self._power

    @property
    def temperature(self):
        """Returns the reactor's temperature."""
        return self._temperature

    def consume_power(self, amt):
        """Consumes power from the reactor. Ensures that power does not go below 0%."""

        self._power = max(0, self._power - amt)

    def generate_power(self):
        """Generates 20 power and 10 heat. Ensures that power and temperature do not exceed 100%."""

        self._power = min(100, self._power + 20)
        self._temperature = min(100, self._temperature + 10)

    def cool(self, amt):
        """Cools down the reactor. Ensures that temperature does not go below 0%."""

        self._temperature = max(0, self._temperature - amt)

    def heat(self, amt):
        """Heats up the reactor. Ensures that temperature does not exceed 100%."""

        self._temperature = min(100, self._temperature + amt)
