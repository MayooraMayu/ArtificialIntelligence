graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

def dfs(graph, start):
    visited = []            
    stack = [start]         
    parent = {start: None} 
    
    print("DFS traversal:")

    while stack:
        node = stack.pop()  
        if node not in visited:
            visited.append(node)
            print(node, end=' -> ')
            for neighbor in reversed(graph[node]):
                if neighbor not in visited:
                    stack.append(neighbor)
                    parent[neighbor] = node
    
    print("END")
    print("\nParent information:")
    for node in graph:
        print(f"Node {node}: Parent = {parent.get(node, 'None')}")
dfs(graph, 'A')
