from sys import stdin
L = lambda: list(map(int, stdin.readline().strip().split()))
def max_sequence(arr):
    lowest = ans = total = 0
    for i in arr:
        total += i
        lowest = min(lowest, total)
        ans = max(ans, total - lowest)
    return ans

def main():
    arr = L()
    print(max_sequence(arr))
if __name__ == "__main__":
    main()
