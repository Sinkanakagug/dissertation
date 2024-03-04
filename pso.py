from helpers import Helpers, generate_random_array, MIN, MAX, generate_starting_population
from solution import Solution
import numpy as np
import random
from algorithm import Algorithm, get_best_solution_from_population
from particle import Particle

class PSO(Algorithm):
    def run(self, pop_size: int, max_velocity: float, min_velocity: float, termination_number: int):
        self.helpers = Helpers()
        global_best_position: list = []
        global_best_value: float = -1
        counter: int = 0
        self.population: list[Particle] = generate_starting_population(self.helpers, pop_size, Particle)

        #Give each particle a velocity
        self.initialise_velocities(max_velocity, min_velocity)

        #Set the global best
        best_particle: Particle = get_best_solution_from_population(self.population) 
        global_best_position: list = best_particle.solution
        global_best_value: list = best_particle.value

        while counter < termination_number:
            #For each particle, move it to the new position, evaluate it. then update its new velocity
            self.update_population(global_best_position, max_velocity, min_velocity)
            best_particle = get_best_solution_from_population(self.population)

            #If the best particle in the current iteration is the best ever
            if best_particle.value < global_best_value:
                global_best_position = best_particle.solution
                global_best_value = best_particle.value
                counter = 0
                continue

            counter += 1
        
        print(self.helpers.evaluation_counter)
        print(global_best_position)
        print(global_best_value)

    def update_population(self, global_best_position: list, max_velocity: float, min_velocity: float):
        for i in range(len(self.population)):
            self.population[i].update_particle(global_best_position, self.max, self.min, max_velocity, min_velocity)
    
    def initialise_velocities(self, max_velocity: float, min_velocity: float):
        for i in range(len(self.population)):
            self.population[i].initialise_velocity(max_velocity, min_velocity)