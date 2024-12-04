"""
Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.

You must not use any built-in exponent function or operator.
    For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.

Example 1:

Input: x = 4
Output: 2
Explanation: The square root of 4 is 2, so we return 2"""


class Solution(object):
    def mySqrt(self, x):

        if x == 0 or x == 1:
            return x
        
        start, end = 1, x
        while start <= end:
            mid = (start + end) // 2
            
            # If mid*mid is equal to x, then mid is the square root of x
            if mid * mid == x:
                return mid
            # If mid*mid is less than x, discard the left half
            elif mid * mid < x:
                start = mid + 1
                result = mid
            # If mid*mid is greater than x, discard the right half
            else:
                end = mid - 1
        
        return result
    
sol=Solution()
print(sol.mySqrt(4)) #2
print(sol.mySqrt(9)) #3


"""
check the year is leap year or not

# 2024 is leap year"""

year=int(input())
if (year%4==0 and year%100!=0)or(year%400==0):
    print('leap year')
else:
    print('not leap year')

""" 
square the value
ip=5
o/p=14916"""

n = int(input())
for i in range (1,n):
        i=i**2
        print(i,end='')

