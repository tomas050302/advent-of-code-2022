matrix = []
with open("input.txt") as f:
    for line in f:
        # append to the matrix all the digits in the line, keep in mind that the line is only composed of a single number
        matrix.append([int(x) for x in line.strip()])


def is_in_edge(i, j):
    return i == 0 or j == 0 or i == len(matrix) - 1 or j == len(matrix[i]) - 1


def is_visible_left(i, j):
    for k in range(j - 1, -1, -1):
        if matrix[i][k] >= matrix[i][j]:
            return False

    return True


def is_visible_right(i, j):
    for k in range(j + 1, len(matrix[i])):
        if matrix[i][k] >= matrix[i][j]:
            return False

    return True


def is_visible_up(i, j):
    for k in range(i - 1, -1, -1):
        if matrix[k][j] >= matrix[i][j]:
            return False

    return True


def is_visible_down(i, j):
    for k in range(i + 1, len(matrix)):
        if matrix[k][j] >= matrix[i][j]:
            return False

    return True


def is_visible(i, j):
    if is_in_edge(i, j):
        return True

    return is_visible_left(i, j) or is_visible_right(i, j) or is_visible_up(i, j) or is_visible_down(i, j)


counter = 1
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if is_visible(i, j):
            counter += 1

print()
print("Part 1 answer:", counter)


def get_first_taller_index_left(i, j):
    if is_in_edge(i, j):
        return 0

    counter = 1
    while (matrix[i][j-counter] < matrix[i][j] and not is_in_edge(i, j-counter)):
        counter += 1
    return counter


def get_first_taller_index_right(i, j):
    if is_in_edge(i, j):
        return 0

    counter = 1
    while (matrix[i][j+counter] < matrix[i][j] and not is_in_edge(i, j+counter)):
        counter += 1
    return counter


def get_first_taller_index_up(i, j):
    if is_in_edge(i, j):
        return 0

    counter = 1
    while (matrix[i-counter][j] < matrix[i][j] and not is_in_edge(i-counter, j)):
        counter += 1
    return counter


def get_first_taller_index_down(i, j):
    if is_in_edge(i, j):
        return 0

    counter = 1
    while (matrix[i+counter][j] < matrix[i][j] and not is_in_edge(i+counter, j)):
        counter += 1
    return counter


highest = 0
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        left = get_first_taller_index_left(i, j)
        right = get_first_taller_index_right(i, j)
        up = get_first_taller_index_up(i, j)
        down = get_first_taller_index_down(i, j)

        result = left * right * up * down
        if (result > highest):
            highest = result

print("Part 2 answer:", highest)
