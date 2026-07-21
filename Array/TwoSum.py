class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        check=0
        result=[]
        dictio = {}
        for i in range(len(nums)):
            check=target-nums[i]
            if check in dictio.keys():
                result=[dictio[check],i] 
            else:
                dictio[nums[i]]=i 
        return result

       

