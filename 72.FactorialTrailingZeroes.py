'''
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

Input: n = 3
Output: 0
Explanation: 3! = 6, no trailing zero.
Example 2:

Input: n = 5
Output: 1
Explanation: 5! = 120, one trailing zero.
Example 3:

Input: n = 0
Output: 0


Constraints:

0 <= n <= 104
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
