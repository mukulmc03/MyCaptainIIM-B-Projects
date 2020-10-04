// Program to implement Switch keyword

import java.util.*;

class MySwitch{
	public static void main(String[] args) {
		int choice;
		Scanner sc = new Scanner(System.in);
		System.out.println("Please, enter your Choice\n\t1. Hi\n\t2. Hey\n\t3. Hello");
		choice = sc.nextInt();

		switch(choice){
			case 1: System.out.println("You said Hi");
					break;

			case 2: System.out.println("You said Hey");
					break;		

			case 3: System.out.println("You said Hello");
					break;

			default: System.out.println("Please, enter Valid Choice");
				
		}
	}
}