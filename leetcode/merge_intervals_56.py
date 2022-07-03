from typing import List
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        #210ms
        if not intervals:
            return []

        result_ranges = []
        last_range = None  # последний отрезок, что мы видели

        for rng in sorted(intervals):  # обязательно сортируем

            if not last_range:
                last_range = rng
                continue

            # если начало текущего отрезка меньше конца предыдущего
            if rng[0] <= last_range[1]:
                # расширяем предыдущий отрезок на текущий
                last_range = (last_range[0], max(rng[1], last_range[1]))

            # старый отрезок всё, начинаем новый
            else:
                result_ranges.append(last_range)
                last_range = rng

        else:
            # граничный случай для последнего элемента
            result_ranges.append(last_range)
        return result_ranges
        #	314 ms
        # intervals.sort(key = lambda i : i[0])
        # output = [intervals[0]]

        # for start, end in intervals[1:]:
        #     last_end = output[-1][1]
        #     if start <= last_end:
        #         output[-1][1] = max(output[-1][1], end)
        #     else:
        #         output.append([start, end])
        # return output
