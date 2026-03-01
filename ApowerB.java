// A power B 
// Given 2 numbers - A and B, evaluate AB.


import java.io.*;
import java.util.*;

public class ApowerB {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        int t=sc.nextInt();
        while(t-->0){
            long m=1000000007;
            long a=sc.nextInt();
            long b=sc.nextInt();
            long pow=1;
            while(b!=0){
                if((b&1)==1){
                    pow=(pow*a)%m;
                }
                a=(a*a)%m;
                b=b>>1;
            }
            System.out.println(pow);
        }
    }
}
