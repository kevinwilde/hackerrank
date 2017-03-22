import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int n = scan.nextInt();
        int m = scan.nextInt();
        
        Edge[] edges = new Edge[m];
        for (int i = 0; i < m; i++) {
            int x = scan.nextInt();
            int y = scan.nextInt();
            int r = scan.nextInt();
            edges[i] = new Edge(x-1, y-1, r);
        }
        
        int[][] dists = floydWarshall(n, edges);
        int q = scan.nextInt();
        
        for (int i = 0; i < q; i++) {
            int a = scan.nextInt();
            int b = scan.nextInt();
            int d = dists[a-1][b-1];
            if (d < Integer.MAX_VALUE) {
                System.out.println(d);
            } else {
                System.out.println(-1);
            }
        }
    }
    
    private static int[][] floydWarshall(int n, Edge[] edges) {
        int[][] dists = new int[n][n];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (i == j) {
                    dists[i][j] = 0;
                } else {
                    dists[i][j] = Integer.MAX_VALUE;
                }
            }
        }
        for (int i = 0; i < edges.length; i++) {
            Edge edge = edges[i];
            dists[edge.from][edge.to] = edge.weight;
        }
        for (int k = 0; k < n; k++) {
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {
                    int t = dists[i][k] + dists[k][j];
                    // All weights are non-negative
                    if (t >= 0 && t < dists[i][j]) {
                        dists[i][j] = t;
                    }
                }
            }
        }
        return dists;
    }
}

class Edge {
    int from;
    int to;
    int weight;

    Edge(int from, int to, int weight) {
        this.from = from;
        this.to = to;
        this.weight = weight;
    }
}
