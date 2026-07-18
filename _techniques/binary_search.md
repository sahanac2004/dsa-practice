# Binary Search

## When to Use?

Ask these questions:
- Is the search space **sorted** (or monotonic)?
- Can I **eliminate half** the possibilities with each step?
- Is the problem asking for **minimum/maximum possible value**?
- Does the problem feel like: "find the smallest X such that condition(X) is true"?

If yes → Binary Search

**Golden signal words:**
> "sorted array", "search", "find position", "minimum capacity", "kth element", "rotated sorted", "peak element"

---

## Variants

### Variant 1 — Classic Binary Search (find element)

```python
def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2   # safe from overflow

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1   # not found
```

**Problems:**
| Problem | LC # | File |
|---------|------|------|
| Binary Search | #704 | binary_search/classic.py |
| Search Insert Position | #35 | binary_search/search_insert.py |
| Search in Rotated Sorted Array | #33 | binary_search/rotated_array.py |

---

### Variant 2 — Find First / Last Occurrence (Lower / Upper Bound)

```python
def find_first(arr, target):
    left, right = 0, len(arr) - 1
    result = -1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            result = mid        # save answer
            right = mid - 1    # but keep going left
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return result


def find_last(arr, target):
    left, right = 0, len(arr) - 1
    result = -1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            result = mid        # save answer
            left = mid + 1     # but keep going right
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return result
```

**Problems:**
| Problem | LC # | File |
|---------|------|------|
| Find First and Last Position | #34 | binary_search/first_last.py |
| Count Occurrences of Target | — | binary_search/count_occurrences.py |

---

### Variant 3 — Binary Search on Answer Space
**Key idea: you're not searching for an element, you're searching for the ANSWER**

**How to identify:**
- Problem asks for "minimum X such that..." or "maximum X such that..."
- You can write an `is_feasible(mid)` function
- Answer space has monotonic property (if X works, X+1 also works or doesn't)

```python
def binary_search_on_answer(arr):
    def is_feasible(capacity):
        # Can we achieve this capacity?
        # Write your check logic here
        days = 1
        current = 0
        for weight in arr:
            if current + weight > capacity:
                days += 1
                current = 0
            current += weight
        return days <= D        # D is your constraint

    # Define the answer range
    left = max(arr)            # minimum possible answer
    right = sum(arr)           # maximum possible answer
    ans = right

    while left <= right:
        mid = (left + right) // 2
        if is_feasible(mid):
            ans = mid          # this works, try smaller
            right = mid - 1
        else:
            left = mid + 1    # doesn't work, try bigger

    return ans
```

**Problems:**
| Problem | LC # | File |
|---------|------|------|
| Capacity to Ship Packages | #1011 | binary_search/ship_packages.py |
| Koko Eating Bananas | #875 | binary_search/koko_bananas.py |
| Minimum Days to Make Bouquets | #1482 | binary_search/min_days_bouquets.py |
| Find Peak Element | #162 | binary_search/peak_element.py |

---

### Variant 4 — Binary Search on Rotated Array

```python
def search_rotated(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid

        # Left half is sorted
        if arr[left] <= arr[mid]:
            if arr[left] <= target < arr[mid]:
                right = mid - 1
            else:
                left = mid + 1
        # Right half is sorted
        else:
            if arr[mid] < target <= arr[right]:
                left = mid + 1
            else:
                right = mid - 1

    return -1
```

---

## Key Things to Remember

| | Use |
|---|---|
| `left <= right` | Classic search (find exact element) |
| `left < right` | Find boundary / peak (don't want infinite loop) |
| `mid = left + (right - left) // 2` | Always (safe from integer overflow) |

## Common Mistakes
- ❌ `mid = (left + right) // 2` — causes overflow in other languages (safe in Python but bad habit)
- ❌ Infinite loop when `left = mid` instead of `left = mid + 1`
- ❌ Wrong boundary for answer space (`left` and `right` must cover full range)

## Complexity
- Time: O(log n)
- Space: O(1)
