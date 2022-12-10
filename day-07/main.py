cur_dir = root = {}
stack = []

MAX = 100000

with open('input.txt', 'r') as f:
    for line in f.readlines():
        line = line.strip()
        if line.startswith('$'):
            if line.find("$ cd") != -1:
                dir = line[5:]
                if dir == "/":
                    stack = []
                    cur_dir = root
                elif dir == "..":
                    cur_dir = stack.pop()
                else:
                    if dir not in cur_dir:
                        cur_dir[dir] = {}
                    stack.append(cur_dir)
                    cur_dir = cur_dir[dir]
        else:
            x, y = line.split()
            if not x == "dir":
                cur_dir[y] = int(x)


def solve(dir):
    sum = 0
    size = 0

    for d in dir.values():
        x, y = solve(d) if type(d) == dict else (d, 0)
        size += x
        sum += y
    if size <= MAX:
        sum += size
    return (size, sum)


print()
print("Part 1 answer", solve(root)[1])

# Part 2


def get_size(d):
    if type(d) == int:
        return d
    return sum(map(get_size, d.values()))


THRESHOLD = get_size(root) - 40000000
ROOT_SIZE = get_size(root)
# get all directories with size > THRESHOLD
# return the smallest one


def get_dir(d):
    ans = ROOT_SIZE
    if get_size(d) >= THRESHOLD:
        ans = get_size(d)
    for dir in d.values():
        if type(dir) == int:
            continue
        candidate = get_dir(dir)
        ans = min(ans, candidate)
    return ans


print("Part 2 answer", get_dir(root))
