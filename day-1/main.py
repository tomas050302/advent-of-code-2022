def main():
    with open('input.txt', 'r') as f:
        lines = f.readlines()
        current_sum = 0
        sums = []
        i = 0
        # foreach line
        for line in lines:
            if (line == "\n"):
                sums.append(current_sum)
                i += 1
                current_sum = 0
                continue
            line = int(line)
            current_sum += line

        sums.sort()
        sums.reverse()
        print()
        print(sums[0]+sums[1]+sums[2])


main()
