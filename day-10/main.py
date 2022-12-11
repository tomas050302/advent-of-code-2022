n_cycles = {
    "addx": 2,
    "noop": 1
}


def is_interesting_cycle(cycle):
    return cycle == 20 or (cycle-20) % 40 == 0


def is_new_line(cycle):
    return cycle % 40 == 0


with open("input.txt") as f:
    x = 1
    cur_cycle = 0
    ans = 0
    for line in f.readlines():
        op = line.strip().split()[0]
        if op == "noop":
            cur_cycle += 1
            if is_interesting_cycle(cur_cycle):
                ans += x * cur_cycle
            continue
        value = line.strip().split()[1]
        n = 2
        for i in range(n):
            cur_cycle += 1
            if is_interesting_cycle(cur_cycle):
                ans += x * cur_cycle

        x += int(value)

    print()
    print("Part 1 answer:", ans)


def build_ctr_line(crt_line, x):


with open("input.txt") as f:
    x = 1
    cur_cycle = 0
    ans = 0
    crt_line = ''
    for line in f.readlines():
        op = line.strip().split()[0]
        if op == "noop":
            cur_cycle += 1
            crt_line = build_ctr_line(crt_line, x)
            if is_new_line(cur_cycle):
                print(crt_line)
            continue
        value = line.strip().split()[1]
        n = 2
        for i in range(n):
            cur_cycle += 1
            if is_interesting_cycle(cur_cycle):
                ans += x * cur_cycle

        x += int(value)
