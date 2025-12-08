def part_1():
    combinations = []
    with open('data/day_3.txt', 'r') as f:
        for line in f:
            s = line.strip()
            batteries = [int(x) for x in s]
            b1 = max(batteries[:-1])
            b2 = max(batteries[input.s(str(b1))+1:])
            jolts = int(str(b1)+str(b2))
            combinations.append(jolts)
    return sum(combinations)

def part_2():
    combinations = []
    with open('data/day_3.txt', 'r') as f:
        for line in f:
            input = line.strip()
            batteries = [int(x) for x in input]
            b = max(batteries[:-11])
            jolts = str(b)
            previous_index = input.index(str(b))

            for i in range(-10,1):
                b = max(batteries[previous_index+1:i]) if i else max(batteries[previous_index+1:])
                jolts += str(b)
                previous_index = input[previous_index:].index(str(b))+previous_index

            combinations.append(int(jolts))

    return sum(combinations)


def part_2():
    combinations = []
    with open('data/day_3.txt', 'r') as f:
        for line in f:
            batteries = [int(x) for x in line.strip()]

            limit = len(batteries) - 11
            b = max(batteries[:limit])
            jolts = str(b)
            previous_index = batteries.index(b, 0, limit)

            for i in range(-10, 1):
                limit = len(batteries) + i if i else len(batteries)

                b = max(batteries[previous_index + 1:limit])
                jolts += str(b)

                previous_index = batteries.index(b, previous_index + 1, limit)

            combinations.append(int(jolts))

    return sum(combinations)


print(part_1())
print(part_2())

