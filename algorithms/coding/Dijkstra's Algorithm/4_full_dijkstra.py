import collections 
import heapq 

class Solution:
    def shortestDist(self, n: int, edges: list[list[int]], src: int) -> dict[int, int]:
        graph = collections.defaultdict(list)
        for u, v, w in edges:
            graph[u].append((v, w))
        
        dist = {i:float("inf") for i in range(n)}
        dist[src] = 0 

        # 新增：Predecessor 记录前驱节点
        # predecessor[i]: {i:prev} 表示在最短路径上，i的前一个节点是prev
        predecessor = {i:None for i in range(n)}

        min_heap = [(0, src)]

        while min_heap:
            d, u = heapq.heappop(min_heap)
            if d > dist[u]:
                continue

            for v, w in graph.get(u, []):
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    heapq.heappush(min_heap, (dist[v], v))

                    # 新增：Predecessor记录更新，这里把最短路径的顺序关系记录好，即从u到v
                    predecessor[v] = u
        
        for i in range(n):
            if dist[i] == float("inf"):
                dist[i] = -1
        
        return dist, predecessor


if __name__ == "__main__":
    n = 4
    edges = [
        [0, 1, 1], [0, 2, 4], [1, 2, 2],
        [1, 3, 5], [2, 3, 1]
    ]
    src = 0
    
    solver = Solution()
    all_distances, predecessor = solver.shortestDist(n, edges, src)
    
    print(f"从源点 {src} 出发到所有节点的最短距离:", all_distances)
    # 期望输出: {0: 0, 1: 1, 2: 3, 3: 4}

    # 如果我们要得到路径，可以用predecessor重建
    # 我们可以从任意一个目标点target开始，不断找到它的前驱节点，然后直到走回到src源点
    # 这个路径就是倒着的从src到target的最短路径，我们把它反过来就是最短路径了
    target = 3
    path = []
    cur = target
    while cur is not None:
        path.append(cur)
        cur = predecessor[cur]
    
    # 注意※这里要检查path是否valid，如果发现最后不是src或者path是空的，说明没有valid的路径
    if not path or path[-1] != src:
        print("Not a valid path")
    else:
        path[:] = path[::-1]
        print("shortest path is: ", path)