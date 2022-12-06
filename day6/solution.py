def solve(file_path, positions: int = 4):
    with open(file_path) as f:
        sequence = f.read().strip('\n').strip()
        stack = []
        number_of_letters = 0
        for idx in range(len(sequence)):
            if len(stack) == 0:
                stack.append(sequence[idx])
                continue
            elif len(stack) == positions:
                number_of_letters = idx
                break

            if sequence[idx] in stack:
                new_start = -1
                for j in range(len(stack) - 1, -1, -1):
                    if stack[j] == sequence[idx]:
                        new_start = j + 1
                        break

                if new_start == len(stack):
                    stack = [sequence[idx]]
                else:
                    stack = stack[new_start:]
                    stack.append(sequence[idx])
            else:
                stack.append(sequence[idx])

        return number_of_letters


if __name__ == '__main__':
    print(solve('input.txt', 4))
    print(solve('input.txt', 14))

