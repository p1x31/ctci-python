from collections import deque
class ZigzagIterator:
    """
    @param: v1: A 1d vector
    @param: v2: A 1d vector
    """
    def __init__(self, v1, v2):
        # do intialization if necessary
        self.v1 = deque(v1)
        self.v2 = deque(v2)
        #left pointer
        self.leftp = 0

    """
    @return: An integer
    """
    def _next(self):
        # write your code here
        if self.leftp % 2 == 1:
            if self.v1:
                return self.v1.popleft()
            else:
                return self.v2.popleft()
        else: 
            if self.v2:
                return self.v2.popleft()
            else:
                return self.v1.popleft()

        
    """
    @return: True if has next
    """
    def hasNext(self):
        # write your code here
        if len(self.v1) + len(self.v2) > 0:
            self.leftp +=1
            return True
        else: 
            return False


# Your ZigzagIterator object will be instantiated and called as such:
# solution, result = ZigzagIterator(v1, v2), []
# while solution.hasNext(): result.append(solution.next())
# Output result