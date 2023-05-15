'''
    runtime: 755 ms Beats 43.62%
    memory: 22 MB Beats 20.88%
'''

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trust_count = [0] * (n + 1)
        for a, b in trust:
            trust_count[a] -= 1
            trust_count[b] += 1
        for i in range(1, n + 1):
            if trust_count[i] == n - 1:
                return i
        return -1