class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        elements={}
        for i in range(len(nums)):
            if nums[i] in elements:
                if abs(elements[nums[i]]-i)<=k:
                    return True          
            elements[nums[i]]=i
        return False

                
