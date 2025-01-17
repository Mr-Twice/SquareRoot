class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0 or x == 1:
            return x  
    
        low, high = 0, x
        result = 0

        while low <= high:
            mid = (low + high) // 2
            if mid * mid <= x:
                result = mid 
                low = mid + 1 
            else:
                high = mid - 1     
        return result

        # a = int(math.sqrt(x))
        # return a
