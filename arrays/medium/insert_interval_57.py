"""
╔═══════════════════════════════════════════════════════════════════╗
║  INSERT INTERVAL                                                  ║
║  LeetCode #57  |  Difficulty: Medium  |  Topic: Arrays / Greedy   ║
║  Link: https://leetcode.com/problems/insert-interval/             ║
╚═══════════════════════════════════════════════════════════════════╝

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📘 SECTION 1 — PROBLEM UNDERSTANDING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Given a list of non-overlapping intervals already sorted by start
  time, and a new interval, insert the new interval into the list,
  merging as needed so the result stays sorted and non-overlapping.

  Input : intervals = [[1,3],[6,9]], newInterval = [2,5]
  Output: [[1,5],[6,9]]

  Example 1 — basic:
    Input : intervals = [[1,3],[6,9]], newInterval = [2,5]
    Output: [[1,5],[6,9]]
    Why?  : newInterval [2,5] overlaps with [1,3] (2 <= 3), merging
             into [1,5]; [6,9] stays untouched (5 < 6)

  Example 2 — slightly tricky (new interval overlaps several at once):
    Input : intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
    Output: [[1,2],[3,10],[12,16]]
    Why?  : [4,8] overlaps with [3,5], [6,7], AND [8,10] all at once —
             they all collapse into a single [3,10] merged interval

  Constraints:
    - 0 <= intervals.length <= 10^4
    - intervals is sorted by start_i in ascending order, non-overlapping
    - newInterval.length == 2
    - 0 <= start <= end <= 10^5

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🧠 SECTION 2 — KANGLISH THINKING — ಹೇಗೆ ಯೋಚಿಸಬೇಕು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  ಮೊದಲು problem odidaga ನಮ್ಮ brain ಏನು think ಮಾಡಬೇಕು:

  ಹಂತ 1 — Problem ಅರ್ಥ ಮಾಡಿಕೊಳ್ಳಿ (What are they asking?)
  ┌─────────────────────────────────────────────────────────┐
  │  Input ಏನು ಕೊಡ್ತಾರೆ?  →  already sorted, non-overlapping   │
  │                          intervals + ಒಂದು new interval     │
  │  Output ಏನು ಬೇಕು?     →  new interval insert ಮಾಡಿ, merge   │
  │                          ಮಾಡಿ ಸರಿಯಾದ sorted result          │
  │  Constraints ಏನಿದೆ?   →  n<=10^4, input ಆಗ್ಲೇ sorted ಇದೆ    │
  │                          (Merge Intervals ಗಿಂತ ಬೇರೆ — sort   │
  │                          ಮಾಡೋ ಅಗತ್ಯ ಇಲ್ಲ)                  │
  └─────────────────────────────────────────────────────────┘

  ಹಂತ 2 — ನನಗೆ ಗೊತ್ತಿರೋ simple way ಏನು? (Brute force thought)
  →  newInterval ಅನ್ನ list ಗೆ append ಮಾಡಿ, Merge Intervals (#56) ಥರ
     ಪೂರ್ತಿ sort + merge ಮಾಡೋದು.
  →  ಆದರೆ ಇದು slow ಯಾಕೆ? → Input ಆಗ್ಲೇ sorted ಇದೆ ಅನ್ನೋ information
     waste ಮಾಡ್ತೀವಿ — ಮತ್ತೆ sort ಮಾಡೋದ್ರಿಂದ O(n log n), ಆದ್ರೆ single
     pass ಇಂದ O(n) ಗೆ ಇಳಿಸ್ಬೋದು.

  ಹಂತ 3 — Better way ಹೇಗೆ ಯೋಚಿಸುವುದು? (Optimization thought)
  →  "Input sorted ಇರೋದ್ರಿಂದ, 3 clean zones ಇರುತ್ತೆ: (1) newInterval
     ಗಿಂತ ಪೂರ್ತಿ ಮುಂಚೆ ಇರೋ intervals (as-is add ಮಾಡು), (2)
     newInterval ಜೊತೆ overlap ಆಗೋ intervals (merge ಮಾಡು), (3)
     newInterval ಗಿಂತ ಪೂರ್ತಿ ನಂತರ ಇರೋ intervals (as-is add ಮಾಡು)."
  →  ಅಹಾ moment: ಈ 3 zones ಅನ್ನ single linear pass ನಲ್ಲೇ handle
     ಮಾಡ್ಬಹುದು! Zone 1: interval.end < newInterval.start ಆಗಿರೋ
     ತನಕ as-is add ಮಾಡು. Zone 2: interval.start <= newInterval.end
     ಆಗಿರೋ ತನಕ, newInterval ಅನ್ನ min/max ಇಂದ grow ಮಾಡ್ತಾ ಹೋಗು
     (merge). Zone 3: ಉಳಿದೆಲ್ಲಾ as-is add ಮಾಡು.
  →  ಇದರಿಂದ ನಾವು Greedy → 3-Zone Linear Scan (No Re-sort) use ಮಾಡಬಹುದು!

  ಹಂತ 4 — Technique ಯಾಕೆ ಇಲ್ಲಿ ಕೆಲಸ ಮಾಡುತ್ತೆ?
  →  Input ಆಗ್ಲೇ sorted ಇರೋದ್ರಿಂದ, "before/overlapping/after" zones
     ಯಾವಾಗ್ಲೂ ಈ order ನಲ್ಲೇ ಬರುತ್ತೆ — random access ಬೇಡ.
  →  Overlapping zone ಒಳಗೆ, newInterval ನ start/end ಅನ್ನ progressively
     grow ಮಾಡ್ತಾ ಹೋದ್ರೆ, ಎಷ್ಟೇ intervals overlap ಆಗ್ಲಿ ಒಂದೇ merged
     interval ಸಿಗುತ್ತೆ.
  →  Sort ಮತ್ತೆ ಮಾಡೋ ಅಗತ್ಯ ಇಲ್ಲದೇ, ಸ್ವತಃ single O(n) pass ಸಾಕು.

  💡 Interview ನಲ್ಲಿ ಹೇಗೆ ಮಾತಾಡಬೇಕು (Think out loud):
  →  "I could append the new interval and re-run a full merge-sort
      like Merge Intervals — O(n log n), but that wastes the fact
      that the input is already sorted."
  →  "Since it's sorted, I can process it in three clean phases:
      intervals entirely before the new one, intervals that overlap
      with it, and intervals entirely after it."
  →  "In the overlapping phase, I keep growing the new interval's
      bounds using min/max until nothing more overlaps — that gives
      the merged interval in one pass."

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🏷️ SECTION 3 — TECHNIQUE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Primary   : Greedy → 3-Zone Linear Scan (No Re-sort)
  Secondary : None

  WHY this technique?
  → Input is guaranteed pre-sorted and non-overlapping, so re-sorting
    (like plain Merge Intervals would) wastes that guarantee
  → Sorted input means overlap with newInterval always forms one
    contiguous block — no scattered overlaps to search for
  → A single left-to-right pass with three phases (before / overlap /
    after) handles any number of overlapping intervals in O(n)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 💡 SECTION 4 — INTUITION (How to think — English)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Key observation: because the input is sorted and non-overlapping,
  every interval that overlaps with newInterval must be contiguous in
  the list. So we can walk through once, copy anything strictly
  before the new interval untouched, absorb everything that overlaps
  by growing the new interval's bounds, then copy everything strictly
  after untouched.

  The journey from brute to optimal:
    Brute thought   →  append newInterval, sort everything, then
                        merge like a fresh Merge Intervals problem
    Problem with it →  O(n log n), throws away the "already sorted"
                        guarantee entirely
    Better question →  "can I exploit the sorted order to avoid
                        re-sorting altogether?"
    Insight         →  overlapping intervals form one contiguous
                        block in sorted order — grow newInterval
                        through that block in a single pass
    Optimal         →  3-phase linear scan, O(n) time, no sort needed

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🐢 SECTION 5 — APPROACH 1 — BRUTE FORCE (Append + Full Re-sort + Merge)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    Append newInterval to the list, sort everything by start, then
    run the standard Merge Intervals linear merge pass over the
    whole sorted list.

  Pseudocode:
    step 1: all_intervals = intervals + [newInterval]
    step 2: sort all_intervals by start
    step 3: merged = [] ; for each interval: merge into merged like #56
    step 4: return merged

  Time  : O(n log n)  →  Why: dominated by re-sorting the whole list
  Space : O(n)  →  Why: result list, plus sort overhead

  ಇದು ಯಾಕೆ ಸಾಕಾಗಲ್ಲ? (Why is this not enough?)
    → Input ಆಗ್ಲೇ sorted ಇದೆ ಅನ್ನೋದನ್ನ ಸಂಪೂರ್ಣ ignore ಮಾಡ್ತೀವಿ —
      3-zone linear scan ಇಂದ sort ಇಲ್ಲದೆ O(n) ಗೆ ಇಳಿಸ್ಬೋದು.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🚶 SECTION 6 — APPROACH 2 — BETTER (skip — brute jumps straight to optimal)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  ಇಲ್ಲಿ intermediate approach ಇಲ್ಲ — append+resort brute force ಇಂದ
  ನೇರವಾಗಿ 3-zone linear scan optimal ಗೆ ಹೋಗಬಹುದು.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🚀 SECTION 7 — APPROACH 3 — OPTIMAL   (3-Zone Linear Scan, No Re-sort)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    Walk through intervals once. Phase 1: while the current
    interval's end is strictly before newInterval's start, copy it
    as-is. Phase 2: while the current interval's start is <=
    newInterval's end (overlap), grow newInterval to
    [min(starts), max(ends)]. Append the (possibly grown)
    newInterval. Phase 3: copy all remaining intervals as-is.

  Key steps:
    1. result = [], i = 0, n = len(intervals)
    2. while i < n and intervals[i][1] < newInterval[0]: result.append(intervals[i]); i += 1
    3. while i < n and intervals[i][0] <= newInterval[1]:
         newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
         i += 1
    4. result.append(newInterval)
    5. while i < n: result.append(intervals[i]); i += 1
    6. return result

  ಕನ್ನಡದಲ್ಲಿ ಒಂದು ಸಲ ಹೇಳಿ (Say it once in Kanglish so it sticks):
    → "ಮೊದಲು newInterval ಗಿಂತ ಪೂರ್ತಿ ಮುಂಚೆ ಇರೋ intervals ಅನ್ನ as-is
        add ಮಾಡು. ಆಮೇಲೆ overlap ಆಗೋ intervals ಸಿಕ್ಕಾಗ, newInterval
        ಅನ್ನ min-start, max-end ಇಂದ grow ಮಾಡ್ತಾ ಹೋಗು. ಆ grown
        newInterval ಅನ್ನ add ಮಾಡು. ಕೊನೆಗೆ ಉಳಿದೆಲ್ಲಾ intervals ಅನ್ನ
        as-is add ಮಾಡು!"

  Time  : O(n)  →  Why: single linear pass, each interval visited once
  Space : O(n)  →  Why: result list holds all output intervals

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🔍 SECTION 8 — DRY RUN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Input: intervals = [[1,3],[6,9]], newInterval = [2,5]

  Phase 1: intervals[0]=[1,3], end=3 < newInterval.start=2? No (3>=2)
           → phase 1 adds nothing, i stays 0
  Phase 2: intervals[0]=[1,3], start=1 <= newInterval.end=5? Yes →
           newInterval = [min(2,1), max(5,3)] = [1,5]; i=1
           intervals[1]=[6,9], start=6 <= newInterval.end=5? No → stop
  Append newInterval=[1,5] → result=[[1,5]]
  Phase 3: intervals[1]=[6,9] remains → result=[[1,5],[6,9]]

  Output: [[1,5],[6,9]]   matches expected

  ಇನ್ನೊಂದು example — tricky case (overlaps several intervals at once):
  Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]

  Phase 1: [1,2], end=2 < 4? Yes → add [1,2], i=1
           [3,5], end=5 < 4? No → stop
  Phase 2: [3,5], start=3 <= 8? Yes → newInterval=[min(4,3),max(8,5)]=[3,8]; i=2
           [6,7], start=6 <= 8? Yes → newInterval=[min(3,6),max(8,7)]=[3,8]; i=3
           [8,10], start=8 <= 8? Yes → newInterval=[min(3,8),max(8,10)]=[3,10]; i=4
           [12,16], start=12 <= 10? No → stop
  Append newInterval=[3,10] → result=[[1,2],[3,10]]
  Phase 3: [12,16] remains → result=[[1,2],[3,10],[12,16]]

  Output: [[1,2],[3,10],[12,16]]   matches expected

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 ⚠️ SECTION 9 — EDGE CASES — ಇವನ್ನ ಮರೆಯಬೇಡ!
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  ✓ Empty intervals list?      →  phases 1 and 3 add nothing, phase 2
                                   never triggers, result = [newInterval]
  ✓ newInterval before everything? →  phase 1 adds nothing, phase 2
                                   possibly merges with the first
                                   interval, rest copied in phase 3
  ✓ newInterval after everything? →  phase 1 copies all of them,
                                   phase 2 does nothing, newInterval
                                   appended alone at the end
  ✓ newInterval overlaps nothing (fits in a gap)? →  phase 2 never
                                   triggers, newInterval inserted as-is
                                   between phase 1 and phase 3 output
  ✓ newInterval swallows the ENTIRE list? →  phase 2 absorbs every
                                   interval, result is just [newInterval]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📊 SECTION 10 — COMPLEXITY SUMMARY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                Time         Space
  Brute Force   O(n log n)   O(n)
  Optimal       O(n)         O(n)    ← use this 

  Time ಯಾಕೆ ಅಷ್ಟು?  → ಒಂದೇ linear pass ನಲ್ಲಿ ಪ್ರತಿ interval ಒಂದೇ ಸಲ
                        visit ಆಗುತ್ತೆ, sort ಬೇಡ.
  Space ಯಾಕೆ ಅಷ್ಟು? → result list ಇಡೋಕೆ O(n).

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🎯 SECTION 11 — PATTERN LEARNED — ಇದರಿಂದ ಕಲಿತದ್ದು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Pattern Name: Greedy Intervals — 3-Zone Scan on Pre-sorted Input

  ಈ pattern ಯಾವಾಗ use ಮಾಡಬೇಕು?
  → Input ಆಗ್ಲೇ sorted ಇದೆ ಅಂತ ಗ್ಯಾರಂಟಿ ಇದ್ದಾಗ (re-sort ಮಾಡೋ ಅಗತ್ಯ
    ಇಲ್ಲ ಅಂತ ಗುರುತಿಸಿದಾಗ)
  → "before / overlapping / after" ಅಂತ problem ಅನ್ನ clean ಆಗಿ
    3 phases ಆಗಿ split ಮಾಡ್ಬಹುದು ಅಂತ ಗೊತ್ತಾದಾಗ
  → Single insertion ಒಂದೇ item ಗೆ ಬರೀ affect ಆಗುತ್ತೆ, ಪೂರ್ತಿ list
    resort ಮಾಡೋ ಅಗತ್ಯ ಇಲ್ಲ ಅಂತ ಇದ್ದಾಗ

  ಇದೇ pattern ಬೇರೆ problems ನಲ್ಲಿ ಕಾಣಿಸುತ್ತೆ:
  → Merge Intervals (#56) — same merge logic, but starts unsorted
  → My Calendar I/II/III — same "does this interval overlap existing ones" idea
  → Employee Free Time — same interval-merging family, harder input shape

  Next time ಇಂತಹ problem ಬಂದ್ರೆ ನಾನು ಮೊದಲು ಇದನ್ನ think ಮಾಡ್ತೇನೆ:
  → "Sorted intervals list ಗೆ ಒಂದೇ interval insert ಮಾಡ್ಬೇಕು ಅಂತ
      ಕೇಳಿದ ತಕ್ಷಣ, re-sort ಮಾಡ್ದೇ, before/overlap/after 3 zones
      ಆಗಿ single pass ನಲ್ಲಿ handle ಮಾಡು ಅಂತ ಮೊದಲು ಯೋಚಿಸು."

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🗣️ SECTION 12 — INTERVIEWALLI HEGE EXPLAIN MAADABEEKU
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  1. Understand:
     "I need to insert a new interval into an already-sorted,
      non-overlapping list, merging with anything it overlaps."

  2. Brute force:
     "I could append it and re-run a full sort-and-merge like Merge
      Intervals — O(n log n), but that ignores the fact the input is
      already sorted."

  3. Optimize:
     "Since the input is sorted, I can process it in three phases in
      one pass: intervals entirely before the new one (copy as-is),
      intervals that overlap (merge by growing min/max bounds), and
      intervals entirely after (copy as-is)."

  4. Code:
     "I will use three while-loops in sequence — before, overlapping,
      after — growing newInterval's bounds during the overlap phase
      and appending it once that phase ends."

  5. Complexity:
     "Time O(n) — a single linear pass, no sorting needed. Space
      O(n) — for the result list."

  ಮುಖ್ಯ: ಸುಮ್ಮನೆ ಕೂತು code ಬರೆಯಬೇಡ!
         Interviewer ಗೆ ನಿನ್ನ thinking process ಕಾಣಬೇಕು.
"""


