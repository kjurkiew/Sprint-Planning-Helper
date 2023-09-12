# Sprint Planning Helper

Sprint Planning Helper is a Python script that helps you find the most efficient set of tasks to be taken from a pool of groomed tasks. It leverages the knapsack algorithm to optimize task selection based on story points and a team's velocity.

## Usage

The script can be executed from the command line by providing two arguments:

1. The path to a CSV file containing task data with the following columns: `task_id`, `story_points`, and `KSP`.
2. The team's velocity, which represents the available capacity for the sprint.

Here's an example of how to run the script:

```
sprint_planning_helper.py csv_with_tasks.csv 13
```

In this example, the script will read task data from the tasks.csv file and attempt to find the most efficient set of tasks with a total story point value that does not exceed the team's velocity of 13.

## Algorithm
The script uses the knapsack algorithm to optimize task selection based on story points and KSP values. It dynamically calculates the most efficient set of tasks to maximize the total KSP within the given velocity constraint.
