# 在naive dijkstra中，性能瓶颈在于：在所有unvisited中寻找dist最小的node，需要traverse一遍。
# 那么如何处理更新操作呢？
# 技巧就是不更新，只添加。然后在heappop的时候判断取出来的是旧距离还是新距离。

# Naive Dijkstra:    time O(V^2),   space O(V),   适合稠密图
# Dijkstra + Heap:   time O(ElogV), space O(V+E), 适合稀疏图

import collections 
import heapq 

class Solution:
    def shortestDist(self, n: int, edges: list[list[int]], src: int) -> dict[int, int]:
        graph = collections.defaultdict(list)
        for u, v, w in edges:
            graph[u].append((v, w))
        
        dist = {i:float("inf") for i in range(n)}
        dist[src] = 0  # 容易忘记的点：设置src点的dist为0，否则无法开始

        min_heap = [(0, src)]

        while min_heap:
            d, u = heapq.heappop(min_heap)
            if d > dist[u]:
                continue

            # Relaxation
            for v, w in graph.get(u, []):
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    heapq.heappush(min_heap, (dist[v], v))
        
        for i in range(n):
            if dist[i] == float("inf"):
                dist[i] = -1
        
        return dist


if __name__ == "__main__":
    n = 4
    edges = [
        [0, 1, 1], [0, 2, 4], [1, 2, 2],
        [1, 3, 5], [2, 3, 1]
    ]
    src = 0
    
    solver = Solution()
    all_distances = solver.shortestDist(n, edges, src)
    
    print(f"从源点 {src} 出发到所有节点的最短距离:")
    print(all_distances)
    # 期望输出: {0: 0, 1: 1, 2: 3, 3: 4}