#include<iostream>
#include <bits/stdc++.h>
using namespace std;

#define U 0
#define N 9

// Finding 0 in every row and col
bool FindUnassignedLoc(int grid[N][N], int& row,int& col){
    for(row =0;row<N;row++){
        for(col=0;col<N;col++){
            if(grid[row][col]== U )
                return true;
        }
    }
    return false;
}

// Check if the assigned no. is placed in its correct row
bool usedInRow(int grid[N][N],int row,int num){
    
        for(int col = 0;col<N;col++){
            if(grid[row][col]==num)
                return true;
        }
    
    return false;
}

// Check if the assigned no. is placed in its correct column
bool usedInCol(int grid[N][N],int col,int num){
    
        for(int row = 0;row<N;row++){
            if(grid[row][col]==num){
                return true;
            }
        }
    
    return false;
}

// Check if the assigned no. is in the correct grid
bool usedInBox(int grid[N][N],int box_row , int box_col,int num){
    for(int row=0;row<3;row++){
        for(int col=0;col<3;col++){
            if(grid[row+box_row][col+box_col]==num)
                return true;
        }
    }
    return false;
}

// Check if the no. is assigned to its accurate spot
bool isSafe(int grid[N][N],int row,int col,int num){
    return !usedInRow(grid,row,num) && !usedInCol(grid,col,num) && !usedInBox(grid,row-row%3,col-col%3,num) && grid[row][col]==U;
}

// Main Soduku solver function
bool Sudoku_solver(int grid[N][N]){
    int row,col;

    // Base Condition
    if(!FindUnassignedLoc(grid,row,col))
        return true;

    for(int num=1;num<=9;num++){

        if(isSafe(grid,row,col,num)){

            //Assign value to the empty box if the above condition return true
            grid[row][col]=num;

            if(Sudoku_solver(grid))
                return true;

            //If above case fail to return true
            grid[row][col] = U;
        }
    }
    return false;
}

// Print the resultant gird
void print_grid(int grid[N][N]){
    for(int row=0;row<N;row++){
        for(int col=0;col<N;col++){
            cout<<grid[row][col]<<" ";
        }
        cout<<endl;
    }
}


int main(){

    int grid[N][N] = {{7,8,0,4,0,0,1,2,0},
                      {6,0,0,0,7,5,0,0,9},
                      {0,0,0,6,0,1,0,7,8},
                      {0,0,7,0,4,0,2,6,0},
                      {0,0,1,0,5,0,9,3,0},
                      {9,0,4,0,6,0,0,0,5},
                      {0,7,0,3,0,0,0,1,2},
                      {1,2,0,0,0,7,4,0,0},
                      {0,4,9,2,0,6,0,0,7}};

    cout<<"-------SUDOKU BOARD UNSOLVED--------"<<endl;
    print_grid(grid);

    if(Sudoku_solver(grid)==true){
        cout<<"-------SUDOKU BOARD SOLVED--------"<<endl;
        print_grid(grid);
    }
    else{
        cout<<"No Solution exist";
    }

    return 0;

}
