#!/usr/bin/python
def traceParents(parents, end_r, end_c, start_r, start_c):    
    cur_r = end_r
    cur_c = end_c
    path = []
    while not (cur_r == start_r and cur_c == start_c):
        path.append((cur_r, cur_c))
        nextc = parents[cur_r][cur_c]
        cur_r = nextc[0]
        cur_c = nextc[1]
    path.append((start_r, start_c))
    path.reverse()
    return path

def nextMove(r, c, pacman_r, pacman_c, food_r, food_c, grid):
    parents = [[None for _ in range(c)] for _ in range(r)]
    visited = [[False for _ in range(c)] for _ in range(r)]
    visited[pacman_r][pacman_c] = True
    
    q = [(pacman_r, pacman_c)]    
    while len(q) > 0:
        cur = q.pop(0)
        cur_r = cur[0]
        cur_c = cur[1]
        
        # Found food
        if cur_r == food_r and cur_c == food_c:
            path = traceParents(parents, cur_r, cur_c, pacman_r, pacman_c)
            print len(path)-1
            for pair in path:
                print pair[0], pair[1]
            return

        # UP
        if cur_r-1 >= 0 and grid[cur_r-1][cur_c] != '%' and not visited[cur_r-1][cur_c]:
            parents[cur_r-1][cur_c] = (cur_r, cur_c)
            q.append((cur_r-1, cur_c))
            visited[cur_r-1][cur_c] = True

        # LEFT
        if cur_c-1 >= 0 and grid[cur_r][cur_c-1] != '%' and not visited[cur_r][cur_c-1]:
            parents[cur_r][cur_c-1] = (cur_r, cur_c)
            q.append((cur_r, cur_c-1))
            visited[cur_r][cur_c-1] = True

        # RIGHT
        if cur_c+1 < c and grid[cur_r][cur_c+1] != '%' and not visited[cur_r][cur_c+1]:
            parents[cur_r][cur_c+1] = (cur_r, cur_c)
            q.append((cur_r, cur_c+1))
            visited[cur_r][cur_c+1] = True

        # DOWN
        if cur_r+1 < r and grid[cur_r+1][cur_c] != '%' and not visited[cur_r+1][cur_c]:
            parents[cur_r+1][cur_c] = (cur_r, cur_c)
            q.append((cur_r+1, cur_c))
            visited[cur_r+1][cur_c] = True
    
    
    return

pacman_r, pacman_c = [ int(i) for i in raw_input().strip().split() ]
food_r, food_c = [ int(i) for i in raw_input().strip().split() ]
r,c = [ int(i) for i in raw_input().strip().split() ]

grid = []
for i in xrange(0, r):
    grid.append(raw_input().strip())

nextMove(r, c, pacman_r, pacman_c, food_r, food_c, grid)