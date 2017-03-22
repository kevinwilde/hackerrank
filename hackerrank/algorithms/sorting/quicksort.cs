using System;
using System.Collections.Generic;
using System.IO;
class Solution {

    static void printSubarray(int[] ar, int start, int end) {
        string output = "";
        for (int i = start; i <= end; i++) {
            output += Convert.ToString(ar[i]) + ' ';
        }
        if (output.Length > 0) {
            Console.WriteLine(output);
        }
    }
    
    static void copyArray(List<int> n, int[] a, int start, int end) {
        for (int i = start; i <= end; i++) {
            a[i] = n[i-start];
        }
    }
    
    static int partition(int[] ar, int start, int end) {
        int pivotValue      = ar[start];
        List<int> leftList  = new List<int>();
        List<int> rightList = new List<int>();

        for (int i = start+1; i <= end; i++) {
            if (ar[i] > pivotValue) { rightList.Add(ar[i]); }
            else { leftList.Add(ar[i]); }
        }
        
        int p = start + leftList.Count;
        copyArray(leftList, ar, start, p-1);
        copyArray(rightList, ar, p+1, end);

        ar[p] = pivotValue;
        
        return p;
    }
    
    static void quickSort(int[] ar, int start, int end) {
        if (start < end) {
            int p = partition(ar, start, end);
            quickSort(ar, start, p-1);
            quickSort(ar, p+1, end);
            printSubarray(ar, start, end);
        }
    }
    
    static void quickSort(int[] ar) {
        quickSort(ar, 0, ar.Length-1);
    }
    

    static void Main(String[] args) {
        int _ar_size;
        _ar_size = Convert.ToInt32(Console.ReadLine());
        int [] _ar =new int [_ar_size];
        String elements = Console.ReadLine();
        String[] split_elements = elements.Split(' ');
        for(int _ar_i=0; _ar_i < _ar_size; _ar_i++) {
            _ar[_ar_i] = Convert.ToInt32(split_elements[_ar_i]); 
        }

        quickSort(_ar);
    }
}