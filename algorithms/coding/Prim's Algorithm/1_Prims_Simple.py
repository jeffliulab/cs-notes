# 核心思想：不断从已访问区域经最短路径向未访问区域扩散

# 首先，我们找到一个入口点，比如是A
# 然后找到所有入口点的邻居，找到距离最短的那个node，比如是C
# 现在，A和C可以加入visited中了。

# 接下来是重点：
# 我们把visited中的所有点拿出来，
# 然后考察所有和visited中的点连接的、不在visited中的点
# 比如说，现在visited中有A和C
# 那么我们接下来就要把AB, CB, CD, CE这些edge全部找出来
# 然后在这些边中找到最短的那一条：
# 假设CB最短，那么我们就把B也加入到visited中

# 那么怎么实现呢？我们用miniheap
# 每次我们都把扩散区域的可能扩散路径放到miniheap中
# 然后从miniheap中弹出最短路径
# 如果这个路径中的末端不在visited中，那么我们就找到了最短扩散路径
# 如果已经在visited中，那么就继续pop就可以了

import heapq
import collections
class Solution:
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:
        graph = collections.defaultdict(list)
        for u, v, w in edges:
            graph[u].append((v, w))
            # 无向图！正反方向都要添加！
            graph[v].append((u, w))
        
        visited = set()
        min_heap = []
        heapq.heappush(min_heap, (0, edges[0][0]))
        output = 0
        while min_heap and len(visited) < n:
            dst, src = heapq.heappop(min_heap)
            if src not in visited:
                visited.add(src)
                output += dst
            for neighbor in graph[src]:
                v, w = neighbor
                if v not in visited: # 这句很关键，防止内存超限
                    heapq.heappush(min_heap, (w, v))
        
        return output if len(visited) == n else -1











