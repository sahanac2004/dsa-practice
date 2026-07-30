"""
╔══════════════════════════════════════════════════════════════════╗
║  MAJORITY ELEMENT II                                                ║
║  LeetCode #229  |  Difficulty: Medium  |  Topic: Arrays             ║
║  Link: https://leetcode.com/problems/majority-element-ii/           ║
╚══════════════════════════════════════════════════════════════════╝

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📘 SECTION 1 — PROBLEM UNDERSTANDING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Given an array of size n, return all elements that appear MORE than
  ⌊n/3⌋ times. Unlike the classic Majority Element (>n/2, guaranteed
  exactly one answer), here there can be at most TWO such elements —
  and there might be zero, one, or two of them.

  Input : nums = [3, 2, 3]
  Output: [3]

  Example 1 — basic:
    Input : nums = [3, 2, 3]
    Output: [3]
    Why?  : n=3, n/3=1, "3" appears twice (>1), "2" appears once (not >1)

  Example 2 — slightly tricky (two valid answers):
    Input : nums = [1, 1, 1, 3, 3, 2, 2, 2]
    Output: [1, 2]
    Why?  : n=8, n/3=2 (floor), "1" appears 3 times (>2), "2" appears
             3 times (>2), "3" appears only 2 times (not >2)

  Constraints:
    - 1 <= nums.length <= 5 * 10^4
    - -10^9 <= nums[i] <= 10^9

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🧠 SECTION 2 — KANGLISH THINKING — ಹೇಗೆ ಯೋಚಿಸಬೇಕು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  ಮೊದಲು problem odidaga ನಮ್ಮ brain ಏನು think ಮಾಡಬೇಕು:

  ಹಂತ 1 — Problem ಅರ್ಥ ಮಾಡಿಕೊಳ್ಳಿ (What are they asking?)
  ┌─────────────────────────────────────────────────────────┐
  │  Input ಏನು ಕೊಡ್ತಾರೆ?  →  ಒಂದು array of numbers          │
  │  Output ಏನು ಬೇಕು?     →  n/3 ಗಿಂತ ಜಾಸ್ತಿ times appear    │
  │                          ಆಗೋ ಎಲ್ಲಾ elements (0, 1 ಅಥವಾ 2) │
  │  Constraints ಏನಿದೆ?   →  n<=5*10^4, at most 2 answers    │
  │                          ಇರೋಕೆ ಸಾಧ್ಯ (pigeonhole)        │
  └─────────────────────────────────────────────────────────┘

  ಹಂತ 2 — ನನಗೆ ಗೊತ್ತಿರೋ simple way ಏನು? (Brute force thought)
  →  ಪ್ರತಿ unique element ಗೂ, ಇಡೀ array ಮತ್ತೊಮ್ಮೆ traverse ಮಾಡಿ count
     ಮಾಡೋದು, count > n/3 ಆದ್ರೆ ಸೇರಿಸೋದು.
  →  ಆದರೆ ಇದು slow ಯಾಕೆ? → O(n²) — ಪ್ರತಿ element ಗೂ ಮತ್ತೆ full scan.

  ಹಂತ 3 — Better way ಹೇಗೆ ಯೋಚಿಸುವುದು? (Optimization thought)
  →  ಮೊದಲು regular Majority Element (n/2) problem ನೆನಪಿಸ್ಕೊಂಡ್ರೆ —
     ಅಲ್ಲಿ Boyer-Moore voting: ಒಂದು candidate + count ಇಟ್ಕೊಂಡು, ಸೇಮ್
     element ಸಿಕ್ಕಿದ್ರೆ count++, ಬೇರೆ element ಸಿಕ್ಕಿದ್ರೆ count--,
     count=0 ಆದ್ರೆ candidate ಬದಲಾಯಿಸೋದು.
  →  ಅಹಾ moment: n/3 ಗೆ, at most TWO elements ಮಾತ್ರ ಆ threshold cross
     ಮಾಡೋಕೆ ಸಾಧ್ಯ (pigeonhole principle — 3 elements ಎಲ್ಲಾ n/3+ ಗಿಂತ
     ಜಾಸ್ತಿ ಇದ್ರೆ total count n ಗಿಂತ ಜಾಸ್ತಿ ಆಗುತ್ತೆ, impossible)! ಆದ್ದರಿಂದ
     Boyer-Moore ಅನ್ನ TWO candidates ಜೊತೆ generalize ಮಾಡಬಹುದು.
  →  ಇದರಿಂದ ನಾವು Boyer-Moore Voting (Extended — 2 Candidates) use
     ಮಾಡಬಹುದು!

  ಹಂತ 4 — Technique ಯಾಕೆ ಇಲ್ಲಿ ಕೆಲಸ ಮಾಡುತ್ತೆ?
  →  Pigeonhole principle: n/3 ಗಿಂತ ಜಾಸ್ತಿ appear ಆಗೋ 3 ಬೇರೆ elements
     ಇರೋಕೆ ಸಾಧ್ಯ ಇಲ್ಲ (3*(n/3+1) > n), ಆದ್ದರಿಂದ answer ಗೆ at most 2
     candidates ಸಾಕು.
  →  Voting ಆಟ ಇಂದ, ನಿಜವಾದ majority (>n/3) elements ಯಾವಾಗ್ಲೂ ಕೊನೆಗೆ
     ಒಂದು candidate slot ನಲ್ಲಿ survive ಆಗ್ತಾವೆ — ಆದ್ರೆ verify ಮಾಡೋದು
     ಕಡ್ಡಾಯ (candidate ಆಗಿದ್ರೂ ನಿಜವಾದ majority ಆಗಿರಬೇಕು ಅಂತ ಇಲ್ಲ).
  →  ಎರಡು separate (candidate, count) pairs track ಮಾಡಿ, final ಆಗಿ
     ಒಂದೇ additional pass ನಲ್ಲಿ verify ಮಾಡಿದ್ರೆ O(n) ನಲ್ಲಿ ಸಿಗುತ್ತೆ.

  💡 Interview ನಲ್ಲಿ ಹೇಗೆ ಮಾತಾಡಬೇಕು (Think out loud):
  →  "The naive way counts every unique element separately —
      O(n²), too slow for n up to 5*10^4."
  →  "By the pigeonhole principle, at most 2 elements can appear more
      than n/3 times, so I only need to track 2 candidates instead of
      one like in the classic Majority Element problem."
  →  "I'll extend Boyer-Moore voting to 2 candidates and 2 counters,
      then verify both candidates with one more pass since being a
      surviving candidate doesn't guarantee actually crossing n/3."

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🏷️ SECTION 3 — TECHNIQUE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Primary   : Boyer-Moore Voting (Extended to 2 Candidates)
  Secondary : Pigeonhole Principle (bounds the answer to at most 2)

  WHY this technique?
  → "More than n/3 times" combined with pigeonhole guarantees at most
    2 possible answers, so exactly 2 voting candidates suffice
  → Boyer-Moore voting finds candidates in O(n) time, O(1) space —
    no hashmap needed
  → A final verification pass is required since surviving the voting
    round doesn't guarantee the >n/3 condition, only narrows candidates

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 💡 SECTION 4 — INTUITION (How to think — English)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Key observation: it's mathematically impossible for 3 distinct
  elements to each appear more than n/3 times (that would need more
  than n total elements). So at most 2 answers can exist, and Boyer-
  Moore voting generalizes cleanly: keep two (candidate, count) slots,
  vote for/against them as you scan, and swap in a new candidate only
  when a counter hits zero. A verification pass at the end confirms
  which surviving candidates actually cross the n/3 threshold.

  The journey from brute to optimal:
    Brute thought   →  count occurrences of every unique element
    Problem with it →  O(n²), a full rescan per distinct element
    Better question →  "how did majority element (n/2) avoid rescanning
                        with just one candidate — can I use two?"
    Insight         →  pigeonhole caps the answer at 2 elements, so
                        Boyer-Moore extends naturally to 2 candidates
    Optimal         →  two-candidate voting pass + verification pass,
                        O(n) time, O(1) space

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🐢 SECTION 5 — APPROACH 1 — BRUTE FORCE (Count Every Unique Element)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    For each distinct value in nums, scan the whole array counting its
    occurrences; keep it if the count exceeds n/3.

  Pseudocode:
    step 1: result = []
    step 2: for val in set(nums):
    step 3:   if count of val in nums > n // 3: result.append(val)
    step 4: return result

  Time  : O(n²)  →  Why: up to n distinct values, each needing an O(n) count
  Space : O(n)   →  Why: set of distinct values

  ಇದು ಯಾಕೆ ಸಾಕಾಗಲ್ಲ? (Why is this not enough?)
    → n=5*10^4 ಆದ್ರೆ n² = 2.5*10^9 — TLE ಆಗತ್ತೆ.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🚶 SECTION 6 — APPROACH 2 — BETTER (HashMap Frequency Count)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    Build a frequency hashmap in one pass, then scan it for values
    whose count exceeds n/3.

  Time  : O(n)  →  one pass to build map, one pass over the map
  Space : O(n)  →  hashmap storing up to n distinct keys

  ಇನ್ನೂ better ಮಾಡಬಹುದಾ? → ಹೌದು — Boyer-Moore voting extended to 2
  candidates ಇಂದ, hashmap ಬೇಡ ಆಗುತ್ತೆ, O(1) space ಗೆ ಇಳಿಸ್ಬೋದು.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🚀 SECTION 7 — APPROACH 3 — OPTIMAL   (Extended Boyer-Moore Voting)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    Track two candidates and two counts. For each number: if it
    matches candidate1 or candidate2, bump that count; else if either
    count is 0, take over that slot; else decrement both counts. After
    the pass, verify both candidates with an actual count to confirm
    they truly exceed n/3 (a required step, not optional).

  Key steps:
    1. cand1, cand2, count1, count2 = None, None, 0, 0
    2. for num in nums:
         if cand1 == num: count1 += 1
         elif cand2 == num: count2 += 1
         elif count1 == 0: cand1, count1 = num, 1
         elif count2 == 0: cand2, count2 = num, 1
         else: count1 -= 1; count2 -= 1
    3. verify: recount actual occurrences of cand1 and cand2 in nums
    4. keep those whose actual count > n // 3

  ಕನ್ನಡದಲ್ಲಿ ಒಂದು ಸಲ ಹೇಳಿ (Say it once in Kanglish so it sticks):
    → "ಎರಡು candidate ಸ್ಲಾಟ್ ಇಟ್ಕೊಂಡು, ಸೇಮ್ candidate ಸಿಕ್ಕಿದ್ರೆ ಆ count
        ಜಾಸ್ತಿ ಮಾಡು, ಸ್ಲಾಟ್ empty (count=0) ಇದ್ರೆ ಆ number ಅನ್ನ candidate
        ಮಾಡು, ಇಲ್ಲಾಂದ್ರೆ ಎರಡೂ count ಕಡಿಮೆ ಮಾಡು. ಕೊನೆಗೆ ಎರಡೂ candidates
        ನ ನಿಜವಾದ count ಮತ್ತೆ ಎಣಿಸಿ n/3 ಗಿಂತ ಜಾಸ್ತಿ ಇರೋದನ್ನ ಮಾತ್ರ ಇಟ್ಕೋ!"

  Time  : O(n)  →  Why: one voting pass + one verification pass, both linear
  Space : O(1)  →  Why: only two candidates and two counters tracked

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🔍 SECTION 8 — DRY RUN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Input: nums = [1, 1, 1, 3, 3, 2, 2, 2]  (n=8, n//3=2)

  num=1: cand1=None → cand1=1, count1=1
  num=1: matches cand1 → count1=2
  num=1: matches cand1 → count1=3
  num=3: no match, cand2=None → cand2=3, count2=1
  num=3: matches cand2 → count2=2
  num=2: no match to cand1(1) or cand2(3), neither count is 0 →
         count1--, count2-- → count1=2, count2=1
  num=2: no match, neither count is 0 → count1--, count2-- →
         count1=1, count2=0
  num=2: no match to cand1(1), cand2 count is 0 → cand2=2, count2=1

  Candidates after voting: cand1=1, cand2=2
  Verify: actual count of 1 in nums = 3 (>2 ✓), actual count of 2 = 3 (>2 ✓)

  Output: [1, 2]   matches expected

  ಇನ್ನೊಂದು example — tricky case (no element exceeds n/3):
  Input: nums = [1, 2, 3]  (n=3, n//3=1)

  num=1: cand1=1, count1=1
  num=2: cand2=2, count2=1
  num=3: no match, both counts nonzero → count1--, count2-- → 0, 0

  Candidates: cand1=1, cand2=2
  Verify: actual count of 1 = 1 (not >1 ✗), actual count of 2 = 1 (not >1 ✗)

  Output: []   both candidates fail verification, correctly empty

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 ⚠️ SECTION 9 — EDGE CASES — ಇವನ್ನ ಮರೆಯಬೇಡ!
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  ✓ Single element array?        →  that element trivially appears
                                     100% of the time, always qualifies
  ✓ No element exceeds n/3?      →  verification pass filters both
                                     candidates out, returns []
  ✓ Exactly one qualifies?       →  the other candidate fails
                                     verification and is dropped
  ✓ Both cand1 and cand2 end up   →  duplicate check needed only if
    equal (rare edge in some         nums has < 2 distinct values;
    implementations)?                using None as sentinel avoids this
  ✓ All elements identical?      →  cand1 takes over immediately and
                                     count1 grows to n, easily passes

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📊 SECTION 10 — COMPLEXITY SUMMARY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                Time      Space
  Brute Force   O(n²)     O(n)
  Better        O(n)      O(n)   (hashmap)
  Optimal       O(n)      O(1)    ← use this

  Time ಯಾಕೆ ಅಷ್ಟು?  → voting pass ಒಂದೇ traverse, verification pass
                        ಇನ್ನೊಂದು traverse — total 2 passes, O(n).
  Space ಯಾಕೆ ಅಷ್ಟು? → ಬರೀ 2 candidates + 2 counters, ಬೇರೆ ಏನೂ ಬೇಡ.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🎯 SECTION 11 — PATTERN LEARNED — ಇದರಿಂದ ಕಲಿತದ್ದು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Pattern Name: Extended Boyer-Moore Voting (k-1 Candidates for >n/k)

  ಈ pattern ಯಾವಾಗ use ಮಾಡಬೇಕು?
  → "Appears more than n/k times" ಥರ threshold problem ಕೇಳಿದಾಗ
  → Pigeonhole principle ಇಂದ answer count bound ಆಗುತ್ತೆ ಅಂತ ಗುರುತಿಸಿ
    (>n/k ಆಗೋ elements at most k-1 ಇರೋಕೆ ಸಾಧ್ಯ)
  → O(1) space ಬೇಕಾದಾಗ, hashmap ಬದಲಿಗೆ voting

  ಇದೇ pattern ಬೇರೆ problems ನಲ್ಲಿ ಕಾಣಿಸುತ್ತೆ:
  → Majority Element (LC 169) — same idea, 1 candidate for >n/2
  → Majority Element (generalized >n/k) — extend to k-1 candidates
  → Find all elements appearing more than ⌊n/4⌋ times — same family

  Next time ಇಂತಹ problem ಬಂದ್ರೆ ನಾನು ಮೊದಲು ಇದನ್ನ think ಮಾಡ್ತೇನೆ:
  → "'>n/k times' ಅಂತ ಕಂಡ ತಕ್ಷಣ, pigeonhole ಇಂದ at most k-1 answers
      ಅಂತ ಲೆಕ್ಕ ಹಾಕಿ, Boyer-Moore ಅನ್ನ ಆ k-1 candidates ಗೆ extend ಮಾಡು
      ಅಂತ ಮೊದಲು ಯೋಚಿಸು — verify ಮಾಡೋದನ್ನ ಮರೆಯಬೇಡ!"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🗣️ SECTION 12 — INTERVIEWALLI HEGE EXPLAIN MAADABEEKU
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  1. Understand:
     "I need every element appearing strictly more than n/3 times —
      there can be zero, one, or two such elements."

  2. Brute force:
     "Count every distinct element by rescanning — O(n²), too slow;
      even a hashmap frequency count is O(n) time but O(n) space."

  3. Optimize:
     "By pigeonhole, at most 2 elements can exceed n/3, so I extend
      the classic Boyer-Moore voting (single candidate for >n/2) to
      track 2 candidates and 2 counters instead."

  4. Code:
     "Scan once, voting for/against the two candidate slots. Then
      scan again to verify each surviving candidate's actual count
      truly exceeds n/3, since surviving the vote doesn't guarantee it."

  5. Complexity:
     "Time O(n) — one voting pass plus one verification pass. Space
      O(1) — only two candidates and two counters, no hashmap."

  ಮುಖ್ಯ: ಸುಮ್ಮನೆ ಕೂತು code ಬರೆಯಬೇಡ — always think out loud!
         Interviewer ಗೆ ನಿನ್ನ thinking process ಕಾಣಬೇಕು.
"""


