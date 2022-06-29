class Solution:
    def summaryRanges(self, nums):
        def repr(group_start, group_end) -> str:
            # это просто правильно печатает группу

            if last_group_start == last_group_end:
                return str(last_group_end)

            return f"{last_group_start}->{last_group_end}"


       
        if not nums:  # граничный случай
            return ''

        numbers_ = sorted(nums)  # сначала располагаем по порядку
        groups = []  # тут будем хранить группы

        last_group_start = None
        last_group_end = None

        for n in numbers_:
            # это первая итерация, просто говорим, что группа началась и закончилась
            if last_group_end is None:
                last_group_start = n
                last_group_end = n

            # если предыдущая группа отличается от текущего числа на 1, 
            # то это число входит в группу, то есть становится концом группы
            elif last_group_end == n-1:
                last_group_end = n

            # иначе мы понимаем, что группа закончилась,
            # мы её запоминаем и начинаем новую
            else:
                groups.append(repr(last_group_start, last_group_end))
                last_group_start = n
                last_group_end = n

        else:
            # посленюю группу придётся обработать вручную
            groups.append(repr(last_group_start, last_group_end))

        return groups

l = Solution()
print(l.summaryRanges([0,1,2,4,5,7]))
print(l.summaryRanges([0,1,2,4,5,7,8,9]))