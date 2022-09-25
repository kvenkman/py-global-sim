from attributes import economy, geography, military, society
class country():
    def __init__(self, name):
        self.name = name

        # initialize attributes
        self.economy = economy()
        self.geography = geography()
        self.military = military()
        self.society = society()
    
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Expected a string value")
        self._name = value
    
    @property
    def population(self):
        return self.society._population

    @population.setter
    def population(self, value):
        self.society.population = value

    def __repr__(self):
        """
        Return a well formatted summary of the object
        """
        pass