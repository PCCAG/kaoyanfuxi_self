from dataclasses import dataclass


@dataclass
class Student:
    name: str
    age: int
    grade: float


s1 = Student("Alice", 18, 3.8)
s2 = Student("Bob", 19, 3.5)

print(s1)  # Student(name='Alice', age=18, grade=3.8)
print(s2)  # Student(name='Bob', age=19, grade=3.5)
print(s1 == s2)  # False

print(s1.age > s2.age)


# `dataclass` 是一个 Python 装饰器，用于简化创建和操作包含数据的类。以下是该装饰器的主要用法和参数解释：

# ### 函数签名

# ```python
# def dataclass(
#     __cls: None,
#     /
# ) -> ((type[_T@dataclass]) -> type[_T@dataclass]): ...
# ```

# ```python
# def dataclass(
#     __cls: type[_T@dataclass],
#     /
# ) -> type[_T@dataclass]: ...
# ```

# ```python
# def dataclass(
#     *,
#     init: bool = True,
#     repr: bool = True,
#     eq: bool = True,
#     order: bool = False,
#     unsafe_hash: bool = False,
#     frozen: bool = False,
#     match_args: bool = True,
#     kw_only: bool = False,
#     slots: bool = False
# ) -> ((type[_T@dataclass]) -> type[_T@dataclass]): ...
# ```

# ### 参数说明

# - `__cls`: 被装饰的类，或者在使用 `None` 时表示该装饰器将返回一个包含所有参数默认值的可调用对象。

# - `init`: 如果为 `True`，则为类添加 `__init__()` 方法。

# - `repr`: 如果为 `True`，则为类添加 `__repr__()` 方法。

# - `eq`: 如果为 `True`，则为类添加富比较的方法（`__eq__`等）。

# - `order`: 如果为 `True`，则为类添加富比较的方法，包括排序。

# - `unsafe_hash`: 如果为 `True`，则为类添加 `__hash__()` 方法。

# - `frozen`: 如果为 `True`，则创建的实例在创建后不能再进行属性赋值，即成为不可变对象。

# - `match_args`: 如果为 `True`，则为类添加 `__match_args__` 元组。

# - `kw_only`: 如果为 `True`，则所有字段默认为仅关键字参数。

# - `slots`: 如果为 `True`，则为类添加 `__slots__` 属性。

# ### 返回值

# 返回与传入的类相同的类，但根据类中定义的字段添加了双下划线方法（如 `__init__`、`__repr__` 等）。

# ### 主要作用

# `dataclass` 装饰器通过检查 PEP 526 中的 `__annotations__`，自动为类生成一些特殊方法，避免了手动编写这些方法的繁琐过程。这些方法包括初始化方法、字符串表示方法、比较方法等。通过设置不同的参数，可以定制生成的类的行为，使其满足特定的需求，如是否可变、是否生成 `__slots__` 属性等。
