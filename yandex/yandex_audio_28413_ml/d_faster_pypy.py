from sys import stdin
import sys


def main():

    # Struggled with this problem for a long while.
    # Idea: Two pointers: moving end forward to find a valid window,
    #                     moving start forward to find a smaller window
    #                     counter and hash_map to determine if the window is valid or not

    # Count the frequencies for chars in t
    input = sys.stdin.readline
    #M = lambda: map(int,stdin.readline().strip().split())   
    #L = lambda: list(map(int, stdin.readline().strip().split()))
    n, k = map(int, input().strip().split()) 
    #statue type
    s = list(map(int, input().strip().split()))
    hash_map = dict()
    min_sum = float("inf")
    #fake hash_map
    #set_for_dictkeys = set(range(1, k + 1))
    hash_map = dict.fromkeys(range(1, k + 1), 1)
    # for c in range(1, k + 1):
    #     # if c in hash_map:
    #     #     hash_map[c] += 1
    #     # else:
    #     #     hash_map[c] = 1
    #     hash_map[c] = hash_map.get(c, 1)

    start, end = 0, 0

    # If the minimal length doesn't change, it means there's no valid window
    #min_window_length = len(s) + 1

    # Start point of the minimal window
    #min_window_start = 0

    # Works as a counter of how many chars still need to be included in a window
    num_of_chars_to_be_included = k

    #for end in range(len(s)):
    for end, value in enumerate(s):
        # If the current char is desired
        #if s[end] in hash_map:
        if value in hash_map:
            # Then we decreased the counter, if this char is a "must-have" now, in a sense of critical value
            #if hash_map[s[end]] > 0:
            if hash_map[value] > 0:
                num_of_chars_to_be_included -= 1
            # And we decrease the hash_map value
            #hash_map[s[end]] -= 1
            hash_map[value] -= 1

        # If the current window has all the desired chars
        while num_of_chars_to_be_included == 0:
            # See if this window is smaller
            # if end - start + 1 < min_window_length:
            #     min_window_length = end - start + 1
            #     min_window_start = start
            min_sum = min(sum(s[start:end + 1]), min_sum)

            # if s[start] is desired, we need to update the hash_map value and the counter
            if s[start] in hash_map:
                hash_map[s[start]] += 1
                # Still, update the counter only if the current char is "critical"
                if hash_map[s[start]] > 0:
                    num_of_chars_to_be_included += 1

            # Move start forward to find a smaller window
            start += 1

        # Move end forward to find another valid window
        #end += 1

    #res = min(sum(s[min_window_start:min_window_start + min_window_length]), min_sum) #if min_window_length != len(s) + 1 else ""
    sys.stdout.write("".join(str(min_sum)))

if __name__ == "__main__":
    main()  