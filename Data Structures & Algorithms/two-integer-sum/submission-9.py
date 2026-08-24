class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Hashmap
        indices = {} #val: index

        #itirate 2 indeces
        for i , n in enumerate(nums):
            # diff
            diff = target - n 
            # diff in Hashmap?
            if diff in indices:
                return [indices[diff], i]

            # Update Hashmap
            indices[n] = i
