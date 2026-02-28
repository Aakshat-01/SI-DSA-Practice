import java.io.*;
import java.util.*;

public class Triple_Trouble {
    static boolean checkBit(int N,int i){
        return (((N>>i)&1) == 1);
    }

    static int f(int[] arr, int N){
        int ans=0;
        for(int i=0;i<=31;i++){
            int set=0,unset=0;
            for(int j=0;j<N;j++){
                if(checkBit(arr[j],i)){
                    set++;
                } else {unset++;}
            }
            if(set%3!=0) {ans=ans|(1<<i);}
        }
        return ans;
    }

    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        int t=sc.nextInt();
        while(t-->0){
            int n=sc.nextInt();
            int[] arr= new int[n];
            for(int i=0;i<n;i++){
                arr[i]=sc.nextInt();
            }
            System.out.println(f(arr,n));
        }
    }
}