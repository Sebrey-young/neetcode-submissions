class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # def map
        res = defaultdict(list)# charCount:list of Anagrams

        # itirate through every string
        for s in strs:
            # count how many char it has
            count = [0] * 26# a...z
            # itirate though every char in each string
            for c in s:
                # count how many of each char and map them using ascii vals
                count[ord(c) - ord("a")] += 1
            # append the string s to the result count using a tupple
            res[tuple(count)].append(s)
        # return the list of values
        return list(res.values())