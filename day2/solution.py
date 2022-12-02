COMBINATIONS_1 = {
    ('A', 'X'): 3,
    ('B', 'X'): 0,
    ('C', 'X'): 6,
    ('A', 'Y'): 6,
    ('B', 'Y'): 3,
    ('C', 'Y'): 0,
    ('A', 'Z'): 0,
    ('B', 'Z'): 6,
    ('C', 'Z'): 3,
}

COMBINATIONS_2 = {
    (k[0], v): k[1]
    for k, v in COMBINATIONS_1.items()
}

FIGURE_SCORE = {
    'X': 1,
    'Y': 2,
    'Z': 3
}

OPERATION_SCORE = {
    'X': 0,
    'Y': 3,
    'Z': 6,
}


def task_1(file_path: str):
    total_score = 0
    with open(file_path) as f:
        for row in f.read().split('\n'):
            if row == '':
                continue
            opponent, my = row.split(' ')

            total_score += COMBINATIONS_1[(opponent, my)] + FIGURE_SCORE[my]

    return total_score


def task_2(file_path: str):
    total_score = 0

    with open(file_path) as f:
        for row in f.read().split('\n'):
            if row == '':
                continue

            opponent, decision = row.split(' ')
            operation_score = OPERATION_SCORE[decision]
            total_score += OPERATION_SCORE[decision]
            total_score += FIGURE_SCORE[COMBINATIONS_2[opponent, operation_score]]

    return total_score


if __name__ == '__main__':
    print(task_1('input.txt'))
    print(task_2('input.txt'))
