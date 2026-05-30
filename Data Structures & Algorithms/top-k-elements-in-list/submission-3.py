class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # create hashmap
        count = {}
        # create array
        freq = [[] for i in range(len(nums)+ 1)]

        # itirate through nums and count how many times a val occurs and add it to hashmap
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        
        # go through each val that was counted
        for n , c in count.items():
            # for every number & count append n
            freq[c].append(n)

        # create result array
        res = []

        # itirate through array in descending order
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                # append the most frequent n val
                res.append(n)
                # check if the len of res is the same as k
                if len(res) == k:
                    return res