class Solution:
    def isValid(self, s: str) -> bool:
        if(len(s)%2!=0):
            return False
        st = deque()
        for i in range(len(s)):
            if(s[i] == '(' or s[i] == '[' or s[i] == '{'):
                st.append(s[i])
                continue
            if(s[i] == ')'):
                if(len(st)!=0 and st[-1] == '('):
                    st.pop()
                else:
                    return False
            if(s[i] == '}'):
                if(len(st)!=0 and st[-1] == '{'):
                    st.pop()
                else:
                    return False
            if(s[i] == ']'):
                if(len(st)!=0 and st[-1] == '['):
                    st.pop()
                else:
                    return False
        if(len(st)>0):
            return False



        
        return True
        