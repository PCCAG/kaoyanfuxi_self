#include <iostream>
#include <typeinfo> // 在 C++ 中，typeid 运算符和 std::type_info 类来查看变量的类型。这主要用于运行时类型信息(RTTI)。
#include <windows.h>
#include <string>
#include <bitset>
// 计数用的变量
namespace CounterVariable
{
    int TimeFunctionOrder = 0;
};
//
void a();
void b();
void c();
void d();
void e();
void f();
//
template <typename Func>
void Endsperate(Func func);
//
template <typename T>
std::string getFunctionName(T func);
//
//
// 主函数
int main()
{

    Endsperate(a);
    Endsperate(b);
    Endsperate(c);
    Endsperate(d);
    Endsperate(e);
    Endsperate(f);
    return 0;
}
//
// template <typename T>
// std::string getFunctionName(T func)
// {
//     return typeid(func).name();
// };

template <typename Func>
void Endsperate(Func func)
{
    using namespace CounterVariable;
    using namespace std;
    TimeFunctionOrder++;
    // 获取控制台句柄
    HANDLE hConsole = GetStdHandle(STD_OUTPUT_HANDLE);
    // 设置文本颜色
    SetConsoleTextAttribute(hConsole, FOREGROUND_RED | FOREGROUND_INTENSITY);
    cout << "\n\n--------Splitting---------" << TimeFunctionOrder << "\n\n";
    // 恢复默认颜色
    SetConsoleTextAttribute(hConsole, FOREGROUND_RED | FOREGROUND_GREEN | FOREGROUND_BLUE);

    func();
    // SetConsoleTextAttribute(hConsole, FOREGROUND_RED | FOREGROUND_INTENSITY);
    cout << "\n\n--------Splitting---------" << TimeFunctionOrder << "\n\n";
    // SetConsoleTextAttribute(hConsole, FOREGROUND_RED | FOREGROUND_GREEN | FOREGROUND_BLUE);
};

// C++指针
void a()
{
    using namespace std;
    int x = 5;
    int *ptr = &x;
    cout << ptr << endl;  // 0xab9d9ff9e4
    cout << *ptr << endl; // 5
    const type_info &type_infoX = typeid(ptr);
    // printf_s("%d", type_infoX.name());
    cout << type_infoX.name() << endl;
    // const std::type_info& typeInfoX = typeid(x);
    //  cout << type(ptr);
    //  cout << ptr 输出的是指针的地址，而 cout << *ptr 输出的是指针所指向的值。
    cout << "Pointer traversing an array." << endl;
    int A[] = {1, 2, 3, 4, 5, 6, 7, 8};
    int *pin = A;
    for (int i = 0; i < size(A); ++i)
    {
        cout << *pin << endl;
        pin++;
        // 2. 指针解引用运算符 *：
        // 指针解引用运算符 *用于访问指针所指向的内存地址上的值。
    }
    cout << "mulity denmison array" << endl;
    int B[3][3] = {{1, 2, 3}, {11, 22, 33}, {111, 222, 333}};
    int C[] = {1, 2};
    cout << *C << endl;
    cout << C << endl;
    cout << *B << endl;
    cout << B << endl;
    cout << &B << endl;
    // 1
    // 0x3b34bff858
    // 0x3b34bff860
    // 0x3b34bff860
    // 0x3b34bff860

    // cout << B 输出的是数组的首元素的地址，即第一行的地址。这个地址是一个指向数组的指针
    // cout << &B 输出的是整个二维数组的地址，而不仅仅是首元素的地址。这个地址是一个指向整个二维数组的指针。
    for (const auto &i : B)
    {
        for (int ii : i)
        {
            cout << ii << " ";
        };
        cout << endl;
    }
}
// C++类型输出
void b()
{
    int x = 42;
    double y = 3.14;
    const char *str = "Hello";

    const std::type_info &typeInfoX = typeid(x);
    const std::type_info &typeInfoY = typeid(y);
    const std::type_info &typeInfoStr = typeid(str);

    std::cout << "Type of x: " << typeInfoX.name() << std::endl;
    std::cout << "Type of y: " << typeInfoY.name() << std::endl;
    std::cout << "Type of str: " << typeInfoStr.name() << std::endl;
    // Type of x : i
    // Type of y : d
    // Type of str : PKc
    // 输出结果 "i" 表示 int 类型，"d" 表示 double 类型，"PKc" 表示指向 const char* 的指针类型。
};
void c(){};

// 进制转换
void d()
{

    int decimalNumber = 42;

    // 转换为二进制
    std::bitset<sizeof(int) * 8> binaryRepresentation(decimalNumber);
    std::cout << "Binary: " << binaryRepresentation << std::endl;
};

// C++枚举
void e()
{

    enum class CustomEnum : char
    {
        Value1,       // char(0)
        Value2,       // char(1)
        Value3 = 100, // char(100)
        Value4        // char(101)
    };
    CustomEnum myVar = CustomEnum::Value1;

    std::cout << "Value1: " << static_cast<int>(CustomEnum::Value1) << std::endl;
    std::cout << "Value2: " << static_cast<int>(CustomEnum::Value2) << std::endl;
    std::cout << "Value3: " << static_cast<int>(CustomEnum::Value3) << std::endl;
    std::cout << "Value4: " << static_cast<int>(CustomEnum::Value4) << std::endl;

    // static_cast 是 C++ 中的一种类型转换操作符，用于进行编译时的类型转换。
    // 它主要用于编译时检查的类型转换，而不执行运行时检查。在你的代码中，static_cast 被用于将枚举值转换为整数进行输出。
};
// C++引用
void f()
{

    using namespace std;
    int a = 10;
    int *p = &a;
    int &d = a;
    cout << p << endl;  // 0x7879bffe0c
    cout << *p << endl; // 10
    cout << d << endl;  // 10
    cout << &d << endl; // 0x7879bffe0c
};
