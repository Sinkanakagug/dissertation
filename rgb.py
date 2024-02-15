from helpers import Helpers, generate_random_solution, generate_neighbour
import numpy as np

MIN = -2.048
MAX = 2.048
DIMENSION = 2
SCALE = 0.02
NUM_OF_NEIGHBOURS = 20
BRANCHING_FACTOR = 10
BRANCHING_SCALE = 0.1

helpers = Helpers()

def start_rgb():
    #Generate a starting solution
    solution = generate_random_solution(DIMENSION, MIN, MAX)
    best_solution = solution.copy()
    best_value = helpers.rosenbrock(solution)

    #Add the starting solution to the stack
    stack = []
    stack.append(best_solution)

    #The exit conditon is if we run out of values in the stack
    while len(stack) > 0:
        #Evaluate the current solution in the stack
        current_solution = stack.pop()
        current_solution_value = helpers.rosenbrock(current_solution)

        #Grow its brach to explore the local area
        best_neighbour, best_neighbour_value = grow_branch(current_solution, current_solution_value)

        #If its the best one we have ever found
        if best_neighbour_value < best_value:
            #Set it as best
            best_solution = best_neighbour
            best_value = best_neighbour_value

            #Generate branches for it
            branches = split_branch(best_solution)

            #Add them to the stack
            for b in branches:
                stack.append(b)

    print(best_solution)
    print(best_value)
    print('Number of evaluations: ' + str(helpers.evaluation_counter))

def evaluate_neighbours(solution, value):
    best_solution = solution
    best_value = value

    for i in range(NUM_OF_NEIGHBOURS):
        neighbour = generate_neighbour(solution, MIN, MAX, SCALE)
        neighbour_value = helpers.rosenbrock(neighbour)

        if neighbour_value < best_value:
            best_solution = neighbour
            best_value = neighbour_value

    return best_solution, best_value

def grow_branch(solution, solution_value):
    neighbour, neighbour_value = evaluate_neighbours(solution, solution_value)

    while(neighbour_value < solution_value):
        solution = neighbour
        solution_value = neighbour_value

        neighbour, neighbour_value = evaluate_neighbours(solution, solution_value)
    
    return solution, solution_value

def split_branch(solution):
    branches = []
    for i in range(BRANCHING_FACTOR):
        branch = solution.copy()
        for i in range(len(branch)):
            perturbation = np.random.uniform(low=-BRANCHING_SCALE, high=BRANCHING_SCALE)
            branch[i] = np.clip(branch[i] + perturbation, MIN, MAX)  # Ensure values stay within bounds
        branches.append(branch)
    
    return branches


start_rgb()