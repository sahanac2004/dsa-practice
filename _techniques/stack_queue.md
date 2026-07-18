# Stack & Queue / Monotonic Stack

## Stack — When to Use?
- **Matching / balancing** (parentheses, brackets)
- **Undo operations** (last in, first out)
- **Monotonic stack** — next greater/smaller element

## Queue — When to Use?
- **BFS** (first in, first out)
- **Sliding window maximum** (monotonic deque)
- **Task scheduling**

---

## Variants

### Variant 1 — Parenthesis Matching
```python
def is_valid(s):
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}
    for char in s:
        if char in mapping:
            top = stack.pop() if stack else '#'
            if mapping[char] != top:
                return False
        else:
            stack.append(char)
    return not stack
```

### Variant 2 — Monotonic Stack (Next Greater Element)
```python
def next_greater(arr):
    n = len(arr)
    result = [-1] * n
    stack = []   # stores indices, decreasing order of values

    for i in range(n):
        while stack and arr[i] > arr[stack[-1]]:
            idx = stack.pop()
            result[idx] = arr[i]   # current is the "next greater"
        stack.append(i)

    return result
```

### Variant 3 — Monotonic Deque (Sliding Window Max)
```python
from collections import deque

def max_sliding_window(nums, k):
    dq = deque()   # stores indices, decreasing order of values
    result = []

    for i in range(len(nums)):
        # remove elements outside window
        while dq and dq[0] < i - k + 1:
            dq.popleft()
        # remove smaller elements (they'll never be max)
        while dq and nums[i] > nums[dq[-1]]:
            dq.pop()
        dq.append(i)
        # window fully formed
        if i >= k - 1:
            result.append(nums[dq[0]])

    return result
```

---

## Problems
| Problem | LC # | Variant | File |
|---------|------|---------|------|
| Valid Parentheses | #20 | Matching | stack_queue/valid_parens.py |
| Daily Temperatures | #739 | Monotonic Stack | stack_queue/daily_temps.py |
| Next Greater Element I | #496 | Monotonic Stack | stack_queue/next_greater.py |
| Largest Rectangle in Histogram | #84 | Monotonic Stack | stack_queue/histogram.py |
| Sliding Window Maximum | #239 | Monotonic Deque | stack_queue/sliding_max.py |
| Min Stack | #155 | Stack design | stack_queue/min_stack.py |

## Complexity
- Stack operations: O(1) push/pop
- Monotonic stack: O(n) — each element pushed/popped once
