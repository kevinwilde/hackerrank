import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {
    
    static boolean moveHorizontally(int mx, int px, int n) {
        if (mx < px) {
            System.out.println("RIGHT");
            return true;
        }
        if (mx > px) {
            System.out.println("LEFT");
            return true;
        }
        return false;
    }
    
    static void moveVertically(int my, int py, int n) {
        if (my < py) {
            System.out.println("DOWN");
            my++;
        }
        if (my > py) {
            System.out.println("UP");
            my--;
        }
    }

    /*
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
    }*/

    static void nextMove(int n, int r, int c, String [] grid) {
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

        boolean move = moveHorizontally(mx, px, n);
        if (!move) {
            moveVertically(my, py, n);  
        }
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n,r,c;
        n = in.nextInt();
        r = in.nextInt();
        c = in.nextInt();
        in.useDelimiter("\n");
        String grid[] = new String[n];


        for(int i = 0; i < n; i++) {
            grid[i] = in.next();
        }

        nextMove(n,r,c,grid);

    }
}
