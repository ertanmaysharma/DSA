class Solution(object):
    def isAnagram(self, s, t):
        if len(s)!= len(t): 
            return False
        Counts = {}
        Countt = {}
        for c in s:
            Counts[c]= Counts.get(c,0) + 1
        for g in t:
            if g not in Counts:
                return False
            Countt[g]=Countt.get(g,0) + 1
            
        return Counts==Countt


        