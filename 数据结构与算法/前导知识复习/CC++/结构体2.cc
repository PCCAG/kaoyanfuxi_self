#include <iostream>
#include <variant>
#include <map>
#include <unordered_map>
#include <string>
#include <any>
#include <stdexcept>
using namespace std;
struct Rectangle
{
    double lenth;
    double width;
    double area = lenth * width;
    double girth = 2 * (lenth + width);
};
struct ComplexNumber
{
    double real;
    double infact;
};
struct Card
{
private:
    std::unordered_map<std::string, int> ShapeMap = {{"Clubs", 1}, {"Diamonds", 2}, {"Hearts", 3}, {"Spades", 0}};
    std::unordered_map<std::string, int> SpecialFaceMap = {{"J", 11}, {"Q", 12}, {"K", 13}, {"A", 14}, {"Joker", 15}, {"BigJoker", 16}};
    std::variant<int, std::string> __face;
    std::variant<int, std::string> __shape;

    // 😅
    template <typename T, typename U>
    T get_variant_value(const std::variant<T, U> &variant, const std::unordered_map<U, T> &valueMap)
    {
        if (std::holds_alternative<T>(variant))
        {
            return std::get<T>(variant);
        }
        else
        {
            try
            {
                return valueMap.at(std::get<U>(variant));
            }
            catch (const std::exception &e)
            {
                std::cerr << "😅 No such Card in ShapeMap or SpecialFaceMap  : " << e.what() << std::endl;
                return -1;
            }
        }
    };

public:
    int face;
    int shape;
    Card(std::variant<int, std::string> &&f, std::variant<int, std::string> &&s) : __face(f), __shape(s)
    {
        face = get_variant_value(__face, SpecialFaceMap);
        shape = get_variant_value(__shape, ShapeMap);
    };
};

int main()
{

    struct Card
        card[] = {{10, "Clubs"}, {11, "Spades"}, {12, "Spades"}, {13, "Diamonds"}, {14, "Spades"}};

    cout << card[0].face << " " << card[0].shape << endl;
    cout << card[1].face << " " << card[1].shape << endl;
    cout << card[2].face << " " << card[2].shape << endl;
    cout << card[3].face << " " << card[3].shape << endl;

    //  struct Rectangle A
    //  {
    //      3, 4
    //  };
    //  struct ComplexNumber C
    //  {
    //      1, 2
    //  };
    //  std::cout << A.lenth << " " << A.width << " " << sizeof(A) << "\n";
    //  printf_s("%g + %gi\n", C.real, C.infact);
    //  printf_s("%f + %fi\n", C.real, C.infact);
    return 0;
}

// struct Card
// {
// private:
//     enum class Shape
//     {
//         Spades,
//         Hearts,
//         Diamonds,
//         Clubs,
//         Joker
//     };
//     enum class Face
//     {
//         Two,
//         Three,
//         Four,
//         Five,
//         Six,
//         Seven,
//         Eight,
//         Nine,
//         Ten,
//         Jack,
//         Queen,
//         King,
//         Ace,
//         SmallJoker,
//         BigJoker
//     };

// public:
//     Shape shape;
//     Face face;
//     Card(Shape s, Face f) : shape(s), face(f) {}

//     bool operator<(const Card &c) const
//     {
//         if (shape == c.shape)
//         {
//             return face < c.face;
//         }
//         else
//         {
//             return shape < c.shape;
//         }
//     }

//     friend std::ostream &operator<<(std::ostream &os, const Card &c);

//     static const int CARD_NUM = 54;
//     static Card cards[CARD_NUM];

//     static void init_cards();
//     static void shuffle_cards();
// };

// std::ostream &operator<<(std::ostream &os, const Card &c)
// {
//     os << c.shape << " " << c.face;
//     return os;
// }

// void Card::init_cards()
// {
//     // initialize the cards array with all 54 cards
// }

// void Card::shuffle_cards()
// {
//     // randomly shuffle the cards array
// }

// 垃圾判断
//  if (holds_alternative<int>(__face))
//  {
//      face = get<int>(__face);
//  }
//  else
//  {
//      face = SpecialFaceMap[get<string>(__face)];
//  }
//  if (holds_alternative<int>(__shape))
//  {
//      shape = get<int>(__shape);
//  }
//  else
//  {
//      shape = ShapeMap[get<string>(__shape)];
//  }

// struct Card
// {
// private:
//     static const std::unordered_map<std::string, int> ShapeMap;
//     static const std::unordered_map<std::string, int> SpecialFaceMap;

//     std::variant<int, std::string> __face;
//     std::variant<int, std::string> __shape;
// 高级
// public:
//     int face;
//     int shape;

//     Card(std::variant<int, std::string> &&f, std::variant<int, std::string> &&s)
//         : __face(std::move(f)), __shape(std::move(s)),
//           face(std::holds_alternative<int>(__face) ? std::get<int>(__face) : SpecialFaceMap[std::get<std::string>(__face)]),
//           shape(std::holds_alternative<int>(__shape) ? std::get<int>(__shape) : ShapeMap[std::get<std::string>(__shape)]){};

//     // 声明为 const 成员函数
//     void someFunction() const
//     {
//         // 不修改对象状态的代码
//     }
// };

// // 预先计算映射值
// const std::unordered_map<std::string, int> Card::ShapeMap = {{"Heart", 1}, {"Diamonds", 2}, {"Hearts", 3}, {"Spades", 0}};
// const std::unordered_map<std::string, int> Card::SpecialFaceMap = {{"J", 11}, {"Q", 12}, {"K", 13}, {"A", 14}, {"Joker", 15}, {"BigJoker", 16}};
