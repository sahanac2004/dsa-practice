"""
╔══════════════════════════════════════════════════════════════════╗
║              COMMON DSA PATTERNS — PYTHON                        ║
║         Copy-paste ready templates for each technique            ║
╚══════════════════════════════════════════════════════════════════╝

INDEX
  1.  Two Pointers — Opposite Ends
  2.  Two Pointers — Slow & Fast (Floyd's)
  3.  Sliding Window — Fixed Size
  4.  Sliding Window — Variable Size
  5.  Binary Search — On Array
  6.  Binary Search — On Answer Space
  7.  HashMap — Complement Lookup
  8.  HashMap — Frequency Count
  9.  Prefix Sum — 1D
  10. Monotonic Stack — Next Greater Element
  11. BFS — Graph / Tree
  12. DFS — Graph / Tree
  13. Backtracking — Subsets / Permutations
  14. Dynamic Programming — 1D
  15. Dynamic Programming — 2D
  16. Union Find (DSU)
  17. Topological Sort — Kahn's BFS
"""

from collections import defaultdict, deque


# ══════════════════════════════════════════════════════════════════
# 1. TWO POINTERS — OPPOSITE ENDS
#    Use when: sorted array, find pair with condition, 3Sum type
# ══════════════════════════════════════════════════════════════════
def two_pointers_opposite(arr, target):
    left, right = 0, len(arr) - 1
    while left < right:
        current = arr[left] + arr[right]
        if current == target:
            return [left, right]          # found
        elif current < target:
            left += 1                     # need bigger sum
        else:
            right -= 1                    # need smaller sum
    return -1


# ══════════════════════════════════════════════════════════════════
# 2. TWO POINTERS — SLOW & FAST (Floyd's)
#    Use when: cycle detection, find middle, nth from end
# ══════════════════════════════════════════════════════════════════
def slow_fast_pointer(head):
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next           # moves 1 step
        fast = fast.next.next      # moves 2 steps
        if slow == fast:
            return True            # cycle detected
    return False


# ══════════════════════════════════════════════════════════════════
# 3. SLIDING WINDOW — FIXED SIZE (window size = k)
#    Use when: "subarray of size k", "every window of size k"
# ══════════════════════════════════════════════════════════════════
def sliding_window_fixed(arr, k):
    # Build first window
    window_sum = sum(arr[:k])
    max_sum = window_sum

    for i in range(k, len(arr)):
        window_sum += arr[i]          # add new right element
        window_sum -= arr[i - k]      # remove old left element
        max_sum = max(max_sum, window_sum)

    return max_sum


# ══════════════════════════════════════════════════════════════════
# 4. SLIDING WINDOW — VARIABLE SIZE
#    Use when: longest/shortest subarray, min window substring
# ══════════════════════════════════════════════════════════════════
def sliding_window_variable(arr):
    left = 0
    ans = 0
    window_state = {}           # or a counter, sum, etc.

    for right in range(len(arr)):
        # --- expand window ---
        # add arr[right] to window_state

        # --- shrink window if condition violated ---
        while False:            # replace False with your condition
            # remove arr[left] from window_state
            left += 1

        # --- update answer ---
        ans = max(ans, right - left + 1)

    return ans


# ══════════════════════════════════════════════════════════════════
# 5. BINARY SEARCH — ON SORTED ARRAY
#    Use when: sorted input, find element or boundary
# ══════════════════════════════════════════════════════════════════
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2    # avoids overflow
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


# ══════════════════════════════════════════════════════════════════
# 6. BINARY SEARCH — ON ANSWER SPACE
#    Use when: "minimum/maximum possible value", capacity problems
#    Key idea: binary search on the ANSWER, not the array index
# ══════════════════════════════════════════════════════════════════
def binary_search_answer(arr):
    def is_feasible(mid):
        # check if 'mid' is a valid answer
        return True  # replace with actual condition

    left, right = 1, max(arr)   # define answer range
    ans = right

    while left <= right:
        mid = (left + right) // 2
        if is_feasible(mid):
            ans = mid
            right = mid - 1     # try smaller (for minimum)
        else:
            left = mid + 1

    return ans


# ══════════════════════════════════════════════════════════════════
# 7. HASHMAP — COMPLEMENT LOOKUP
#    Use when: find pair/triple that sums to target
# ══════════════════════════════════════════════════════════════════
def hashmap_complement(nums, target):
    seen = {}                              # {value: index}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]   # found the pair
        seen[num] = i
    return []


