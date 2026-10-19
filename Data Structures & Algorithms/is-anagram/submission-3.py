class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Optimizations
        # 1. Early exit using length
        # 2. check for missing count (New char), Negative Count (Extra Char)
        # 3. 
        if len(s) != len(t):
            return False

        counts = {}
        for ch in s:
            counts[ch] = counts.get(ch, 0) + 1

        for ch in t:
            if ch not in counts or counts[ch] == 0:
                return False
            counts[ch] -= 1

        return True