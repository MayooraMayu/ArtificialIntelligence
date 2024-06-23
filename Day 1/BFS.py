from collections import deque
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}
def bfs(graph, start):
    visited = []            
    queue = deque([start]) 
    level = {start: 0}    
    parent = {start: None}  
    
    print("BFS traversal:")

    while queue:
        node = queue.popleft()  
        print(node, end=' -> ')  
        
        for neighbor in graph[node]:
            if neighbor not in level:  
                queue.append(neighbor)  
                level[neighbor] = level[node] + 1  
                parent[neighbor] = node  
    
    print("END")
    print("\nLevel and Parent information:")
    for node in graph:
        print(f"Node {node}: Level = {level.get(node, 'Not visited')}, Parent = {parent.get(node, 'None')}")
bfs(graph, 'A')
