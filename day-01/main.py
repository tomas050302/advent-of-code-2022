def main():
    with open('input.txt', 'r') as f:
        current_sum = 0
        sums = []
        for line in f.readlines():
            line = line.strip()
            if line == '':
                sums.append(current_sum)
                current_sum = 0
                continue
            current_sum += int(line)

        sums.sort()
        sums.reverse()
        print()
        print("Part 1 answer: " + str(sums[0]))
        print("Part 2 answer: " + str(sums[0]+sums[1]+sums[2]))


main()
