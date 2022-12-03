import string


def task_1(file_path):
    score = 0
    with open(file_path) as f:
        for row in f.read().split('\n'):
            if not row:
                continue

            left = set(row[:len(row) // 2])
            right = set(row[len(row) // 2:])

            intersect = list(left.intersection(right))
            if len(intersect) != 1:
                raise RuntimeError('More than 1 item in two compartments')

            item = intersect[0]
            try:
                idx = string.ascii_lowercase.index(item)
                score += idx + 1
            except ValueError:
                idx = string.ascii_uppercase.index(item)
                score += idx + 27

    return score


def task_2(file_path):
    score = 0

    with open(file_path) as f:
        rows = f.read().split('\n')[:-1]

        for i in range(0, len(rows), 3):
            intersection = list(
                set(rows[i])
                .intersection(set(rows[i+1]))
                .intersection(set(rows[i+2]))
            )

            if len(intersection) != 1:
                raise RuntimeError('More than 1 item common in group')

            item = intersection[0]
            try:
                idx = string.ascii_lowercase.index(item)
                score += idx + 1
            except ValueError:
                idx = string.ascii_uppercase.index(item)
                score += idx + 27

    return score


if __name__ == '__main__':
    print(task_1('input.txt'))
    print(task_2('input.txt'))
