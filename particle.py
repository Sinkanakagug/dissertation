from helpers import Helpers, generate_random_array
from solution import Solution
import random

#These are constants that will not change
C1 = 2
C2 = 2
W = 0.1

class Particle(Solution):
    def __init__(self, helpers: Helpers, solution: list = []) -> None:
        Solution.__init__(self, helpers, solution)

        self.velocity = []
        self.best_position = []
        self.best_value = -1

        #Initialise the best to what we are now
        self.best_position = self.solution
        self.best_value = self.value


    def move_particle(self, max: float, min: float):
        # Add the velocity to the the position
        for i in range(len(self.solution)):
            self.solution[i] = self.solution[i] + self.velocity[i]

            # If we have gone outside the maximum, prevent it
            if self.solution[i] > max:
                self.solution[i] = max
                continue

            # If we have gone outside the minimum, prevent it
            if self.solution[i] < min:
                self.solution[i] = min
                continue

    def update_velocity(self, global_best_position: list, max_velocity: float, min_velocity: float):
        c_random = random.random()
        s_random = random.random()

        #Update particle's velocity value
        for i in range(len(self.solution)):
            cognitive = C1 * c_random * (self.best_position[i] - self.solution[i])
            social = C2 * s_random * (global_best_position[i] - self.solution[i])
            self.velocity[i] = W * (cognitive + social + self.velocity[i])

            if self.velocity[i] > max_velocity:
                self.velocity[i] = max_velocity

            if self.velocity[i] < min_velocity:
                self.velocity[i] = min_velocity
    
    def check_solution_quality_and_update_best(self):
        #Update the position value
        self.update_solution_value()

        #If its the best one this particle has seen, update the best
        if self.value < self.best_value:
            self.best_position = self.solution
            self.best_value = self.value

    def update_particle(self, global_best_position: list, max: float, min: float, max_velocity: float, min_velocity: float):
        self.move_particle(max, min)
        self.check_solution_quality_and_update_best()
        self.update_velocity(global_best_position, max_velocity, min_velocity)

    # Generate the starting velocity, randomly between 1 and -1
    def initialise_velocity(self, max_velocity: float, min_velocity: float):
        self.velocity = generate_random_array(max=max_velocity, min=min_velocity)