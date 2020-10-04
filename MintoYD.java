// Write a Java program to convert minutes into number of years and days.

import java.util.*;

class MintoYD{
	static double min;
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		System.out.println("Input the Number of Minutes: ");
		min = sc.nextDouble();

		mintoYD();

	}

	public static void mintoYD(){
		double minInY = 60 * 24 * 365;
		long years = (long)(min / minInY);
		int days = (int)(min / 60 / 24) % 365;

		System.out.println((int) min + " minutes is approximately " + years + " years and " + days + " days");
	}
}