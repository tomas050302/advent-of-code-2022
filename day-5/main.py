stacks = [['T', 'R', 'G', 'W', 'Q', 'M', 'F', 'P'], ['R', 'F', 'H'], ['D', 'S', 'H', 'G', 'V', 'R', 'Z', 'P'],
          ['G', 'W', 'F', 'B', 'P', 'H', 'Q'], ['H', 'J', 'M', 'S', 'P'],
          ['L', 'P', 'R', 'S', 'H', 'T', 'Z', 'M'], [
    'L', 'M', 'N', 'H', 'T', 'P'], ['R', 'Q', 'D', 'F'],
    ['H', 'P', 'L', 'N', 'C', 'S', 'D']]


for stack in stacks:
    # reverse every stack because I entered it in the wrong order :)
    stack = stack.reverse()


with open("input.txt") as f:
    lines = f.readlines()

    lines = lines[10:]  # skip the first 10 lines

    for line in lines:
        words = line.split()[1::2]
        quantity = int(words[0])
        stack_index = int(words[1]) - 1
        dest_stack_index = int(words[2]) - 1

        for i in range(quantity):
            stacks[dest_stack_index].append(stacks[stack_index].pop())

    print()
    print("Part 1 answer = ", end="")
    for stack in stacks:
        print(stack[-1], end="")
    print()


# -- Part 2 --

stacks = [['T', 'R', 'G', 'W', 'Q', 'M', 'F', 'P'], ['R', 'F', 'H'], ['D', 'S', 'H', 'G', 'V', 'R', 'Z', 'P'],
          ['G', 'W', 'F', 'B', 'P', 'H', 'Q'], ['H', 'J', 'M', 'S', 'P'],
          ['L', 'P', 'R', 'S', 'H', 'T', 'Z', 'M'], [
    'L', 'M', 'N', 'H', 'T', 'P'], ['R', 'Q', 'D', 'F'],
    ['H', 'P', 'L', 'N', 'C', 'S', 'D']]


for stack in stacks:
    # reverse every stack because I entered it in the wrong order :)
    stack = stack.reverse()

with open("input.txt") as f:
    lines = f.readlines()

    lines = lines[10:]  # skip the first 10 lines

    for line in lines:
        words = line.split()[1::2]
        quantity = int(words[0])
        stack_index = int(words[1]) - 1
        dest_stack_index = int(words[2]) - 1

        # pop last [quantity] elements from stack to dest_stack but keeping the order
        stacks[dest_stack_index].extend(stacks[stack_index][-quantity:])
        stacks[stack_index] = stacks[stack_index][:-quantity]

    print("Part 2 answer = ", end="")
    for stack in stacks:
        print(stack.pop(), end="")
    print()
