from helpers import Helpers, generate_starting_population, fitness_sort_variable, get_random_number_in_range, generate_random_array
from solution import Solution
import numpy as np
import random
from algorithm import Algorithm, sort_population, get_best_solution_from_population
from genetic_solution import GeneticSolution
from solution_factory import SolutionFactory

class GA(Algorithm):
    def run(self, pop_size: int, mutation_rate: float, termination_number: int):
        self.helpers = Helpers()
        counter = 0
        population = generate_starting_population(self.helpers, pop_size, GeneticSolution)
        
        best_solution_obj = get_best_solution_from_population(population)
        best_solution = best_solution_obj.solution
        best_solution_value = best_solution_obj.value

        #Keep going until we have not improved for termination_number of times
        while counter < termination_number:
            #Trim the worst 50% of solutions
            population = self.trim_population(population)

            #Population is now in order of best value, go through, 2 at a time, mating them as parents
            population = self.mate_population(population)
            generation_best = get_best_solution_from_population(population)

            if generation_best.value < best_solution_value:
                best_solution = generation_best.solution
                best_solution_value = generation_best.value
                counter = 0
            
            #Allow population to mutate
            population = self.allow_population_to_mutate(population, mutation_rate)
            counter += 1

        print(self.helpers.evaluation_counter)
        print(best_solution)
        print(best_solution_value)
    
    def mate(self, mother: GeneticSolution, father: GeneticSolution) -> tuple[GeneticSolution, GeneticSolution]:
        child1_solution = []
        child2_solution = []

        for i in range(len(mother.solution)):
            mother_gene = mother.solution[i]
            father_gene = father.solution[i]
            r = random.random()

            child1_solution.append(r * mother_gene + (1 - r) * father_gene)
            child2_solution.append(r * father_gene + (1 - r) * mother_gene)
        
        child1 = SolutionFactory.create_solution(GeneticSolution, self.helpers, child1_solution)
        child2 = SolutionFactory.create_solution(GeneticSolution, self.helpers, child2_solution)

        return child1, child2

    def trim_population(self, population: list[GeneticSolution]) -> list[GeneticSolution]:
        population = sort_population(population)
        return population[:(len(population) // 2)]
    
    def mate_population(self, population: list) -> list[GeneticSolution]:
        new_population:list = population.copy()

        #Get 2 solutions at a time
        for i in range(0, len(population), 2):
            if i >= (len(population) - 1):
                continue
            
            mother: GeneticSolution = population[i]
            father: GeneticSolution = population[i + 1]

            #If both exist
            if mother and father:
                child1, child2 = self.mate(mother, father)
                new_population.extend([child1, child2])
        
        return new_population
    
    def allow_population_to_mutate(self, population: list[GeneticSolution], mutation_rate: float) -> list[GeneticSolution]:
        for solution in population:
            #This will mutate each gene to a random number based on the value of mutation_rate
            solution.mutate(mutation_rate)
        
        return population
