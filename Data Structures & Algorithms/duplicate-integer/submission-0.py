class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash_table = {}
        for num in nums:
            hash_table[num] = hash_table.get(num, 0) + 1
            if hash_table[num] > 1: return True

        return False
        