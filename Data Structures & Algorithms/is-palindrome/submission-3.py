class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = len(s)-1
        i = 0
        while i<n:
            while i<n and not s[n].isalnum():
                n-=1
            while i<n and not s[i].isalnum():
                i+=1

            if s[i].lower() != s[n].lower():
                return False
            n -= 1
            i += 1
        return True