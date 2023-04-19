from collections import defaultdict
from queue import Queue

def can_determine_permutation(n, m, pairs):
    # Create the directed graph
    graph = defaultdict(list)
    in_degree = [0] * (n + 1)
    for x, y in pairs:
        graph[x].append(y)
        in_degree[y] += 1

    # Perform topological sort
    q = Queue()
    for i in range(1, n + 1):
        if in_degree[i] == 0:
            q.put(i)

    order = []
    while not q.empty():
        node = q.get()
        order.append(node)
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                q.put(neighbor)

    if len(order) != n:
        return "No"

    # Reconstruct the permutation
    a = [0] * n
    for i, node in enumerate(order):
        a[node - 1] = i + 1

    return "Yes\n" + " ".join(str(x) for x in a)
