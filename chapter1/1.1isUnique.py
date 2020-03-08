"String has all unique characters."

string = input("Please entre a string: \n")
s1 = set(string)
print(len(s1)==len(string))
"""
Without Extra Data Structure: 
The approach is valid for strings having alphabet as a-z. 
This approach is little tricky. Instead of maintaining a boolean array,
we maintain an integer value called checker(32 bits). 
As we iterate over the string,
we find the int value of the character with respect to ‘a’ 
with the statement int bitAtIndex = str.charAt(i)-‘a’;
Then the bit at that int value is set to 1 with the statement 1 << bitAtIndex .
Now, if this bit is already set in the checker,
the bit AND operation would make checker > 0. 
Return false in this case.
Else Update checker to make the bit 1 at that index with the statement checker = checker | (1 <<bitAtIndex);
"""
def uniqueCharacters(str):
        #Assuming string can have characters a-z 
        #this has 32 bits set to 0 
        checker = 0 
        for i in range(len(str)):
            bitAtIndex = ord(str[i]) - ord('a')
            # if that bit is already set in checker, 
            # return false 
            if ((checker & (1 << bitAtIndex)) > 0): 
                return False
            # otherwise update and continue by 
            # setting that bit in the checker 
            checker = checker | (1 << bitAtIndex)
        # no duplicates encountered, return true 
        return True 

print(uniqueCharacters('bcdefga'))

print(uniqueCharacters('aab'))
     