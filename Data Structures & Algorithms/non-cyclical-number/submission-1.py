class Solution:
    def isHappy(self, n: int) -> bool:
        def happy(num):
            return sum(int(digit)**2 for digit in str(num))
        def helper(num, seen):
            if num == 1:
                return True
            if num in seen:
                return False
            seen.add(num)
            return helper(happy(num), seen)
        return helper(n,set())