def part_1():
    ranges = []
    invalid_ids = []
    with open('data/day_2.txt', 'r') as f:
        for line in f:
            ranges += [r for r in line.strip().split(",")]

    for r in ranges:
        start, end = map(int, r.split("-"))
        for n in range(start, end+1):
            s = str(n)
            if len(s)%2==0:
                mid = len(s)//2
                if s[:mid] == s[mid:]:
                    invalid_ids.append(n)
    return sum(invalid_ids)

def part_2():
    ranges = []
    invalid_ids = []
    with open('data/day_2.txt', 'r') as f:
        for line in f:
            ranges += [r for r in line.strip().split(",")]

    for r in ranges:
        start, end = map(int, r.split("-"))
        for n in range(start, end + 1):
            s = str(n)
            length = len(s)
            for i in range(1, length // 2 + 1):
                if length % i == 0:
                    pattern = s[:i]
                    if (pattern * (length//i)) == s:
                        if n not in invalid_ids:
                            invalid_ids.append(n)

    return sum(invalid_ids)


print(part_1())
print(part_2())

