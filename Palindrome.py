"""
Runtime: 77 ms, faster than 79.13% of Python3 online submissions for Palindrome Number.
Memory Usage: 13.9 MB, less than 59.40% of Python3 online submissions for Palindrome Number.

Given an integer x, return true if x is palindrome integer.

An integer is a palindrome when it reads the same backward as forward.

For example, 121 is a palindrome while 123 is not.
"""

class Solution:
    def isPalindrome(self, x: int) -> bool:
        res = False
        if x>=0:
            rev_val = str(x)[::-1]
            if  rev_val == str(x):
                res = True
                
        return res
if __name__ == "__main__":
	sol=Solution()
	res = sol.isPalindrome(121)
	print(res)
