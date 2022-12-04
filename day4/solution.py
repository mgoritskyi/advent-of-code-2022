def solution(file_path):
    common_ranges = 0
    overlap_ranges = 0
    with open(file_path) as f:
        for row in f.read().split('\n'):
            if not row:
                continue

            l, r = row.split(',')
            l_min, l_max = l.split('-')
            r_min, r_max = r.split('-')
            l_min, l_max = int(l_min), int(l_max)
            r_min, r_max = int(r_min), int(r_max)

            if (
                (l_min <= r_min and l_max >= r_max)
                or (r_min <= l_min and r_max >= l_max)
            ):
                common_ranges += 1
                overlap_ranges += 1
            elif r_max >= l_min >= r_min or l_max >= r_min >= l_min:
                overlap_ranges += 1

    return common_ranges, overlap_ranges


print(solution('input.txt'))
