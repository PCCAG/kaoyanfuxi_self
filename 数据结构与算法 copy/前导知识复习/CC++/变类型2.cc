#include <variant> //C++ 17
#include <string>
#include <iostream>
#include <any>
using namespace std;
struct Rectangle
{
private:
    variant<int, double> area(variant<int, double> a, variant<int, double> b){
        

    };
    variant<int, double> girth;

public:
    variant<int, double> length;
    variant<int, double> width;
};

void print(const auto &a) // C++17 +
{
    cout << a << endl;
}

int main()
{
    Rectangle A;
    A.length = 3;
    A.width = 4;
    int lenth = get<int>(A.length);
    int width = get<int>(A.width);
    print(lenth);
    print(width);
    return 0;
}