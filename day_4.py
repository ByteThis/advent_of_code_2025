def part_1():
    with open('data/day_4.txt') as f:
        raw_lines = [f".{line.strip()}." for line in f if line.strip()]

    width = len(raw_lines[0])
    empty_row = "." * width
    grid = [empty_row] + raw_lines + [empty_row]

    accessible_rolls = 0

    for r in range(1, len(grid) - 1):
        for c in range(1, width - 1):
            if grid[r][c] == '.':
                continue

            neighbors = 0

            for i in (-1, 0, 1):
                for j in (-1, 0, 1):
                    if i == 0 and j == 0:
                        continue

                    if grid[r + i][c + j] == '@':
                        neighbors += 1

            if neighbors <= 3:
                accessible_rolls += 1

    return accessible_rolls


def part_2():
    with open('data/day_4.txt') as f:
        raw_lines = [list(f".{line.strip()}.") for line in f if line.strip()]

        width = len(raw_lines[0])
        empty_row = list("." * width)
        grid = [empty_row] + raw_lines + [empty_row[:]]

        accessible_rolls = 0

        while True:
            to_remove = []

            for r in range(1, len(grid) - 1):
                for c in range(1, width - 1):
                    if grid[r][c] == '.':
                        continue

                    neighbors = 0

                    for i in (-1, 0, 1):
                        for j in (-1, 0, 1):
                            if i == 0 and j == 0:
                                continue

                            if grid[r + i][c + j] == '@':
                                neighbors += 1

                    if neighbors <= 3:
                        accessible_rolls += 1
                        to_remove.append((r, c))

            if not to_remove:
                break

            for r, c in to_remove:
                grid[r][c] = '.'

        return accessible_rolls


print(part_1())
print(part_2())

