from abc import abstractmethod
from parameter import Parameter
from result import Result
from tuning_average_results import TuningAverageResults
from best_average import BestAverage
import math

class ParameterTuning:
    def __init__(self, dimension: int, max: float, min: float, iterations_per_param: int) -> None:
        self.dimension = dimension
        self.max = max
        self.min = min
        self.iterations_per_param = iterations_per_param
        self.best_params = []
        # self.best_average_value = BestAverage()
        self.best_average_error_threshold_number = -1
        self.best_success_percentage = -1
        self.total_iterations_to_complete = 0
        self.iterations = 0
        self.percentage = -1

    @abstractmethod
    def run(self, **kwargs):
        pass
    
    def evaluate_averages(self, averages: TuningAverageResults, parameters: list[Parameter]):
        #Check if the average values beat the previously stored average. Pass in max or min for whether we want the value to be maximised of minimised
        if averages.percentage_success > self.best_success_percentage:
            self.best_success_percentage = averages.percentage_success
            self.best_average_error_threshold_number = averages.error_threshold_number
            self.best_params = [{'name': param.name, 'current': param.current} for param in parameters]
            return
        
        if averages.percentage_success == self.best_success_percentage:
            if averages.error_threshold_number < self.best_average_error_threshold_number or self.best_average_error_threshold_number == -1:
                self.best_success_percentage = averages.percentage_success
                self.best_average_error_threshold_number = averages.error_threshold_number
                self.best_params = [{'name': param.name, 'current': param.current} for param in parameters]
                return
        # self.best_average_value.evaluate_average(averages.average_value, parameters, 'min', True)
        # self.best_average_error_threshold_number.evaluate_average(averages.error_threshold_number, parameters, 'min', False)
        # self.best_success_percentage.evaluate_average(averages.percentage_success, parameters, 'max', True)

    def calculate_progress_start(self, parameters: list[Parameter]):
        total = 0
        for parameter in parameters:
            parameter_total = (parameter.max - parameter.start) / parameter.increment

            if total == 0:
                total = parameter_total
                continue

            total *= parameter_total
        
        self.total_iterations_to_complete = total

    def update_progress(self):
        self.iterations += 1
        previous_percentage = self.percentage

        print(f'Progress: {self.iterations} / {self.total_iterations_to_complete}', end='\r')

        # self.percentage = 0 if self.total_iterations_to_complete == 0 or self.iterations == 0 else math.floor(self.iterations / self.total_iterations_to_complete)

        # if previous_percentage != self.percentage:
        #     print(f'Progress: {self.percentage}% / 100%', end='\r')
