class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        compliments = {} #key: compliment, value: index hashmap
        result = []
        for index, item in enumerate(numbers):
            if compliments.get(item) is None:
                # we are looking for difference between target and given number
                #put index at the target-item position
                compliments[target-item] = (index+1)
            else:
                result = [compliments[item],(index+1)]
        return result