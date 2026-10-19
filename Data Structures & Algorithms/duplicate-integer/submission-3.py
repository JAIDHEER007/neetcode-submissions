class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # O(nlogn) -> time
        # O(1) -> space complexity

        # sort nums
        nums.sort()
        
        for index in range(1, len(nums)):
            if nums[index - 1] == nums[index]:
                return True

        return False
        