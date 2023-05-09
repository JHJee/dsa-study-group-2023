'''
    runtime: 254 ms Beats 11.5 %
    memory: 14.2 MB Beats 94.25 %
'''

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        provinces = 0

        n = len(isConnected)
        def bfs(node):
            queue = deque([node])

            while queue:
                curr = queue.popleft()
                for neighbor in range(n):
                    if isConnected[curr][neighbor] == 1:
                        isConnected[curr][neighbor] = isConnected[neighbor][curr] = 0
                        queue.append(neighbor)

        for i in range(n):
            if isConnected[i][i] == 1:
                provinces += 1
                bfs(i)

        return provinces