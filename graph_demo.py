from collections import defaultdict

def findCircleNum(isConnected: list[list[int]]) -> int:
    def dfs(node):
        for neighbor in graph[node]:
            # the next 2 lines are needed to prevent cycles
            if neighbor not in seen:
                seen.add(neighbor)
                dfs(neighbor)
    
    # build the graph
    n = len(isConnected)
    graph = defaultdict(list)
    for i in range(n):
        for j in range(i+1, n):
            if isConnected[i][j]:
                graph[i].append(j)
                graph[j].append(i)
    print(graph)

    seen = set()
    ans = 0
    
    for i in range(n):
        if i not in seen:
            # add all nodes of a connected component to the set
            ans += 1
            seen.add(i)
            dfs(i)

    print("ans", ans)

"""2 Islands / aka connected components: 0 -> 1 -> 2 -> 3 AND 4 -> 5"""
findCircleNum(isConnected = [
    [0,1,0,0,0,0],
    [1,0,1,0,0,0],
    [0,1,0,1,0,0],
    [0,0,1,0,0,0],
    [0,0,0,0,0,1],
    [0,0,0,0,1,0],
])