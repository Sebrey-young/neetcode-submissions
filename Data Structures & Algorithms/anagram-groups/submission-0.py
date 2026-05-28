class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # create default dictionary/hashmap
        res = defaultdict(list) #charCount : list of Anagrams

        # 
        for s in strs:
            count = [0] * 26 #a.....z

            # count how many of each char we have
            for c in s:
                count[ord(c) - ord("a")] += 1 #ord changes a single char into its Unicode int, so that if a = 80 -> 80 - 80 = 0

            # group/append all anagrams with a particular count together 
            res[tuple(count)].append(s) #set as tuple b/c in python lists cannot be keys and tuples are non mutables

        # return all the lists in the hashmap as values NOT the keys
        return list(res.values())
            