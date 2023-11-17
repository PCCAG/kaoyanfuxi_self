from typing import overload


class MyClass:
    @overload
    def my_function(self, arg: int) -> int:
        ...

    @overload
    def my_function(self, arg: str) -> str:
        ...

    def my_function(self, arg):
        # 具体的实现代码在这里
        if isinstance(arg, int):
            return arg * 2
        elif isinstance(arg, str):
            return arg.upper()
        else:
            raise TypeError("Unsupported argument type")


# 使用
obj = MyClass()
result_int = obj.my_function(42)  # 调用第一个 @overload-decorated 函数的具体实现
result_str = obj.my_function("hello")  # 调用第二个 @overload-decorated 函数的具体实现
