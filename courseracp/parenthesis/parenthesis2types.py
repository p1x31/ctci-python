# Parameters:
# (int) left: set to n, keep track of open brackets that need to be added
# (int) right: set to n, keep track of close brackets that need to be add
# (str) curr: set to "", used to store the current version of the string
# (dict()) res: hold all valid strings, is returned by the function
###
n = int(input())
counter = 0
def generateParanthesis(n):

    def paren(left, right, curr, res):
        global counter

        # evaluate current string
        # if we are out of brackets to add, we must be at a valid string
        if left == 0 and right == 0:
            res.append(curr)
            counter += 1
            print(curr,counter)
            return
        
        # recursive call: add either open or close 
        # if adding open bracket is valid
        if left > 0:
            # add open bracket, decr count
            paren(left-1, right, curr + "(", res)

        # if adding close bracket is valid
        if right > left:
            # add close bracket, decr count
            paren(left, right-1, curr + ")", res)
        
        return res
    
    res = paren(n, n, "", [])

    return res
generateParanthesis(n)
#print(generateParanthesis(n))