class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n==1:
            return True
        while n>1:                  
            a=n/2                        
            if a==1:            
                return True
            n = a
        return False