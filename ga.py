from helpers import Helpers, generate_random_population, fitness_sort_variable, get_random_number_in_range
import numpy as np
import random

helpers = Helpers()

POP_SIZE = 32
ERROR_THRESHOLD = 10 ** -5
MUTATION_RATE = 0.2

def start_ga():
    population = generate_random_population(POP_SIZE)
    best_solution = []
    best_solution_value = 1

    while (best_solution_value > ERROR_THRESHOLD):
        # Get the fitness of the whole population
        evaluated_population = helpers.evaluate_population(population)

        parents = get_parents_from_evaluated_population(evaluated_population)

        best_parent_value = get_best_parent_value(parents)
        parents = remove_fitness_from_parents(parents)

        if best_parent_value < best_solution_value:
            best_solution_value = best_parent_value
            best_solution = parents[0]
        
        population = mate_parents(parents)
        mutate_population(population)
    
    print(best_solution)
    print(best_solution_value)
    print('Number of evaluations: ' + str(helpers.evaluation_counter))

def get_parents_from_evaluated_population(evaluated_population):
    # Sort based on fitness
    sorted_population = sorted(evaluated_population, key=fitness_sort_variable)

    # 'Kill' off the worst performing half to use as parents
    return sorted_population[:(len(sorted_population) // 2)]

#Go back to the trimmed population only
def remove_fitness_from_parents(parents):
    return [solutions for solutions, _ in parents]

#Return the best of the passed in parents
def get_best_parent_value(parents):
    return parents[0][1]

def mate_parents(parents):
    #Randomise which paretn mates with which
    random.shuffle(parents)

    mated_population = []

    #Step of 2, to deal with each parent once, in pairs
    for i in range(0, len(parents), 2):
        mother, father = parents[i], parents[i + 1]
        child1, child2 = mate(mother, father)

        mated_population.extend([mother, father, child1, child2])
    
    return mated_population

def mate(mother, father):
    child1 = []
    child2 = []

    #For each gene in both solutions
    for gene1, gene2 in zip(mother, father):
        r = random.random()
        #Apply mating function to gene from mother and gene from father
        child1.append(r * gene1 + (1 - r) * gene2)
        child2.append(r * gene2 + (1 - r) * gene1)

    return child1, child2

def mutate_population(population):
    #Go through all solutions
    for i in range(len(population)):
        #And all genes in each solution
        for j in range(len(population[i])):
            r = random.random()

            #Randomly mutate the gene on a rate of mutation rate
            if r < MUTATION_RATE:
                population[i][j] = get_random_number_in_range()
    
    return population

start_ga()