# ----------
# User Instructions:
#
# Implement the function optimum_policy2D below.
#
# You are given a car in grid with initial state
# init. Your task is to compute and return the car's
# optimal path to the position specified in goal;
# the costs for each motion are as defined in cost.
#
# There are four motion directions: up, left, down, and right.
# Increasing the index in this array corresponds to making a
# a left turn, and decreasing the index corresponds to making a
# right turn.

import utils

forward = [[-1, 0],  # go up
           [0, -1],  # go left
           [1, 0],  # go down
           [0, 1]]  # go right
forward_name = ['up', 'left', 'down', 'right']

# action has 3 values: right turn, no turn, left turn
action = [-1, 0, 1]
action_name = ['R', '#', 'L']

# EXAMPLE INPUTS:
# grid format:
#     0 = navigable space
#     1 = unnavigable space
grid = [[1, 1, 1, 0, 0, 0],
        [1, 1, 1, 0, 1, 0],
        [0, 0, 0, 0, 0, 0],
        [1, 1, 1, 0, 1, 1],
        [1, 1, 1, 0, 1, 1]]

init = [4, 3, 0]  # given in the form [row,col,direction]
# direction = 0: up
#             1: left
#             2: down
#             3: right

goal = [2, 0]  # given in the form [row,col]

cost = [2, 1, 20]  # cost has 3 values, corresponding to making


# a right turn, no turn, and a left turn

# EXAMPLE OUTPUT:
# calling optimum_policy2D with the given parameters should return
# [[' ', ' ', ' ', 'R', '#', 'R'],
#  [' ', ' ', ' ', '#', ' ', '#'],
#  ['*', '#', '#', '#', '#', 'R'],
#  [' ', ' ', ' ', '#', ' ', ' '],
#  [' ', ' ', ' ', '#', ' ', ' ']]
# ----------

# ----------------------------------------
# modify code below
# ----------------------------------------

def optimum_policy2D(grid, init, goal, cost):
    value = [[[999 for _ in range(len(grid[0]))] for _ in range(len(grid))],
             [[999 for _ in range(len(grid[0]))] for _ in range(len(grid))],
             [[999 for _ in range(len(grid[0]))] for _ in range(len(grid))],
             [[999 for _ in range(len(grid[0]))] for _ in range(len(grid))]]
    for i in range(len(value)):
        value[i][goal[0]][goal[1]] = 0

    policy = [[[' ' for _ in range(len(grid[0]))] for _ in range(len(grid))],
              [[' ' for _ in range(len(grid[0]))] for _ in range(len(grid))],
              [[' ' for _ in range(len(grid[0]))] for _ in range(len(grid))],
              [[' ' for _ in range(len(grid[0]))] for _ in range(len(grid))]]
    for i in range(len(policy)):
        policy[i][goal[0]][goal[1]] = '*'

    open = []
    for o in range(len(forward)):
        open.append([goal[0], goal[1], o, 0])

    while len(open) > 0:
        next = open.pop()
        x = next[0]
        y = next[1]
        o = next[2]
        for o2 in range(len(forward)):
            for a in range(len(action)):
                if o == (o2 + action[a]) % len(forward):
                    x2 = x - forward[o][0]
                    y2 = y - forward[o][1]
                    if 0 <= x2 < len(grid) and 0 <= y2 < len(grid[0]):
                        if grid[x2][y2] == 0 and value[o][x][y] + cost[a] < value[o2][x2][y2]:
                            value[o2][x2][y2] = value[o][x][y] + cost[a]
                            policy[o2][x2][y2] = action_name[a]
                            open.append([x2, y2, o2])

    utils.display(policy)
    utils.display(value, 3)

    policy2D = [[' ' for _ in range(len(grid[0]))] for _ in range(len(grid))]

    x = init[0]
    y = init[1]
    o = init[2]
    if policy[o][x][y] != ' ':
        policy2D[x][y] = policy[o][x][y]
        while policy[o][x][y] != '*':
            if policy[o][x][y] == 'R':
                o = (o - 1) % len(forward)
            elif policy[o][x][y] == 'L':
                o = (o + 1) % len(forward)
            x += forward[o][0]
            y += forward[o][1]
            policy2D[x][y] = policy[o][x][y]

    return policy2D


utils.display(optimum_policy2D(grid, init, goal, cost))
