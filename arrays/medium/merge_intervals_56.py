"""
╔═══════════════════════════════════════════════════════════════════╗
║  MERGE INTERVALS                                                  ║
║  LeetCode #56  |  Difficulty: Medium  |  Topic: Arrays / Greedy   ║
║  Link: https://leetcode.com/problems/merge-intervals/             ║
╚═══════════════════════════════════════════════════════════════════╝

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📘 SECTION 1 — PROBLEM UNDERSTANDING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Given an array of intervals [start, end], merge all overlapping
  intervals and return the resulting non-overlapping set that covers
  all the intervals in the input.

  Input : intervals = [[1,3],[2,6],[8,10],[15,18]]
  Output: [[1,6],[8,10],[15,18]]

  Example 1 — basic:
    Input : intervals = [[1,3],[2,6],[8,10],[15,18]]
    Output: [[1,6],[8,10],[15,18]]
    Why?  : [1,3] and [2,6] overlap (2 <= 3), so they merge into
             [1,6]; the rest don't touch anything

  Example 2 — slightly tricky (touching, not overlapping, endpoints):
    Input : intervals = [[1,4],[4,5]]
    Output: [[1,5]]
    Why?  : [1,4] ends exactly where [4,5] begins — they're
             considered overlapping (touching counts), so they merge

  Constraints:
    - 1 <= intervals.length <= 10^4
    - intervals[i].length == 2
    - 0 <= start_i <= end_i <= 10^4
    - Intervals may be given in ANY order (not pre-sorted)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🧠 SECTION 2 — KANGLISH THINKING — ಹೇಗೆ ಯೋಚಿಸಬೇಕು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  ಮೊದಲು problem odidaga ನಮ್ಮ brain ಏನು think ಮಾಡಬೇಕು:

  ಹಂತ 1 — Problem ಅರ್ಥ ಮಾಡಿಕೊಳ್ಳಿ (What are they asking?)
  ┌─────────────────────────────────────────────────────────┐
  │  Input ಏನು ಕೊಡ್ತಾರೆ?  →  [start,end] intervals list,       │
  │                          ಯಾವುದೇ order ನಲ್ಲಿ ಇರ್ಬೋದು         │
  │  Output ಏನು ಬೇಕು?     →  overlapping intervals merge ಮಾಡಿ  │
  │                          non-overlapping final list         │
  │  Constraints ಏನಿದೆ?   →  n<=10^4, unsorted ಆಗ್ಬೋದು          │
  └─────────────────────────────────────────────────────────┘

  ಹಂತ 2 — ನನಗೆ ಗೊತ್ತಿರೋ simple way ಏನು? (Brute force thought)
  →  ಪ್ರತಿ interval pair ಗೂ overlap ಚೆಕ್ ಮಾಡಿ merge ಮಾಡ್ತಾ, ಯಾವುದೇ
     change ಆಗ್ದೇ ಇರೋ ತನಕ repeat ಮಾಡೋದು.
  →  ಆದರೆ ಇದು slow ಯಾಕೆ? → O(n²) ಅಥವಾ ಇನ್ನೂ ಜಾಸ್ತಿ (repeated passes) —
     n=10^4 ಗೆ ಸಾಕಷ್ಟು slow, unsorted ಆಗಿರೋದ್ರಿಂದ overlap detect
     ಮಾಡೋಕೆ ಪ್ರತಿ pair check ಬೇಕಾಗುತ್ತೆ.

  ಹಂತ 3 — Better way ಹೇಗೆ ಯೋಚಿಸುವುದು? (Optimization thought)
  →  "intervals ಅನ್ನ start time ಪ್ರಕಾರ sort ಮಾಡಿದ್ರೆ, overlap ಆಗೋ
     intervals ಯಾವಾಗ್ಲೂ ಪಕ್ಕ ಪಕ್ಕ ಬರ್ತಾವೆ — ಆಗ ಒಂದೇ linear pass ನಲ್ಲಿ
     ಸಾಕಾಗುತ್ತೆ."
  →  ಅಹಾ moment: Sort ಮಾಡಿದ ಮೇಲೆ, result list ನ ಕೊನೆಯ interval ಜೊತೆ
     current interval ಅನ್ನ compare ಮಾಡಿ — current.start <=
     last.end ಆದ್ರೆ overlap ಆಗುತ್ತೆ, last.end = max(last.end,
     current.end) ಮಾಡಿ merge ಮಾಡು. ಇಲ್ಲಾಂದ್ರೆ current ಅನ್ನ ಹೊಸ interval
     ಆಗಿ result ಗೆ add ಮಾಡು.
  →  ಇದರಿಂದ ನಾವು Greedy → Sort by Start + Merge Adjacent use ಮಾಡಬಹುದು!

  ಹಂತ 4 — Technique ಯಾಕೆ ಇಲ್ಲಿ ಕೆಲಸ ಮಾಡುತ್ತೆ?
  →  Sort ಮಾಡಿದ ಮೇಲೆ, ಯಾವುದೇ interval ಜೊತೆ overlap ಆಗೋ possibility
     ಇರೋದು ಅದರ ಹಿಂದೆ ಬರೋ (already processed) interval ಜೊತೆ ಮಾತ್ರ —
     ಮುಂದೆ ಬರೋ ಯಾವ interval ಜೊತೆಗೂ ಅಲ್ಲ (start ಗಳು increasing).
  →  ಇದ್ರಿಂದ ಒಂದೇ result ಇಟ್ಕೊಂಡು "ಕೊನೆಯ merged interval" ಜೊತೆ ಮಾತ್ರ
     compare ಮಾಡಿದ್ರೆ ಸಾಕು — ಪ್ರತಿ interval ಗೂ ಪೂರ್ತಿ list ಜೊತೆ
     compare ಮಾಡೋ ಅಗತ್ಯ ಇಲ್ಲ.
  →  Single pass ಇಂದ O(n) (sort ಬಿಟ್ಟು) — overall O(n log n).

  💡 Interview ನಲ್ಲಿ ಹೇಗೆ ಮಾತಾಡಬೇಕು (Think out loud):
  →  "Since the intervals can come in any order, the naive approach
      compares every pair — O(n²)."
  →  "If I sort by start time first, any interval that could overlap
      with the current one must be immediately before it — so a
      single linear pass after sorting is enough."
  →  "I keep a result list and only ever compare the current interval
      against the last one merged so far, extending its end if they
      overlap."

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🏷️ SECTION 3 — TECHNIQUE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Primary   : Greedy → Sort by Start + Merge Adjacent
  Secondary : None

  WHY this technique?
  → Intervals aren't guaranteed sorted, so sorting by start first
    turns a global overlap problem into a local, adjacent-only one
  → After sorting, only the most recently merged interval can ever
    overlap with the next one — no need to re-check earlier intervals
  → A single linear pass after the sort achieves the merge, giving
    an overall O(n log n) solution dominated by the sort

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 💡 SECTION 4 — INTUITION (How to think — English)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Key observation: once intervals are sorted by start time, overlap
  checking becomes purely local — interval i can only possibly
  overlap with interval i-1 (or the currently merged block ending at
  or after it), never with something further back or further ahead.

  The journey from brute to optimal:
    Brute thought   →  compare every pair of intervals, merge, repeat
                        until no more merges happen
    Problem with it →  O(n²) or worse, doesn't exploit any structure
    Better question →  "if intervals were sorted, would overlap
                        detection become a simple adjacent comparison?"
    Insight         →  sort by start time, then only the last merged
                        interval needs comparing against the next one
    Optimal         →  sort + single linear merge pass, O(n log n)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🐢 SECTION 5 — APPROACH 1 — BRUTE FORCE (Repeated Pairwise Merge)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    Repeatedly scan all pairs of intervals; whenever two overlap,
    merge them into one and restart the scan. Stop when a full pass
    produces no merges.

  Pseudocode:
    step 1: merged_any = True
    step 2: while merged_any:
    step 3:   merged_any = False
    step 4:   for each pair (i, j): if they overlap: merge them, remove
              the originals, set merged_any = True, restart scan
    step 5: return the remaining intervals

  Time  : O(n³) worst case  →  Why: repeated full pairwise scans until stable
  Space : O(n)  →  Why: result list of intervals

  ಇದು ಯಾಕೆ ಸಾಕಾಗಲ್ಲ? (Why is this not enough?)
    → n=10^4 ಗೆ repeated pairwise scans ಖಂಡಿತ TLE ಆಗುತ್ತೆ. Sort +
      single pass ಇಂದ O(n log n) ಗೆ ಇಳಿಸ್ಬೋದು.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🚶 SECTION 6 — APPROACH 2 — BETTER (skip — brute jumps straight to optimal)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  ಇಲ್ಲಿ intermediate approach ಇಲ್ಲ — sort-based insight ಸಿಕ್ಕ ತಕ್ಷಣ
  ನೇರವಾಗಿ optimal ಗೆ ಹೋಗಬಹುದು.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🚀 SECTION 7 — APPROACH 3 — OPTIMAL   (Sort by Start + Merge Adjacent)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    Sort intervals by start value. Initialize result with the first
    interval. For every subsequent interval, compare its start with
    the end of the last interval in result: if it's <= (overlap or
    touching), extend the last interval's end to the max of the two
    ends; otherwise, append this interval as a new entry.

  Key steps:
    1. intervals.sort(key=lambda x: x[0])
    2. merged = [intervals[0]]
    3. for start, end in intervals[1:]:
         if start <= merged[-1][1]: merged[-1][1] = max(merged[-1][1], end)
         else: merged.append([start, end])
    4. Return merged

  ಕನ್ನಡದಲ್ಲಿ ಒಂದು ಸಲ ಹೇಳಿ (Say it once in Kanglish so it sticks):
    → "intervals ಅನ್ನ start ಪ್ರಕಾರ sort ಮಾಡು. ಮೊದಲ interval ಅನ್ನ
        result ಗೆ ಹಾಕು. ಪ್ರತಿ next interval ಗೂ, ಅದರ start <= result ನ
        last interval ನ end ಆದ್ರೆ overlap ಆಗುತ್ತೆ — last end ಅನ್ನ
        max ಮಾಡಿ update ಮಾಡು. ಇಲ್ಲಾಂದ್ರೆ ಹೊಸ interval ಆಗಿ result ಗೆ
        add ಮಾಡು!"

  Time  : O(n log n)  →  Why: dominated by the sort; the merge pass
                    itself is O(n)
  Space : O(n)  →  Why: sorted copy + result list (O(log n) extra
                    for the sort itself, implementation-dependent)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🔍 SECTION 8 — DRY RUN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
  (already sorted by start)

  merged = [[1,3]]
  [2,6]: start=2 <= merged[-1].end=3 → overlap! merged[-1] = [1, max(3,6)=6]
         merged = [[1,6]]
  [8,10]: start=8 <= merged[-1].end=6? No → append → merged = [[1,6],[8,10]]
  [15,18]: start=15 <= merged[-1].end=10? No → append → merged = [[1,6],[8,10],[15,18]]

  Output: [[1,6],[8,10],[15,18]]   matches expected

  ಇನ್ನೊಂದು example — tricky case (touching endpoints, unsorted input):
  Input: intervals = [[4,5],[1,4]]

  After sort by start: [[1,4],[4,5]]
  merged = [[1,4]]
  [4,5]: start=4 <= merged[-1].end=4 → overlap (touching counts)!
         merged[-1] = [1, max(4,5)=5] → merged = [[1,5]]

  Output: [[1,5]]   matches expected

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 ⚠️ SECTION 9 — EDGE CASES — ಇವನ್ನ ಮರೆಯಬೇಡ!
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  ✓ Single interval?           →  result is just that one interval,
                                   loop never runs
  ✓ No intervals overlap at all? →  every interval appended as its
                                   own entry, result == sorted input
  ✓ All intervals overlap into one? →  everything collapses into a
                                   single merged interval
  ✓ Unsorted input?            →  handled by the initial sort step
  ✓ Touching endpoints (a.end == b.start)? →  correctly treated as
                                   overlapping via the <= comparison

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📊 SECTION 10 — COMPLEXITY SUMMARY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                Time         Space
  Brute Force   O(n³)        O(n)
  Optimal       O(n log n)   O(n)    ← use this 

  Time ಯಾಕೆ ಅಷ್ಟು?  → Sort ಗೆ O(n log n), ಆಮೇಲಿನ merge pass O(n) —
                        sort ಯೇ dominant term.
  Space ಯಾಕೆ ಅಷ್ಟು? → merged result list ಇಡೋಕೆ O(n).

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🎯 SECTION 11 — PATTERN LEARNED — ಇದರಿಂದ ಕಲಿತದ್ದು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Pattern Name: Greedy Intervals — Sort by Start, Merge Adjacent

  ಈ pattern ಯಾವಾಗ use ಮಾಡಬೇಕು?
  → Intervals overlap ಮಾಡ್ಬೇಕಾ ಅಂತ ಚೆಕ್ ಮಾಡ್ಬೇಕಾದಾಗ, ಆದ್ರೆ order
    guarantee ಇಲ್ಲದೆ ಇದ್ದಾಗ
  → Sort ಮಾಡಿದ ಮೇಲೆ problem "local adjacent comparison" ಆಗಿ
    simplify ಆಗುತ್ತೆ ಅಂತ ಗೊತ್ತಾದಾಗ
  → "Combine overlapping ranges into one" ಅನ್ನೋ ಯಾವುದೇ variation
    ಕೇಳಿದಾಗ

  ಇದೇ pattern ಬೇರೆ problems ನಲ್ಲಿ ಕಾಣಿಸುತ್ತೆ:
  → Insert Interval (#57) — same merging logic, insertion twist
  → Non-overlapping Intervals (#435) — same sort-by-start family,
    counting removals instead of merging
  → Meeting Rooms (#252/#253) — same interval-overlap detection idea

  Next time ಇಂತಹ problem ಬಂದ್ರೆ ನಾನು ಮೊದಲು ಇದನ್ನ think ಮಾಡ್ತೇನೆ:
  → "Intervals overlap/merge ಕೇಳಿದ ತಕ್ಷಣ, ಮೊದಲು start ಪ್ರಕಾರ sort
      ಮಾಡು, ಆಮೇಲೆ ಕೊನೆಯ merged interval ಜೊತೆ ಮಾತ್ರ compare ಮಾಡ್ತಾ
      single pass ಮಾಡು ಅಂತ ಮೊದಲು ಯೋಚಿಸು."

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🗣️ SECTION 12 — INTERVIEWALLI HEGE EXPLAIN MAADABEEKU
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  1. Understand:
     "I need to merge all overlapping intervals into a minimal set of
      non-overlapping intervals that still covers everything."

  2. Brute force:
     "Repeatedly scanning all pairs and merging until stable works,
      but is O(n³) in the worst case — way too slow for n=10^4."

  3. Optimize:
     "If I sort the intervals by start time first, any interval that
      could overlap with the current one must be the one right before
      it in the result — so I only ever need to compare against the
      last merged interval."

  4. Code:
     "I will sort by start, then do a single pass: extend the last
      result interval's end if the next interval's start falls within
      it, otherwise start a new interval in the result."

  5. Complexity:
     "Time O(n log n) — dominated by the sort. Space O(n) — for the
      result list."

  ಮುಖ್ಯ: ಸುಮ್ಮನೆ ಕೂತು code ಬರೆಯಬೇಡ!
         Interviewer ಗೆ ನಿನ್ನ thinking process ಕಾಣಬೇಕು.
"""


