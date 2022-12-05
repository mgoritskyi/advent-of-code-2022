import typing as t

from collections import defaultdict


def read_input(file_path) -> t.Tuple[
    t.Dict[str, t.List[str]],
    t.List[t.Tuple[int, str, str]],
]:
    stacks = defaultdict(list)
    actions = []

    with open(file_path) as f:
        rows = f.read().split('\n')

        for i in range(len(rows[8])):
            if rows[8][i].strip() == '':
                continue

            for j in range(7, -1, -1):
                if len(rows[j]) <= i:
                    break
                if rows[j][i].strip() == '':
                    break

                stacks[rows[8][i]].append(rows[j][i])

        for row in rows[10:]:
            if row == '':
                continue

            row_items = row.split(' ')
            actions.append((int(row_items[1]), row_items[3], row_items[5]))

    return stacks, actions


def solution(stacks, actions, move_multiple: bool = False):
    for action in actions:
        i = action[0]
        to_move = []
        while i != 0:
            to_move.append(stacks[action[1]].pop())
            i -= 1

        if move_multiple:
            to_move.reverse()

        stacks[action[2]].extend(to_move)

    return ''.join([v[-1] for v in stacks.values()])


if __name__ == '__main__':
    print(solution(*read_input('input.txt'), move_multiple=False))
    print(solution(*read_input('input.txt'), move_multiple=True))
