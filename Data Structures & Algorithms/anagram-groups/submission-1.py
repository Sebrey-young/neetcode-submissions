class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # create a deafault hashmap
        res = defaultdict(list)

        # count how many times a char appears in a string
        for s in strs:
            count = [0] * 26 #a...z

            # count how many of each char we have 
            for c in s:
                count[ord(c) - ord("a")] += 1

            # append all strings s with the same count into count
            res[tuple(count)].append(s)
        # return the list of values in the hashmap
        return list(res.values())