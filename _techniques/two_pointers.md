# Two Pointers

## When to Use?

Ask these questions about the problem:
- Is the input **sorted** (or can I sort it)?
- Do I need to find a **pair / triplet** satisfying a condition?
- Do I need to **detect a cycle** or find the **middle** of a linked list?
- Do I need to **partition** or **rearrange** in-place?

If yes to any → Think Two Pointers

---

## Variants

### Variant 1 — Opposite Ends (L & R)
**Pointers start from both ends and move toward each other**

**Signals in problem:**
- Sorted array + find pair with target sum
- Container with most water
- Reverse in-place
- Valid palindrome

**Template:**
```python
left, right = 0, len(arr) - 1
while left < right:
    if condition_met:
        # process answer
    elif need_bigger:
        left += 1
    else:
        right -= 1
```

**Problems:**
| Problem | LC # | File |
|---------|------|------|
| Two Sum II (sorted) | #167 | arrays/two_sum_sorted.py |
| 3Sum | #15 | arrays/three_sum.py |
| Container With Most Water | #11 | arrays/container_water.py |
| Valid Palindrome | #125 | strings/valid_palindrome.py |

---

### Variant 2 — Slow & Fast (Floyd's Algorithm)
**Both pointers start at same end, fast moves 2x speed**

**Signals in problem:**
- Detect cycle in linked list
- Find middle of linked list
- Find duplicate number (array as linked list)
- Happy number

**Template:**
```python
slow = head
fast = head
while fast and fast.next:
    slow = slow.next        # 1 step
    fast = fast.next.next   # 2 steps
    if slow == fast:
        return True         # cycle!
```

**Problems:**
| Problem | LC # | File |
|---------|------|------|
| Linked List Cycle | #141 | linked_lists/detect_cycle.py |
| Middle of Linked List | #876 | linked_lists/middle_list.py |
| Find Duplicate Number | #287 | arrays/find_duplicate.py |

---

### Variant 3 — Same Direction (Partition)
**Both pointers start from same side, one is slow writer**

**Signals in problem:**
- Remove duplicates in-place
- Move zeroes
- Dutch national flag (sort 0s 1s 2s)

**Template:**
```python
write = 0
for read in range(len(arr)):
    if arr[read] meets condition:
        arr[write] = arr[read]
        write += 1
```

**Problems:**
| Problem | LC # | File |
|---------|------|------|
| Remove Duplicates from Sorted Array | #26 | arrays/remove_duplicates.py |
| Move Zeroes | #283 | arrays/move_zeroes.py |
| Sort Colors | #75 | arrays/sort_colors.py |

---

## Common Mistakes
- ❌ Forgetting to handle duplicates in 3Sum → always skip duplicates at every pointer
- ❌ Using `left < right` vs `left <= right` — use `<` for pairs (stop when they meet)
- ❌ Sorting when problem doesn't allow it (check constraints)

## Complexity
- Time: O(n) for most two pointer problems (single pass)
- Space: O(1) — no extra space (in-place)
