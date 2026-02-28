import java.io.*;
import java.util.*;

public class Sum_of_XOR_of_pairs {
    static boolean checkBit(long N,int i){
        return (((N>>i)&1) == 0);
    }
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        int t=sc.nextInt();
        while(t-->0){
            int n=sc.nextInt();
            long arr[]=new long[n];
            for(int i=0;i<n;i++){
                arr[i]=sc.nextLong();
            }
            long sum=0;
            for(int i=0;i<=31;i++){
                int c=0;
                for(int j=0;j<n;j++){
                    if(checkBit(arr[j],i)){
                        c++;
                    }
                }
                sum+=(1L<<i)*(c*(n-c));
            }
            System.out.println(2*sum);
        }
    }
}