# ═══════════════════════════════════════════════════════════════════
# BRUTE FORCE — O(n^2) Time | O(n) Space  (Count Every Unique Element)
# ═══════════════════════════════════════════════════════════════════
def majority_element_ii_brute(nums):
    """ಇದು ಮೊದಲ ಆಲೋಚನೆ — ಪ್ರತಿ unique value ಗೂ full scan ಮಾಡಿ count ಮಾಡೋದು"""
    n = len(nums)
    result = []
    for val in set(nums):
        if nums.count(val) > n // 3:
            result.append(val)
    return result


# ═══════════════════════════════════════════════════════════════════
# OPTIMAL — O(n) Time | O(1) Space  (Extended Boyer-Moore Voting)
# ═══════════════════════════════════════════════════════════════════
def majority_element_ii(nums):
    """ಇದು final answer — 2 candidates ಜೊತೆ voting ಮಾಡಿ, ಆಮೇಲೆ verify ಮಾಡು"""
    cand1 = cand2 = None
    count1 = count2 = 0

    # Voting pass — narrow down to at most 2 candidates
    for num in nums:
        if cand1 == num:
            count1 += 1
        elif cand2 == num:
            count2 += 1
        elif count1 == 0:
            cand1, count1 = num, 1
        elif count2 == 0:
            cand2, count2 = num, 1
        else:
            count1 -= 1
            count2 -= 1

    # Verification pass — confirm candidates actually exceed n/3
    n = len(nums)
    result = []
    for cand in (cand1, cand2):
        if cand is not None and nums.count(cand) > n // 3:
            result.append(cand)
    return result


# ═══════════════════════════════════════════════════════════════════
# TEST CASES
# ═══════════════════════════════════════════════════════════════════
if __name__ == "__main__":
    import sys
    sys.stdout.reconfigure(encoding="utf-8")   # Windows cp1252 can't print emoji otherwise

    # Test 1 — Basic example
    assert majority_element_ii([3, 2, 3]) == [3]

    # Test 2 — Two valid answers
    assert sorted(majority_element_ii([1, 1, 1, 3, 3, 2, 2, 2])) == [1, 2]

    # Test 3 — Edge case: no element qualifies
    assert majority_element_ii([1, 2, 3]) == []

    # Test 4 — Edge case: single element
    assert majority_element_ii([5]) == [5]

    # Test 5 — Tricky: all elements identical
    assert majority_element_ii([7, 7, 7, 7]) == [7]

    print("All tests passed! ")
