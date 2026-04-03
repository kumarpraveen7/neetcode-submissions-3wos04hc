class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        d = dict()
        tempLen = 0
        i = 0
        j = 0

        while(j<len(s)):
            if(s[j] not in d):
                d[s[j]] = 1
                tempLen = max(tempLen,len(d))
                j+=1
            else:
                while(s[j] in d):
                    del d[s[i]]
                    i+=1
                
            
        return tempLen
