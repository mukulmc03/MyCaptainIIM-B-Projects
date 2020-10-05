// Write a program for matrix addition and matrix multiplication.

class MatAddMul{
	static int a[][] = {{1, 3, 4},{2, 4, 3},{3, 4, 5}};
	static int b[][]={{1, 3, 4},{2, 4, 3},{1, 2, 4}};

	public static void main(String[] args) {
		MatAdd();
		MatMul();
	}

	static void MatAdd(){
		System.out.println("Matrix Addition is: ");
		for (int i = 0 ; i < 3; i ++ ) {
			for (int j = 0 ; j < 3 ; j ++ ) {
					 		System.out.print(a[i][j] + b[i][j] + " ");
					 	}
					 	System.out.println();	 	
		}	
	} 

	static void MatMul(){
		System.out.println("Matrix Multiplication is: ");
		int c[][] = new int[3][3];
		for (int k = 0; k < 3 ; k ++ ) {
			for (int l = 0 ; l < 3 ; l ++ ) {
				c[k][l] = 0;
				for (int m = 0 ; m < 3 ; m ++ ) {
					c[k][l] += a[k][m] * b[m][l];
				}
				System.out.print(c[k][l] + " ");
			}
			System.out.println();
		}
	}	
}