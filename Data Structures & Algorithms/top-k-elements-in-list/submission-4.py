class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # create hashmap
        count = {}
        # create array using input arrya
        freq = [[] for i in range(len(nums) + 1)]

        # count how many times a value appears
        for n in nums:
            count[n] = 1 + count.get(n , 0)

        # go through every val that was counted
        for n ,  c in count.items():
            # append n for every number & count 
            freq[c].append(n)

        # create result array
        res = []

        # itirate through res array in desc order
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                # append most freq n val
                res.append(n)
                # check if the res array is the same size as k
                if len(res) == k:
                    return res