class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # check lenght
        if len(s) != len(t):
            return False
        
        # create Hashmaps
        countS, countT = {} , {}

        # itirate and propagate hashmaps
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)

        # check if the values in the hashmaps match
        for c in countS:
            if countS[c] != countT.get(c, 0):
                return False

        return True