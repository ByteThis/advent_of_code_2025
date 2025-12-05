def part_1():
    dial = 50
    zero_counter = 0
    with open('data/day_1.txt', 'r') as f:
        for line in f:
            rotation = int(line.strip().replace('L','-').replace('R',''))
            dial += rotation

            if dial%100 == 0:
                zero_counter += 1

    return zero_counter

def part_2():
    dial = 50
    zero_counter = 0
    with open('data/day_1.txt', 'r') as f:
        for line in f:
            rotation = int(line.strip().replace('L','-').replace('R',''))
            current_dial = dial + rotation

            if rotation >= 0:
                passes = current_dial // 100
            else:
                passes = ((dial - 1) // 100) - ((current_dial - 1) // 100)

            zero_counter += passes
            dial = current_dial % 100

    return zero_counter


print(part_1())
print(part_2())

