#include <variant> //C++ 17
#include <string>
#include <iostream>
using namespace std;
void print(const auto &a) // C++17 +
{
    cout << a << endl;
}
int main()
{
    variant<int, double, string> myVariant;
    // 这里创建了一个 std::variant 对象 myVariant，
    // 它可以包含 int、double 或 std::string 类型的值。
    // 这个 std::variant 变量可以在程序运行时存储其中的任一类型的值。
    myVariant = "Nice";
    string c = get<string>(myVariant);
    myVariant = 10;
    int a = get<int>(myVariant);
    myVariant = 1.1;
    // 使用 std::get 时要确保类型匹配，否则会抛出 std::bad_variant_access 异常。
    // 为了避免异常，可以使用 std::holds_alternative 进行类型检查：

    double b = get<double>(myVariant);

    print(a);
    print(b);
    print(c);

    return 0;
}