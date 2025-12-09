def part_1():
    with open('data/day_5.txt', 'r') as f:
        range_input, ingredient_input = f.read().strip().split('\n\n')

        ranges = sorted(tuple(map(int, line.split('-'))) for line in range_input.splitlines())
        ingredients = {int(line) for line in ingredient_input.splitlines()}

        valid_count = 0

        for val in ingredients:
            for start, end in ranges:

                if val < start:
                    break

                if val <= end:
                    valid_count += 1
                    break

        return valid_count


def part_2():
    with open('data/day_5.txt', 'r') as f:
        range_input, ingredient_input = f.read().strip().split('\n\n')

        ranges = sorted(tuple(map(int, line.split('-'))) for line in range_input.splitlines())

        total_count = 0
        highest_seen = float('-inf')

        for start, end in ranges:
            effective_start = max(start, highest_seen + 1)

            if end >= effective_start:
                total_count += (end - effective_start + 1)
                highest_seen = end

        return total_count


print(part_1())
print(part_2())

