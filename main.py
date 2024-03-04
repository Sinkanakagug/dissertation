from ga import GA
from pso import PSO
from rgb import RGB
from sa import SA

MAX = 2.048
MIN = -2.048
DIMENSION = 2

# ga = GA(DIMENSION, MAX, MIN)
# ga.run(100, 0, 500)

# pso = PSO(DIMENSION, MAX, MIN)
# pso.run(400, 1, -1, 200)

# rgb = RGB(DIMENSION, MAX, MIN)
# rgb.run(0.02, 40, 15, 0.15)

sa = SA(DIMENSION, MAX, MIN)
sa.run(400, 1, 100, 0.05)