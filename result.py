class Result:
    def __init__(self, evaluation_counter: float, best_solution_value: float, error_threshold_number: float, best_solution: list[float] = [], percentage_success: float = 0) -> None:
        self.evaluation_counter = evaluation_counter
        self.best_solution_value = best_solution_value
        self.error_threshold_number = error_threshold_number
        self.best_solution = best_solution
        self.percentage_success = percentage_success