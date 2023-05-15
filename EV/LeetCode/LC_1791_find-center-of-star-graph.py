'''
    runtime: 817 ms Beats 57.55%
    memory: 252.1 MB Beats 16.17%
'''

class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        option_a =  edges[0][0]
        option_b = edges[0][1]
        return option_a if option_a in edges[-1] else option_b