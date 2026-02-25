def solution(edges):
    # edge[in, out]
    n = 0
    for edge in edges:
        n = max(n, edge[0], edge[1])
    graph = [list() for _ in range(n+1)]
    in_set = []
    # 그래프화
    for edge in edges:
        graph[edge[0]].append(edge[1])
    add_node = 0
    # 추가된 노드 찾기
    in_count = [0] * (n+1)
    for g in graph:
        for i in g:
            in_count[i] += 1
    for i, g in enumerate(graph):
        if in_count[i] == 0 and len(g) >= 2:
            add_node = i
    # answer = [생성노드, 도넛, 막대, 8자]
    answer = [add_node, 0,0,0]
    for i, g in enumerate(graph):
        if i == 0 or i == add_node:
            continue
        if len(g) == 0 and in_count[i] >= 1:
            answer[2] += 1
        elif len(g) == 2 and in_count[i] >= 2:
            answer[3] += 1
    answer[1] = len(graph[add_node]) - answer[2] - answer[3]
    answer[0] = add_node
    return answer