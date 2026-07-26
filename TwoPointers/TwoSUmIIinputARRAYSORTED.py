class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        final=[]
        dictionary={}
        for i in range(len(numbers)):
            check=target-numbers[i]
            if check in dictionary:
                final.append(dictionary[check]+1)
                final.append(i+1)
            else:
                dictionary[numbers[i]]=i
            
        return final



        