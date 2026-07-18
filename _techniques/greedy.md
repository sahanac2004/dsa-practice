# Greedy

## When to Use?

- **Local optimal choice → Global optimal result**
- Problem involves **intervals** (meeting rooms, activity selection)
- Problem involves **sorting + picking best** at each step
- Keywords: "minimum number of", "maximum we can achieve", "earliest deadline"

**How to verify greedy works:** Prove that picking the local best never hurts future choices. If you can't prove it, try DP instead.

---

## Variants

### Variant 1 — Interval Scheduling
```python
# Sort by end time, greedily pick non-overlapping intervals
def erase_overlap_intervals(intervals):
    intervals.sort(key=lambda x: x[1])  # sort by END time
    count = 0
    prev_end = float('-inf')

    for start, end in intervals:
        if start >= prev_end:   # no overlap
            prev_end = end
        else:
            count += 1          # remove this interval

    return count
```

### Variant 2 — Jump Game (can we reach end?)
```python
def can_jump(nums):
    max_reach = 0
    for i, jump in enumerate(nums):
        if i > max_reach:
            return False        # can't reach here
        max_reach = max(max_reach, i + jump)
    return True
```

---

## Problems
| Problem | LC # | File |
|---------|------|------|
| Jump Game | #55 | greedy/jump_game.py |
| Jump Game II | #45 | greedy/jump_game_2.py |
| Non-overlapping Intervals | #435 | greedy/non_overlap_intervals.py |
| Meeting Rooms II | #253 | greedy/meeting_rooms.py |
| Gas Station | #134 | greedy/gas_station.py |
| Candy | #135 | greedy/candy.py |

## Complexity
- Usually O(n log n) due to sorting
- O(n) if no sorting needed
