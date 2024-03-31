from parameter_tuning import ParameterTuning
from parameter import Parameter
from ga import GA
from tuning_average_results import TuningAverageResults

class GATuning(ParameterTuning):
    def __init__(self, dimension: int, max: float, min: float, iterations_per_param: int) -> None:
        super().__init__(dimension, max, min, iterations_per_param)
    
    def run(self, pop_size: Parameter, mutation_rate: Parameter, termination_number: Parameter):
        ga = GA(self.dimension, self.max, self.min)

        self.calculate_progress_start([pop_size, mutation_rate, termination_number])

        pop_size.current = pop_size.start

        #Run nested loops, trying every combination of parameters
        while pop_size.current < pop_size.max:
            mutation_rate.current = mutation_rate.start

            while mutation_rate.current < mutation_rate.max:
                termination_number.current = termination_number.start

                while termination_number.current < termination_number.max:
                    results = []

                    for i in range(self.iterations_per_param):
                        results.append(ga.run(pop_size.current, mutation_rate.current, termination_number.current))
                    
                    averages = TuningAverageResults(results)

                    self.evaluate_averages(averages, [pop_size, mutation_rate, termination_number])

                    self.update_progress()

                    termination_number.increment_parameter()
                
                mutation_rate.increment_parameter()
        
            pop_size.increment_parameter()

        output = [f"{obj['name']}: {obj['current']}" for obj in self.best_params]
        print(f'Best parameters: {output} - {str(self.best_success_percentage)} - {str(self.best_average_error_threshold_number)}')