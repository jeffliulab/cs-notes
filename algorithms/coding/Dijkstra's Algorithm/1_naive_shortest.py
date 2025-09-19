def dijkstra_naive_dist(graph, start, end):
    """
    Naive Dijkstra(朴素Dijkstra), 只找最短路径长度，并不使用heap优化
    graph: dict, {u: [(v, w), ...]} 邻接表
        u: vertex u, 表示某个边的起点
        v: vertex v，表示某个边的终点
        w: edge's weight, 表示边的权重
    start: 起点
    end: 终点
    return: 最短距离 (float)，若不可达则为 inf
    """
    # 1. INIT 存储所有node到一个set中，确保能完整traverse图中的所有nodes
    nodes = set(graph.keys())
    for u, edges in graph.items():
        for v, _ in edges:
            nodes.add(v)

    # dist负责记录目前已知的最短距离，即从起点到当前已知点的最短路径长度
    dist = {n: float("inf") for n in nodes}
    dist[start] = 0

    # visited记录已经确定了最短路径的点
    visited = set()

    """
    这里要注意，Dijkstra是单源最短路径算法，即给定一个起点，算出从该点到图中所有其他点的最短距离
    一般我们把起始点叫做src（source）或者start
    """
    
    # 2. Iteration
    while len(visited) < len(nodes):
        # 2-1. 选出所有nodes中dist最小的节点u
        u = None 
        min_dist = float("inf")
        for n in nodes:
            if n not in visited and dist[n] < min_dist:
                min_dist = dist[n]
                u = n 
        
        # 2-2. 如果没有可扩展的点，或者剩余的点都不可达，结束（防止有孤立的点导致死循环）
        if u is None or dist[u] == float("inf"):
            break 
        
        # 2-3. 如果我们不需要找到所有结果，只需要找到给定的end的最短路径，那么这里就可以结束了
        if u == end:
            return dist[u]
        
        # 2-4. Relaxation 松弛所有u的出边
        """
        这个是Dijkstra的核心步骤，其核心意思就是：
        我们从u这个点出发看看，如果经过u到u的邻居，能不能让路径距离更短
        如果更短的话，就用经过u的这个距离更新u的邻居的最短路径
        """
        visited.add(u)
        for v, w in graph.get(u, []):
            if dist[v] > dist[u] + w:
                dist[v] = dist[u] + w
        
    return dist.get(end, float("inf"))

if __name__ == "__main__":
    graph = {
        'A': [('B', 1), ('C', 4)],
        'B': [('C', 2), ('D', 5)],
        'C': [('D', 1)],
    }

    dist = dijkstra_naive_dist(graph, 'A', 'D')
    print("Shortest path for 'A' to 'D':", dist)       # 4