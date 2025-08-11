#include <iostream>

    int main() {   
    int w, h, a;
    std::cin >> w >> h >> a;
    std::cout <<((w % a == 0 ? w / a : w / a + 1) * (h % a == 0 ? h / a : h / a + 1));
    return 0;
}
