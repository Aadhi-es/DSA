class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        elements={}
        for i in range (len(strs)):
            a=str(sorted(strs[i]))
            if a in elements:
                elements[a].append(strs[i])
            else:
                elements[a]=[strs[i]]
        final=[]
        for i in elements.values():
            final.append(i)
        return final

        