class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # create hashset for nums
        hashset = set()

        # itirate through nums
        for n in nums:
            # check if n is in the hashset, if yes return true, if not then we add it
            if n in hashset:
                return True
            hashset.add(n)
        return False
