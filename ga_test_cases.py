import unittest
from parameterized import parameterized
from ga import get_parents_from_evaluated_population, remove_fitness_from_parents, mate_parents, mate


class GATests(unittest.TestCase):
    @parameterized.expand([
        (
            'evaluated population',
            [
                ([-1.02, 1.3], 10.819616000000003),
                ([1.3564, 1.4408], 16.04879361193217),
                ([1.0793, 1.1221], 0.1893739776480077),
                ([1.7834, 0.2871], 837.7990758450114),
                ([0.2907, 0.1407], 0.81887754661201),
                ([1.8569, -1.3104], 2265.045194097131),
                ([1.0946, 0.4666], 53.52536650967056),
                ([-0.6226, 0.4271], 2.7886128506177594),
            ],
            [
                ([1.0793, 1.1221], 0.1893739776480077),
                ([0.2907, 0.1407], 0.81887754661201),
                ([-0.6226, 0.4271], 2.7886128506177594),
                ([-1.02, 1.3], 10.819616000000003),
            ]
        )
    ])
    def test_get_parents_from_evaluated_population(self, name, input, result):
        self.assertEqual(get_parents_from_evaluated_population(input), result)

    @parameterized.expand([
        (
            'parents',
            [
                ([-1.02, 1.3], 10.819616000000003),
                ([1.3564, 1.4408], 16.04879361193217),
                ([1.0793, 1.1221], 0.1893739776480077),
                ([1.7834, 0.2871], 837.7990758450114),
                ([0.2907, 0.1407], 0.81887754661201),
                ([1.8569, -1.3104], 2265.045194097131),
                ([1.0946, 0.4666], 53.52536650967056),
                ([-0.6226, 0.4271], 2.7886128506177594),
            ],
            [
                [-1.02, 1.3],
                [1.3564, 1.4408],
                [1.0793, 1.1221],
                [1.7834, 0.2871],
                [0.2907, 0.1407],
                [1.8569, -1.3104],
                [1.0946, 0.4666],
                [-0.6226, 0.4271],
            ],
        )
    ])
    def test_remove_fitness_from_parents(self, name, input, result):
        self.assertEqual(remove_fitness_from_parents(input), result)

    @parameterized.expand([
        (
            'parents',
            [
                [1.0793, 1.1221],
                [0.2907, 0.1407],
                [-0.6226, 0.4271],
                [-1.02, 1.3],
            ],
        )
    ])
    def test_mate_parents(self, name, input):
        dimension = len(input[0])
        children = mate_parents(input)
        self.assertEqual(len(children), len(input) * 2)

        for child in children:
            self.assertIsInstance(child, list)
            self.assertEqual(len(child), dimension)

    @parameterized.expand([
        (
            'mother_father',
            [
                [1.3564, 1.4408],
                [1.0793, 1.1221]
            ]
        )
    ])
    def test_mate(self, name, input):
        mother = input[0]
        father = input[1]
        child1, child2 = mate(mother, father)

        print(child1, child2)

        for i in range(len(child1)):
            self.assertInRange(mother[i], father[i], child1[i])

        for i in range(len(child2)):
            self.assertInRange(mother[i], father[i], child2[i])

    def assertInRange(self, bound1, bound2, value):
        if not (min(bound1, bound2) <= value <= max(bound1, bound2)):
            raise AssertionError(f"Value {value} not within the range ({bound1}, {bound2})")

if __name__ == '__main__':
    unittest.main()
