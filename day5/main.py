lines = open("input.txt").read().strip().splitlines()
ranges = []
ids = []
i = 0
while i < len(lines) and lines[i].strip() != "" and "-" in lines[i]:
    a, b = lines[i].strip().split("-")
    ranges.append((int(a), int(b)))
    i += 1
while i < len(lines) and lines[i].strip() == "":
    i += 1
while i < len(lines):
    if lines[i].strip():
        ids.append(int(lines[i].strip()))
    i += 1
    
def count_fresh(ranges, ids):
    total = 0
    for x in ids:
        fresh = False
        for a, b in ranges:
            if a <= x <= b:
                fresh = True
                break
        if fresh:
            total += 1
    return total

def count_fresh_ranges(ranges):
    if not ranges:
        return 0
    r = sorted(ranges)
    total = 0
    cur_a, cur_b = r[0]
    for a, b in r[1:]:
        if a <= cur_b + 1:
            if b > cur_b:
                cur_b = b
        else:
            total += cur_b - cur_a + 1
            cur_a, cur_b = a, b
    total += cur_b - cur_a + 1
    return total

print("part1 total =", count_fresh(ranges, ids))
print("part2 total =", count_fresh_ranges(ranges))