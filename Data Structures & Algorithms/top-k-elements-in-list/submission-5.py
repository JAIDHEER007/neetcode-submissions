class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Naive solution
        hm = {}
        for num in nums:
            hm[num] = hm.get(num, 0) + 1
        
        count_hm = {}
        for key, value in hm.items():
            if value in count_hm:
                count_hm[value].append(key)
            else:
                count_hm[value] = [key]

        result = []
        sorted_counts = sorted(count_hm.keys(), reverse = True)

        while k > 0:
            for sorted_count in sorted_counts:
                for value in count_hm[sorted_count]:
                    if not k > 0: 
                        break
                    result.append(value)
                    k -= 1

        return result


    

        