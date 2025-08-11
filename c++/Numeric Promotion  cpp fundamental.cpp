// Numeric Promotion  cpp fundamental.cpp : This file contains the 'main' function. Program execution begins and ends there.

#include <iostream>
#include <typeinfo> // to know the type of a variable


int main()
{
	float f = 1.02000f; // float
	double d = 1.02000f; // double
	// Numeric promotion occurs when an operation involves mixed types.
	
	int x = 10; // int

	std::cout << (x * f) << "\n"; // Numeric promotion occurs here, x is promoted to float

	auto a = f * d; // auto -> deduces the type based on the expression with numeruc promotion principle

    std::cout << "Hello World!\n";
	std::cout << "Type of a: " << typeid(a).name() << "\n"; // prints the type of a
}