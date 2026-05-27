class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Build hashmap 
        prevMap = {} #value : index

        # use 2 indeces
        for i , n in enumerate(nums): #enumarate keeps track of the index and values in the list
            # calculate the difference
            diff = target - n

            # check if the diff is in hashmap
            if diff in prevMap:
                return [prevMap[diff], i] #returns the indeces of the difference and the current index
            prevMap[n] = i #updates the index n to the current index i
        return 