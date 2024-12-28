def traverse(graph, start, end, action):
    path = []
    visited = [start]
    while visited:
        current = visited.pop(0)
        if current not in path:
            path.append(current)
            if current == end:
                # print(path)
                return (True, path)
            if current not in graph:
                continue
        visited = action(visited, graph[current])
    return (False, path)

def extend_bfs_path(visited, current):
    return visited + current

def extend_dfs_path(visited, current):
    return current + visited

def main():
    graph = {
        'Frankfurt': ['Mannheim', 'Wurzburg', 'Kassel'],
        'Mannheim': ['Karlsruhe'],
        'Karlsruhe': ['Augsburg'],
        'Augsburg': ['Munchen'],
        'Wurzburg': ['Erfurt', 'Nurnberg'],
        'Nurnberg': ['Stuttgart', 'Munchen'],
        'Kassel': ['Munchen'],
        'Erfurt': [],
        'Stuttgart': [],
        'Munchen': []
    }
    
    bfs_path = traverse(graph, 'Frankfurt', 'Nurnberg', extend_bfs_path)
    dfs_path = traverse(graph, 'Frankfurt', 'Nurnberg', extend_dfs_path)
    
    print(f'bfs Frankfurt-Nurnberg: {bfs_path[1] if bfs_path[0] else 'Not found'}')
    print(f'dfs Frankfurt-Nurnberg: {dfs_path[1] if dfs_path[0] else 'Not found'}')
    
    bfs_nopath = traverse(graph, 'Wurzburg', 'Kassel', extend_bfs_path)
    dfs_nopath = traverse(graph, 'Wurzburg', 'Kassel', extend_dfs_path)
    
    print(f'bfs Wurzburg-Kassel: {bfs_nopath[1] if bfs_nopath[0] else 'Not found'}')
    print(f'dfs Wurzburg-Kassel: {dfs_nopath[1] if dfs_nopath[0] else 'Not found'}')


if __name__ == '__main__':
    main()
