from helpers import Helpers, generate_starting_population, generate_single_solution
from algorithm import Algorithm, get_best_solution_from_population
from particle import Particle
from result import Result

class PSO(Algorithm):
    def run(self, pop_size: int, max_velocity: float, min_velocity: float, termination_number: int, starting_population: list = [], helpers: Helpers = None):
        if helpers:
            self.helpers = helpers
        else:
            self.helpers = Helpers()

        global_best_position: list = []
        global_best_value: float = -1
        counter: int = 0
        self.population: list[Particle] = []
        if len(starting_population) > 0:
            particles = self.create_particles_from_branches(starting_population, helpers)
            self.population = particles
        else:
            self.population = generate_starting_population(self.helpers, pop_size, Particle)

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
        
        return Result(self.helpers.evaluation_counter, global_best_value, self.helpers.error_threshold_number, best_particle.solution)

    def update_population(self, global_best_position: list, max_velocity: float, min_velocity: float):
        for i in range(len(self.population)):
            self.population[i].update_particle(global_best_position, self.max, self.min, max_velocity, min_velocity)
    
    def initialise_velocities(self, max_velocity: float, min_velocity: float):
        for i in range(len(self.population)):
            self.population[i].initialise_velocity(max_velocity, min_velocity)
    
    def create_particles_from_branches(self, branches: list, helpers):
        particles = []
        for i in range(len(branches)):
            particles.append(generate_single_solution(helpers, Particle, branches[i].solution))
        
        return particles