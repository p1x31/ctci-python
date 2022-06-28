class Solution:
    def findRepeatedDnaSequences(self, s: str):
        #89ms
        # # dict to store the count of each sequence
        # d = {}
        # # list to store the repeated sequences
        # res = []
        # # iterate through the string
        # for i in range(len(s) - 9):
        #     # get the 10-letter sequence
        #     seq = s[i:i+10]
        #     # if the sequence is already in the dictionary, add 1 to the count
        #     if seq in d:
        #         d[seq] += 1
        #     # if the sequence is not in the dictionary, add it to the dictionary and set the count to 1
        #     else:
        #         d[seq] = 1
        # # iterate through the dictionary
        # for k, v in d.items():
        #     # if the count is greater than 1, add the sequence to the list
        #     if v > 1:
        #         res.append(k)
        # return res
        #47 ms
        seen, res = set(), set()

        for l in range(len(s) - 9):
            cur = s[l:l+10]
            if cur in seen:
                res.add(cur)
            seen.add(cur)
        return list(res)
l = Solution()
print(l.findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"))