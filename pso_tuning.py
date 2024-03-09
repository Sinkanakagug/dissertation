from parameter_tuning import ParameterTuning
from parameter import Parameter
from pso import PSO
from tuning_average_results import TuningAverageResults

class PSOTuning(ParameterTuning):
    def __init__(self, dimension: int, max: float, min: float, iterations_per_param: int) -> None:
        super().__init__(dimension, max, min, iterations_per_param)

    def run(self, pop_size: Parameter, max_velocity: Parameter, min_velocity: Parameter, termination_number: Parameter):
        pso = PSO(self.dimension, self.max, self.min)

        pop_size.current = pop_size.start

        #Run nested loops
        while pop_size.current < pop_size.max:
            max_velocity.current = max_velocity.start

            while max_velocity.current < max_velocity.max:
                min_velocity.current = min_velocity.start

                while min_velocity.current < min_velocity.max:
                    termination_number.current = termination_number.max

                    while termination_number.current < termination_number.max:
                        results = []

                        for i in range(self.iterations_per_param):
                            results.append(pso.run(pop_size.current, max_velocity.current, min_velocity.current, termination_number.current))

                        averages = TuningAverageResults(results)

                        self.evaluate_averages(averages, [pop_size, max_velocity, min_velocity, termination_number])

                        termination_number.increment_parameter()
                    
                    min_velocity.increment_parameter()

                max_velocity.increment_parameter()

            pop_size.increment_parameter()

        print(f'Best parameters for accuracy: {str(self.best_average_value)}')
        print(f'Best parameters for fast accuracy: {str(self.best_average_error_threshold_number)}')
        print(f'Best parameters for success rate: {str(self.best_success_percentage)}')

                