lines = open("input.txt").read().splitlines()
w = max(len(l) for l in lines)
rows = len(lines)
grid = [list(l.ljust(w)) for l in lines]

def is_sep_col(col):
    for r in range(rows):
        if grid[r][col] != " ":
            return False
    return True

seps = [is_sep_col(c) for c in range(w)]

segments = []
in_seg = False
start = 0
for c in range(w):
    if not seps[c] and not in_seg:
        in_seg = True
        start = c
    if seps[c] and in_seg:
        in_seg = False
        segments.append((start, c - 1))
if in_seg:
    segments.append((start, w - 1))

def solve_segments(segments):
    total = 0
    for a, b in segments:
        nums = []
        for r in range(rows - 1):
            s = "".join(grid[r][a:b+1]).strip()
            if s:
                nums.append(int(s))
        op = "".join(grid[rows - 1][a:b+1]).strip()
        if op == "+":
            val = 0
            for x in nums:
                val += x
        else:
            val = 1
            for x in nums:
                val *= x
        total += val
    return total

print("total =", solve_segments(segments))