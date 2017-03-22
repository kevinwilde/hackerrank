class Node:
    def __init__(self):
        self.parent = self
        self.count = 1
        
def union(x, y):
    if x == None or y == None:
        return
    xRoot = find(x)
    yRoot = find(y)
    if xRoot == yRoot:
        return
    else:
        yRoot.parent = xRoot
        xRoot.count += yRoot.count
    
def find(x):
    if x == None:
        return None
    if x.parent != x:
        x.parent = find(x.parent)
    return x.parent

def main():
    n, q = map(int, input().split())
    nodes = [Node() for _ in range(n)]
    for _ in range(q):
        query = input().split()
        
        if query[0] == 'M':
            assert(len(query) == 3)
            union(nodes[int(query[1])-1], nodes[int(query[2])-1])
        elif query[0] == 'Q':
            assert(len(query) == 2)
            print(find(nodes[int(query[1])-1]).count)
            
main()