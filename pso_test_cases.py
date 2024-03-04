import unittest
from parameterized import parameterized
from pso import update_solution_velocity, move_solution, move_population, remove_velocity_from_population, update_population_bests


class GATests(unittest.TestCase):
    @parameterized.expand([
        (
            'update_solution_velocity',
            (  # solution
                [1.54, -0.23],  # current_position
                [0.84, 1]  # solution_velocity
            ),
            [  # current_solution_best
                1.24, 0.96
            ],
            [  # global_best_position
                1.18, 0.98
            ],
            (
                [1.54, -0.23],  # current_position
                [0.18, 3.4]  # new_velocity
            )
        )
    ])
    def test_update_solution_velocity(self, name, solution, current_solution_best, global_best_position, result):
        test_result = update_solution_velocity(
            solution, current_solution_best, global_best_position)
        self.assertEqual(test_result[0], result[0])
        self.assertEqual(len(test_result[1]), 2)

    @parameterized.expand([
        (
            'move_solution',
            (  # solution
                [1.54, -0.23],  # position
                [0.84, 1]  # velocity
            ),
            (
                [2.38, 0.77],  # position
                [0.84, 1]  # velocity
            )
        )
    ])
    def test_move_solution(self, name, solution, result):
        test_result = move_solution(solution)
        self.assertListEqual(test_result[0], result[0])
        self.assertListEqual(test_result[1], result[1])

    @parameterized.expand([
        (
            'move_population',
            [  # population
                (  # solution
                    [1.54, -0.23],  # position
                    [0.84, 1]  # velocity
                ),
                (  # solution
                    [0.02, -1.41],  # position
                    [0.2, -0.4]  # velocity
                ),
                (  # solution
                    [0.02, 2.24],  # position
                    [0.09, 1.01]  # velocity
                ),
            ],
            [
                (
                    [2.38, 0.77],  # position
                    [0.84, 1]  # velocity
                ),
                (
                    [0.22, -1.81],  # position
                    [0.2, -0.4]  # velocity
                ),
                (
                    [0.11, 3.25],  # position
                    [0.09, 1.01]  # velocity
                ),
            ]
        )
    ])
    def test_move_population(self, name, population, result):
        move_population(population)
        self.assertListEqual(population, result)

    @parameterized.expand([
        (
            'remove_velocity_from_population',
            [  # population
                (  # solution
                    [1.54, -0.23],  # position
                    [0.84, 1]  # velocity
                ),
                (  # solution
                    [0.02, -1.41],  # position
                    [0.2, -0.4]  # velocity
                ),
                (  # solution
                    [0.02, 2.24],  # position
                    [0.09, 1.01]  # velocity
                ),
            ],
            [
                [1.54, -0.23],  # position
                [0.02, -1.41],  # position
                [0.02, 2.24],  # position
            ]
        )
    ])
    def test_remove_velocity_from_population(self, name, population, result):
        test_result = remove_velocity_from_population(population)
        self.assertListEqual(test_result, result)

    @parameterized.expand([
        (
            'update_population_bests',
            [ #current_position_fitnesses
                ([1.54, -0.23], 677.1238559999999),
                ([0.02, -1.41], 199.88321599999995),
                ([0.02, 2.24], 502.54121600000013),
            ],
            [ #pop_best_positions
                [2.38, 0.77],
                [-0.01, 0.07],
                [0.2, -0.47],
            ],
            [ #pop_best_values
                2397.419535999999,
                1.508701,
                26.65
            ],
            [ #pop_best_positions - after
                [1.54, -0.23],
                [-0.01, 0.07],
                [0.2, -0.47],
            ],
            [ #pop_best_values - after
                677.1238559999999,
                1.508701,
                26.65
            ],
        )
    ])
    def test_update_population_bests(self, name, current_position_fitnesses, pop_best_positions, pop_best_values, pop_best_positions_result, pop_best_values_result):
        update_population_bests(current_position_fitnesses, pop_best_positions, pop_best_values)
        self.assertEqual(pop_best_positions, pop_best_positions_result)
        self.assertEqual(pop_best_values, pop_best_values_result)

    def assertInRange(self, bound1, bound2, value):
        if not (min(bound1, bound2) <= value <= max(bound1, bound2)):
            raise AssertionError(
                f"Value {value} not within the range ({bound1}, {bound2})")


if __name__ == '__main__':
    unittest.main()
