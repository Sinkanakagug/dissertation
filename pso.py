from helpers import Helpers, generate_random_population
import numpy as np
import random

helpers = Helpers()

POP_SIZE = 20
C1 = 2
C2 = 2
TERMINATION_NUMBER = 5000

def start_pso():
    counter = 0
    population = generate_random_population(POP_SIZE)
    pop_best_positions = population.copy()
    pop_best_values = [helpers.rosenbrock(p) for p in population]
    best_value_index = pop_best_values.index(min(pop_best_values))
    global_best_position = pop_best_positions[best_value_index]
    global_best_value = pop_best_values[best_value_index]

    #Assign a velocity of 0 to each of the starting pop
    #TODO: CHANGE TO RANDOM VELOCITIES
    attach_zero_velocities(population)

    while counter < TERMINATION_NUMBER:
        #Population is upadted with new velocities (not moved yet)
        population = update_all_solution_velocities(population, pop_best_positions, global_best_position)

        #Move population according to new velocities (in place)
        move_population(population)

        #Calculate fitness of population current positions
        current_positions = remove_velocity_from_population(population)
        current_position_fitnesses = helpers.evaluate_population(current_positions)

        #Update any population best positions in place
        update_population_bests(current_position_fitnesses, pop_best_positions, pop_best_values)

        #Update global best positions
        best_value_index = pop_best_values.index(min(pop_best_values))
        if pop_best_values[best_value_index] > global_best_value:
            global_best_position = pop_best_positions[best_value_index]
            global_best_value = pop_best_values[best_value_index]

            #If globals updated, reset termination counter
            counter = 0
            continue

        counter = counter + 1
    
    print(global_best_position)
    print(global_best_value)
    print('Number of evaluations: ' + str(helpers.evaluation_counter))


def update_all_solution_velocities(population, pop_best_positions, global_best_position):
    new_population = []
    for i in range(len(population)):
        new_population.append(update_solution_velocity(population[i], pop_best_positions[i], global_best_position))

    return new_population

#Take a solution and change its velocity (the position has not been updated yet)
def update_solution_velocity(solution, current_solution_best, global_best_position):
    solution_velocity = solution[1]
    current_position = solution[0]
    new_velocity = []

    for i in range(len(current_position)):
        cognitive = C1 * random.random() * (current_solution_best[i] - current_position[i])
        social = C2 * random.random() * (global_best_position[i] - current_position[i])
        new_velocity.append(solution_velocity[i] + cognitive + social)
    
    return (current_position, new_velocity)

def move_population(population):
    new_population = []

    #Move each solution individually, set the population to the newly moved version
    for solution in population:
        new_population.append(move_solution(solution))

    population = new_population    

#For each positional value, add the velocity to it
def move_solution(solution):
    position = solution[0]
    velocity = solution[1]

    for i in range(len(position)):
        position[i] = position[i] + velocity[i]
    
    return (position, velocity)

#Return just the positions, free from velocities to be evaluated
def remove_velocity_from_population(population):
    return [solutions for solutions, _ in population]

def update_population_bests(current_position_fitnesses, pop_best_positions, pop_best_values):
    #Go through each particle
    for i in range(len(current_position_fitnesses)):
        #If the particles new position is better than the previous best
        if current_position_fitnesses[i][1] < pop_best_values[i]:
            print('here')
            #Replace it
            pop_best_positions[i] = current_position_fitnesses[i][0]
            pop_best_values[i] = current_position_fitnesses[i][1]

#Give each solution in population a starting velocity of 0
def attach_zero_velocities(population):
    dimension = len(population[0])
    for i in range(len(population)):
        population[i] = (population[i], np.zeros(dimension))

start_pso()