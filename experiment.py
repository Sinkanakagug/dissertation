from algorithm import Algorithm
from pso import PSO
from rgb import RGB
from rgb_mod import RGB_Mod
from ga import GA
from sa import SA
from result import Result
import csv

#Run each algorithm 100 times, with the specified parameter. Store the results in a separate csv file for each

class Experiment:
    def __init__(self, algorithms: list[Algorithm], parameters: list[list]) -> None:
        for i in range(len(algorithms)):
            algorithm = algorithms[i]
            file_name = get_algorithm_name(algorithm) + '.csv'

            with open(file_name, 'a', newline='') as csvfile:
                csv_writer = csv.writer(csvfile)

                for j in range(100):
                    if len(parameters[i]) > 3:
                        result = algorithm.run(parameters[i][0], parameters[i][1], parameters[i][2], parameters[i][3])
                    else:
                        result = algorithm.run(parameters[i][0], parameters[i][1], parameters[i][2])
                    row = [result.error_threshold_number]
                    csv_writer.writerow(row)


def get_algorithm_name(algorithm: Algorithm) -> str:
    algorithm_type = type(algorithm)

    if algorithm_type == PSO:
        return 'pso'
    if algorithm_type == GA:
        return 'ga'
    if algorithm_type == SA:
        return 'sa'
    if algorithm_type == RGB:
        return 'rgb'
    if algorithm_type == RGB_Mod:
        return 'rgb_mod'