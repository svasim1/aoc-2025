banks = open("input.txt").read().strip().split("\n")

def find_battery(bank):
    n = len(bank)
    battery = [int(c) for c in bank]
    suffix_max = [0] * n
    suffix_max[-1] = -1
    for i in range(n - 2, -1, -1):
        suffix_max[i] = max(battery[i+1], suffix_max[i+1])
    best = 0
    for i in range(n - 1):
        candidate = 10 * battery[i] + suffix_max[i]
        if candidate > best:
            best = candidate
    return best

total = 0
for bank in banks:
    val = find_battery(bank)
    total += val

print("total =", total)