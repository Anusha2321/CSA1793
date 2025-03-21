def map_coloring(graph, colors):
    assignment = {}

    def is_valid(node, color):
        return all(assignment.get(neighbor) != color for neighbor in graph[node])

    def backtrack(node_idx):
        if node_idx == len(graph): return assignment
        node = list(graph.keys())[node_idx]
        for color in colors:
            if is_valid(node, color):
                assignment[node] = color
                if backtrack(node_idx + 1): return assignment
                del assignment[node]
        return None

    return backtrack(0)

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D'],
    'D': ['B', 'C']
}
colors = ['Red', 'Green', 'Blue']
print(map_coloring(graph, colors))


#output
{'A': 'Red', 'B': 'Green', 'C': 'Blue', 'D': 'Red'}
