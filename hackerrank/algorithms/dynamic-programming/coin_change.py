def ways_to_make_change(n, m ,c):
    table = [[0 for _ in range(m)] for _ in range(n+1)]
    
    for i in range(m):
        table[0][i] = 1
    
    for i in range(1, n+1):
        for j in range(m):
            x = table[i - c[j]][j] if i-c[j] >= 0 else 0
            y = table[i][j-1] if j >= 1 else 0
            table[i][j] = x + y
    
    return table[n][m-1]

def main():
    n, m = (int(x) for x in input().split())
    c = [int(x) for x in input().split()]
    print(ways_to_make_change(n, m, c))
    
if __name__ == '__main__':
    main()