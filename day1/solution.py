def execute(file_path: str):
    gnome_calories = []

    with open(file_path) as f:
        current_value = 0
        for row in f.read().split('\n'):
            if row == '':
                gnome_calories.append(current_value)
                current_value = 0
            else:
                try:
                    current_value += int(row)
                except ValueError:
                    raise RuntimeError(f'Invalid input value {row}')

        if current_value != 0:
            gnome_calories.append(current_value)

    return sorted(gnome_calories, reverse=True)


if __name__ == '__main__':
    carrying = execute('input.txt')

    task_1 = carrying[0]
    task_2 = sum(carrying[:3])

    print(f'Task 1: {task_1}')
    print(f'Task 2: {task_2}')
