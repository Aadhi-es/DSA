class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        store=list(set(nums))
        store.sort()
        counter=0
        j=store[0] 
        diff=0
        for i in store:
            if i==j:
                diff+=1
                j+=1
            else:
                diff=1
                j=i+1
            counter=max(counter,diff)
                
        
        return counter



        