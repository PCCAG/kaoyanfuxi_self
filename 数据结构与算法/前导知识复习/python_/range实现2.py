class Range:
    def __init__(self, start, stop, step=1):
        self.start = start
        self.stop = stop
        self.step = step

    def __iter__(self):
        # 返回一个新的迭代器对象
        return RangeIterator(self.start, self.stop, self.step)


class RangeIterator:
    def __init__(self, start, stop, step):
        self.current = start
        self.stop = stop
        self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        if (self.step > 0 and self.current < self.stop) or (
            self.step < 0 and self.current > self.stop
        ):
            result = self.current
            self.current += self.step
            return result
        else:
            raise StopIteration()


r = Range(2, 8, 2)
# print(r[2])
print(list(r))
print(list(iter(r)))
for i in r:
    print(i)
i = iter(r)
for _ in r:
    print(next(i))
