# def __next__(self) -> int:
#     if self._current_index < self._lenth:
#         print(self._current, "current")
#         print(self._current_index, "index")
#         result = self._current
#         self._current = (
#             self[self._current_index + 1]
#             if self._current_index != self._lenth - 1
#             else self[self._current_index]
#         )
#         self._current_index += 1
#         return result
#     else:
#         raise StopIteration()

# def __iter__(self):
#     return self
