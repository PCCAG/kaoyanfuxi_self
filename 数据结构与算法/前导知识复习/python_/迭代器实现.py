# from sys import exception
from typing import Callable, Union, Sequence
from rich import print  # noqa: F401
from numbers import Number  # noqa: F401


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
    # a = Vector(data=[1, 2, 3, 4, 5, 6, 7, 8])

    # i_a = iter(a)
    # while 1:
    #     try:
    #         print(next(i_a))
    #     except StopIteration:
    #         break
    #     except Exception:
    #         break

    class Range:
        def __init__(self, start, end):
            self.start = start
            self.end = end

        def __iter__(self):
            # 返回一个迭代器对象，这个对象包含了 __next__ 方法
            self.current = self.start
            return self

        def __next__(self):
            # 定义迭代逻辑，返回下一个元素
            if self.current <= self.end:
                result = self.current
                self.current += 1
                return result
            else:
                # 没有元素可返回时，抛出 StopIteration 异常
                raise StopIteration

    # 使用你的可迭代类
    my_iterable = Range(1, 5)

    # 使用 for 循环遍历
    for value in Range(2, 10):
        print(value)

    print(list(my_iterable))  # [1, 2, 3, 4, 5]
