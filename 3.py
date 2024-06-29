class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        htb = []
        lenmax = 0
        flag = 1
        for si in s:
            if si in htb: 
                if len(htb) > lenmax:
                    lenmax = len(htb)
                htb = htb[htb.index(si)+1:]
                
                flag = 0
            elif flag: lenmax +=1
            htb.append(si)
        if len(htb) > lenmax:
            lenmax = len(htb)
        return lenmax