# --------------
# USER INSTRUCTIONS
#
# Write a function called stochastic_value that
# returns two grids. The first grid, value, should
# contain the computed value of each cell as shown
# in the video. The second grid, policy, should
# contain the optimum policy for each cell.
#
# --------------
# GRADING NOTES
#
# We will be calling your stochastic_value function
# with several different grids and different values
# of success_prob, collision_cost, and cost_step.
# In order to be marked correct, your function must
# RETURN (it does not have to print) two grids,
# value and policy.
#
# When grading your value grid, we will compare the
# value of each cell with the true value according
# to this model. If your answer for each cell
# is sufficiently close to the correct answer
# (within 0.001), you will be marked as correct.

# import utils

delta = [[-1, 0],  # go up
         [0, -1],  # go left
         [1, 0],  # go down
         [0, 1]]  # go right

delta_name = ['^', '<', 'v', '>']  # Use these when creating your policy grid.


# ---------------------------------------------
#  Modify the function stochastic_value below
# ---------------------------------------------

def stochastic_value(grid, goal, cost_step, collision_cost, success_prob):
    failure_prob = (1.0 - success_prob) / 2.0  # Probability(stepping left) = prob(stepping right) = failure_prob
    value = [[collision_cost for _ in range(len(grid[0]))] for _ in range(len(grid))]
    policy = [[' ' for _ in range(len(grid[0]))] for _ in range(len(grid))]

    changed = True
    while changed:
        changed = False
        # utils.display(value)
        for x in range(len(grid)):
            for y in range(len(grid[x])):
                if x == goal[0] and y == goal[1] and value[x][y] > 0:
                    value[x][y] = 0
                    policy[x][y] = '*'
                    changed = True
                elif grid[x][y] == 0:
                    min_i = -1
                    min_v = 999
                    for i in range(len(delta)):
                        sum_v = cost_step
                        for s in [-1, 0, 1]:
                            o = (i + s) % 4
                            x2 = x + delta[o][0]
                            y2 = y + delta[o][1]
                            c2 = collision_cost if collision(x2, y2, grid) else value[x2][y2]
                            v2 = c2 * (success_prob if s == 0 else failure_prob)
                            sum_v += v2
                        if sum_v < min_v:
                            min_i = i
                            min_v = sum_v
                    if min_v < value[x][y]:
                        value[x][y] = min_v
                        policy[x][y] = delta_name[min_i]
                        changed = True

    return value, policy


def collision(x, y, grid):
    return not (0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == 0)


# ---------------------------------------------
#  Use the code below to test your solution
# ---------------------------------------------

grid = [[0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 1, 1, 0]]
goal = [0, len(grid[0]) - 1]  # Goal is in top right corner
cost_step = 1
collision_cost = 100
success_prob = 0.5

value, policy = stochastic_value(grid, goal, cost_step, collision_cost, success_prob)
for row in value:
    print '[%.4f, %.4f, %.4f, %.4f],' % (row[0], row[1], row[2], row[3])
for row in policy:
    print row

# Expected outputs:
#
# [57.9029, 40.2784, 26.0665,  0.0000]
# [47.0547, 36.5722, 29.9937, 27.2698]
# [53.1715, 42.0228, 37.7755, 45.0916]
# [77.5858, 100.00, 100.00, 73.5458]
#
# ['>', 'v', 'v', '*']
# ['>', '>', '^', '<']
# ['>', '^', '^', '<']
# ['^', ' ', ' ', '^']
