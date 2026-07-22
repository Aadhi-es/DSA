class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ele={}
        final=[]
        j=0
        for i in nums:
            if i in ele:
                ele[i]+=1
            else:
                ele[i]=1
        new_dict=dict(sorted(ele.items(),key=lambda c:c[1],reverse=True))
        for i in new_dict:
            if j<k:
                final.append(i)
                j+=1
            else:
                break
        return final
        
            
        