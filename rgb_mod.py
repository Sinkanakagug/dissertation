from helpers import Helpers
import numpy as np
from algorithm import Algorithm
from branch_mod import Branch_Mod
from result import Result
from solution_factory import SolutionFactory

class RGB_Mod(Algorithm):
    def run(self, neighbour_scale: float, num_of_neighbours: int, branching_factor: int, branching_scale: float):
        self.helpers = Helpers()
        starting_solution = SolutionFactory.create_solution(Branch_Mod, self.helpers)
        best_solution: Branch_Mod = starting_solution

        stack: list[Branch_Mod] = []
        stack.append(starting_solution)

        while len(stack) > 0:
            current_solution = stack.pop()
            best_neighbour = current_solution.grow_branch(num_of_neighbours, neighbour_scale, self.max, self.min, best_solution)

            if best_neighbour.value < best_solution.value:
                best_solution = best_neighbour

                branches = best_solution.split_branch(branching_factor, branching_scale, self.min, self.max)

                for b in branches:
                    stack.append(b)

        return Result(self.helpers.evaluation_counter, best_solution.value, self.helpers.error_threshold_number, best_solution.solution)