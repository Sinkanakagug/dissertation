from parameter_tuning import ParameterTuning
from parameter import Parameter
from rgb import RGB
from tuning_average_results import TuningAverageResults

class RGBTuning(ParameterTuning):
    def __init__(self, dimension: int, max: float, min: float, iterations_per_param: int) -> None:
        super().__init__(dimension, max, min, iterations_per_param)

    def run(self, neighbour_scale: Parameter, num_of_neighbours: Parameter, branching_factor: Parameter, branching_scale: Parameter):
        rgb = RGB(self.dimension, self.max, self.min)

        self.calculate_progress_start([neighbour_scale, num_of_neighbours, branching_factor, branching_scale])

        neighbour_scale.current = neighbour_scale.start

        #Run nested loops
        while neighbour_scale.current < neighbour_scale.max:
            num_of_neighbours.current = num_of_neighbours.start

            while num_of_neighbours.current < num_of_neighbours.max:
                branching_factor.current = branching_factor.start

                while branching_factor.current < branching_factor.max:
                    branching_scale.current = branching_scale.start

                    while branching_scale.current < branching_scale.max:
                        results = []

                        for i in range(self.iterations_per_param):
                            results.append(rgb.run(neighbour_scale.current, num_of_neighbours.current, branching_factor.current, branching_scale.current))
                        
                        averages = TuningAverageResults(results)

                        self.evaluate_averages(averages, [neighbour_scale, num_of_neighbours, branching_factor, branching_scale])

                        self.update_progress()

                        branching_scale.increment_parameter()

                    branching_factor.increment_parameter()
                
                num_of_neighbours.increment_parameter()

            neighbour_scale.increment_parameter()
        
        output = [f"{obj['name']}: {obj['current']}" for obj in self.best_params]
        print(f'Best parameters: {output} - {str(self.best_success_percentage)} - {str(self.best_average_error_threshold_number)}')