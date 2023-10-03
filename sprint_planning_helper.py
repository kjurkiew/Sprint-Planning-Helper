# sprint_planning_helper.py - finding the most efficient set of tasks to be taken from the file

import csv
import sys
from typing import List, Tuple, Dict

CSV_FILE_COLUMNS = ["task_id", "story_points", "KSP"]


def collecting_data_from_csv(
    file_name: str,
) -> Tuple[List[int], Dict[int, int], Dict[int, int]]:
    """
    Collects data from a CSV file.

    Args:
        file_name (str): The name of the CSV file.

    Returns:
        Tuple[List[int], Dict[int, int], Dict[int, int]]: A tuple containing task IDs, story points, and KSP values.
    """
    task_id, story_points, KSP = [], {}, {}

    try:
        with open(file_name, "r", encoding="utf-8") as csvfile:
            data_from_csv = csv.DictReader(csvfile)
            for row in data_from_csv:
                for column in CSV_FILE_COLUMNS:
                    if column == "task_id":
                        task_id.append(int(row[column]))
                    else:
                        column_data = int(row[column])
                        if column == "story_points":
                            story_points[int(row["task_id"])] = column_data
                        elif column == "KSP":
                            KSP[int(row["task_id"])] = column_data
    except FileNotFoundError:
        print("File not found.")
        sys.exit(1)

    return task_id, story_points, KSP


def initialize_result_array(task_id: List[int], velocity: int) -> List[List[int]]:
    """
    Initializes a result array for solving the knapsack problem.

    Args:
        task_id (List[int]): List of task IDs.
        velocity (int): The available velocity.

    Returns:
        List[List[int]]: A 2D array for dynamic programming.
    """
    result = []
    for i in range(len(task_id) + 1):
        result.append([0 for j in range(velocity + 1)])

    return result


def knapsack(
    array: List[List[int]],
    data_from_csv: Tuple[List[int], Dict[int, int], Dict[int, int]],
    velocity: int,
) -> List[int]:
    """
    Solves the knapsack problem to find the most efficient set of tasks.

    Args:
        array (List[List[int]]): The result array for dynamic programming.
        data_from_csv (Tuple[List[int], Dict[int, int], Dict[int, int]]): Data from the CSV file.
        velocity (int): The available velocity.

    Returns:
        List[int]: A list of task IDs in the optimal solution.
    """
    story_points = data_from_csv[1]
    KSP = data_from_csv[2]
    left_id = len(story_points)
    output_tasks = []

    for ids in range(left_id + 1):
        for v in range(velocity + 1):
            # Base Case
            if ids == 0 or v == 0:
                array[ids][v] = 0
            # If value of the ids item is lower than left velocity
            # Return the maximum of two cases:
            # 1 - element ids included
            # 2 - element ids not included
            elif story_points[ids - 1] <= v:
                array[ids][v] = max(
                    KSP[ids - 1] + array[ids - 1][v - story_points[ids - 1]],
                    array[ids - 1][v],
                )
            # If value of the element is higher than left velocity
            # then this item cannot be included in the optimal solution
            else:
                array[ids][v] = array[ids - 1][v]

    result = array[left_id][velocity]

    v = velocity
    for ids in range(left_id, 0, -1):
        if result <= 0:
            break
        if result == array[ids - 1][v]:
            continue
        else:
            output_tasks.append(ids - 1)
            result -= KSP[ids - 1]
            v -= story_points[ids - 1]

    return output_tasks


def conv_list_to_string(output_tasks_list: List[int]) -> str:
    """
    Converts a list of task IDs to a comma-separated string.

    Args:
        output_tasks_list (List[int]): List of task IDs.

    Returns:
        str: Comma-separated string of task IDs.
    """
    output_tasks_list = sorted(output_tasks_list)
    output_tasks = ", ".join(map(str, output_tasks_list))

    return output_tasks


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python planning_helper.py <file_name> <velocity>")
        sys.exit(1)

    file_name = sys.argv[1]
    velocity = int(sys.argv[2])

    data_from_csv = collecting_data_from_csv(file_name)
    task_id = data_from_csv[0]

    array = initialize_result_array(task_id, velocity)
    output_tasks_list = knapsack(array, data_from_csv, velocity)
    output_tasks = conv_list_to_string(output_tasks_list)
    sys.stdout.write(output_tasks)
