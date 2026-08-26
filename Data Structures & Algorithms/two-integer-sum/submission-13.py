class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # map
        prevMap = {} #val;indec

        # itirate
        for i , n in enumerate(nums):
            # diff
            diff = target - n
            
            # is diff in map?
            if diff in prevMap:
                return [prevMap[diff], i]
            # update map
            prevMap[n] = i