# ══════════════════════════════════════════════════════════════════
# 8. HASHMAP — FREQUENCY COUNT
#    Use when: anagram check, character count, find majority
# ══════════════════════════════════════════════════════════════════
def hashmap_frequency(s):
    freq = defaultdict(int)
    for char in s:
        freq[char] += 1
    return freq

    # Alternative using Counter
    # from collections import Counter
    # return Counter(s)


# ══════════════════════════════════════════════════════════════════
# 9. PREFIX SUM — 1D
#    Use when: range sum queries, subarray sum equals k
# ══════════════════════════════════════════════════════════════════
def prefix_sum(arr):
    n = len(arr)
    prefix = [0] * (n + 1)
    for i in range(n):
        prefix[i + 1] = prefix[i] + arr[i]

    # Query: sum from index l to r (inclusive)
    def range_sum(l, r):
        return prefix[r + 1] - prefix[l]

    return prefix, range_sum


# ══════════════════════════════════════════════════════════════════
# 10. MONOTONIC STACK — NEXT GREATER ELEMENT
#     Use when: next greater/smaller, histogram area, temperatures
# ══════════════════════════════════════════════════════════════════
def next_greater_element(arr):
    n = len(arr)
    result = [-1] * n
    stack = []              # stores indices

    for i in range(n):
        # while stack not empty AND current > stack's top element
        while stack and arr[i] > arr[stack[-1]]:
            idx = stack.pop()
            result[idx] = arr[i]    # arr[i] is the next greater
        stack.append(i)

    return result


# ══════════════════════════════════════════════════════════════════
# 11. BFS — GRAPH / TREE (Shortest path, Level order)
#     Use when: shortest path (unweighted), level-by-level traversal
# ══════════════════════════════════════════════════════════════════
def bfs(graph, start):
    visited = set([start])
    queue = deque([start])
    result = []

    while queue:
        node = queue.popleft()
        result.append(node)

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return result


# ══════════════════════════════════════════════════════════════════
# 12. DFS — GRAPH (Connected components, cycle detection)
#     Use when: explore all paths, connected components, cycle
# ══════════════════════════════════════════════════════════════════
def dfs(graph, node, visited=None):
    if visited is None:
        visited = set()
    visited.add(node)

    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

    return visited


# ══════════════════════════════════════════════════════════════════
# 13. BACKTRACKING — SUBSETS / PERMUTATIONS
#     Use when: generate all possibilities, combinations, permutations
# ══════════════════════════════════════════════════════════════════
def backtracking_subsets(nums):
    result = []

    def backtrack(start, current):
        result.append(current[:])      # add copy of current state

        for i in range(start, len(nums)):
            current.append(nums[i])    # choose
            backtrack(i + 1, current)  # explore
            current.pop()              # unchoose (backtrack)

    backtrack(0, [])
    return result


def backtracking_permutations(nums):
    result = []

    def backtrack(current, remaining):
        if not remaining:
            result.append(current[:])
            return

        for i in range(len(remaining)):
            current.append(remaining[i])
            backtrack(current, remaining[:i] + remaining[i+1:])
            current.pop()

    backtrack([], nums)
    return result


# ══════════════════════════════════════════════════════════════════
# 14. DYNAMIC PROGRAMMING — 1D
#     Use when: optimal substructure, overlapping subproblems
# ══════════════════════════════════════════════════════════════════
def dp_1d(nums):
    n = len(nums)
    dp = [0] * n
    dp[0] = nums[0]            # base case

    for i in range(1, n):
        dp[i] = max(dp[i-1], nums[i])    # recurrence relation

    return dp[n - 1]


# ══════════════════════════════════════════════════════════════════
# 15. DYNAMIC PROGRAMMING — 2D (LCS type)
#     Use when: two sequences, substring/subsequence problems
# ══════════════════════════════════════════════════════════════════
def dp_2d(s1, s2):
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]   # (m+1) x (n+1)

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    return dp[m][n]


# ══════════════════════════════════════════════════════════════════
# 16. UNION FIND (Disjoint Set Union)
#     Use when: connected components, cycle in undirected graph
# ══════════════════════════════════════════════════════════════════
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])   # path compression
        return self.parent[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return False                   # already connected = cycle!
        if self.rank[px] < self.rank[py]:
            px, py = py, px
        self.parent[py] = px              # union by rank
        if self.rank[px] == self.rank[py]:
            self.rank[px] += 1
        return True


# ══════════════════════════════════════════════════════════════════
# 17. TOPOLOGICAL SORT — KAHN'S BFS
#     Use when: dependency ordering, course schedule type
# ══════════════════════════════════════════════════════════════════
def topological_sort(n, edges):
    graph = defaultdict(list)
    indegree = [0] * n

    for u, v in edges:
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

    return order if len(order) == n else []    # empty = cycle exists