# ═══════════════════════════════════════════════════════════════════
# BRUTE FORCE — O(n log n) Time | O(n) Space  (Append + Full Re-sort + Merge)
# ═══════════════════════════════════════════════════════════════════
def insert_brute(intervals, new_interval):
    """ಇದು ಮೊದಲ ಆಲೋಚನೆ — newInterval append ಮಾಡಿ ಪೂರ್ತಿ sort+merge ಮಾಡೋದು"""
    all_intervals = sorted(intervals + [new_interval], key=lambda x: x[0])
    if not all_intervals:
        return []

    merged = [list(all_intervals[0])]
    for start, end in all_intervals[1:]:
        if start <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], end)
        else:
            merged.append([start, end])

    return merged


# ═══════════════════════════════════════════════════════════════════
# OPTIMAL — O(n) Time | O(n) Space  (3-Zone Linear Scan, No Re-sort)
# ═══════════════════════════════════════════════════════════════════
def insert(intervals, new_interval):
    """ಇದು final answer — before/overlap/after 3 zones ಆಗಿ single pass ನಲ್ಲಿ insert ಮಾಡು"""
    result = []
    i, n = 0, len(intervals)
    new_start, new_end = new_interval

    # Phase 1 — intervals entirely before newInterval
    while i < n and intervals[i][1] < new_start:
        result.append(intervals[i])
        i += 1

    # Phase 2 — intervals overlapping newInterval, grow its bounds
    while i < n and intervals[i][0] <= new_end:
        new_start = min(new_start, intervals[i][0])
        new_end = max(new_end, intervals[i][1])
        i += 1
    result.append([new_start, new_end])

    # Phase 3 — intervals entirely after newInterval
    while i < n:
        result.append(intervals[i])
        i += 1

    return result


# ═══════════════════════════════════════════════════════════════════
# TEST CASES
# ═══════════════════════════════════════════════════════════════════
if __name__ == "__main__":
    import sys
    sys.stdout.reconfigure(encoding="utf-8")   # Windows cp1252 can't print emoji otherwise

    # Test 1 — Basic example
    assert insert([[1, 3], [6, 9]], [2, 5]) == [[1, 5], [6, 9]]

    # Test 2 — Edge case: empty intervals list
    assert insert([], [5, 7]) == [[5, 7]]

    # Test 3 — Edge case: newInterval overlaps nothing (fits in a gap)
    assert insert([[1, 2], [8, 9]], [4, 5]) == [[1, 2], [4, 5], [8, 9]]

    # Test 4 — Tricky: overlaps several intervals at once
    assert insert([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]) == \
        [[1, 2], [3, 10], [12, 16]]

    print("All tests passed! ")
