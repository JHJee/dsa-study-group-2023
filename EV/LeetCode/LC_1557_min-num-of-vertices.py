'''
    runtime: 1254 ms Beats 17.82%
    memory: 54.2 MB Beats 28.78%
'''

class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        all_nodes = set(range(n))
        for _, v in edges:
            if v in all_nodes:
                all_nodes.remove(v)
        return list(all_nodes)