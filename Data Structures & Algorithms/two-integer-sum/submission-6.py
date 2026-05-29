class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Create hashmap
        prevMap = {} #val:index

        # use 2 indeces to keep track of the values in the list
        for i , n in enumerate(nums):
            # calc the diff
            diff = target - n

            # check if the diff is in the hashmap
            if diff in prevMap:
                return [prevMap[diff], i]
            
            prevMap[n] = i
        