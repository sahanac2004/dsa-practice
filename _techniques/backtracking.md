# Backtracking

## When to Use?

- Need to **generate all possibilities** (subsets, permutations, combinations)
- Problem says "find all", "generate all", "list all valid"
- Need to **explore paths** and **undo choices** (N-Queens, Sudoku)

**Golden signal words:**
> "all subsets", "all permutations", "all combinations", "find all paths", "generate all valid"

---

## Core Idea

```
Choose → Explore → Unchoose (backtrack)
```

Every backtracking problem follows this exact pattern.

## Universal Template

```python
def backtrack(current_state, remaining_choices):
    # BASE CASE — when to stop and record answer
    if is_solution(current_state):
        result.append(current_state[:])  # always add a COPY
        return

    for choice in remaining_choices:
        # CHOOSE
        current_state.append(choice)

        # EXPLORE
        backtrack(current_state, updated_choices)

        # UNCHOOSE (backtrack)
        current_state.pop()
```

---

## Variants

### Variant 1 — Subsets (no duplicates in input)

```python
def subsets(nums):
    result = []

    def backtrack(start, current):
        result.append(current[:])          # every state is a valid subset

        for i in range(start, len(nums)):
            current.append(nums[i])
            backtrack(i + 1, current)      # i+1 means no reuse
            current.pop()

    backtrack(0, [])
    return result
```

---

### Variant 2 — Subsets with Duplicates (sort + skip)

```python
def subsets_with_dup(nums):
    nums.sort()                             # MUST sort first
    result = []

    def backtrack(start, current):
        result.append(current[:])

        for i in range(start, len(nums)):
            if i > start and nums[i] == nums[i-1]:  # skip duplicates
                continue
            current.append(nums[i])
            backtrack(i + 1, current)
            current.pop()

    backtrack(0, [])
    return result
```

---

### Variant 3 — Permutations

```python
def permutations(nums):
    result = []

    def backtrack(current, used):
        if len(current) == len(nums):
            result.append(current[:])
            return

        for i in range(len(nums)):
            if used[i]:
                continue
            used[i] = True
            current.append(nums[i])
            backtrack(current, used)
            current.pop()
            used[i] = False

    backtrack([], [False] * len(nums))
    return result
```

---

### Variant 4 — Combinations (choose k from n)

```python
def combinations(n, k):
    result = []

    def backtrack(start, current):
        if len(current) == k:
            result.append(current[:])
            return

        for i in range(start, n + 1):
            current.append(i)
            backtrack(i + 1, current)
            current.pop()

    backtrack(1, [])
    return result
```

---

### Variant 5 — With Pruning (N-Queens, Sudoku)
**Pruning = skip invalid choices early to avoid useless exploration**

```python
def n_queens(n):
    result = []
    cols = set()
    diag1 = set()   # row - col
    diag2 = set()   # row + col

    def backtrack(row, board):
        if row == n:
            result.append(board[:])
            return

        for col in range(n):
            if col in cols or (row - col) in diag1 or (row + col) in diag2:
                continue    # PRUNING — skip invalid placement

            cols.add(col)
            diag1.add(row - col)
            diag2.add(row + col)
            board.append(col)

            backtrack(row + 1, board)

            cols.remove(col)
            diag1.remove(row - col)
            diag2.remove(row + col)
            board.pop()

    backtrack(0, [])
    return result
```

---

## Problems

| Problem | LC # | Variant | File |
|---------|------|---------|------|
| Subsets | #78 | Subsets | backtracking/subsets.py |
| Subsets II | #90 | Subsets + duplicates | backtracking/subsets_2.py |
| Permutations | #46 | Permutations | backtracking/permutations.py |
| Permutations II | #47 | Perms + duplicates | backtracking/permutations_2.py |
| Combination Sum | #39 | Combinations (reuse allowed) | backtracking/combo_sum.py |
| Combination Sum II | #40 | Combinations (no reuse) | backtracking/combo_sum_2.py |
| N-Queens | #51 | With pruning | backtracking/n_queens.py |
| Sudoku Solver | #37 | With pruning | backtracking/sudoku.py |
| Word Search | #79 | Grid backtracking | backtracking/word_search.py |
| Palindrome Partitioning | #131 | With validity check | backtracking/palindrome_partition.py |

---

## Common Mistakes
- ❌ `result.append(current)` instead of `result.append(current[:])` — you're appending a reference!
- ❌ Not sorting when duplicates exist — will get duplicate results
- ❌ Not pruning — solution will TLE on large inputs

## Complexity
- Subsets: O(n × 2ⁿ) — 2ⁿ subsets, each takes O(n) to copy
- Permutations: O(n × n!) — n! permutations, each takes O(n) to copy
- Combinations: O(k × C(n,k))
