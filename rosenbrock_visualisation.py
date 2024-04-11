import numpy as np

from pymoo.problems import get_problem
from pymoo.visualization.fitness_landscape import FitnessLandscape

rosenbrock = get_problem('rosenbrock', n_var=2)

FitnessLandscape(rosenbrock, angle=(45, 45), _type='surface').show()