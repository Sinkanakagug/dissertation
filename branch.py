from solution import Solution
import numpy as np
from helpers import Helpers
from solution_factory import SolutionFactory

class Branch(Solution):
    def __init__(self, helpers: Helpers, solution: list = []) -> None:
        Solution.__init__(self, helpers, solution)

    def split_branch(self, branching_factor: int, branching_scale: float, min: float, max: float):
        branches = []
        for i in range(branching_factor):
            branch = self.solution.copy()
            for i in range(len(branch)):
                perturbation = np.random.uniform(low=-branching_scale, high=branching_scale)
                branch[i] = np.clip(branch[i] + perturbation, min, max)  # Ensure values stay within bounds
            
            new_branch = SolutionFactory.create_solution(Branch, self.helpers, branch)
            branches.append(new_branch)
        
        return branches
    
    def get_best_neighbour(self, num_of_neighbours: int, neighbour_scale: float, max: float, min: float) -> 'Branch':
        best_solution = self

        for i in range(num_of_neighbours):
            neighbour = self.generate_neighbour(neighbour_scale, min, max)

            if neighbour.value < best_solution.value:
                best_solution = neighbour

        return best_solution
    
    def grow_branch(self, num_of_neighbours: int, neighbour_scale: float, max: float, min: float) -> 'Branch':
        #Get the best neightbour
        neighbour = self.get_best_neighbour(num_of_neighbours, neighbour_scale, max, min)
        best_neighbour = self

        #While we keep improving the neightbour
        while(neighbour.value < best_neighbour.value):
            best_neighbour = neighbour
            neighbour = self.get_best_neighbour(num_of_neighbours, neighbour_scale, max, min)
        
        return best_neighbour