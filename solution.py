from helpers import Helpers, generate_random_array
import numpy as np
from solution_factory import SolutionFactory

class Solution:
    def __init__(self, helpers: Helpers, solution: list = []) -> None:
        self.solution = solution if len(solution) > 0 else generate_random_array()
        self.value = -1
        self.helpers = helpers
        
        self.update_solution_value()
    
    def update_solution_value(self):
        self.value = self.helpers.rosenbrock(self.solution)
    
    def generate_neighbour(self, scale: float, min: float, max: float) -> 'Solution':
        neighbour_solution = self.solution.copy()
        for i in range(len(neighbour_solution)):
            perturbation = np.random.uniform(low=-scale, high=scale)
            # Ensure values stay within bounds
            neighbour_solution[i] = np.clip(neighbour_solution[i] + perturbation, min, max)

        return SolutionFactory.create_solution(type(self), self.helpers, neighbour_solution)