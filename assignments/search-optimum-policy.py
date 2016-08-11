# ----------
# User Instructions:
#
# Write a function optimum_policy that returns
# a grid which shows the optimum policy for robot
# motion. This means there should be an optimum
# direction associated with each navigable cell from
# which the goal can be reached.
#
# Unnavigable cells as well as cells from which
# the goal cannot be reached should have a string
# containing a single space (' '), as shown in the
# previous video. The goal cell should have '*'.
# ----------

import utils

# grid = [[0, 1, 0, 0, 0, 0],
#         [0, 1, 0, 0, 0, 0],
#         [0, 1, 0, 0, 0, 0],
#         [0, 1, 0, 0, 0, 0],
#         [0, 0, 0, 0, 1, 0]]
grid = [[0, 1, 0, 0, 0, 0],
        [0, 1, 1, 0, 1, 0],
        [0, 0, 0, 0, 1, 0],
        [0, 1, 1, 1, 1, 0],
        [0, 1, 0, 1, 1, 0]]
init = [0, 0]
goal = [len(grid) - 1, len(grid[0]) - 1]
cost = 1  # the cost associated with moving from a cell to an adjacent one

delta = [[-1, 0],  # go up
         [0, -1],  # go left
         [1, 0],  # go down
         [0, 1]]  # go right

delta_name = ['^', '<', 'v', '>']


def optimum_policy(grid, goal, cost):
    value = [[99 for _ in range(len(grid[0]))] for _ in range(len(grid))]
    policy = [[' ' for _ in range(len(grid[0]))] for _ in range(len(grid))]
    policy[goal[0]][goal[1]] = '*'

    step = 0
    open = [[goal[0], goal[1]]]
    while len(open) > 0:
        next = open.pop()
        x = next[0]
        y = next[1]
        value[x][y] = step
        for i in range(len(delta)):
            x2 = x + delta[i][0]
            y2 = y + delta[i][1]
            if 0 <= x2 < len(grid) and 0 <= y2 < len(grid[0]):
                if value[x2][y2] == 99 and grid[x2][y2] == 0:
                    open.append([x2, y2])
                    policy[x2][y2] = delta_name[(i + 2) % len(delta)]

        step += cost

    return policy


utils.display(optimum_policy(grid, goal, cost))
