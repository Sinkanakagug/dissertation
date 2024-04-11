from branch import Branch
from helpers import Helpers

class Branch_Mod(Branch):
    def __init__(self, helpers: Helpers, solution: list = []) -> None:
        super().__init__(helpers, solution)
    
    def get_best_neighbour(self, num_of_neighbours: int, neighbour_scale: float, max: float, min: float, biases: list[float]) -> 'Branch':
        best_solution = self
        best_value = best_solution.value

        for i in range(num_of_neighbours):
            neighbour = self.generate_neighbour(neighbour_scale, min, max, biases)

            if neighbour.value < best_value:
                best_solution = neighbour
                best_value = neighbour.value

        return best_solution
    
    def grow_branch(self, num_of_neighbours: int, neighbour_scale: float, max: float, min: float, best_solution) -> 'Branch':
        biases = self.create_bias(best_solution, 0.3)

        #Get the best neightbour
        neighbour = self.get_best_neighbour(num_of_neighbours, neighbour_scale, max, min, biases)
        best_neighbour = self
        best_neighbour_value = best_neighbour.value

        #While we keep improving the neighbour
        while(neighbour.value < best_neighbour_value):
            best_neighbour = neighbour
            best_neighbour_value = best_neighbour.value

            neighbour = best_neighbour.get_best_neighbour(num_of_neighbours, neighbour_scale, max, min, biases)
        
        return best_neighbour

    def create_bias(self, best_solution, bias_factor: float):
        biases = []
        #Create a bias based on the difference between the current solution and the best solution
        for i in range(len(best_solution.solution)):
            bias = (best_solution.solution[i] - self.solution[i]) * bias_factor
            biases.append(bias)
        
        return biases