'''
    runtime: 32 ms Beats 64.94%
    memory: 13.8 MB Beats 45.20%
'''

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        stones = Counter(stones)
        result = 0
        
        # for jewel in list(jewels):
            # result += stones[jewel]
        for char in range(0, len(jewels)):
            result += stones[jewels[char]]
        
        return result