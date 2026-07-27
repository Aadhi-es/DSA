class Solution:
    def isValid(self, s: str) -> bool:
        bracket=[]
        openn=['(','{','[']
        for i in s:
            if i in openn:
                bracket.append(i)
            else:
                if len(bracket)!=0:
                    a=bracket.pop()
                    if a=='{' and i=='}':
                        continue
                    elif a=='[' and i==']':
                        continue
                    elif a=='(' and i==')':
                        continue
                    else:
                        return False
                else:
                    return False
        return len(bracket)==0
        


        