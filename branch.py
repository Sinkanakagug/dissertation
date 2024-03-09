from solution import Solution
import numpy as np
from helpers import Helpers
from solution_factory import SolutionFactory

class Branch(Solution):
    def __init__(self, helpers: Helpers, solution: list = []) -> None:
        Solution.__init__(self, helpers, solution)

    def split_branch(self, branching_factor: int, branching_scale: float, min: float, max: float) -> list['Branch']:
        branches = []
        for i in range(branching_factor):
            branch = self.generate_neighbour(branching_scale, min, max)
            branches.append(branch)
        
        return branches
    
    def get_best_neighbour(self, num_of_neighbours: int, neighbour_scale: float, max: float, min: float) -> 'Branch':
        best_solution = self
        best_value = best_solution.value

        for i in range(num_of_neighbours):
            neighbour = self.generate_neighbour(neighbour_scale, min, max)

            if neighbour.value < best_value:
                best_solution = neighbour
                best_value = neighbour.value

        return best_solution
    
    def grow_branch(self, num_of_neighbours: int, neighbour_scale: float, max: float, min: float) -> 'Branch':
        #Get the best neightbour
        neighbour = self.get_best_neighbour(num_of_neighbours, neighbour_scale, max, min)
        best_neighbour = self
        best_neighbour_value = best_neighbour.value

        #While we keep improving the neighbour
        while(neighbour.value < best_neighbour_value):
            best_neighbour = neighbour
            best_neighbour_value = best_neighbour.value

            neighbour = best_neighbour.get_best_neighbour(num_of_neighbours, neighbour_scale, max, min)
        
        return best_neighbour