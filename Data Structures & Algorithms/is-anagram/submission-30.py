class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Same lenght
        if len(s) != len(t):
            return False
        
        # Hashmaps
        countS, countT = {}, {}

        # Itirate and propagate Hashmaps
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)

        # Compare Hashmap values
        for c in countS:
            if countS[c] != countT.get(c, 0):
                return False
        return True