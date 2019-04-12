# -*- coding: utf-8 -*-

# 有向图中指定一个点到其他各顶点的路径——单源最短路径

# 每次找到离源点最近的一个顶点，然后以该顶点为重心进行扩展
# 最终得到源点到其余所有点的最短路径
# 一种贪婪算法

# 此方法不能解决负权值边的图
# Dijkstra最短路经算法时间复杂度为o(n^2)

import networkx as nx

def Dijkstra(G, start, end):
    RG = G.reverse()
    # 经处理过的节点，需要记录
    dist = {}
    previous = {}
    # 初始化数据
    for v in RG.nodes():
        dist[v] = float('inf')
        previous[v] = None
    dist[end] = 0
    u = end
    while u != start:
        # 查询到目前开销最小的节点
        u = min(dist, key=dist.get)
        # 获取该节点当前开销
        distu = dist[u]
        del dist[u]
        # 遍历当前节点的所有邻居
        for u, v in RG.edges(u):
            if v in dist:
                # 计算经过当前节点到达相邻结点的开销,即当前节点的开销加上当前节点到相邻节点的开销
                alt = distu + RG[u][v]['weight']
                # 如果经当前节点前往该邻居更近，就更新该邻居的开销
                if alt < dist[v]:
                    dist[v] = alt
                    # 同时将该邻居的父节点设置为当前节点
                    previous[v] = u
    path = (start, )
    last = start
    while last != end:
        nxt = previous[last]
        path += (nxt, )
        last = nxt
    return path

if __name__ == '__main__':
    G = nx.DiGraph()
    G.add_edge(0, 1, weight=80)
    G.add_edge(1, 2, weight=50)
    G.add_edge(1, 3, weight=30)
    G.add_edge(3, 2, weight=10)
    G.add_edge(2, 4, weight=20)
    G.add_edge(2, 5, weight=30)
    G.add_edge(2, 6, weight=10)
    G.add_edge(5, 3, weight=5)
    G.add_edge(3, 6, weight=25)
    G.add_edge(4, 5, weight=10)
    G.add_edge(4, 6, weight=10)
    G.add_edge(5, 6, weight=35)
    rs = Dijkstra(G, 0, 6)
    print(rs)