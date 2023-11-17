# from ast import Expression
# import operator
# from ast import List
from typing import Callable, Union, Sequence
from rich import print
from numbers import Number  # noqa: F401

# from dataclasses import dataclass


# 定义一个Vector类，它有following属性：
# demension
# data
# len

# 功能:

# 索引与改变相应的值
# 相加,相乘
# 遍历, 打印


class Vector:
    def __init__(self, d: int = 0, data: Sequence[Union[int, float]] = []) -> None:
        self._coords: list[int | float] = list(data) if data else [0] * d  # 值
        self._d: int = d if d else len(self._coords)  # 维度
        if self._d != len(self._coords):
            raise ValueError(
                f"Dimension mismatch: expected {d} elements, got {len(data)}"
            )

    def __len__(self) -> int:
        return self._d

    def __str__(self) -> str:
        return f"<{str(self._coords)[1:-1]}>"

    def __getitem__(self, j: int) -> Union[int, float]:
        return self._coords[j]

    def __setitem__(self, j: int, val: Union[int, float]) -> None:
        self._coords[j] = val

    def __eq__(self, other: "Vector") -> bool:
        return self._coords == other._coords

    def __ne__(self, other: "Vector") -> bool:
        return not self == other  # rely on __eq__

    def __element_wise_operation(
        self,
        other: Union[int | float, "Vector"],
        operation: Callable[[Union[int, float], Union[int, float]], Union[int, float]],
    ) -> "Vector":
        if isinstance(other, (int, float)):
            result = Vector(len(self))
            result._coords = [operation(x, other) for x in self._coords]
            return result
        elif isinstance(other, Vector):
            if len(self) != len(other):  # 维度不同时报错
                raise ValueError("dimensions must agree")
            result = Vector(len(self))
            result._coords = [
                operation(x, y) for x, y in zip(self._coords, other._coords)
            ]
            return result
        else:
            raise TypeError(
                "unsupported operand type(s) for *: 'Vector' and '{}'".format(
                    type(other)
                )
            )

    def __add__(self, other: Union[int | float, "Vector"]) -> "Vector":
        return self.__element_wise_operation(other, operation=lambda x, y: x + y)

    def __sub__(self, other: Union[int | float, "Vector"]) -> "Vector":
        return self.__element_wise_operation(other, operation=lambda x, y: x - y)

    def __mul__(self, other: Union[int | float, "Vector"]) -> "Vector":
        return self.__element_wise_operation(other, operation=lambda x, y: x * y)


if __name__ == "__main__":
    a = Vector(4)
    a[0] = 3
    a[1] = 30
    a[2] = 300.76
    print(a[0], a[1], a[2])
    print(a.__len__())
    #
    print(a)  # <__main__.Vector object at 0x0000027E7B1CD630>
    # <3, 30, 300.76, 0>

    print(a + a + a)
    print(a - a - a - a)
    print(a * a * a)

    print(Vector(4, data=(1, 2, 3, 4)))
    print(a == Vector(4, [3, 30, 300.76, 0]))
    print(a == Vector(4, [1, 30, 300.76, 0]))

    b = Vector(7, (1, 2, 3, 4, 5, 6, 7))
    print(b)
    # c = Vector(2, data=(1, 2, 3, 4))#ValueError: Dimension mismatch: expected 2 elements, got 4
    d = Vector(data=[1, 2, 3, 3])

    print(d)

    for i in b:
        print(i)

    # lambda1 = lambda x, y: x - y
    # print(type(lambda1))  # <class 'function'>


# from typing import Sequence, Union, Callable


# class Vector:
#     def __init__(self, d: int = 0, data: Sequence[Union[int, float]] = []) -> None:
#         if d == 0:
#             d = len(data)
#         self._coords: list[Union[int, float]] = list(data) if data else [0] * d
#         self._d: int = d
#         if self._d != len(self._coords):
#             raise ValueError(
#                 f"Dimension mismatch: expected {d} elements, got {len(data)}"
#             )

#     def __len__(self) -> int:
#         return self._d

#     def __str__(self) -> str:
#         return f"<{', '.join(map(str, self._coords))}>"

#     def __getitem__(self, j: int) -> Union[int, float]:
#         return self._coords[j]

#     def __setitem__(self, j: int, val: Union[int, float]) -> None:
#         self._coords[j] = val

#     def __eq__(self, other: "Vector") -> bool:
#         return self._coords == other._coords

#     def __ne__(self, other: "Vector") -> bool:
#         return not self == other

#     def __element_wise_operation(
#         self,
#         other: Union[int | float, "Vector"],
#         operation: Callable[[Union[int, float], Union[int, float]], Union[int, float]],
#     ) -> "Vector":
#         if isinstance(other, (int, float)):
#             result = Vector(len(self))
#             result._coords = [operation(x, other) for x in self._coords]
#             return result
#         elif isinstance(other, Vector):
#             if len(self) != len(other):
#                 raise ValueError("Dimensions must agree")
#             result = Vector(len(self))
#             result._coords = [
#                 operation(x, y) for x, y in zip(self._coords, other._coords)
#             ]
#             return result
#         else:
#             raise TypeError(
#                 f"Unsupported operand type(s) for *: 'Vector' and '{type(other)}'"
#             )

#     def __add__(self, other: Union[int | float, "Vector"]) -> "Vector":
#         return self.__element_wise_operation(other, operation=lambda x, y: x + y)

#     def __sub__(self, other: Union[int | float, "Vector"]) -> "Vector":
#         return self.__element_wise_operation(other, operation=lambda x, y: x - y)

#     def __mul__(self, other: Union[int | float, "Vector"]) -> "Vector":
#         return self.__element_wise_operation(other, operation=lambda x, y: x * y)


# 这个Vector的实现是一个基本的向量类，它可以实现向量的创建、访问、修改、比较、加减乘等运算。它的优点是代码简洁，使用了类型注解和文档字符串，提高了可读性和可维护性。它的缺点是有些功能不完善，还有些方面可以改进，例如：

# - 它没有定义向量的复制方法，如果要复制一个向量，需要使用Vector类的构造函数，如v2 = Vector(len(v1), v1)，这不太方便，也不符合Python的习惯。可以定义一个__copy__方法，让向量支持copy模块的copy函数，如v2 = copy.copy(v1)。
# - 它没有定义向量的迭代方法，如果要遍历向量的元素，需要使用索引，如for i in range(len(v)): print(v[i])，这不太高效，也不符合Python的习惯。可以定义一个__iter__方法，让向量支持迭代协议，如for x in v: print(x)。
# - 它没有定义向量的哈希方法，如果要将向量作为字典的键或集合的元素，需要使用tuple函数，如d = {tuple(v): 1}，这不太直观，也不符合Python的习惯。可以定义一个__hash__方法，让向量支持哈希协议，如d = {v: 1}。
# - 它没有定义向量的标量积和向量积方法，这是向量的常用运算，可以增加向量的功能性。可以定义一个dot方法和一个cross方法，分别实现向量的标量积和向量积，如v1.dot(v2)和v1.cross(v2)。
# - 它没有定义向量的模和单位向量方法，这是向量的常用属性，可以增加向量的可用性。可以定义一个norm方法和一个unit方法，分别返回向量的模和单位向量，如v.norm()和v.unit()。
