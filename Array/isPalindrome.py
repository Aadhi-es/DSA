class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        a=""
        for i in s:
            if i.isalnum()==True :
                a+=i
        rev=a[::-1] # Since string cant use reverse only slicing
        if a==rev:
            return True
        else:
            return False