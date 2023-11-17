from functools import singledispatch
from bisect import bisect
from typing import NoReturn, List, Union


@singledispatch
def classifier(d: Union[int, List[int]]) -> NoReturn:
    raise TypeError("Unsupported type")


@classifier.register(int)
def _(d: int) -> int:
    """Classify an individual score."""
    score_range = [60, 70, 86, 100]
    score_class = [3, 2, 1, 0]
    index: int = bisect(score_range, d)
    return score_class[index if index < len(score_class) else len(score_class) - 1]


@classifier.register(list)
def _(d: List[int]) -> List[int]:
    """Classify a list of scores."""
    return [classifier(i) for i in d]


grades = {0: "very good", 1: "good", 2: "pass", 3: "failed"}
test_list = [59, 60, 70, 71, 85, 69, 86, 88, 100]


# 测试单个值
for score in test_list:
    print(f"{grades[classifier(score)]} {score}")


# 测试一个列表
result_list = classifier(test_list)
print(f"{list(zip([grades[i] for i in result_list], test_list))}")


# 这段文档描述了 Python 中的 `bisect` 函数，该函数用于在一个已排序的列表中找到插入指定元素的位置。

# 让我解释一下文档中的各个部分：

# 1. **函数签名：**
#    ```python
#    (variable) def bisect(
#        a: SupportsLenAndGetItem[SupportsRichComparisonT@bisect_right],
#        x: SupportsRichComparisonT@bisect_right,
#        lo: int = 0,
#        hi: int | None = None,
#        *,
#        key: None = None
#    ) -> int
#    ```

#    这是 `bisect` 函数的定义。它接受一个已排序列表 `a`，一个待插入元素 `x`，以及可选的参数 `lo`（默认值为 0）、`hi`（默认值为列表 `a` 的长度），以及关键字参数 `key`（默认值为 `None`）。返回值是一个整数，表示插入元素 `x` 后，列表 `a` 中的索引位置。

# 2. **函数作用：**
#    ```python
#    Return the index where to insert item x in list a, assuming a is sorted.
#    ```

#    函数的作用是返回在已排序列表 `a` 中插入元素 `x` 的位置。如果列表已经是有序的，返回的索引值 `i` 满足以下条件：对于 `a[:i]` 中的每个元素 `e`，都有 `e <= x`，对于 `a[i:]` 中的每个元素 `e`，都有 `e > x`。

# 3. **参数说明：**
#    ```python
#    Optional args lo (default 0) and hi (default len(a)) bound the slice of a to be searched.
#    ```

#    函数有两个可选参数 `lo` 和 `hi`，它们限定了要搜索的列表 `a` 的切片范围。`lo` 默认为 0，`hi` 默认为列表 `a` 的长度。

# 综合而言，`bisect` 函数通过二分查找的方式，找到在已排序列表中插入元素 `x` 的正确位置，并返回该位置的索引值。
#
# 如果 `x` 已经存在于列表中，那么插入后会放在相同元素的最右侧。这个函数对于在有序列表中插入元素并保持有序性非常有用。
