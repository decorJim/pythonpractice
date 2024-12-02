

public class Main {

    public static boolean search2DMatrixs(int[][] matrix, int target) {

        int nbRows = matrix.length;
        int nbColumns = matrix[0].length;

        int row = 0;
        int column = matrix[0].length - 1;

        while(row >= 0 && row < nbRows && column >= 0 && column < nbColumns) {
            if (matrix[row][column] == target) {
                return true;
            } else if (matrix[row][column] > target) {
                column--;
            } else if (matrix[row][column] < target) {
                row++;
            }
        }
        return false;
    }

    public static void main(String[] args) {

        int[][] matrix = {
                {1,4,7,11,15},
                {2,5,8,12,19},
                {3,6,9,16,22},
                {10,13,14,17,24},
                {18,21,23,26,30}
        };

        for (int i = 0; i < matrix.length; i++) {
            for (int j = 0; j < matrix[0].length; j++) {
                System.out.print(matrix[i][j] + " ");
            }
            System.out.println();
        }
        System.out.println();

        System.out.println(search2DMatrixs(matrix, 5));
        System.out.println(search2DMatrixs(matrix, 20));

    }
}