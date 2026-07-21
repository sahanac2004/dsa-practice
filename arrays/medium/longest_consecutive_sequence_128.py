"""
╔══════════════════════════════════════════════════════════════════╗
║  LONGEST CONSECUTIVE SEQUENCE                                     ║
║  LeetCode #128  |  Difficulty: Medium  |  Topic: Arrays / HashSet ║
║  Link: https://leetcode.com/problems/longest-consecutive-sequence/║
╚══════════════════════════════════════════════════════════════════╝

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📘 SECTION 1 — PROBLEM UNDERSTANDING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Given an unsorted array of integers, find the length of the
  longest run of CONSECUTIVE integers (like 3,4,5,6) that appear
  somewhere in the array — they don't need to be adjacent in the
  array itself. Must run in O(n), so sorting is technically off-limits
  for the optimal solution.

  Input : nums = [100, 4, 200, 1, 3, 2]
  Output: 4

  Example 1 — basic:
    Input : nums = [100, 4, 200, 1, 3, 2]
    Output: 4
    Why?  : the consecutive run 1,2,3,4 exists (in any order in the
             array), and it's the longest such run — length 4

  Example 2 — slightly tricky (duplicates present):
    Input : nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
    Output: 9
    Why?  : 0 through 8 is a consecutive run of length 9; the
             duplicate 0 doesn't extend or break the sequence

  Constraints:
    - 0 <= nums.length <= 10^5
    - -10^9 <= nums[i] <= 10^9
    - Must achieve O(n) time complexity

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🧠 SECTION 2 — KANGLISH THINKING — ಹೇಗೆ ಯೋಚಿಸಬೇಕು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  ಮೊದಲು problem odidaga ನಮ್ಮ brain ಏನು think ಮಾಡಬೇಕು:

  ಹಂತ 1 — Problem ಅರ್ಥ ಮಾಡಿಕೊಳ್ಳಿ (What are they asking?)
  ┌─────────────────────────────────────────────────────────┐
  │  Input ಏನು ಕೊಡ್ತಾರೆ?  →  unsorted integer array           │
  │  Output ಏನು ಬೇಕು?     →  longest consecutive run ನ length │
  │                          (array order matter ಆಗಲ್ಲ)        │
  │  Constraints ಏನಿದೆ?   →  n=10^5, O(n) expect (sort ಮಾಡಿದ್ರೆ│
  │                          O(n log n) ಆಗುತ್ತೆ — ಸಾಲಲ್ಲ)      │
  └─────────────────────────────────────────────────────────┘

  ಹಂತ 2 — ನನಗೆ ಗೊತ್ತಿರೋ simple way ಏನು? (Brute force thought)
  →  Array ಅನ್ನ sort ಮಾಡಿ, ಆಮೇಲೆ consecutive runs ಅನ್ನ linear ಆಗಿ
     ಎಣಿಸೋದು.
  →  ಆದರೆ ಇದು slow ಯಾಕೆ? → Sort ಮಾಡೋಕೆ O(n log n) — problem
     explicitly O(n) ಕೇಳ್ತಾ ಇದೆ.

  ಹಂತ 3 — Better way ಹೇಗೆ ಯೋಚಿಸುವುದು? (Optimization thought)
  →  "Sort ಇಲ್ಲದೆ 'ಈ number ಗೆ ಮುಂದೆ/ಹಿಂದೆ ಇರೋ number ಇದೆಯಾ' ಅಂತ
     O(1) ನಲ್ಲಿ ಗೊತ್ತಾಗ್ಬೇಕಾದ್ರೆ, HashSet ಇಂದ membership check
     ಮಾಡ್ಬೋದಲ್ವಾ?"
  →  ಅಹಾ moment: ಪ್ರತಿ number ಗೂ sequence extend ಮಾಡ್ತಾ ಹೋದ್ರೆ
     O(n²) ಆಗ್ಬೋದು (repeat ಆಗುತ್ತೆ) — ಆದ್ರೆ ನಾವು ಒಂದೇ sequence ಗೆ
     ಒಂದೇ ಸಲ start ಮಾಡಿದ್ರೆ ಸಾಕು! ಒಂದು number `n` ಗೆ, `n-1` set ನಲ್ಲಿ
     ಇಲ್ಲಾಂದ್ರೆ ಮಾತ್ರ ಅದು ಒಂದು sequence ನ START — ಆಗ ಮಾತ್ರ n, n+1,
     n+2... count ಮಾಡ್ತಾ ಹೋಗು.
  →  ಇದರಿಂದ ನಾವು HashSet + "Start of Sequence Detection" use ಮಾಡಬಹುದು!

  ಹಂತ 4 — Technique ಯಾಕೆ ಇಲ್ಲಿ ಕೆಲಸ ಮಾಡುತ್ತೆ?
  →  HashSet membership check O(1) average — n-1, n+1 ಇದೆಯಾ ಅಂತ
     instant ಆಗಿ ಗೊತ್ತಾಗುತ್ತೆ, sort ಬೇಡ.
  →  "n-1 set ನಲ್ಲಿ ಇಲ್ಲ" ಅನ್ನೋ check ಇಂದ ಪ್ರತಿ sequence ಅನ್ನ ಒಂದೇ
     ಸಲ (ಅದರ start point ಇಂದ ಮಾತ್ರ) traverse ಮಾಡ್ತೀವಿ — total work
     ಎಲ್ಲಾ elements ಗೂ ಸೇರಿ O(n) ಆಗುತ್ತೆ (amortized).
  →  Array order matter ಆಗಲ್ಲ ಅನ್ನೋದ್ರಿಂದ, set ಒಂದೇ ಸಾಕು — index
     tracking ಬೇಡ.

  💡 Interview ನಲ್ಲಿ ಹೇಗೆ ಮಾತಾಡಬೇಕು (Think out loud):
  →  "The obvious approach is to sort and scan — O(n log n), but the
      problem explicitly asks for O(n)."
  →  "I can put everything in a hash set for O(1) lookups, then for
      each number check if it's the START of a sequence — meaning
      num - 1 is not in the set."
  →  "Only sequence starts trigger a counting walk forward, so even
      though it looks like nested loops, every number is visited at
      most twice total — that keeps it O(n)."

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🏷️ SECTION 3 — TECHNIQUE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Primary   : HashSet → Start-of-Sequence Detection
  Secondary : None

  WHY this technique?
  → O(n) is required, ruling out sorting (O(n log n))
  → HashSet gives O(1) average membership checks for "does n-1 /
    n+1 exist"
  → Only starting from true sequence starts (num-1 not in set) keeps
    the total work across all numbers linear, not quadratic

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 💡 SECTION 4 — INTUITION (How to think — English)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Key observation: if we only start "walking" a sequence from numbers
  that have no predecessor in the set (num - 1 not present), then
  every number in the array gets visited by the walk at most once
  across the whole algorithm — even though it looks like an O(n)
  outer loop with an O(n) inner while loop.

  The journey from brute to optimal:
    Brute thought   →  sort the array, scan for consecutive runs
    Problem with it →  sorting costs O(n log n), problem wants O(n)
    Better question →  "can I check neighbor existence in O(1) instead
                        of relying on sorted order?"
    Insight         →  a hashset gives O(1) lookups; only start
                        counting from true sequence starts to avoid
                        redundant work
    Optimal         →  build a set, for each num with no num-1 in the
                        set, count forward while num+1, num+2... exist

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🐢 SECTION 5 — APPROACH 1 — BRUTE FORCE (Sort + Scan)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    Sort the array, then walk through it once, tracking the length of
    the current consecutive run — resetting when the next value isn't
    exactly current+1 (skipping duplicates), and tracking the max.

  Pseudocode:
    step 1: if empty: return 0
    step 2: sort nums
    step 3: longest = current = 1
    step 4: for i in range(1, n):
    step 5:   if nums[i] == nums[i-1]: continue        # skip duplicate
    step 6:   elif nums[i] == nums[i-1] + 1: current += 1
    step 7:   else: current = 1
    step 8:   longest = max(longest, current)
    step 9: return longest

  Time  : O(n log n)  →  Why: dominated by the sort
  Space : O(1) or O(n)  →  Why: depends on sort implementation (in-place vs not)

  ಇದು ಯಾಕೆ ಸಾಕಾಗಲ್ಲ? (Why is this not enough?)
    → Problem explicitly O(n) ಕೇಳ್ತಾ ಇದೆ — sort ಇಂದ log n factor
      ಬರುತ್ತೆ, ಅದನ್ನ ತಪ್ಪಿಸ್ಬೋದು HashSet trick ಇಂದ.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🚶 SECTION 6 — APPROACH 2 — BETTER (skip — brute jumps straight to optimal)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  ಇಲ್ಲಿ intermediate approach ಇಲ್ಲ — sort-based brute force ಇಂದ
  ನೇರವಾಗಿ HashSet-based O(n) optimal ಗೆ ಹೋಗಬಹುದು.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🚀 SECTION 7 — APPROACH 3 — OPTIMAL   (HashSet — Start-of-Sequence Detection)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    Put all numbers into a set (removes duplicates, O(1) lookups).
    For each number, only bother counting a sequence if it's a TRUE
    start — meaning num - 1 is NOT in the set. From there, keep
    checking num+1, num+2, ... as long as they exist in the set,
    counting the length. Track the maximum length seen.

  Key steps:
    1. num_set = set(nums)
    2. longest = 0
    3. for num in num_set:
         if (num - 1) not in num_set:          # true sequence start
             length = 1
             while (num + length) in num_set: length += 1
             longest = max(longest, length)
    4. Return longest

  ಕನ್ನಡದಲ್ಲಿ ಒಂದು ಸಲ ಹೇಳಿ (Say it once in Kanglish so it sticks):
    → "ಎಲ್ಲಾ numbers ಅನ್ನ set ಗೆ ಹಾಕು. ಪ್ರತಿ number ಗೂ, (number-1) set
        ನಲ್ಲಿ ಇಲ್ಲಾಂದ್ರೆ ಮಾತ್ರ ಇದು sequence ನ START ಅಂತ — ಅಲ್ಲಿಂದ
        number+1, number+2 ಅಂತ set ನಲ್ಲಿ ಇರೋ ತನಕ count ಮಾಡ್ತಾ ಹೋಗು,
        longest track ಮಾಡು!"

  Time  : O(n)  →  Why: amortized — each number is part of exactly
                    one sequence walk across the whole run
  Space : O(n)  →  Why: hashset stores up to n unique numbers

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🔍 SECTION 8 — DRY RUN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Input: nums = [100, 4, 200, 1, 3, 2]
  num_set = {100, 4, 200, 1, 3, 2}

  num=100 → 99 not in set → START. length=1; 101 not in set → longest=1
  num=4   → 3 IS in set → skip (not a start)
  num=200 → 199 not in set → START. length=1; 201 not in set → longest stays 1
  num=1   → 0 not in set → START. length=1;
            2 in set→length=2; 3 in set→length=3; 4 in set→length=4;
            5 not in set → stop. longest=max(1,4)=4
  num=3   → 2 IS in set → skip
  num=2   → 1 IS in set → skip

  Output: 4    matches expected (sequence 1,2,3,4)

  ಇನ್ನೊಂದು example — tricky case (duplicates):
  Input: nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
  num_set = {0,1,2,3,4,5,6,7,8}  (duplicate 0 collapses automatically)

  num=0 → -1 not in set → START. walk: 1,2,3,4,5,6,7,8 all in set →
          length=9. longest=9
  (every other num like 3,7,2,5,8,4,6,1 has num-1 in set → all skipped)

  Output: 9    matches expected

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 ⚠️ SECTION 9 — EDGE CASES — ಇವನ್ನ ಮರೆಯಬೇಡ!
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  ✓ Empty array?              →  num_set is empty, loop never runs,
                                  returns 0
  ✓ Single element?           →  that element is its own start,
                                  length=1, returns 1
  ✓ All same elements?        →  set collapses to one value, longest=1
  ✓ Negative numbers?         →  works identically, no special casing
                                  (n-1, n+1 arithmetic is sign-agnostic)
  ✓ Duplicates scattered around? →  set() dedupes automatically, no
                                  double-counting or double-walking

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📊 SECTION 10 — COMPLEXITY SUMMARY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                Time         Space
  Brute Force   O(n log n)   O(1)/O(n) (sort-dependent)
  Optimal       O(n)         O(n)    ← use this  

  Time ಯಾಕೆ ಅಷ್ಟು?  → ಪ್ರತಿ number sequence walk ನಲ್ಲಿ ಒಂದೇ ಸಲ visit
                        ಆಗುತ್ತೆ (start ಇಂದ ಮಾತ್ರ walk ಮಾಡೋದ್ರಿಂದ) —
                        amortized O(n).
  Space ಯಾಕೆ ಅಷ್ಟು? → ಎಲ್ಲಾ unique numbers ಇಡೋಕೆ hashset ಬೇಕು.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🎯 SECTION 11 — PATTERN LEARNED — ಇದರಿಂದ ಕಲಿತದ್ದು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Pattern Name: HashSet — Only Walk From True Starts

  ಈ pattern ಯಾವಾಗ use ಮಾಡಬೇಕು?
  → "Longest run/sequence" ಕೇಳಿದಾಗ, ಆದ್ರೆ array order matter
    ಆಗ್ದೇ ಇದ್ದಾಗ (sorting cost avoid ಮಾಡ್ಬೇಕಾದಾಗ)
  → O(n) explicitly ಕೇಳ್ತಾ ಇದ್ದಾಗ, sorting-based approach ಸಾಲ್ದೇ
    ಇದ್ದಾಗ
  → "Redundant work ತಪ್ಪಿಸೋಕೆ ಒಂದೇ starting point ಇಂದ ಮಾತ್ರ walk
    ಮಾಡ್ಬೇಕು" ಅನ್ನೋ condition ಹಾಕ್ಬಹುದು ಅಂತ ಗೊತ್ತಾದಾಗ

  ಇದೇ pattern ಬೇರೆ problems ನಲ್ಲಿ ಕಾಣಿಸುತ್ತೆ:
  → Longest Consecutive Sequence variants on Trees/Graphs
  → Number of Islands / connected components (only visit unvisited starts)
  → Binary Tree Longest Consecutive Sequence — same "grow from start" idea

  Next time ಇಂತಹ problem ಬಂದ್ರೆ ನಾನು ಮೊದಲು ಇದನ್ನ think ಮಾಡ್ತೇನೆ:
  → "Longest consecutive/contiguous run ಕೇಳಿದ ತಕ್ಷಣ, sort ಮಾಡ್ದೇ,
      HashSet ಇಟ್ಕೊಂಡು 'predecessor ಇಲ್ಲದ start points' ಇಂದ ಮಾತ್ರ
      walk ಮಾಡು ಅಂತ ಮೊದಲು ಯೋಚಿಸು."

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🗣️ SECTION 12 — INTERVIEWALLI HEGE EXPLAIN MAADABEEKU
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  1. Understand:
     "I need the length of the longest run of consecutive integers
      present in the array, regardless of their order — and it must
      run in O(n)."

  2. Brute force:
     "Sort the array and scan for consecutive runs — O(n log n), but
      the problem explicitly wants O(n), so sorting is out."

  3. Optimize:
     "I put all numbers in a hash set for O(1) lookups. Then, instead
      of starting a walk from every number, I only start from numbers
      that have no predecessor (num-1) in the set — that guarantees
      each number is walked at most once overall."

  4. Code:
     "I will use a hashset plus a start-detection check, because it
      lets me avoid sorting while still visiting the total work in
      linear time."

  5. Complexity:
     "Time O(n) amortized — every number is part of exactly one
      sequence walk. Space O(n) for the hashset."

  ಮುಖ್ಯ: ಸುಮ್ಮನೆ ಕೂತು code ಬರೆಯಬೇಡ!
         Interviewer ಗೆ ನಿನ್ನ thinking process ಕಾಣಬೇಕು.
"""


