import sprint_planning_helper
import unittest
from typing import List, Dict, Tuple


class TestSprintPlanningHelper(unittest.TestCase):
    """
    A test suite for the Sprint Planning Helper module.
    """

    def test_collecting_data_from_csv(self):
        """
        Test collecting data from a CSV file.
        """
        total = sprint_planning_helper.collecting_data_from_csv("test.csv")
        self.assertEqual(total[0], [0, 1, 2, 3, 4, 5])
        self.assertEqual(total[1], {0: 3, 1: 2, 2: 8, 3: 5, 4: 2, 5: 2})
        self.assertEqual(total[2], {0: 5, 1: 3, 2: 2, 3: 9, 4: 1, 5: 3})

    def test_initialize_result_array(self):
        """
        Test initializing the result array.
        """
        total = sprint_planning_helper.initialize_result_array([0, 1, 2, 3, 4, 5], 13)
        self.assertEqual(
            total,
            [
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            ],
        )

    def test_knapsack(self):
        """
        Test the knapsack algorithm.
        """
        array = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        ]
        data_from_csv: Tuple[List[int], Dict[int, int], Dict[int, int]] = (
            [0, 1, 2, 3, 4, 5],
            {0: 3, 1: 2, 2: 8, 3: 5, 4: 2, 5: 2},
            {0: 5, 1: 3, 2: 2, 3: 9, 4: 1, 5: 3},
        )
        total = sprint_planning_helper.knapsack(array, data_from_csv, 13)
        self.assertEqual(total, [5, 3, 1, 0])

    def test_conv_list_to_string(self):
        """
        Test converting a list to a comma-separated string.
        """
        total = sprint_planning_helper.conv_list_to_string([5, 3, 1, 0])
        self.assertEqual(total, "0, 1, 3, 5")


if __name__ == "__main__":
    unittest.main()
