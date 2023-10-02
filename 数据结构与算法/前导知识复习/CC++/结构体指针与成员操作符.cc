#include <iostream>
struct ComplexNumber
{
    double real;
    double img;
};
int main()
{
    struct ComplexNumber A;
    struct ComplexNumber *p = &A;
    p->real = 4;
    p->img = 9;
    std::cout << A.img << " " << A.real;
    return 0;
}