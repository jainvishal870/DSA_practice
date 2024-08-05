'''
iven a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).


Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21


Constraints:

-231 <= x <= 231 - 1
'''

#Solution

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        INT_MAX = (2**31 - 1)
        INT_MIN = (-2**31)
        x_reversed = 0
        sign = -1 if x < 0 else 1
        x = abs(x)

        if x == 0:
            return 0
        while x > 0:
            rem = (x % 10)
            x = x // 10
            x_reversed = (x_reversed * 10) + rem

        answer = (sign * x_reversed)

        if answer > INT_MAX or answer < INT_MIN:
            return 0
        else:
            return answer
        









##Reminder to use this method always to split the digits of the integer rather than typecasting it to str
num = -139
negative = False
ans = 0
if num < 0:
    negative = True
    num = abs(num)
    
while num > 0:
    rem = num % 10
    ans = ans * 10 + rem
    num = num // 10
    

if negative:
    ans = ans * (-1)
    
print(ans)
    
    
