
import java.util.*;

public class PrimeNo {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		System.out.println("Enter a Number: ");
		int num = sc.nextInt();
		
		boolean isPrime = true;
		
		for(int i = 2; i < num ; i ++) {
			if (num % i == 0) {
				isPrime = false;
			}
		}if(isPrime) {
			System.out.println(num+ " is a Prime Number");
		}else {
			System.out.println(num+ " is not a Prime Number");
		}
		sc.close();
	}

}
