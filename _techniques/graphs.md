# Graphs

## When to Use?

- Problem involves **nodes and connections** (cities, computers, people)
- Problem involves **grid traversal** (treat each cell as a node)
- Need **shortest path**, **connected components**, **cycle detection**
- Need **ordering based on dependencies** (topological sort)

---

## Variants

### Variant 1 — BFS (Breadth First Search)
**Use for: shortest path (unweighted), level order, minimum steps**

```python
from collections import deque

def bfs(graph, start):
    visited = {start}
    queue = deque([start])
    distance = {start: 0}

    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                distance[neighbor] = distance[node] + 1
                queue.append(neighbor)

    return distance
```

**Problems:**
| Problem | LC # | File |
|---------|------|------|
| Number of Islands | #200 | graphs/number_of_islands.py |
| Rotting Oranges | #994 | graphs/rotting_oranges.py |
| Word Ladder | #127 | graphs/word_ladder.py |
| Shortest Path in Binary Matrix | #1091 | graphs/shortest_path_binary.py |

---

### Variant 2 — DFS (Depth First Search)
**Use for: connected components, cycle detection, all paths**

```python
def dfs(graph, node, visited):
    visited.add(node)
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

# Usage
visited = set()
for node in range(n):
    if node not in visited:
        dfs(graph, node, visited)   # each call = one component
```

**Problems:**
| Problem | LC # | File |
|---------|------|------|
| Clone Graph | #133 | graphs/clone_graph.py |
| Number of Provinces | #547 | graphs/number_provinces.py |
| Pacific Atlantic Water Flow | #417 | graphs/pacific_atlantic.py |

---

### Variant 3 — Topological Sort (Kahn's BFS)
**Use for: dependency ordering, course schedule, build order**

```python
from collections import deque, defaultdict

def topo_sort(n, edges):
    graph = defaultdict(list)
    indegree = [0] * n

    for u, v in edges:          # u must come before v
        graph[u].append(v)
        indegree[v] += 1

    queue = deque([i for i in range(n) if indegree[i] == 0])
    order = []

    while queue:
        node = queue.popleft()
        order.append(node)
        for neighbor in graph[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)

    return order if len(order) == n else []  # [] means cycle exists
```

**Problems:**
| Problem | LC # | File |
|---------|------|------|
| Course Schedule | #207 | graphs/course_schedule.py |
| Course Schedule II | #210 | graphs/course_schedule_2.py |
| Alien Dictionary | #269 | graphs/alien_dictionary.py |

---

### Variant 4 — Dijkstra (Weighted Shortest Path)
**Use for: shortest path with weights, minimum cost path**

```python
import heapq

def dijkstra(graph, src, n):
    dist = [float('inf')] * n
    dist[src] = 0
    heap = [(0, src)]           # (distance, node)

    while heap:
        d, u = heapq.heappop(heap)
        if d > dist[u]:
            continue            # stale entry, skip
        for v, weight in graph[u]:
            if dist[u] + weight < dist[v]:
                dist[v] = dist[u] + weight
                heapq.heappush(heap, (dist[v], v))

    return dist
```

**Problems:**
| Problem | LC # | File |
|---------|------|------|
| Network Delay Time | #743 | graphs/network_delay.py |
| Path With Minimum Effort | #1631 | graphs/min_effort_path.py |
| Cheapest Flights Within K Stops | #787 | graphs/cheapest_flights.py |

---

### Variant 5 — Union Find (DSU)
**Use for: connected components, cycle in undirected graph, MST**

```python
class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # path compression
        return self.parent[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py: return False       # already connected
        if self.rank[px] < self.rank[py]: px, py = py, px
        self.parent[py] = px
        if self.rank[px] == self.rank[py]: self.rank[px] += 1
        return True
```

**Problems:**
| Problem | LC # | File |
|---------|------|------|
| Number of Connected Components | #323 | graphs/connected_components_dsu.py |
| Redundant Connection | #684 | graphs/redundant_connection.py |
| Accounts Merge | #721 | graphs/accounts_merge.py |

---

## BFS vs DFS — When to Choose?

| Use BFS when... | Use DFS when... |
|---|---|
| Shortest path (unweighted) | Connected components |
| Level-by-level traversal | Cycle detection |
| Minimum steps to reach | All possible paths |
| Multi-source spread (rotting oranges) | Topological sort (DFS version) |

## Grid as Graph
```python
# 4-directional movement
directions = [(0,1), (0,-1), (1,0), (-1,0)]

def neighbors(r, c, rows, cols):
    for dr, dc in directions:
        nr, nc = r + dr, c + dc
        if 0 <= nr < rows and 0 <= nc < cols:
            yield nr, nc
```

## Complexity
- BFS/DFS: O(V + E) — vertices + edges
- Dijkstra: O((V + E) log V)
- DSU operations: O(α(n)) ≈ O(1) amortized
