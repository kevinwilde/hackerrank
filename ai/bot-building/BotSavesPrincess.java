import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {
    
    static void moveHorizontally(int mx, int px, int n) {
        while (mx < px) {
            System.out.println("RIGHT");
            mx++;
        }
        while (mx > px) {
            System.out.println("LEFT");
            mx--;
        }
    }
    
    static void moveVertically(int my, int py, int n) {
        while (my < py) {
            System.out.println("DOWN");
            my++;
        }
        while (my > py) {
            System.out.println("UP");
            my--;
        }
    }

    static void displayPathtoPrincess(int n, String [] grid){
        int mx = -1;
        int my = -1;
        int px = -1;
        int py = -1;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i].charAt(j) == 'p') {
                    px = j;
                    py = i;
                }
                else if (grid[i].charAt(j) == 'm') {
                    mx = j;
                    my = i;
                }
            }
        }
        moveHorizontally(mx, px, n);
        moveVertically(my, py, n);    
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int m;
        m = in.nextInt();
        String grid[] = new String[m];
        for(int i = 0; i < m; i++) {
            grid[i] = in.next();
        }
        displayPathtoPrincess(m,grid);
    }
}
