class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # def map/dict
        res = defaultdict(list) #charCount: List of Anagrams

        # itirate through every string
        for s in strs:
            # count how many chars there are
            count = [0] * 26 #a...z

            # itirate through every char in each string
            for c in s:
                # count how many of each char there are using ascii vals
                count [ord(c) - ord("a")] += 1

                # append the resulting tuple count to s
            res[tuple(count)].append(s)
        
        # return the list of values from the map
        return list(res.values())
