'''
    runtime: 1797 ms Beats 92.53 %
    memory: 106.5 MB Beats 51.2 %
'''

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        visited = set()
        queue = deque([source])
        
        while queue:
            node = queue.popleft()
            if node == destination:
                return True
            if node not in visited:
                visited.add(node)
                queue.extend(n for n in graph[node] if n not in visited)
        
        return False