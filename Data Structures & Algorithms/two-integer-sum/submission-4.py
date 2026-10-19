class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        for (index, num) in enumerate(nums):
            if num in hash_map:
                return [hash_map[num], index]
            hash_map[num] = index
            hash_map[target - num] = index

        return [-1, -1]

        