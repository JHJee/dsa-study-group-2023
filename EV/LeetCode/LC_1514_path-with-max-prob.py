'''
    runtime:  687 ms Beats 79%
    memory:  29.1 MB Beats 5.2%
'''

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        maps = defaultdict(list)

        for i in range(len(edges)):
            maps[edges[i][0]].append((edges[i][1], succProb[i]))
            maps[edges[i][1]].append((edges[i][0], succProb[i]))
        
        q = [(-1, start)]
        dist = defaultdict(float)
        dist[start] = -1
        
        while q:
            curr_dist, curr = heapq.heappop(q)
            if curr == end:
                return -(curr_dist)
            for node, prob in maps[curr]:
                temp = curr_dist * prob
                if temp < dist[node]:
                    dist[node] = temp
                    heapq.heappush(q, (temp, node))
        return 0