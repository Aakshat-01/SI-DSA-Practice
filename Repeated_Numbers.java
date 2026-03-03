// Repeated Numbers
// You are given an array of N elements. 
// All elements of the array are in range 1 to N-2. 
// All elements occur once except two numbers, which occur twice. 
// Your task is to find the two repeating numbers.

import java.io.*;
import java.util.*;

public class Repeated_Numbers {

    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        int t=sc.nextInt();
        while(t-->0){
            int n=sc.nextInt();
            int[] arr=new int[n];
            for(int i=0;i<n;i++){
                arr[i]=sc.nextInt();
            }
            int[] hash=new int[1000000+1];
            for(int i=0;i<n;i++){
                hash[arr[i]]+=1;
            }
            for(int i=0;i<hash.length;i++){
                if(hash[i]>1){
                    System.out.print(i+" ");
                }
            }
            System.out.println();
        }
    }
}