from abc import abstractmethod
from parameter import Parameter
from result import Result
from tuning_average_results import TuningAverageResults
from best_average import BestAverage

#Weighted values for the results of parameter tuning, to evaluate the current parameters
SUCCESS_RATE_WEIGHT = 1
THRESHOLD_SPEED_WEIGHT = 0.8
SOLUTION_VALUE_WEIGHT = 0.4
TOTAL_EVALUATIONS_WEIGHT = 0.2

class ParameterTuning:
    def __init__(self, dimension: int, max: float, min: float, iterations_per_param: int) -> None:
        self.dimension = dimension
        self.max = max
        self.min = min
        self.iterations_per_param = iterations_per_param
        self.best_average_value = BestAverage()
        self.best_average_error_threshold_number = BestAverage()
        self.best_success_percentage = BestAverage()

    @abstractmethod
    def run(self, **kwargs):
        pass
    
    def evaluate_averages(self, averages: TuningAverageResults, parameters: list[Parameter]):
        #Check if the average values beat the previously stored average. Pass in max or min for whether we want the value to be maximised of minimised
        self.best_average_value.evaluate_average(averages.average_value, parameters, 'min', True)
        self.best_average_error_threshold_number.evaluate_average(averages.error_threshold_number, parameters, 'min', False)
        self.best_success_percentage.evaluate_average(averages.percentage_success, parameters, 'max', True)