#include <iostream>
#include <variant> //C++ 17 +
using namespace std;
namespace Costom
{
    struct Rectangle
    {

        int Length;
        int width;
        int area = Length * width;
        int girth = 2 * (Length + width);
    };

};
//
void print(const auto &a) // C++17 +
{
    cout << a << endl;
}
//
template <typename T>
void print2(const T &a)
{
    cout << a << endl;
};
int main()
{
    using namespace Costom;
    // 两种结构初始化方法
    Rectangle A = {2, 3};
    Rectangle B{3, 4}; // C++11 +
    print(A.Length);
    print(B.area);
    print(sizeof(A));
    print(sizeof(B));
    //
    print2(A.Length);
    print2(B.area);
    print2(sizeof(A));
    print2(sizeof(B));
    // 16 16
    return 0;
}

// struct Rectangle
// {
//     struct AddVisitor
//     {
//         template <typename T, typename U>
//         auto operator()(const T &a, const U &b) const
//         {
//             return a + b;
//         }
//     };
//     struct multiplyVisitor
//     {
//         template <typename T, typename U>
//         auto operator()(const T &a, const U &b) const
//         {
//             return a * b;
//         }
//     };
//     variant<int, double> Length;
//     variant<int, double> width;
//     variant<int, double> area = visit(multiplyVisitor{}, Length, width);
//     variant<int, double> girth_half = visit(AddVisitor{}, Length, width);
//     variant<int, double> girth = visit(AddVisitor{}, girth_half, girth_half);
// };