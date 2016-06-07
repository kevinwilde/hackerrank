class Node:
    def __init__(self):
        self.predecessor = -1
        self.cost = float("inf")
        self.neighbors = []
        self.visited = False
        self.popped = False
    def addNeighbor(self, neighbor, dist):
        self.neighbors.append([neighbor, dist])
    def markVisited(self):
        self.visited = True

def containsUnpoppedNodes(arr, size):
    res = False
    for i in range(size):
        if arr[i].popped == False:
            res = True
            break
    return res        
        
def extractMin(arr, size):
    minCost = float("inf")
    minIndex = -1
    for i in range(size):
        if ((arr[i].popped == False) and (arr[i].cost < minCost)):
            minCost = arr[i].cost
            minIndex = i
    arr[minIndex].popped = True
    return minIndex

def main():
    T = int(input())
    for j in range(T):
        numNodes, numEdges = map(int, input().split())
        nodes = []
        for k in range(numNodes):
            nodes.append(Node())
        for k in range(numEdges):
            x, y, r = map(int, input().split())
            nodes[x-1].addNeighbor(y-1, r)
            nodes[y-1].addNeighbor(x-1, r)
        startNode = int(input()) - 1
        nodes[startNode].visited = True
        nodes[startNode].cost = 0
        
        #while containsUnpoppedNodes(nodes, numNodes):
        for kk in range(numNodes):
            u = extractMin(nodes, numNodes)        
            for n in range(len(nodes[u].neighbors)):
                neighborNode = nodes[u].neighbors[n][0]
                weight = nodes[u].neighbors[n][1]
                newCost = weight + nodes[u].cost
                if newCost < nodes[neighborNode].cost:
                    nodes[neighborNode].cost= newCost
                    nodes[neighborNode].predecessor = u
                    

        ans = ""
        for i in range(numNodes):
            if nodes[i].cost == 0:
                continue
            elif nodes[i].cost == float("inf"):
                ans += "-1 "
            else:
                ans += str(nodes[i].cost) + " "
        print(ans)

if __name__ == '__main__':
    main()