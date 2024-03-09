from parameter import Parameter

class BestAverage:
    def __init__(self) -> None:
        self.average = -1
        self.parameters = []

    def __str__(self) -> str:
        parameter_str = ''

        for parameter in self.parameters:
            parameter_str += f'{parameter.name}: {parameter.current} '

        return f'Average: {self.average}, Parameters: {parameter_str}'

    def evaluate_average(self, average: float, parameters: list[Parameter], min_or_max: str, allow_zero: bool):
        #Never set as the best average if it is zero and zero is not allowed
        if not(allow_zero) and average == 0:
            return
        
        #If the average has yet to be set to any value
        if self.average == -1:
            self.average = average
            self.parameters = parameters

            return
        
        #If the new average is better than the one previously stored
        if min_or_max == 'min' and average < self.average:
            self.average = average
            self.parameters = parameters

            return
        
        if min_or_max == 'max' and average > self.average:
            self.average = average
            self.parameters = parameters

            return
