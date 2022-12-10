def map_to_value(x):
    if x.islower():
        return ord(x) - ord('a') + 1
    else:
        return ord(x) - ord('A') + 27


with open("input.txt", 'r') as f:
    value = 0
    for line in f.readlines():
        line = line.strip()

        first_half = line[:len(line)//2]
        second_half = line[len(line)//2:]

        for x in first_half:
            if x in second_half:
                value += map_to_value(x)
                break  # after finding the first match, break out of the loop

    print()
    print("Part 1 answer:", value)

with open("input.txt", 'r') as f:
    value = 0
    for line1, line2, line3 in zip(f, f, f):
        for x in line1:
            if x in line2 and x in line3:
                value += map_to_value(x)
                break

    print("Part 2 answer:", value)
