// Subset Sum 
// Given a set of non-negative integers, and a value S, 
// determine if there is a subset of the given set with sum equal to S.


import java.io.*;
import java.util.*;

public class Subset_Sum {
    static boolean checkBit(int N,int i){
        return (((N>>i)&1) == 1);
    }

    static boolean check(int[] arr, int N, int k){
        for(int i=0;i<(1<<N);i++){
            int sum=0;
            for(int j=0;j<N;j++){
                if(checkBit(i,j)){
                    sum+=arr[j];
                }
            }
            if(sum==k) return true;
        }
        return false;
    }

    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        int t=sc.nextInt();
        while(t-->0){
            int n=sc.nextInt();
            int k=sc.nextInt();
            int[] arr=new int[n];
            for(int i=0;i<n;i++){
                arr[i]=sc.nextInt();
            }
            if(check(arr,n,k)) System.out.println("YES");
            else System.out.println("NO");
        }
    }
}