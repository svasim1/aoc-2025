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

def find_battery_k(bank, k):
    n = len(bank)
    if k <= 0 or n < k:
        return 0
    result_digits = []
    start = 0
    remaining = k
    while remaining > 0:
        last_index = n - remaining
        
        best_digit = -1
        best_idx = start
        for i in range(start, last_index + 1):
            d = ord(bank[i]) - 48 
            if d > best_digit:
                best_digit = d
                best_idx = i
                if best_digit == 9:
                    break
        result_digits.append(str(best_digit))
        start = best_idx + 1
        remaining -= 1
    return int("".join(result_digits))

# part 1
total = 0
for bank in banks:
    val = find_battery(bank)
    total += val
print("part1 total =", total)

# part 2
total12 = 0
for bank in banks:
    val12 = find_battery_k(bank, 12)
    total12 += val12
print("part2 total =", total12)