# Sliding Window

## When to Use?

Ask these questions:
- Do I need a **contiguous** subarray or substring?
- Am I **maximizing or minimizing** a length / sum?
- Does the window **grow and shrink** based on some condition?

All 3 yes → Sliding Window

**Golden signal words in problem:**
> "longest", "shortest", "minimum window", "subarray", "substring", "contiguous", "at most k", "exactly k"

---

## Variants

### Variant 1 — Fixed Size Window (k is given)
**Window size never changes. Slide it from left to right.**

**Signals:**
- "subarray of size k"
- "every window of size k"
- "average of subarrays of length k"

**Template:**
```python
# Build first window
window_sum = sum(arr[:k])
ans = window_sum

for i in range(k, len(arr)):
    window_sum += arr[i]        # add new right element
    window_sum -= arr[i - k]    # remove old left element
    ans = max(ans, window_sum)  # update answer

return ans
```

**Problems:**
| Problem | LC # | File |
|---------|------|------|
| Maximum Average Subarray I | #643 | sliding_window/max_avg_subarray.py |
| Find All Anagrams in String | #438 | sliding_window/find_anagrams.py |
| Permutation in String | #567 | sliding_window/permutation_string.py |

---

### Variant 2 — Variable Size Window
**Window expands to the right, shrinks from left when condition breaks.**

**Signals:**
- "longest substring without..."
- "minimum length subarray with sum >= k"
- "at most k distinct characters"

**Template:**
```python
left = 0
ans = 0
window = {}   # or sum, count, etc.

for right in range(len(arr)):
    # ① EXPAND — add arr[right] into window
    window[arr[right]] = window.get(arr[right], 0) + 1

    # ② SHRINK — while window is invalid
    while len(window) > k:               # your condition here
        window[arr[left]] -= 1
        if window[arr[left]] == 0:
            del window[arr[left]]
        left += 1

    # ③ UPDATE ANSWER
    ans = max(ans, right - left + 1)

return ans
```

**Problems:**
| Problem | LC # | File |
|---------|------|------|
| Longest Substring Without Repeating | #3 | sliding_window/longest_no_repeat.py |
| Longest Substring with At Most K Distinct | #340 | sliding_window/at_most_k_distinct.py |
| Minimum Window Substring | #76 | sliding_window/min_window_substring.py |
| Fruit Into Baskets | #904 | sliding_window/fruit_baskets.py |

---

### Variant 3 — Variable Size with HashMap
**Track character/element frequency inside window using a HashMap.**

**Signals:**
- "anagram", "permutation" inside a window
- "frequency of characters"

**Template:**
```python
from collections import Counter

need = Counter(t)          # what we need
have = {}                  # what we have in window
formed = 0                 # how many chars satisfied
required = len(need)

left = 0
ans = float('inf'), -1, -1

for right in range(len(s)):
    char = s[right]
    have[char] = have.get(char, 0) + 1
    if char in need and have[char] == need[char]:
        formed += 1

    while formed == required:
        # update answer
        if right - left + 1 < ans[0]:
            ans = (right - left + 1, left, right)
        # shrink from left
        left_char = s[left]
        have[left_char] -= 1
        if left_char in need and have[left_char] < need[left_char]:
            formed -= 1
        left += 1

return "" if ans[0] == float('inf') else s[ans[1]:ans[2]+1]
```

---

## Fixed vs Variable — How to Decide?

| | Fixed | Variable |
|---|---|---|
| Window size | Given as k | You find it |
| Shrink condition | Never (just slide) | When window becomes invalid |
| Answer type | Usually a value | Usually a length or substring |

---

## Common Mistakes
- ❌ Forgetting to shrink window (infinite loop risk)
- ❌ Not cleaning up HashMap when element count goes to 0
- ❌ Off-by-one on window size: `right - left + 1`

## Complexity
- Time: O(n) — each element enters and exits window exactly once
- Space: O(k) — window state / HashMap
