from ga import GA
from pso import PSO
from rgb import RGB
from sa import SA
from ga_tuning import GATuning
from parameter import Parameter

MAX = 2.048
MIN = -2.048
DIMENSION = 2
ITERATIONS_PER_PARAM = 5


pop_size = Parameter('pop_size', start=4, increment=2, max=200)
mutation_rate = Parameter('mutation_rate', start=0, increment=0.05, max=0.9)
termination_number = Parameter('termination_number', start=50, increment=10, max=500)

ga_tuning = GATuning(DIMENSION, MAX, MIN, ITERATIONS_PER_PARAM)
ga_tuning.run(pop_size, mutation_rate, termination_number)

# ga = GA(DIMENSION, MAX, MIN)
# result = ga.run(100, 0, 500)

# pso = PSO(DIMENSION, MAX, MIN)
# pso.run(400, 1, -1, 200)

# rgb = RGB(DIMENSION, MAX, MIN)
# rgb.run(0.02, 20, 10, 0.1)

# sa = SA(DIMENSION, MAX, MIN)
# sa.run(400, 1, 100, 0.05)
# print(f'Total evaluations: {result.evaluation_counter} Found acceptable solution at: {result.error_threshold_number} Best value: {result.best_solution_value} Best solution: {result.best_solution}')