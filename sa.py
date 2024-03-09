from algorithm import Algorithm
from helpers import Helpers
from annealing_solution import AnnealingSolution
from solution_factory import SolutionFactory
import math
import random

class SA(Algorithm):
    def run(self, temperature: float, cooling_rate: float, iterations_per_temperature: int, neighbour_scale: float):
        helpers = Helpers()
        current_solution: AnnealingSolution = SolutionFactory.create_solution(AnnealingSolution, helpers)
        best_solution: AnnealingSolution = current_solution

        while temperature > 0:
            for i in range(iterations_per_temperature):
                neighbour = current_solution.generate_neighbour(neighbour_scale, self.min, self.max)

                if neighbour.value < current_solution.value:
                    current_solution = neighbour

                    if neighbour.value < best_solution.value:
                        best_solution = neighbour
                    
                    continue

                error_difference = neighbour.value - current_solution.value

                probability = math.exp(-error_difference / temperature)

                if random.random() < probability:
                    current_solution = neighbour
            
            temperature -= cooling_rate
        
        print(best_solution.solution)
        print(best_solution.value)
        print('Number of evaluations: ' + str(helpers.evaluation_counter))