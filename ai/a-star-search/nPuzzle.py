class PriorityQueue:
    def __init__(self):
        self.lst = []
    
    def enqueue(self, x):
        assert(len(x)==3)
        self.lst.append(x)
        self.lst = sorted(self.lst, key=lambda x: x[1])
        
    def dequeue(self):
        return self.lst.pop(0)
        
    def empty(self):
        return len(self.lst) == 0
    
def numPos(board, num):
    k = len(board)
    for rowNum in range(k):
        for colNum in range(k):
            if board[rowNum][colNum] == num:
                return (rowNum, colNum)
    return (-1, -1)

def manhattanDist(board, goal):
    k = len(board)
    assert(len(goal) == k)
    d = 0
    for i in range(k*k):
        curPos = numPos(board, i)
        goalPos = numPos(goal, i)
        d += abs(curPos[0] - goalPos[0]) + abs(curPos[1] - goalPos[1])
    return d

def numMisplacedTiles(board, goal):
    n = 0
    k = len(board)
    assert(len(goal) == k)
    for i in range(k):
        for j in range(k):
            if board[i][j] != goal[i][j]:
                n += 1
    return n

def heuristic(board, goal):
    return manhattanDist(board, goal) + numMisplacedTiles(board, goal)

def canGo(board, direction):
    zp = numPos(board, 0)
    d = direction.lower()
    k = len(board)
    if d == "u":
        return zp[0] > 0
    elif d == "d":
        return zp[0] < k-1
    elif d == "l":
        return zp[1] > 0
    elif d == "r":
        return zp[1] < k-1
    return False

def go(board, direction):
    from copy import deepcopy
    newB = deepcopy(board)
    zp = numPos(board, 0)
    zRow = zp[0]
    zCol = zp[1]
    d = direction.lower()
    if d == "u":
        newB[zRow][zCol] = newB[zRow-1][zCol]
        newB[zRow-1][zCol] = 0
    elif d == "d":
        newB[zRow][zCol] = newB[zRow+1][zCol]
        newB[zRow+1][zCol] = 0
    elif d == "l":
        newB[zRow][zCol] = newB[zRow][zCol-1]
        newB[zRow][zCol-1] = 0
    elif d == "r":
        newB[zRow][zCol] = newB[zRow][zCol+1]
        newB[zRow][zCol+1] = 0        
    return newB

def solve(board, goal):
    closed = []
    openQ = PriorityQueue()
    moves = []
    
    md = manhattanDist(board, goal)
    openQ.enqueue((board, md, []))
    while not openQ.empty():
        cur = openQ.dequeue()
        b = cur[0]
        moves = cur[2]
        g = len(moves)
        if b not in closed:
            closed.append(b)
            if b == goal:
                return moves
            
            if canGo(b, "u"):
                upB = go(b, "u")
                h = heuristic(upB, goal)
                openQ.enqueue((upB, g+h, moves+["UP"]))
            if canGo(b, "d"):
                downB = go(b, "d")
                h = heuristic(downB, goal)
                openQ.enqueue((downB, g+h, moves+["DOWN"]))
            if canGo(b, "l"):
                leftB = go(b, "l")
                h = heuristic(leftB, goal)
                openQ.enqueue((leftB, g+h, moves+["LEFT"]))
            if canGo(b, "r"):
                rightB = go(b, "r")
                h = heuristic(rightB, goal)
                openQ.enqueue((rightB, g+h, moves+["RIGHT"]))
    return []

def main():
    k = int(input())
    board = []
    for _ in range(k):
        row = []
        for _ in range(k):
            row.append(int(input()))
        board.append(row)  
    goal = [[i for i in range(k)] for _ in range(k)]
    for i in range(k):
        goal[i] = [n+i*k for n in goal[i]]
    moves = solve(board, goal)
    print(len(moves))
    for move in moves:
        print(move)
        
main()
