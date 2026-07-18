# Dynamic Programming

## When to Use?

Ask these questions:
- Does the problem ask for **count of ways**, **maximum/minimum**, or **yes/no (is it possible)**?
- Does it have **overlapping subproblems** (same sub-computation done multiple times)?
- Does it have **optimal substructure** (optimal answer built from optimal smaller answers)?
- Are there **choices at each step** (take/skip, left/right, include/exclude)?

If yes → Think DP

**Golden signal words:**
> "number of ways", "maximum profit", "minimum cost", "longest", "shortest", "can you reach", "count distinct"

---

## How to Approach Any DP Problem (5 Steps)

```
Step 1 → Define dp[i] clearly in English
Step 2 → Write the recurrence relation
Step 3 → Identify base cases
Step 4 → Identify traversal order (left→right? right→left? both?)
Step 5 → Identify the final answer (dp[n]? max(dp)? dp[n][m]?)
```

---

## Variants

### Variant 1 — 1D DP (linear / fibonacci type)

**Signals:** Only depends on previous 1 or 2 states

```python
# Climbing Stairs type
dp[0] = 1
dp[1] = 1
for i in range(2, n + 1):
    dp[i] = dp[i-1] + dp[i-2]
```

**Problems:**
| Problem | LC # | File |
|---------|------|------|
| Climbing Stairs | #70 | dynamic_programming/climbing_stairs.py |
| House Robber | #198 | dynamic_programming/house_robber.py |
| Min Cost Climbing Stairs | #746 | dynamic_programming/min_cost_stairs.py |

---

### Variant 2 — 0/1 Knapsack
**Take or skip each item. Each item used at most once.**

**Signals:** "select items", "subset sum", "partition equal subset", "target sum"

```python
# dp[i][w] = max value using first i items with capacity w
dp = [[0] * (W + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for w in range(W + 1):
        # skip item i
        dp[i][w] = dp[i-1][w]
        # take item i (if it fits)
        if weights[i-1] <= w:
            dp[i][w] = max(dp[i][w], dp[i-1][w - weights[i-1]] + values[i-1])
```

**Problems:**
| Problem | LC # | File |
|---------|------|------|
| 0/1 Knapsack | Classic | dynamic_programming/knapsack_01.py |
| Subset Sum | Classic | dynamic_programming/subset_sum.py |
| Partition Equal Subset Sum | #416 | dynamic_programming/partition_equal.py |
| Target Sum | #494 | dynamic_programming/target_sum.py |

---

### Variant 3 — Unbounded Knapsack
**Each item can be used unlimited times.**

**Signals:** "coins", "unlimited supply", "can repeat"

```python
dp = [0] * (amount + 1)
dp[0] = 1   # base case: 1 way to make 0

for coin in coins:
    for amount in range(coin, target + 1):
        dp[amount] += dp[amount - coin]   # reuse same row (unbounded)
```

**Problems:**
| Problem | LC # | File |
|---------|------|------|
| Coin Change | #322 | dynamic_programming/coin_change.py |
| Coin Change II (count ways) | #518 | dynamic_programming/coin_change_ways.py |
| Rod Cutting | Classic | dynamic_programming/rod_cutting.py |

---

### Variant 4 — DP on Strings (LCS type)
**Two sequences, find longest common subsequence/substring**

**Signals:** "two strings", "edit distance", "common subsequence", "longest palindromic"

```python
# dp[i][j] = LCS of s1[:i] and s2[:j]
dp = [[0] * (n + 1) for _ in range(m + 1)]

for i in range(1, m + 1):
    for j in range(1, n + 1):
        if s1[i-1] == s2[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1        # extend
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])  # skip one
```

**Problems:**
| Problem | LC # | File |
|---------|------|------|
| Longest Common Subsequence | #1143 | dynamic_programming/lcs.py |
| Edit Distance | #72 | dynamic_programming/edit_distance.py |
| Longest Palindromic Subsequence | #516 | dynamic_programming/lps.py |
| Distinct Subsequences | #115 | dynamic_programming/distinct_subseq.py |

---

### Variant 5 — LIS (Longest Increasing Subsequence)

```python
# O(n²) DP
dp = [1] * n
for i in range(1, n):
    for j in range(i):
        if nums[j] < nums[i]:
            dp[i] = max(dp[i], dp[j] + 1)
return max(dp)

# O(n log n) with Binary Search (advanced)
```

**Problems:**
| Problem | LC # | File |
|---------|------|------|
| Longest Increasing Subsequence | #300 | dynamic_programming/lis.py |
| Russian Doll Envelopes | #354 | dynamic_programming/russian_doll.py |

---

### Variant 6 — DP on Trees

```python
# Post-order DFS — solve children first, then current node
def dp_tree(node):
    if not node:
        return 0
    left = dp_tree(node.left)
    right = dp_tree(node.right)
    # use left and right to compute current
    return ...
```

---

## Memoization vs Tabulation

| | Memoization (Top-Down) | Tabulation (Bottom-Up) |
|---|---|---|
| Style | Recursive + cache | Iterative + table |
| Direction | Big → small | Small → big |
| Space | O(n) call stack | O(n) table |
| When to use | Natural recursion | When stack overflow risk |

```python
# Memoization — add @cache or memo dict
from functools import lru_cache

@lru_cache(maxsize=None)
def dp(i):
    if i <= 1: return i
    return dp(i-1) + dp(i-2)
```

---

## Common Mistakes
- ❌ Wrong dp definition — spend time defining dp[i] clearly before coding
- ❌ Wrong base cases — always verify dp[0], dp[1] manually
- ❌ Off by one in loops — be careful with 1-indexed vs 0-indexed dp
- ❌ Forgetting to return `max(dp)` vs `dp[n]` — depends on definition

## Complexity
- Time: O(states × transitions) — usually O(n) or O(n²) or O(n×m)
- Space: O(states) — can often optimize to O(1) or O(n) with rolling array
