def load_grid(input_path):
    grid = []
    with open(input_path) as f:
        for row in f.read().split('\n'):
            if row == '':
                continue

            grid.append([int(i) for i in row])

    return grid


def task_1(grid):
    visible_trees = 0

    for i in range(1, len(grid) - 1):
        for j in range(1, len(grid[i]) - 1):
            height = grid[i][j]
            if height > max(grid[i][0:j]):
                # check if visible from left
                visible_trees += 1
            elif height > max(grid[i][j+1:]):
                # check if visible from right
                visible_trees += 1
            elif height > max([grid[k][j] for k in range(i)]):
                # check if visible from top
                visible_trees += 1
            elif height > max([grid[k][j] for k in range(i + 1, len(grid))]):
                # check if visible from bottom
                visible_trees += 1

    # edge trees
    visible_trees += (len(grid) + len(grid[0]) - 2) * 2

    return visible_trees


def task_2(grid):
    max_scenic_score = 0

    for i in range(1, len(grid) - 1):
        for j in range(1, len(grid[i]) - 1):
            height = grid[i][j]
            left, right, top, bottom = 0, 0, 0, 0
            # check how many trees we see on the left
            for k in range(j-1, -1, -1):
                left += 1
                if grid[i][k] >= height:
                    break

            # check how many trees we see on the right
            for k in range(j+1, len(grid[i])):
                right += 1
                if grid[i][k] >= height:
                    break

            # check how many trees we see on the top
            for k in range(i - 1, -1, -1):
                top += 1
                if grid[k][j] >= height:
                    break

            # check how many trees we see on the bottom
            for k in range(i + 1, len(grid)):
                bottom += 1
                if grid[k][j] >= height:
                    break

            score = left * right * top * bottom
            if score > max_scenic_score:
                max_scenic_score = score

    return max_scenic_score


grid_of_trees = load_grid('input.txt')
print(task_1(grid_of_trees))
print(task_2(grid_of_trees))
