import numpy as np
import random

MIN = -2.048
MAX = 2.048
DIMENSION = 2
ERROR_THRESHOLD = 1e-5

class Helpers:
    def __init__(self):
        self.evaluation_counter = 0
        self.error_threshold_number = 0
        self.min = MIN
        self.max = MAX

    def rosenbrock(self, x):
        self.evaluation_counter += 1
        sum_val = 0
        for i in range(len(x) - 1):
            sum_val += 100 * (x[i + 1] - x[i]**2)**2 + (1 - x[i])**2

        #The first time we get a result under the threshold, record the number of iterations
        if sum_val < ERROR_THRESHOLD and self.error_threshold_number == 0:
            self.error_threshold_number = self.evaluation_counter

        return sum_val


def generate_random_array(dimenion=DIMENSION, max=MAX, min=MIN):
    arr = np.random.rand(dimenion) * (max * 2) + min
    return arr

def get_random_number_in_range():
    return random.uniform(MIN, MAX)

def generate_starting_population(helpers, pop_size, solution_type, starting_population: list[list[float]]=[]) -> list:
    population = []

    if len(starting_population) > 0:
        for i in range(pop_size):
            from solution_factory import SolutionFactory
            solution = SolutionFactory.create_solution(solution_type, helpers, solution=starting_population[i])
            population.append(solution)
    else:
        #Create a new solution for pop size
        for i in range(pop_size):
            from solution_factory import SolutionFactory
            solution = SolutionFactory.create_solution(solution_type, helpers)
            population.append(solution)
    
    return population

def generate_single_solution(helpers, solution_type, solution_numbers):
    from solution_factory import SolutionFactory
    return SolutionFactory.create_solution(solution_type, helpers, solution=solution_numbers)