from result import Result

class TuningAverageResults:
    def __init__(self, results: list[Result]) -> None:
        sum_evaluation_counter = 0
        sum_best_solution_value = 0.0
        sum_error_threshold_number = 0

        #Used to find the percentage success of the runs and to remove unsuccessful attempts
        num_successes = 0

        for result in results:
            sum_evaluation_counter += result.evaluation_counter
            sum_best_solution_value += result.best_solution_value

            #If the result was successfully under the threshold
            if result.error_threshold_number > 0:
                num_successes += 1

            sum_error_threshold_number += result.error_threshold_number
        
        num_of_results = len(results)
        self.average_value = sum_best_solution_value / num_of_results
        self.percentage_success = 0 if num_successes == 0 else num_successes / num_of_results
        self.error_threshold_number = 0 if num_successes == 0 else sum_error_threshold_number / num_successes