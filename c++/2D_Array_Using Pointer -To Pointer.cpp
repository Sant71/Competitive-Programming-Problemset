
#include <iostream>

int main()
{

    srand(time(0));

    int row, col;

    std::cin >> row >> col;

    int** Array2D = new int* [row];
    
    for (int i = 0; i < row; i++)
    {
        *(Array2D + i) = new int[col]();
    }
    
    for (int i = 0; i < row; i++)
    { 
        for (int j = 0; j < col; j++)
        {
            std::cout << Array2D[i][j] << " ";
        }
        std::cout <<"\n";

    }

    for (int i = 0; i < row; i++)

            delete[] Array2D[i];
    delete[] Array2D;
}
