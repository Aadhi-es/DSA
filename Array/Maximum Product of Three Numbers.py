class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        firsthalf = nums[-1] * nums[-2] * nums[-3]
        secondhalf=nums[0] * nums[1] * nums[-1]
        return max(firsthalf,secondhalf)
        


            

        