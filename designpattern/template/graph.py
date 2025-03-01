def bfs(graph, start, end):
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
        visited = visited + graph[current]
    return (False, path)


def dfs(graph, start, end):
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
        visited = graph[current] + visited
    return (False, path)

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
    
    bfs_path = bfs(graph, 'Frankfurt', 'Nurnberg')
    dfs_path = dfs(graph, 'Frankfurt', 'Nurnberg')
    
    print(f'bfs Frankfurt-Nurnberg: {bfs_path[1] if bfs_path[0] else 'Not found'}')
    print(f'dfs Frankfurt-Nurnberg: {dfs_path[1] if dfs_path[0] else 'Not found'}')
    
    bfs_nopath = bfs(graph, 'Wurzburg', 'Kassel')
    dfs_nopath = dfs(graph, 'Wurzburg', 'Kassel')
    
    print(f'bfs Wurzburg-Kassel: {bfs_nopath[1] if bfs_nopath[0] else 'Not found'}')
    print(f'dfs Wurzburg-Kassel: {dfs_nopath[1] if dfs_nopath[0] else 'Not found'}')


if __name__ == '__main__':
    main()
