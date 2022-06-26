from sys import stdin
I = lambda: int(stdin.readline().strip())
M = lambda: map(int, stdin.readline().strip().split())
def main():
    x, y = M()
    deck = [1, 2, 3]
    #if x is one of 1,2,3 or y is one of 1,2,3 than c is whats left
    deck.remove(x)
    deck.remove(y)
    print(deck[0]) 
if __name__ == "__main__":
    main()