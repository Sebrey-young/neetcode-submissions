class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Hashmap
        prevMap = {} #val:indec

        #itirate 2 indeces
        for i , n in enumerate(nums):
            # diff
            diff = target - n
            # diff in Hashmap?
            if diff in prevMap:
                return [prevMap[diff], i]
            # Update Hashmap
            prevMap[n] = i