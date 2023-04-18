'''
    runtime: 100 ms Beats 72.61 %
    memory: 15.8 MB Beats 33.35 %
'''

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        paths = []
        n = len(graph)
        source, target = 0, n - 1
        stack = [(source, [source])]

        while stack:
            node, path = stack.pop()
            if node == target:
                paths.append(path)
                continue
                
            for neighbor in graph[node]:
                stack.append((neighbor, path + [neighbor]))

        return paths