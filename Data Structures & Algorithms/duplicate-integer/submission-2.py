class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # O(n) -> time 
        # O(n) -> space complexity

        s = set()
        for num in nums:
            if num not in s:
                s.add(num)
            else:
                return True

        return False
        