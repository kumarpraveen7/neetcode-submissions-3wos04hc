class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {')': '(', ']': '[', '}': '{'}
        if(len(s)%2!=0):
            return False
        st = deque()
        for i in range(len(s)):
            if(s[i] not in pairs):
                st.append(s[i])

            else:
                if(len(st)!=0 and st[-1] == pairs[s[i]]):
                    st.pop()
                else: 
                    return False
        if(len(st)>0):
            return False



        
        return True
        