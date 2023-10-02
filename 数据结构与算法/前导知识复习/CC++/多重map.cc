#include <iostream>
#include <map>
#include <string>
std::string a;
// 等值范围查找（Equal Range Lookup）： 使用 equal_range 函数可以获取一个键对应的值的范围。
void equip_range_()
{
    std::multimap<int, std::string> myMultimap;

    myMultimap.insert({1, "apple"});
    myMultimap.insert({2, "banana"});
    myMultimap.insert({1, "apricot"});
    myMultimap.insert({3, "cherry"});

    // 查找键为 1 的所有值
    auto range = myMultimap.equal_range(1);

    // 遍历范围
    for (auto it = range.first; it != range.second; ++it)
    {
        std::cout << "Key: " << it->first << ", Value: " << it->second << std::endl;
    }
}
void key_value_equip()
{

    std::multimap<int, std::string> myMultimap;

    myMultimap.insert({1, "apple"});
    myMultimap.insert({1, "apple"});
    myMultimap.insert({1, "apple"});

    // 使用范围迭代器
    for (auto it = myMultimap.begin(); it != myMultimap.end(); ++it)
    {
        std::cout << "Key: " << it->first << ", Value: " << it->second << std::endl;
    };
}

int main()
{
    // std::multimap 允许重复的键，这使得每个键都可以对应多个值。
    // 在 std::map 中，每个键唯一对应一个值，而在 std::multimap 中，一个键可以对应多个值，形成多对一的映射关系。
    // 范围迭代器（Range Iterators）： 使用迭代器可以访问 std::multimap 中的键值对。由于可能存在多个值对应于相同的键，迭代器会遍历这些值。
    std::multimap<int, std::string>
        myMultimap;

    myMultimap.insert({1, "apple"});
    myMultimap.insert({2, "banana"});
    myMultimap.insert({1, "apricot"});
    myMultimap.insert({3, "cherry"});

    // 使用范围迭代器
    for (auto it = myMultimap.begin(); it != myMultimap.end(); ++it)
    {
        std::cout << "Key: " << it->first << ", Value: " << it->second << std::endl;
    }

    equip_range_();
    key_value_equip();
    return 0;
}
