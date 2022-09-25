from abc import ABC, abstractmethod

class attribute(ABC):

    def __init__(self):
        pass

    @abstractmethod
    def step(self):
        raise NotImplementedError


class economy(attribute):
    def __init__(self):
        self.gdp = None
        self.gdp_rate = None        
        pass

    def step(self):
        pass

class geography(attribute):
    def __init__(self):
        pass

    def step(self):
        pass

class military(attribute):
    def __init__(self):
        self.at_war = False
        pass

    def step(self):
        pass

class society(attribute):
    def __init__(self):
        self.population = 0
        self.population_rate = 0
        self.male_ratio = 0.5
        self.female_ratio = 1 - self.male_ratio

        self.immigration_rate = 0
        self.emigration_rate = 0
        
    @property
    def population(self):
        return self._population

    @population.setter
    def population(self, value):
        if not isinstance(value, int):
            raise TypeError("Expected int value")
        self._population = value

    def step(self):
        population_step = int((self.population_rate + self.immigration_rate - self.emigration_rate)*self.population/100)
        self.population += population_step
