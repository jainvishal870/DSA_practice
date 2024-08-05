'''
You are given a positive integer n. Each digit of n has a sign according to the following rules:

The most significant digit is assigned a positive sign.
Each other digit has an opposite sign to its adjacent digits.
Return the sum of all digits with their corresponding sign.


Example 1:

Input: n = 521
Output: 4
Explanation: (+5) + (-2) + (+1) = 4.
Example 2:

Input: n = 111
Output: 1
Explanation: (+1) + (-1) + (+1) = 1.
Example 3:

Input: n = 886996
Output: 0
Explanation: (+8) + (-8) + (+6) + (-9) + (+9) + (-6) = 0.


Constraints:

1 <= n <= 109
'''
##Solution

class Solution(object):
    def alternateDigitSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        total_sum = 0

        sign = 1
        while n > 0:
            rem=n%10
            n = n/10
            sign *= -1
            total_sum += rem * sign



        return total_sum * sign


