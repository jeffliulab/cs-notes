import collections
import heapq
from typing import List, Optional, Tuple

def prims_algorithm_mst(num_nodes: int, edges: List[List[int]]) -> Optional[List[Tuple[int, int, int]]]:
    """
    使用 Prim 算法计算图的最小生成树 (MST)。

    Args:
        num_nodes (int): 图中节点的数量 (节点通常从 0 到 n-1 编号)。
        edges (List[List[int]]): 图的边列表，格式为 [[u, v, weight], ...]。

    Returns:
        Optional[List[Tuple[int, int, int]]]: 
        如果图是连通的，则返回构成最小生成树的边的列表，格式为 [(u, v, weight), ...]。
        如果图是不连通的，则返回 None。
    """
    # --- 1. 边界情况处理 ---
    if num_nodes == 0:
        return []
    if not edges and num_nodes > 1:
        return None # 无法连接多个节点

    # --- 2. 构建图的邻接表表示 ---
    # defaultdict 让我们在添加边时无需检查键是否存在
    # 存储格式: {node: [(neighbor, weight), ...]}
    graph = collections.defaultdict(list)
    for u, v, w in edges:
        graph[u].append((v, w))
        graph[v].append((u, w))

    # --- 3. 初始化 ---
    visited = set()  # 存放已经包含在MST中的节点
    mst_edges = []   # 存放构成MST的边
    
    # 最小堆，存放格式为 (weight, start_node, end_node)
    # 这样可以轻松地找到权重最小的边
    min_heap = []
    
    # 选择一个起始点，这里我们选择节点 0
    start_node = 0
    visited.add(start_node)
    
    # 将起始点的所有邻边加入最小堆
    for neighbor, weight in graph[start_node]:
        heapq.heappush(min_heap, (weight, start_node, neighbor))

    # --- 4. 主循环 ---
    # 当MST中的边数达到 num_nodes - 1 时，说明所有节点都已连接
    while min_heap and len(mst_edges) < num_nodes - 1:
        # 从堆中弹出权重最小的边
        weight, u, v = heapq.heappop(min_heap)
        
        # 如果边的目标节点 v 已经被访问过，则跳过，避免形成环路
        if v in visited:
            continue
            
        # 这是一个有效的边，采纳它
        visited.add(v)
        mst_edges.append((u, v, weight))
        
        # 将新加入的节点 v 的所有邻边加入堆中
        # 这些边是连接已知区域和未知区域的新候选边
        for neighbor_node, neighbor_weight in graph[v]:
            if neighbor_node not in visited:
                heapq.heappush(min_heap, (neighbor_weight, v, neighbor_node))

    # --- 5. 返回结果 ---
    # 如果最终MST的边数等于 n-1，说明图是连通的
    if len(mst_edges) == num_nodes - 1:
        return mst_edges
    # 否则，图是不连通的
    return None

### 测试用例 (Test Cases)

# 下面是一些测试用例，您可以直接运行这段代码来查看结果。

if __name__ == "__main__":
    print("--- 测试用例 ---")

    # 测试用例 1: 一个标准的连通图
    print("\n[测试 1: 标准连通图]")
    n1 = 5
    edges1 = [[0, 1, 10], [0, 2, 3], [1, 3, 2], [2, 1, 4], [2, 3, 8], [2, 4, 2], [3, 4, 5]]
    mst1 = prims_algorithm_mst(n1, edges1)
    if mst1:
        total_weight1 = sum(w for _, _, w in mst1)
        print(f"输入: n={n1}, edges={edges1}")
        print(f"找到的最小生成树边集: {mst1}")
        print(f"最小总权重: {total_weight1}")
        # 预期的总权重: 3+2+2+4 = 11
    else:
        print("未找到最小生成树 (图可能不连通)")

    print("-" * 20)

    # 测试用例 2: 一个不连通的图
    print("\n[测试 2: 不连通的图]")
    n2 = 5
    # 节点 0,1,2 连通; 节点 3,4 连通; 但两组之间不通
    edges2 = [[0, 1, 1], [1, 2, 1], [3, 4, 5]]
    mst2 = prims_algorithm_mst(n2, edges2)
    print(f"输入: n={n2}, edges={edges2}")
    if mst2:
        total_weight2 = sum(w for _, _, w in mst2)
        print(f"找到的最小生成树边集: {mst2}")
        print(f"最小总权重: {total_weight2}")
    else:
        print("未找到最小生成树 (图不连通) -> 结果正确！")

    print("-" * 20)

    # 测试用例 3: 带有环路的图
    print("\n[测试 3: 带有环路的图]")
    n3 = 4
    # 0-1-2-0 形成一个环, 算法必须选择权重最小的边 (0,2) 和 (2,1)
    edges3 = [[0, 1, 10], [0, 2, 1], [1, 2, 2], [1, 3, 5]]
    mst3 = prims_algorithm_mst(n3, edges3)
    if mst3:
        total_weight3 = sum(w for _, _, w in mst3)
        print(f"输入: n={n3}, edges={edges3}")
        print(f"找到的最小生成树边集: {mst3}")
        print(f"最小总权重: {total_weight3}")
        # 预期的总权重: 1+2+5 = 8
    else:
        print("未找到最小生成树 (图可能不连通)")
        
    print("-" * 20)
    
    # 测试用例 4: 边界情况 - 只有一个节点
    print("\n[测试 4: 只有一个节点]")
    n4 = 1
    edges4 = []
    mst4 = prims_algorithm_mst(n4, edges4)
    if mst4 is not None:
        total_weight4 = sum(w for _, _, w in mst4)
        print(f"输入: n={n4}, edges={edges4}")
        print(f"找到的最小生成树边集: {mst4}") # 预期为空列表 []
        print(f"最小总权重: {total_weight4}")
    else:
        print("返回了 None，检查边界逻辑")