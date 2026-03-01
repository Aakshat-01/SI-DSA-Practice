import java.io.*;
import java.util.*;

public class Reverse_Bits {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        int t=sc.nextInt();
        while(t-->0){
            long n=sc.nextInt();
            long rev=0;
            for(int i=0;i<32;i++){
                long bit=n&1;
                rev=rev<<1;
                rev=rev|bit;
                n=n>>1;
            }
            System.out.println(rev);
        }
    }
}
