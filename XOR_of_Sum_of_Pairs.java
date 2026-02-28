// XOR of Sum of Pairs 
// You are given an array of integers. 
// Find the XOR of all the pairwise sums formed by the elements of the array.


import java.io.*;
import java.util.*;

public class XOR_of_Sum_of_Pairs {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        int t=sc.nextInt();
        while(t-->0){
            int n=sc.nextInt();
            long arr[]=new long[n];
            for(int i=0;i<n;i++){
                arr[i]=sc.nextLong();
            }
            long ans=0;
            for(int i=0;i<n;i++){
                ans=ans^(arr[i]+arr[i]);
            }
            System.out.println(ans);
        }
    }
}