# ═══════════════════════════════════════════════════════════════════
# BRUTE FORCE — O(n log n) Time | O(1)/O(n) Space  (Sort + Scan)
# ═══════════════════════════════════════════════════════════════════
def longest_consecutive_brute(nums):
    """ಇದು ಮೊದಲ ಆಲೋಚನೆ — sort ಮಾಡಿ consecutive run ಎಣಿಸೋದು"""
    if not nums:
        return 0

    nums_sorted = sorted(nums)
    longest = current = 1

    for i in range(1, len(nums_sorted)):
        if nums_sorted[i] == nums_sorted[i - 1]:
            continue  # skip duplicate
        elif nums_sorted[i] == nums_sorted[i - 1] + 1:
            current += 1
        else:
            current = 1
        longest = max(longest, current)

    return longest


# ═══════════════════════════════════════════════════════════════════
# OPTIMAL — O(n) Time | O(n) Space  (HashSet — Start-of-Sequence Detection)
# ═══════════════════════════════════════════════════════════════════
def longest_consecutive(nums):
    """ಇದು final answer — predecessor ಇಲ್ಲದ start points ಇಂದ ಮಾತ್ರ walk ಮಾಡು"""
    num_set = set(nums)
    longest = 0

    for num in num_set:
        if (num - 1) not in num_set:  # true sequence start
            length = 1
            while (num + length) in num_set:
                length += 1
            longest = max(longest, length)

    return longest


# ═══════════════════════════════════════════════════════════════════
# TEST CASES
# ═══════════════════════════════════════════════════════════════════
if __name__ == "__main__":
    import sys
    sys.stdout.reconfigure(encoding="utf-8")   # Windows cp1252 can't print emoji otherwise

    # Test 1 — Basic example
    assert longest_consecutive([100, 4, 200, 1, 3, 2]) == 4

    # Test 2 — Edge case: empty array
    assert longest_consecutive([]) == 0

    # Test 3 — Edge case: all same elements
    assert longest_consecutive([5, 5, 5, 5]) == 1

    # Test 4 — Tricky: duplicates mixed into a long run
    assert longest_consecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]) == 9

    print("All tests passed! ")
