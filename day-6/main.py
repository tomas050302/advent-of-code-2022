INTERVAL = 4
SECOND_INTERVAL = 14

with open("input.txt") as f:
    lines = f.readlines()
    line = lines[0]
    for i in range(0, len(line)):
        four_chars = line[i:i+INTERVAL]
        if len(set(four_chars)) == INTERVAL:
            print()
            print("Part 1 answer:", i+INTERVAL)
            break

with open("input.txt") as f:
    lines = f.readlines()
    line = lines[0]
    for i in range(0, len(line)):
        four_chars = line[i:i+SECOND_INTERVAL]
        if len(set(four_chars)) == SECOND_INTERVAL:
            print("Part 2 answer:", i+SECOND_INTERVAL)
            break
