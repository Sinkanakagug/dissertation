from parameter_tuning import ParameterTuning
from parameter import Parameter
from sa import SA
from tuning_average_results import TuningAverageResults

class SATuning(ParameterTuning):
    def __init__(self, dimension: int, max: float, min: float, iterations_per_param: int) -> None:
        super().__init__(dimension, max, min, iterations_per_param)
    
    def run(self, temperature: Parameter, cooling_rate: Parameter, iterations_per_temperature: Parameter, neighbour_scale: Parameter):
        sa = SA(self.dimension, self.max, self.min)

        self.calculate_progress_start([temperature, cooling_rate, iterations_per_temperature, neighbour_scale])

        temperature.current = temperature.start

        #Run nested loops
        while temperature.current < temperature.max:
            cooling_rate.current = cooling_rate.start

            while cooling_rate.current < cooling_rate.max:
                iterations_per_temperature.current = iterations_per_temperature.start

                while iterations_per_temperature.current < iterations_per_temperature.max:
                    neighbour_scale.current = neighbour_scale.start

                    while neighbour_scale.current < neighbour_scale.max:
                        results = []

                        for i in range(self.iterations_per_param):
                            results.append(sa.run(temperature.current, cooling_rate.current, iterations_per_temperature.current, neighbour_scale.current))
                        
                        averages = TuningAverageResults(results)

                        self.evaluate_averages(averages, [temperature, cooling_rate, iterations_per_temperature, neighbour_scale])

                        self.update_progress()

                        neighbour_scale.increment_parameter()

                    iterations_per_temperature.increment_parameter()

                cooling_rate.increment_parameter()

            temperature.increment_parameter()

        output = [f"{obj['name']}: {obj['current']}" for obj in self.best_params]
        print(f'Best parameters: {output} - {str(self.best_success_percentage)} - {str(self.best_average_error_threshold_number)}')