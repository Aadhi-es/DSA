class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length=len(nums)
        prefix=[]
        multi=1
        pref=1
        #Pref is used for skipping the current element 
        final=[]
        sufix=[]
        for i in range(length):
            multi=multi*pref
            prefix.append(multi)
            pref=nums[i]    
        pref,multi=1,1
        for i in range(-1,-(length+1),-1): 
            multi=multi*pref
            sufix.append(multi)
            pref=nums[i]    
        sufix.reverse()   
        for i in range(length):
            final.append(prefix[i] * sufix[i])
        return final



