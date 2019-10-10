dirs = [(0, -1) , (0, 1), (-1, 0), (1, 0)]

def check(x, y, t):
    return (x == t[0] and abs(y - t[1]) == 1) or (y == t[1] and abs(x - t[0]) == 1)

def digitJumping(grid, start, finish):
    h = len(grid)
    w = len(grid[0])
    mark = [[False for i in range(w)] for j in range(h)]
    res = [[0 for i in range(w)] for j in range(h)]
    q = [start]
    while (q):
        t = q.pop(0)

        mark[t[0]][t[1]] = True
        # 4 directions bfs
        for x in range(h):
            for y in range(w):
                if ((grid[t[0]][t[1]] == grid[x][y] or check(x, y, t)) and not mark[x][y]):
                    if finish == [x, y]:
                        return res[t[0]][t[1]] + 1
                    else:
                        q.append([x, y])
                        res[x][y] = res[t[0]][t[1]] + 1

        return 0
grid = [[0, 1, 4, 2, 3],
        [1, 4, 2, 8, 2],
        [2, 2, 3, 4, 9],
        [8, 7, 2, 2, 3]]
start = [0, 0]
finish = [3, 4]
print(digitJumping(grid, start, finish))