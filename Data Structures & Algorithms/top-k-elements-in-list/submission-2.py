class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # solved using Bucket Sort
        # use hashmap to count the occurances of each val.
        count = {}
        # use an array thats gonna be the same size as the input array + 1
        freq = [[] for i in range(len(nums) + 1)]
        # itirate through nums and count how many times a val occurs and add it to the hashmap
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        # go through each val that was counted
        for n, c in count.items():
            # for every key/val pair /number & count we are appending n
            freq[c].append(n)

        # create result array
        res = []
        # itirate through array freq in descending order
        for i in range(len(freq) - 1 , 0, -1):
                for n in freq[i]:
            # append the n val that occurs most frequently
                    res.append(n)
            # check if the result array is the same size as k
                if len(res) == k:
                    return res
