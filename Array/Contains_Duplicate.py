class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dictt={}
        for i in nums:
            if i in dictt:
                return True
            else:
                dictt[i]=1
        return False



        