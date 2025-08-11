// Domino piling.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>

int main()
{
	int m,n;
	std::cin >> m >> n;

	int a = m * n;

	if (a % 2 == 0)
		std::cout << a / 2<<std::endl;
	else 
		std::cout << a  << std::endl;


}
