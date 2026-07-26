class Solution:
    def maxProduct(self, n: int) -> int:
        final=[]
        s=str(n)
        for i in s:
            final.append(int(i))
        final.sort()
        final.reverse()
        return final[0]*final[1] 
     

        