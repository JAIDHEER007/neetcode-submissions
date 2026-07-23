from itertools import zip_longest

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_map = {}
        for chars in zip_longest(s, t):
            hash_map[chars[0]] = hash_map.get(chars[0], 0) + 1
            hash_map[chars[1]] = hash_map.get(chars[1], 0) - 1
        for val in hash_map.values():
            if val != 0: return False
        return True
        