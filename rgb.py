from helpers import Helpers
import numpy as np
from algorithm import Algorithm
from branch import Branch
from result import Result
from solution_factory import SolutionFactory

class RGB(Algorithm):
    def run(self, neighbour_scale: float, num_of_neighbours: int, branching_factor: int, branching_scale: float):
        self.helpers = Helpers()
        starting_solution = SolutionFactory.create_solution(Branch, self.helpers)
        best_solution = starting_solution

        stack: list[Branch] = []
        stack.append(starting_solution)

        while len(stack) > 0:
            current_solution = stack.pop()
            best_neighbour = current_solution.grow_branch(num_of_neighbours, neighbour_scale, self.max, self.min)

            if best_neighbour.value < best_solution.value:
                best_solution = best_neighbour

                branches = best_solution.split_branch(branching_factor, branching_scale, self.min, self.max)

                for b in branches:
                    stack.append(b)
        
        return Result(self.helpers.evaluation_counter, best_solution.value, self.helpers.error_threshold_number, best_solution.solution)