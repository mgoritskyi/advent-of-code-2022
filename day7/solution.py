DIRS_AND_SIZE = {}
ROWS = []


def read_dir(dir_path, idx=0):
    dir_size = 0
    nested_dirs = set()
    while idx < len(ROWS):
        if ROWS[idx].startswith('$'):
            cmd = ROWS[idx].split(' ')
            command = cmd[1]

            if command == 'cd':
                path = cmd[2]
                if path == '..':
                    idx += 1
                    break

                if dir_path == '/':
                    nested_dir_path = dir_path + path
                else:
                    nested_dir_path = '/'.join([dir_path, path])

                nested_dir_size, idx = read_dir(nested_dir_path, idx + 1)
                dir_size += nested_dir_size
                DIRS_AND_SIZE[nested_dir_path] = nested_dir_size
                continue
            else:
                idx += 1
        else:
            t, name = ROWS[idx].split(' ')
            if t == 'dir':
                nested_dirs.add(name)
            else:
                dir_size += int(t)
            idx += 1

    return dir_size, idx


def calculate_file_system(input_path):
    with open(input_path) as f:
        global ROWS, DIRS_AND_SIZE
        ROWS = f.read().strip().split('\n')[1:]
        root_size, _ = read_dir('/')
        DIRS_AND_SIZE['/'] = root_size


def task_1():
    return sum([v for v in DIRS_AND_SIZE.values() if v < 100000])


def task_2():
    total_size = 70_000_000
    should_be_free = 30_000_000
    size_used = DIRS_AND_SIZE['/']
    size_to_be_free = should_be_free - (total_size - size_used)
    smallest_dir_size_to_delete = size_used

    for v in DIRS_AND_SIZE.values():
        if size_to_be_free <= v < smallest_dir_size_to_delete:
            smallest_dir_size_to_delete = v

    return smallest_dir_size_to_delete


calculate_file_system('input.txt')
print(task_1())
print(task_2())
