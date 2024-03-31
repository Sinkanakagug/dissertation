from abc import abstractmethod
from solution import Solution
import numpy as np
from result import Result

class Algorithm:
    def __init__(self, dimension: int, max: float, min: float) -> None:
        self.dimension = dimension
        self.min = min
        self.max = max
        self.name = ''

    @abstractmethod
    def run(self, **kwargs) -> Result:
        pass
    
def sort_population(population: list[Solution]) -> list[Solution]:
    return sorted(population, key=lambda solution: solution.value)

#Get the best performing solution in a population
def get_best_solution_from_population(population)-> Solution:
    return min(population, key=lambda solution: solution.value)