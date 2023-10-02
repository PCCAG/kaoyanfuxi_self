#include <iostream>
#include <variant>
#include <map>
#include <unordered_map>
#include <string>
#include <any>
#include <stdexcept>
#include <cstdio> //C库
using namespace std;
int main()
{
    int a = 1;
    int *p = &a;
    cout << *p;

    // C++
    int *h = new int[5];
    delete[] h;
    // C
    int *h2 = (int *)malloc(sizeof(int));
    free(h2);

    return 0;
}