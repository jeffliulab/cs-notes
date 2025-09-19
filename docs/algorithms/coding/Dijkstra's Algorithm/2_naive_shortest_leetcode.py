import collections

# LeetCode/面试中常用的 Solution 类格式
class Solution:
    """
    函数被封装在一个类中，这是平台的标准做法。
    函数名通常是像 shortestPath, findTheCity 这样具有描述性的名字。
    """
    def shortestPath(self, n: int, edges: list[list[int]], src: int) -> dict[int, int]:
        """
        这个函数签名 (signature) 是最核心的改变。
        我们不再直接接收一个预处理好的 graph，而是接收 n 和 edges 来自己构建图。
        返回类型通常是 Dict[int, int] 或 List[int]，这里我们用字典，并按要求处理为 -1。
        """
        # 变化 1: 根据输入 edges 构建邻接表
        # 在这个模式下，图需要我们自己从边列表构建。使用 defaultdict 会更简洁。
        graph = collections.defaultdict(list)
        for u, v, w in edges:
            graph[u].append((v, w))

        # 变化 2: 使用 n 来初始化所有节点的距离，而不是从 graph 中推断
        # 这是我们之前讨论过的关键点：节点是 0 到 n-1。
        # 这就取代了你原来代码中遍历 graph 来收集所有 nodes 的步骤。
        dist = {i: float("inf") for i in range(n)}
        dist[src] = 0

        # visited 集合的逻辑保持不变
        visited = set()

        # 核心 Dijkstra 逻辑开始 (与你的代码几乎完全一样)
        # 我们可以用一个 for 循环代替 while，因为最多只会选择 n 个节点。
        for _ in range(n):
            # 2-1. 选出所有未访问节点中 dist 最小的节点 u
            u = None 
            min_dist = float("inf")
            
            # 变化 3: 遍历 0 到 n-1 来寻找下一个节点
            for i in range(n):
                if i not in visited and dist[i] < min_dist:
                    min_dist = dist[i]
                    u = i 
            
            # 2-2. 如果没有可扩展的点，或者剩余的点都不可达，结束
            if u is None:
                break 
            
            # 将选出的节点 u 加入 visited
            visited.add(u)
            
            # 2-4. Relaxation (松弛) - 这部分逻辑完全没有改变
            # 你的原始实现是完全正确的。
            for v, w in graph.get(u, []):
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
        
        # 变化 4: 格式化最终输出
        # LeetCode 题目通常要求将不可达的 inf 转换为 -1。
        # 我们不再需要 end 参数，因为我们要返回所有节点的距离。
        for i in range(n):
            if dist[i] == float("inf"):
                dist[i] = -1
        
        return dist

# === 测试代码 ===
if __name__ == "__main__":
    # 1. 将你原来的 graph 例子转换为 LeetCode 格式
    # 假设: A=0, B=1, C=2, D=3
    n = 4
    edges = [
        [0, 1, 1],  # A -> B, weight 1
        [0, 2, 4],  # A -> C, weight 4
        [1, 2, 2],  # B -> C, weight 2
        [1, 3, 5],  # B -> D, weight 5
        [2, 3, 1]   # C -> D, weight 1
    ]
    src = 0  # start = 'A'

    # 2. 调用修改后的函数
    solver = Solution()
    all_distances = solver.shortestPath(n, edges, src)

    # 3. 打印结果
    # 期望的 A->D 的路径是 A->B->C->D，总权重 1+2+1=4
    # 期望的 A->C 的路径是 A->B->C，总权重 1+2=3
    print(f"从源点 {src} 出发到所有节点的最短距离:")
    print(all_distances)
    # 期望输出: {0: 0, 1: 1, 2: 3, 3: 4}