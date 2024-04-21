from ga import GA
from pso import PSO
from rgb import RGB
from rgb_mod import RGB_Mod
from sa import SA
from ga_tuning import GATuning
from pso_tuning import PSOTuning
from sa_tuning import SATuning
from rgb_tuning import RGBTuning
from parameter import Parameter
from experiment import Experiment
from solution_factory import SolutionFactory

MAX = 2.048
MIN = -2.048
DIMENSION = 2
ITERATIONS_PER_PARAM = 10

###################################################################################

#Region 1 - Parameter tuning

###################################################################################

#Genetic algorithm tuning
# pop_size = Parameter('pop_size', start=50, increment=10, max=300)
# mutation_rate = Parameter('mutation_rate', start=0, increment=0.001, max=0.01)
# termination_number = Parameter('termination_number', start=50, increment=50, max=400)

# ga_tuning = GATuning(DIMENSION, MAX, MIN, ITERATIONS_PER_PARAM)
# ga_tuning.run(pop_size, mutation_rate, termination_number)

#Particle swarm optimisation tuning
# pop_size = Parameter('pop_size', start=100, increment=20, max=400)
# max_velocity = Parameter('max_velocity', start=0.1, increment=0.1, max=1)
# min_velocity = Parameter('min_velocity', start=-0.1, increment=-0.1, max=-1)
# termination_number = Parameter('termination_number', start=200, increment=50, max=400)

# pso_tuning = PSOTuning(DIMENSION, MAX, MIN, ITERATIONS_PER_PARAM)
# pso_tuning.run(pop_size, max_velocity, min_velocity, termination_number)

#Simulated annealing tuning
# temperature = Parameter('temperature', start=50, increment=50, max=300)
# cooling_rate = Parameter('cooling_rate', start=1, increment=2, max=10)
# iterations_per_temperature = Parameter('iterations_per_temperature', start=80, increment=20, max=200)
# neighbour_scale = Parameter('neighbour_scale', start=0.01, increment=0.01, max=0.2)

# sa_tuning = SATuning(DIMENSION, MAX, MIN, ITERATIONS_PER_PARAM)
# sa_tuning.run(temperature, cooling_rate, iterations_per_temperature, neighbour_scale)

#Random growing branches tuning
# neighbour_scale = Parameter('neighbour_scale', start=0.01, increment=0.01, max=0.03)
# num_of_neighbours = Parameter('num_of_neighbours', start=5, increment=5, max=50)
# branching_factor = Parameter('branching_factor', start=2, increment=2, max=40)
# branching_scale = Parameter('branching_scale', start=0.05, increment=0.05, max=0.2)

# rgb_tuning = RGBTuning(DIMENSION, MAX, MIN, ITERATIONS_PER_PARAM)
# rgb_tuning.run(neighbour_scale, num_of_neighbours, branching_factor, branching_scale)

###################################################################################

#End of region 1 - Parameter tuning

###################################################################################



###################################################################################

#Region 2 - Single run of an algorithm

###################################################################################

# ga = GA(DIMENSION, MAX, MIN)
# result = ga.run(100, 0, 500)

# rgb = RGB(DIMENSION, MAX, MIN)
# result = rgb.run(0.02, 10, 20, 0.05)

# rgb_mod = RGB_Mod(DIMENSION, MAX, MIN)
# result = rgb_mod.run(0.02, 10, 20, 0.05)

# # # pso = PSO(DIMENSION, MAX, MIN)
# # # result = pso.run(100, 0.05, -0.05, 200)

# # # sa = SA(DIMENSION, MAX, MIN)
# # # sa.run(400, 1, 100, 0.05)
# print(f'Total evaluations: {result.evaluation_counter} Found acceptable solution at: {result.error_threshold_number} Best value: {result.best_solution_value} Best solution: {result.best_solution}')
# exit()

###################################################################################

#End of region 2 - Single run of an algorithm

###################################################################################



###################################################################################

#Region 3 - Data collection

###################################################################################


#Data collection
# algorithms = []
# params = []

# ga = GA(DIMENSION, MAX, MIN)
# ga_params = [130, 0.006, 50]

# pso = PSO(DIMENSION, MAX, MIN)
# pso_params = [130, 0.6, -0.1, 300]

# rgb = RGB(DIMENSION, MAX, MIN)
# rgb_params = [0.02, 10, 20, 0.05]

# sa = SA(DIMENSION, MAX, MIN)
# sa_params = [100, 1, 160, 0.11]

# rgb_mod = RGB_Mod(DIMENSION, MAX, MIN)
# rgb_mod_params = [0.02, 10, 20, 0.05]

# algorithms.append(ga)
# algorithms.append(pso)
# algorithms.append(rgb)
# algorithms.append(sa)
# algorithms.append(rgb_mod)

# params.append(ga_params)
# params.append(pso_params)
# params.append(rgb_params)
# params.append(sa_params)
# params.append(rgb_mod_params)

# experiment = Experiment(algorithms, params)

###################################################################################

#End of region 3 - Data collection

###################################################################################