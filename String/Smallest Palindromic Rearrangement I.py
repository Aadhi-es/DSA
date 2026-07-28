class Solution:
    def smallestPalindrome(self, s: str) -> str:
        Count=Counter(s)
        sortedCounter=sorted(Count.keys())
        newstring=""
        midchar=""
        for i in sortedCounter:
            freq=Count[i] 
            newstring=newstring+(i*(freq//2))
            if freq%2!=0:
                midchar=i
        newstring = newstring+midchar+newstring[::-1]
        return newstring

        