from algorithm import Algorithm
from pso import PSO
from rgb import RGB
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

                for i in range(100):
                    result = algorithm.run(parameters[i])
                    row = [result.error_threshold_number]
                    csv_writer.writerow(row)


def get_algorithm_name(algorithm: Algorithm) -> str:
    type = type(algorithm)

    if type == PSO:
        return 'pso'
    if type == GA:
        return 'ga'
    if type == SA:
        return 'sa'
    if type == RGB:
        return 'rgb'