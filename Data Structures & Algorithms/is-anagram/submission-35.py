class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # lenght
        if len(s) != len(t):
            return False
        
        # Hashmaps
        countS, countT = {}, {}

        # itirate/propagate hashmaps
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)

        # compare maps
        for c in countS:
            if countS[c] != countT.get(c, 0):
                return False

        return True
