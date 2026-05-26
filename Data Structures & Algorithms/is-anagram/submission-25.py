class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # check if the len is the same
        if len(s) != len(t):
            return False

        # Build hashmaps
        countS, countT = {} , {}

        # itirate and propagate the hashmaps
        for i in range(len(s)):
            countS[s[i]] =1 + countS.get(s[i], 0)
            countT[t[i]] =1 + countT.get(t[i], 0)
        
        # check if the key values match
        for c in countS:
            if countS[c] != countT.get(c, 0):
                return False

        return True