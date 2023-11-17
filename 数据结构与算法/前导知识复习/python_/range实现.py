# from copy import copy
from rich import print
from typing import Optional


class Range:
    def __init__(self, start: int, stop: Optional[int] = None, step: int = 1) -> None:
        if step == 0:
            raise ValueError("step cannot be 0")
        self._start: int = start if stop is not None else 0
        self._stop: int = stop if stop is not None else start
        self._step: int = step
        self._length: int = max(
            0, (self._stop - self._start + abs(step) - 1) // abs(step)
        )
        self._current_index: int = 0

    def __len__(self) -> int:
        return self._length

    def __getitem__(self, k: int) -> int:
        if k < 0:
            k += len(self)
        if not 0 <= k < self._length:
            raise IndexError("index out of range")

        return (
            self._start + k * self._step
            if self._step > 0
            else self._start + (len(self) - k - 1) * abs(self._step)
        )

    def __iter__(self) -> "RangeIterator":
        return Range.RangeIterator(self)

    class RangeIterator:
        def __init__(self, range_obj: "Range") -> None:
            self.range_obj: "Range" = range_obj
            self._current_index: int = range_obj._current_index

        def __next__(self) -> int:
            if self._current_index < self.range_obj._length:
                result = self.range_obj[self._current_index]
                self._current_index += 1
                return result
            else:
                raise StopIteration()

        def __iter__(self) -> "Range.RangeIterator":
            return self


r = Range(8, step=-2)
print(list(r))
print(list(iter(r)))
for p, i in enumerate(r):
    print(i)
    print(r[p])

print(range(2))
# r = range(1, 10)
# print(r[1])  # 2

# print(list(r))

# Range类的实现


## 参数
# from tomlkit import value
# from unittest import result
# from sympy import N


# class Range:
#     def __init__(self, start, stop, step=1):
#         self.start = start
#         self.stop = stop
#         self.step = step

#     def __iter__(self):
#         # 返回一个迭代器对象，通常是自己
#         return self

#     def __next__(self):
#         # 返回迭代器中的下一个元素
#         if (self.step > 0 and self.start < self.stop) or (
#             self.step < 0 and self.start > self.stop
#         ):
#             result = self.start
#             self.start += self.step
#             return result
#         else:
#             # 迭代结束时抛出 StopIteration 异常
#             raise StopIteration()


# # 使用自定义的 Range 类
# r = Range(2, 8, 1)

# # 使用 list() 函数将迭代器转换为列表
# print(list(r))

# # 通过 iter() 函数获取迭代器，并使用 list() 函数转换为列表
# print(list(iter(r)))

# # 使用 for 循环迭代
# for i in r:
#     print(i)


# r = Range(2, 8, 1)
# print(list(r))
# print(list(iter(r)))
# for i in r:
#     print(i)


# r = Range(5, 10, -2)
# # r = range(0, 7, 7)

# print(r.__len__())
# # print(list(r))

# for i in r:
#     print(i)


# r = Range(5, 10, -2)
# # r = range(0, 7, 7)

# print(r.__len__())
# # print(list(r))

# for i in r:
#     print(i)
# print("---")

# i = iter(r)
# for _ in r:
#     print(next(i))


# 迭代器是一个带有 `__iter__` 和 `__next__` 方法的对象。让我详细解释这两个方法以及迭代器的工作原理。

# ### `__iter__` 方法

# - 所有可迭代的对象都需要实现 `__iter__` 方法，该方法应该返回一个迭代器对象。
# - 这个方法通常返回 `self` 或者另一个实现了 `__next__` 方法的对象。
# - 当你调用 `iter(iterable)` 时，它实际上就是调用了 `iterable.__iter__()`。

# ### `__next__` 方法

# - 迭代器对象必须实现 `__next__` 方法，该方法返回迭代器的下一个元素。
# - 当没有更多元素可供迭代时，应该抛出 `StopIteration` 异常，以通知调用者迭代结束。
# - 当你调用 `next(iterator)` 时，它实际上就是调用了 `iterator.__next__()`。

# ### 自定义的 Range 类

# 现在，让我们来看看如何在自定义的 `Range` 类中实现这两个方法：

# ```python
# class Range:
#     def __init__(self, start, stop, step=1):
#         self.start = start
#         self.stop = stop
#         self.step = step

#     def __iter__(self):
#         # 返回一个新的迭代器对象
#         return RangeIterator(self.start, self.stop, self.step)

# class RangeIterator:
#     def __init__(self, start, stop, step):
#         self.current = start
#         self.stop = stop
#         self.step = step

#     def __iter__(self):
#         return self

#     def __next__(self):
#         if (self.step > 0 and self.current < self.stop) or (self.step < 0 and self.current > self.stop):
#             result = self.current
#             self.current += self.step
#             return result
#         else:
#             raise StopIteration()
# ```

# ### 迭代器的工作原理

# 1. **使用 `list()` 函数进行迭代：**
#    ```python
#    r = Range(2, 8, 1)
#    print(list(r))
#    ```
#    这里，`list(r)` 实际上调用了 `r.__iter__()` 获取迭代器对象，然后通过迭代器对象的 `__next__` 方法逐个获取元素，直到抛出 `StopIteration` 异常为止。

# 2. **使用 `iter()` 函数和 `for` 循环进行迭代：**
#    ```python
#    r = Range(2, 8, 1)
#    print(list(iter(r)))
#    for i in r:
#        print(i)
#    ```
#    这里，`iter(r)` 返回了迭代器对象，然后 `for` 循环通过调用迭代器对象的 `__next__` 方法逐个获取元素，直到抛出 `StopIteration` 异常为止。

# 3. **使用手动获取迭代器和 `next()` 函数进行迭代：**
#    ```python
#    i = iter(r)
#    for _ in r:
#        print(next(i))
#    ```
#    在这里，`iter(r)` 获取了迭代器对象，然后通过调用 `next(i)` 逐个获取元素，直到抛出 `StopIteration` 异常为止。

# 总之，迭代器是一个用于支持迭代协议的对象，它可以被 `iter()` 函数调用，并且可以通过 `next()` 函数逐个返回元素。当没有更多元素可供迭代时，迭代器应该抛出 `StopIteration` 异常，标志着迭代的结束。
