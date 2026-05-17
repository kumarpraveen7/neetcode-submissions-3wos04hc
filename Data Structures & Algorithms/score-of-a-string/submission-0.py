class Solution:
    def scoreOfString(self, s: str) -> int:

        i = 0

        cnt = 0

        while(i<len(s)-1):

            cnt+= abs(ord(s[(i+1)%len(s)])  -  ord(s[i]))
            print( abs(ord(s[(i+1)%len(s)])  -  ord(s[i])))
            i+=1
        return cnt


        