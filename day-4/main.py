with open('input.txt', 'r') as f:
    count = 0
    count_overlap = 0
    for line in f:
        first, second = line.split(',')
        first_interval_begin, first_interval_end = first.split('-')
        second_interval_begin, second_interval_end = second.split('-')

        first_interval_begin = int(first_interval_begin)
        first_interval_end = int(first_interval_end)
        second_interval_begin = int(second_interval_begin)
        second_interval_end = int(second_interval_end)

        if (first_interval_begin >= second_interval_begin and first_interval_end <= second_interval_end) or (second_interval_begin >= first_interval_begin and second_interval_end <= first_interval_end):
            count += 1
        if (first_interval_begin <= second_interval_begin and first_interval_end >= second_interval_begin) or (second_interval_begin <= first_interval_begin and second_interval_end >= first_interval_begin):
            count_overlap += 1

print()
print("Part 1 answer:", count)
print("Part 2 answer:", count_overlap)
