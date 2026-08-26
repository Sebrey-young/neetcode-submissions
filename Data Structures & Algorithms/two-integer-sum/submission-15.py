class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # map
        prevMap = {} #val:indec

        # itirate
        for c , k in enumerate(nums):
            # diff
            diff = target - k

            # diff in map?
            if diff in prevMap:
                return [prevMap[diff], c]

            # update map
            prevMap[k] = c