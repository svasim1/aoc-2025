def accessible(grid):
    h = len(grid)
    w = len(grid[0]) if h > 0 else 0
    dirs = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
    total = 0
    for i in range(h):
        for j in range(w):
            if grid[i][j] != "@":
                continue
            occ = 0
            for di, dj in dirs:
                ni = i + di
                nj = j + dj
                if 0 <= ni < h and 0 <= nj < w and grid[ni][nj] == "@":
                    occ += 1
            if occ < 4:
                total += 1
    return total

def remove_all(grid):
    g = [list(row) for row in grid]
    h = len(g)
    w = len(g[0]) if h > 0 else 0
    dirs = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
    total = 0
    while True:
        to_remove = []
        for i in range(h):
            for j in range(w):
                if g[i][j] != "@":
                    continue
                occ = 0
                for di, dj in dirs:
                    ni = i + di
                    nj = j + dj
                    if 0 <= ni < h and 0 <= nj < w and g[ni][nj] == "@":
                        occ += 1
                if occ < 4:
                    to_remove.append((i, j))
        if not to_remove:
            break
        for i, j in to_remove:
            g[i][j] = "."
        total += len(to_remove)
    return total

grid = open("input.txt").read().strip().splitlines()

print("part1 total =", accessible(grid))
print("part2 total =", remove_all(grid))