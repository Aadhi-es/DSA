class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        character={}
        if len(s)!=len(t):
            return False
        for i in s:
            if i in character:
                character[i]=character[i]+1
            else:
                character[i]=1
        for i in t:
            if i in character and character[i]!=0:
                character[i]=character[i]-1
            else:
                return False
        return True
        



                
                
        