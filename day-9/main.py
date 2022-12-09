def is_far(pos1, pos2):
    return abs(pos1[0] - pos2[0]) > 1 or abs(pos1[1] - pos2[1]) > 1


visited = set()
with open("input.txt") as f:
    current_pos_h = (0, 0)
    current_pos_t = (0, 0)
    visited.add(current_pos_t)

    for line in f.readlines():
        [direction, distance] = line.strip().split()
        distance = int(distance)
        if direction == "R":
            for i in range(distance):
                current_pos_h = (current_pos_h[0] + 1, current_pos_h[1])
                if is_far(current_pos_h, current_pos_t):
                    current_pos_t = (current_pos_h[0] - 1, current_pos_h[1])
                    visited.add(current_pos_t)
        elif direction == "L":
            for i in range(distance):
                current_pos_h = (current_pos_h[0] - 1, current_pos_h[1])
                if is_far(current_pos_h, current_pos_t):
                    current_pos_t = (current_pos_h[0] + 1, current_pos_h[1])
                    visited.add(current_pos_t)
        elif direction == "U":
            for i in range(distance):
                current_pos_h = (current_pos_h[0], current_pos_h[1] + 1)
                if is_far(current_pos_h, current_pos_t):
                    current_pos_t = (current_pos_h[0], current_pos_h[1] - 1)
                    visited.add(current_pos_t)
        elif direction == "D":
            for i in range(distance):
                current_pos_h = (current_pos_h[0], current_pos_h[1] - 1)
                if is_far(current_pos_h, current_pos_t):
                    current_pos_t = (current_pos_h[0], current_pos_h[1] + 1)
                    visited.add(current_pos_t)

print()
print("Part 1 answer:", len(visited))
