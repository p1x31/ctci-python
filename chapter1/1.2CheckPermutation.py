#Given two strings, write a method to decide if one is a permutation of the other.

#Same length, different order 
#Provided itemgetter(0) is O(1) when used with data, the sort is O(n log n) both on average and in the worst case.

string = input("Please entre a string: \n")

def checkPremutations(string, string2):
    str = sorted(string)
    strCmp = sorted(string2)
    print(str==strCmp)

checkPremutations(string, "abc")

#hash map store frequency for every character 
#subtract one frequency from another if 0 than string is permutation O(n) complexity

def checkPremutationsHash(string, test_str):
    #all_freq = [[] for _ in range(len(string))]
    #one way to cal frequences
    #how many of each char repreated, convert string to a set. Use set as set of keys
    test_freq = {i : test_str.count(i) for i in set(test_str)} 
    #another way
    all_freq = {}
    for i in string: 
        if i in all_freq: 
            all_freq[i] += 1
        else: 
            all_freq[i] = 1
    
    print(all_freq == test_freq)
    #print(all_freq)
    #print(test_freq)
checkPremutationsHash(string, "zxc")