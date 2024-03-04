from helpers import Helpers
from solution import Solution

class AnnealingSolution(Solution):
    def __init__(self, helpers: Helpers, solution: list = []) -> None:
        super().__init__(helpers, solution)