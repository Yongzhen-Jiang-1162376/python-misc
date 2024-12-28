BFS = 1
DFS = 2

def traverse(graph, start, end, algorithm):
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
        if algorithm == BFS:
            visited = extend_bfs_path(visited, graph[current])
        elif algorithm == DFS:
            visited = extend_dfs_path(visited, graph[current])
        else:
            raise ValueError('No such algorithm')
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
    
    bfs_path = traverse(graph, 'Frankfurt', 'Nurnberg', BFS)
    dfs_path = traverse(graph, 'Frankfurt', 'Nurnberg', DFS)
    
    print(f'bfs Frankfurt-Nurnberg: {bfs_path[1] if bfs_path[0] else 'Not found'}')
    print(f'dfs Frankfurt-Nurnberg: {dfs_path[1] if dfs_path[0] else 'Not found'}')
    
    bfs_nopath = traverse(graph, 'Wurzburg', 'Kassel', BFS)
    dfs_nopath = traverse(graph, 'Wurzburg', 'Kassel', DFS)
    
    print(f'bfs Wurzburg-Kassel: {bfs_nopath[1] if bfs_nopath[0] else 'Not found'}')
    print(f'dfs Wurzburg-Kassel: {dfs_nopath[1] if dfs_nopath[0] else 'Not found'}')


if __name__ == '__main__':
    main()