# ═══════════════════════════════════════════════════════════════════
# BRUTE FORCE — O(n^3) Time | O(n) Space  (Repeated Pairwise Merge)
# ═══════════════════════════════════════════════════════════════════
def merge_brute(intervals):
    """ಇದು ಮೊದಲ ಆಲೋಚನೆ — no-more-merges ಆಗೋ ತನಕ ಪ್ರತಿ pair ಚೆಕ್ ಮಾಡಿ merge ಮಾಡೋದು"""
    result = [list(iv) for iv in intervals]
    merged_any = True

    while merged_any:
        merged_any = False
        for i in range(len(result)):
            for j in range(i + 1, len(result)):
                a, b = result[i], result[j]
                if a[0] <= b[1] and b[0] <= a[1]:  # overlap check
                    a[0], a[1] = min(a[0], b[0]), max(a[1], b[1])
                    result.pop(j)
                    merged_any = True
                    break
            if merged_any:
                break

    return sorted(result)


# ═══════════════════════════════════════════════════════════════════
# OPTIMAL — O(n log n) Time | O(n) Space  (Sort by Start + Merge Adjacent)
# ═══════════════════════════════════════════════════════════════════
def merge(intervals):
    """ಇದು final answer — start ಪ್ರಕಾರ sort ಮಾಡಿ single pass ನಲ್ಲಿ merge ಮಾಡು"""
    intervals = sorted(intervals, key=lambda x: x[0])
    merged = [list(intervals[0])]

    for start, end in intervals[1:]:
        if start <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], end)
        else:
            merged.append([start, end])

    return merged


# ═══════════════════════════════════════════════════════════════════
# TEST CASES
# ═══════════════════════════════════════════════════════════════════
if __name__ == "__main__":
    import sys
    sys.stdout.reconfigure(encoding="utf-8")   # Windows cp1252 can't print emoji otherwise

    # Test 1 — Basic example
    assert merge([[1, 3], [2, 6], [8, 10], [15, 18]]) == [[1, 6], [8, 10], [15, 18]]

    # Test 2 — Edge case: single interval
    assert merge([[5, 7]]) == [[5, 7]]

    # Test 3 — Edge case: all intervals overlap into one
    assert merge([[1, 4], [2, 5], [3, 6]]) == [[1, 6]]

    # Test 4 — Tricky: touching endpoints, unsorted input
    assert merge([[4, 5], [1, 4]]) == [[1, 5]]

    print("All tests passed! ")
