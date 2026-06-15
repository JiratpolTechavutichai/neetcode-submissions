class Solution:
    def isValid(self, s: str) -> bool:
        righttoleft = {')':'(', '}':'{', ']':'['}
        temp = []
        for sym in s:
            if sym not in righttoleft:
                temp.append(sym)
            else:
                if not temp:
                    return False
                if temp[-1] != righttoleft[sym]:
                    return False
                else:
                    temp.pop()
        return len(temp) == 0
