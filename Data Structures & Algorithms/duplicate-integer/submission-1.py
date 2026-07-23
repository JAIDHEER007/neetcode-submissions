class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        ledger = set()
        for num in nums:
            if num in ledger: return True
            else: ledger.add(num)
        return False
        