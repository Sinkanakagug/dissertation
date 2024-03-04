from solution import Solution
import random
from helpers import get_random_number_in_range, Helpers

class GeneticSolution(Solution):
    def __init__(self, helpers: Helpers, solution: list = []) -> None:
        Solution.__init__(self, helpers, solution)

    #Based on the mutation rate, mutate a gene randomly
    def mutate(self, mutation_rate: float):
        for i in range(len(self.solution)):
            r = random.random()

            #Randomly mutate the gene on a rate of mutation rate
            if r < mutation_rate:
                self.solution[i] = get_random_number_in_range()
                self.update_solution_value()