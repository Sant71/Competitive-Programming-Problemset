
//Multiply Two Numbers and Determine If the Result Is an Integer or Float
#include <iostream>
#include <limits>


int main()
{
    constexpr   float eps = std::numeric_limits<float>::epsilon();
    srand(static_cast<unsigned>(time(0))); // تهيئة المولد

    while (eps) {
        float r = static_cast<float>(rand()) / RAND_MAX;
        float a = r, b = r;
        //eps is the smallest difference between two floating-point numbers it is used to compare floating-point numbers for equality


        //fmod  returns the remainder of dividing two floating-point numbers
        // if the remainder is 0, then the result is an integer
        //ternary operator (condition ? if true :if  false)
        std::cout << a * b << ((fmod(a * b, 1) < eps) ? " The result is an integer.\n" : "The result is a float.\n");
    }
}
    /* AdeepseekI suggesion :

#include <iostream>
#include <cmath>
#include <limits>

int main() {
    float a = 1.0000001f;
    float b = 1.0f;

    // بدون epsilon (مقارنة غير آمنة)
    if (fmod(a, b) == 0.0f) { // قد يفشل بسبب أخطاء التقريب
        std::cout << "Integer (unreliable)\n";
    }

    // مع epsilon (مقارنة آمنة)
    float eps = std::numeric_limits<float>::epsilon();
    if (std::abs(fmod(a, b)) < eps) {
        std::cout << "Integer (reliable)\n";
    }
}



*/




