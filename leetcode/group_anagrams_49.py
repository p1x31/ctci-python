from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs):
        
        # groups = defaultdict(list)

        # for word in strs:  # O(n)
        #     key = sorted(word)
           
        #     groups[key].append(word)

        # return [sorted(strs) for strs in groups.values()]  # O(n*log(n))

        res = defaultdict(list) # mapping charCount to list of anagrams
        for word in strs:
            count = [0] * 26 # 26 letters in the alphabet
            # for every worl d, count the number of times each letter appears
            for c in word:
                count[ord(c) - ord('a')] += 1
            res[tuple(count)].append(word)
        return res.values() # O(n * m * 26)


l = Solution()
print(l.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))