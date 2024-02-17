from helpers import Helpers, generate_random_population, attach_zero_velocities
import numpy as np
import random

helpers = Helpers()

POP_SIZE = 10
C1 = 2
C2 = 2

def start_pso():
    population = generate_random_population(POP_SIZE)
    pop_best_positions = population.copy()
    pop_best_values = [helpers.rosenbrock(p) for p in population]
    global_best_position = pop_best_positions[pop_best_values.index(min(pop_best_values))]

    #Assign a velocity of 0 to each of the starting pop
    attach_zero_velocities(population)

    print(population)

    #Population is upadted with new velocities (not moved yet)
    population = update_all_solution_velocities(population, pop_best_positions, global_best_position)

    #Move population according to new velocities (in place)
    move_population(population)

    print(population)

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

start_pso()