def characterReplacement(s: str, k: int) -> int:
        # 229ms
        # count = {}
        # res = 0

        # l = 0
        # for r in range(len(s)):
        #     #if the character doesn't exist in the count, add it
        #     count[s[r]] = count.get(s[r], 0) + 1
        #     while (r - l + 1) - max(count.values()) > k:
        #         count[s[l]] -= 1
        #         l += 1
        #     res = max(res, r - l + 1)
            
        # return res
        #122ms
        count = {}
        res = 0
        l = 0
        maxf = 0
        for r in range(len(s)):
            #if the character doesn't exist in the count, add it
            count[s[r]] = count.get(s[r], 0) + 1
            maxf = max(maxf, count[s[r]])
            while (r - l + 1) - maxf > k:
                count[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
            
        return res
print(characterReplacement("ABAB", 2))
assert(characterReplacement("ABAB", 2) == 4)
print(characterReplacement("AABABBA", 1))