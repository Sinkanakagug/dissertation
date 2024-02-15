import numpy as np

class Helpers:
    def __init__(self):
        self.evaluation_counter = 0

    def rosenbrock(self, x):
        self.evaluation_counter += 1
        sum_val = 0
        for i in range(len(x) - 1):
            sum_val += 100 * (x[i + 1] - x[i]**2)**2 + (1 - x[i])**2
        return sum_val
    
def generate_random_solution(dimension, min, max):
        solution = np.random.rand(dimension) * (max * 2) + min
        return solution

def generate_neighbour(solution, min, max, scale):
    neighbour = solution.copy()
    for i in range(len(neighbour)):
        perturbation = np.random.uniform(low=-scale, high=scale)
        neighbour[i] = np.clip(neighbour[i] + perturbation, min, max)  # Ensure values stay within bounds
    return neighbour