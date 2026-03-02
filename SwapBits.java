import java.io.*;
import java.util.*;

public class SwapBits {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        int t=sc.nextInt();
        while(t-->0){
            int n=sc.nextInt();
            int ans=0,p=0;
            for(int i=0;i<16;i++){
                int bit1=(n>>p)&1;
                int bit2=(n>>(p+1))&1;
                ans+=(bit1<<(p+1));
                ans+=(bit2<<(p));
                p+=2;
            }
            System.out.println(ans);
        }
    }
}
