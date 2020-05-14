import java.util.*;
import java.lang.*;
import java.io.*;

class SumOfPowers
 {
	public static void main (String[] args)
	 {
	 Scanner scan = new Scanner(System.in);
	 int T = scan.nextInt();
	 for(int i = 0; i < T; i++){
	     int X = scan.nextInt();
	     int n = scan.nextInt();
	     System.out.println(expressNumber(X,n));
	  }
	 }

	 public static int nthRootCalculator(int X, int power){
	     return (int) Math.floor( Math.pow(Math.E,Math.log(X)/power));
	 }

	 public static int expressNumber(int X, int n){
	     return recExpressNumber(X,0,1,n);
	 }

	 public static int power(int num, int n){
	     if(n == 0){
	         return 1;
	     } else if(n % 2 == 0){
	         return power(num,n/2) * power(num,n/2);
	     } else {
	         return num * power(num,n/2) * power(num, n/2);
	     }
	 }

	 private static int recExpressNumber(int X,int n ,int current_sum, int current_nbr){
	     int result = 0;

	     int p = power(current_nbr,n);
	     while(p + current_sum < X)
	     {
	         result = recExpressNumber(X,n ,p + current_sum, current_nbr + 1);
	         current_nbr++;
	         p = power(current_nbr,n);
	     }
	     if(p + current_sum == X){
	         result++;
	     }

	     return result;
	 }
}
