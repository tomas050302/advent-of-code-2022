n_cycles = {
    "addx": 2,
    "noop": 1
}


def is_interesting_cycle(cycle):
    return cycle == 20 or cycle % 40 == 0


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
        n = n_cycles[op]
        for i in range(n):
            cur_cycle += 1
        if op == "addx":
            x += int(value)
        if is_interesting_cycle(cur_cycle):
            ans += x * cur_cycle

    print()
    print(ans)
