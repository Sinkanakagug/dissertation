import numpy as np
import random

MIN = -2.048
MAX = 2.048
DIMENSION = 2


class Helpers:
    def __init__(self):
        self.evaluation_counter = 0
        self.min = MIN
        self.max = MAX

    def rosenbrock(self, x):
        self.evaluation_counter += 1
        sum_val = 0
        for i in range(len(x) - 1):
            sum_val += 100 * (x[i + 1] - x[i]**2)**2 + (1 - x[i])**2
        return sum_val

    #Take a list of solutions and add a fitness
    def evaluate_population(self, population):
        evaluated_population = []
        # Evaluate every solution in the population, return list of tuples matching solution with fitness
        for i in range(len(population)):
            solution_fitness = self.rosenbrock(population[i])
            evaluated_population.append((population[i], solution_fitness))
        return evaluated_population


def generate_random_solution():
    solution = np.random.rand(DIMENSION) * (MAX * 2) + MIN
    return solution


def generate_random_population(pop_size):
    population = []
    for i in range(pop_size):
        population.append(generate_random_solution())
    return population


def generate_neighbour(solution, scale):
    neighbour = solution.copy()
    for i in range(len(neighbour)):
        perturbation = np.random.uniform(low=-scale, high=scale)
        # Ensure values stay within bounds
        neighbour[i] = np.clip(neighbour[i] + perturbation, MIN, MAX)
    return neighbour


def fitness_sort_variable(tuple):
    return tuple[1]


def get_random_number_in_range():
    return random.uniform(MIN, MAX)