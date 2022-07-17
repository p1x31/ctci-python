from typing import List
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = list()
        occurence_count = Counter(nums)
        for key, value in occurence_count.most_common(k):
            res.append(key)
        return res
l = Solution()
print(l.topKFrequent([1,1,1,2,2,3], 2))