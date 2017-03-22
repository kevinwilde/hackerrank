import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    static int[] findNearestDirty(int posr, int posc, String[] board) {
        ArrayList<int[]> dirtyCells = new ArrayList<int[]>();
        for (int i = 0; i < 5; i++) {
            for (int j = 0; j < 5; j++) {
                if (board[i].charAt(j) == 'd') {
                    dirtyCells.add(new int[]{i, j});
                }
            }
        }
        int numDirtyCells = dirtyCells.size();
        double minDist = 99.0;
        int[] nearestDirty = new int[]{-1, -1};
        for (int i = 0; i < numDirtyCells; i++) {
            double dist = Math.sqrt(Math.pow(dirtyCells.get(i)[0] - posr, 2) + Math.pow(dirtyCells.get(i)[1] - posc, 2));
            if (dist < minDist) {
                minDist = dist;
                nearestDirty = dirtyCells.get(i);
            }
        }
        return nearestDirty;
    }
    
    static void nextMove(int posr, int posc, String[] board){
        if (board[posr].charAt(posc) == 'd') {
            System.out.println("CLEAN");
        }
        else {
            int[] nearD = findNearestDirty(posr, posc, board);
            if (nearD[0] < posr) { System.out.println("UP"); }
            else if (nearD[0] > posr) { System.out.println("DOWN"); }
            else if (nearD[1] < posc) { System.out.println("LEFT"); }
            else if (nearD[1] > posc) { System.out.println("RIGHT"); }
            else { System.out.println("Oops"); }
        }
    }
    
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int [] pos = new int[2];
        String board[] = new String[5];
        for(int i=0;i<2;i++) pos[i] = in.nextInt();
        for(int i=0;i<5;i++) board[i] = in.next();
        nextMove(pos[0], pos[1], board);
    }
}
