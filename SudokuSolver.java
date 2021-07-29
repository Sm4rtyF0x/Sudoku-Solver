/**
 * 
 * Main
 */
public class SudokuSolver {
    public int[][] grid = {
        {0,0,0,0,1,7,0,5,0},
        {0,0,0,0,0,0,9,8,4},
        {0,0,0,0,0,6,0,7,0},
        {0,5,0,0,0,0,4,0,0},
        {0,1,0,2,0,3,0,0,0},
        {7,0,0,0,0,0,0,0,2},
        {0,0,0,0,9,0,0,0,0},
        {0,0,4,0,8,0,0,0,5},
        {9,0,8,7,0,0,0,0,0},
    };

    public void print_grid(){
        System.out.println();
        for (int i = 0; i < 9; i++){
            if (i % 3 == 0){
                System.out.println("+---------+---------+---------+");
            }
            for (int j = 0; j < 9; j++){
                if (j % 3 == 0){
                    System.out.print("|");
                }
                System.out.print(String.format(" %s ",grid[i][j]));
                if (j == 8){
                    System.out.print("|");
                }
            }
            System.out.println();
            if (i == 8){
                System.out.print("+---------+---------+---------+");
            }
        }
        System.out.println();
        System.out.println();
    }

    public boolean posible(int x, int y, int n){
        for (int i = 0; i < 9; i++){
            if (grid[i][x] == n){
                return false;
            }
        }
        for (int i = 0; i < 9; i++){
            if (grid[y][i] == n){
                return false;
            }
        }
        int x0 = (int) Math.floor(x / 3) * 3;
        int y0 = (int) Math.floor(y / 3) * 3;
        for (int i = 0; i < 3; i++){
            for(int j = 0; j < 3; j++){
                if(grid[y0+i][x0+j] == n){
                    return false;
                }
            }
        }
        return true;
    }

    public String solve(){
        
        for (int y = 0; y < 9; y++){
            for (int x = 0; x < 9; x++){
                if (grid[y][x] == 0){
                    for (int n=1; n <=9; n++){
                        if (posible(x, y, n) == true){
                            grid[y][x] = n;
                            solve();
                            grid[y][x] = 0;
                        }
                    }
                    return null;
                }
            }
        }
        print_grid();
        return null;
    }

    public static void main(String[] args) {
        SudokuSolver m = new SudokuSolver();
        m.print_grid();
        m.solve();
    }
}