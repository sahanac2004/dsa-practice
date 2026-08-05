"""
╔══════════════════════════════════════════════════════════════════╗
║  FIRST MISSING POSITIVE                                             ║
║  LeetCode #41  |  Difficulty: Hard  |  Topic: Arrays / Array-as-Hashmap ║
║  Link: https://leetcode.com/problems/first-missing-positive/        ║
╚══════════════════════════════════════════════════════════════════╝

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📘 SECTION 1 — PROBLEM UNDERSTANDING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Given an unsorted array of integers (which may include negatives,
  zeros, duplicates, and gaps), find the smallest positive integer
  that does NOT appear in the array. Must run in O(n) time and O(1)
  extra space.

  Input : nums = [3,4,-1,1]
  Output: 2

  Example 1 — basic:
    Input : nums = [3,4,-1,1]
    Output: 2
    Why?  : 1 is present, 2 is missing — 2 is the smallest missing
             positive

  Example 2 — slightly tricky (array is exactly 1..n, nothing missing):
    Input : nums = [1,2,0]
    Output: 3
    Why?  : 1 and 2 are present, so the answer is the next integer
             after the complete run, n+1 = 3

  Constraints:
    - 1 <= nums.length <= 10^5
    - -2^31 <= nums[i] <= 2^31 - 1

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🧠 SECTION 2 — KANGLISH THINKING — ಹೇಗೆ ಯೋಚಿಸಬೇಕು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  Problem odi aada mele namma brain enu think maadabeeku:

  ಹಂತ 1 — Problem ಅರ್ಥ ಮಾಡಿಕೊಳ್ಳಿ (What are they asking?)
  ┌─────────────────────────────────────────────────────────┐
  │  Input ಏನು ಕೊಡ್ತಾರೆ?  →  unsorted array (neg, 0, dup     │
  │                          ಎಲ್ಲಾ ಇರ್ಬೋದು)                  │
  │  Output ಏನು ಬೇಕು?     →  smallest missing positive int    │
  │  Constraints ಏನಿದೆ?   →  n<=10^5, O(n) time + O(1) space  │
  │                          ಕಡ್ಡಾಯ                          │
  └─────────────────────────────────────────────────────────┘

  ಹಂತ 2 — ನನಗೆ ಗೊತ್ತಿರೋ simple way ಏನು? (Brute force thought)
  →  1 ಇಂದ ಶುರು ಮಾಡಿ, ಪ್ರತಿ positive integer i ಗೂ, array ನಲ್ಲಿ i
     ಇದೆಯಾ ಅಂತ linear search ಮಾಡಿ ಚೆಕ್ ಮಾಡೋದು, ಸಿಗ್ದೇ ಇದ್ರೆ ಅದೇ answer.
  →  ಆದರೆ ಇದು slow ಯಾಕೆ? → ಪ್ರತಿ i ಗೂ O(n) search, i ಗರಿಷ್ಠ n+1 ತನಕ
     ಹೋಗ್ಬೋದು → O(n²).

  ಹಂತ 3 — Better way ಹೇಗೆ ಯೋಚಿಸುವುದು? (Optimization thought)
  →  ಒಂದು key observation: answer ಯಾವಾಗ್ಲೂ 1 ಇಂದ n+1 ರ ನಡುವೆ ಇರುತ್ತೆ
     (n elements ಇದ್ರೆ, ಗರಿಷ್ಠ n distinct positive numbers ಮಾತ್ರ
     ಇರೋಕೆ ಸಾಧ್ಯ, ಆದ್ದರಿಂದ 1..n ಎಲ್ಲಾ ಇದ್ರೆ ಮಾತ್ರ answer n+1). ಒಂದು
     hashset ಇಟ್ಕೊಂಡು, ಎಲ್ಲಾ elements ಸೇರಿಸಿ, 1 ಇಂದ n+1 ತನಕ ಚೆಕ್
     ಮಾಡಿದ್ರೆ O(n) ಸಿಗುತ್ತೆ, ಆದ್ರೆ O(n) extra space ಬೇಕಾಗುತ್ತೆ.
  →  ಅಹಾ moment: extra space ಬೇಡ ಅಂದ್ರೆ, array ಅನ್ನೇ hashmap ಆಗಿ use
     ಮಾಡ್ಬಹುದು! ಪ್ರತಿ value v (1<=v<=n) ಅನ್ನ ಅದರ "correct" index
     v-1 ಗೆ place ಮಾಡಿ (cyclic placement/swap ಇಂದ). ಆಮೇಲೆ scan ಮಾಡಿ,
     ಎಲ್ಲಿ index i ಗೆ nums[i] != i+1 ಸಿಗುತ್ತೋ, ಅದೇ (i+1) ಯೇ answer.
  →  ಇದರಿಂದ ನಾವು Array-as-Hashmap (Index Placement / Cyclic Sort)
     use ಮಾಡಬಹುದು!

  ಹಂತ 4 — Technique ಯಾಕೆ ಇಲ್ಲಿ ಕೆಲಸ ಮಾಡುತ್ತೆ?
  →  Answer 1..n+1 range ನಲ್ಲೇ ಇರೋದ್ರಿಂದ, ಆ range ಗೆ ಸಂಬಂಧ ಇಲ್ಲದ
     values (negatives, 0, > n) ಅನ್ನ ignore ಮಾಡ್ಬಹುದು — ಅವು ಎಂದೂ
     answer ಆಗೋಕೆ ಆಗಲ್ಲ.
  →  ಪ್ರತಿ valid value v ಅನ್ನ index v-1 ಗೆ swap ಮಾಡಿದ್ರೆ, ಪ್ರತಿ swap
     ಒಂದು element ಅನ್ನ ಅದರ ಸರಿಯಾದ ಸ್ಥಳಕ್ಕೆ ಇಡುತ್ತೆ — ಪ್ರತಿ index
     ಗರಿಷ್ಠ ಒಂದು ಸಲ ಮಾತ್ರ correct place ಗೆ ಹೋಗುತ್ತೆ, ಆದ್ದರಿಂದ total
     swaps O(n).
  →  Array ಅನ್ನೇ storage ಆಗಿ reuse ಮಾಡೋದ್ರಿಂದ, extra hashmap/set ಬೇಡ
     — O(1) extra space ಸಿಗುತ್ತೆ.

  💡 Interview ನಲ್ಲಿ ಹೇಗೆ ಮಾತಾಡಬೇಕು (Think out loud):
  →  "Checking each candidate 1,2,3... against the array directly is
      O(n²) — too slow, and a hash set gets O(n) but needs O(n) extra
      space, which the problem explicitly disallows."
  →  "Since the answer must lie in the range [1, n+1], I can use the
      array itself as a hashmap — place each valid value v at index
      v-1 by swapping."
  →  "After placing everything correctly, a single scan finds the
      first index where the value doesn't match index+1 — that's the
      answer."

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🏷️ SECTION 3 — TECHNIQUE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Primary   : Array-as-Hashmap (Index Placement / Cyclic Sort)
  Secondary : None

  WHY this technique?
  → The answer is bounded within [1, n+1] by pigeonhole (n slots can't
    hold n+1 distinct positive integers), narrowing the search space
  → Placing each valid value at its "home" index (value-1) via swaps
    turns the array into a lookup structure with zero extra memory
  → Each element reaches its correct position in at most one swap
    "chain" per index, bounding total swaps to O(n)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 💡 SECTION 4 — INTUITION (How to think — English)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Key observation: with n elements, the answer can never exceed n+1
  (if 1..n are all present, the answer is n+1; otherwise it's some
  value <= n). This means only values in [1, n] matter — everything
  else (negatives, zero, values > n) can be left alone. Swap each
  in-range value to its "home" index (value v belongs at index v-1)
  until every position either holds its correct value or holds
  something out of range. Then scan once: the first index i where
  nums[i] != i+1 reveals the answer.

  The journey from brute to optimal:
    Brute thought   →  linear-search each candidate 1,2,3,... in the array
    Problem with it →  O(n²), too slow
    Better question →  "can I use O(n) extra space with a hash set?
                        the constraint says no extra space though —
                        can the array itself act as that structure?"
    Insight         →  place each valid value at index (value-1) via
                        in-place swaps, turning the array into its
                        own presence-lookup table
    Optimal         →  in-place cyclic placement + one scan, O(n)
                        time, O(1) space

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🐢 SECTION 5 — APPROACH 1 — BRUTE FORCE (Linear Search Each Candidate)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    Starting from 1, check whether each candidate integer exists in
    the array using a direct linear scan. Return the first one that
    doesn't.

  Pseudocode:
    step 1: candidate = 1
    step 2: while candidate in nums: candidate += 1
    step 3: return candidate

  Time  : O(n²)  →  Why: up to n candidates, each an O(n) membership check
  Space : O(1)   →  Why: no extra structures beyond the candidate counter

  ಇದು ಯಾಕೆ ಸಾಕಾಗಲ್ಲ? (Why is this not enough?)
    → n=10^5 ಆದ್ರೆ n² = 10^10 — TLE ಆಗತ್ತೆ.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🚶 SECTION 6 — APPROACH 2 — BETTER (Hash Set of Present Values)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    Insert all array values into a hash set, then check candidates
    1, 2, 3, ... up to n+1 for set membership in O(1) each.

  Time  : O(n)  →  one pass to build the set, one pass to check candidates
  Space : O(n)  →  hash set storing up to n values

  ಇನ್ನೂ better ಮಾಡಬಹುದಾ? → ಹೌದು — problem explicitly O(1) extra space
  ಕೇಳುತ್ತೆ, ಆದ್ದರಿಂದ hash set ಬದ್ಲು array-as-hashmap (in-place
  placement) use ಮಾಡ್ಬೇಕು.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🚀 SECTION 7 — APPROACH 3 — OPTIMAL   (In-Place Index Placement)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    For each index i, while nums[i] is in range [1, n] and not
    already at its home index (nums[nums[i]-1] != nums[i]), swap
    nums[i] with nums[nums[i]-1]. After this pass, scan for the first
    index i where nums[i] != i+1 — return i+1. If none found, return
    n+1.

  Key steps:
    1. n = len(nums)
    2. for i in range(n):
         while 1 <= nums[i] <= n and nums[nums[i]-1] != nums[i]:
           swap nums[i], nums[nums[i]-1]
    3. for i in range(n):
         if nums[i] != i + 1: return i + 1
    4. return n + 1

  ಕನ್ನಡದಲ್ಲಿ ಒಂದು ಸಲ ಹೇಳಿ (Kanglish one-liner so it sticks):
    → "ಪ್ರತಿ index i ಗೂ, nums[i] value 1 ಇಂದ n range ನಲ್ಲಿ ಇದ್ರೆ,
        ಅದನ್ನ ಅದರ 'home' index (value-1) ಗೆ swap ಮಾಡ್ತಾ ಹೋಗು.
        ಕೊನೆಗೆ scan ಮಾಡಿ, ಎಲ್ಲಿ nums[i] != i+1 ಸಿಗುತ್ತೋ ಅಲ್ಲಿ i+1
        ಯೇ answer, ಎಲ್ಲಾ match ಆದ್ರೆ n+1!"

  Time  : O(n)  →  Why: each element is swapped to its home index at
                    most once across the whole array (amortized)
  Space : O(1)  →  Why: rearrangement happens in-place, no extra
                    structures beyond loop variables

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🔍 SECTION 8 — DRY RUN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Input: nums = [3,4,-1,1]  (n=4)

  i=0: nums[0]=3, in [1,4], nums[3-1]=nums[2]=-1 != 3 → swap
       nums[0],nums[2] → [-1,4,3,1]
       nums[0]=-1, not in [1,4] → stop
  i=1: nums[1]=4, in [1,4], nums[4-1]=nums[3]=1 != 4 → swap
       nums[1],nums[3] → [-1,1,3,4]
       nums[1]=1, in [1,4], nums[1-1]=nums[0]=-1 != 1 → swap
       nums[1],nums[0] → [1,-1,3,4]
       nums[1]=-1, not in [1,4] → stop
  i=2: nums[2]=3, in [1,4], nums[3-1]=nums[2]=3 == 3 → already home, stop
  i=3: nums[3]=4, in [1,4], nums[4-1]=nums[3]=4 == 4 → already home, stop

  Array after placement: [1,-1,3,4]

  Scan: i=0: nums[0]=1==1 ✓; i=1: nums[1]=-1 != 2 → return i+1=2

  Output: 2   matches expected

  ಇನ್ನೊಂದು example — tricky case (1..n all present):
  Input: nums = [1,2,0]  (n=3)

  i=0: nums[0]=1, home index 0, nums[0]=1==1 → already home
  i=1: nums[1]=2, home index 1, nums[1]=2==2 → already home
  i=2: nums[2]=0, not in [1,3] → skip

  Array unchanged: [1,2,0]
  Scan: i=0: 1==1 ✓; i=1: 2==2 ✓; i=2: nums[2]=0 != 3 → return i+1=3

  Output: 3   matches expected

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 ⚠️ SECTION 9 — EDGE CASES — ಇವನ್ನ ಮರೆಯಬೇಡ!
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  ✓ All negative or zero values? →  no swaps happen at all, final
                                     scan immediately returns 1
  ✓ Array is exactly [1..n]      →  every value already at its home
    (shuffled)?                     index after placement, scan
                                     finds nothing missing, returns n+1
  ✓ Duplicate values?            →  the `nums[nums[i]-1] != nums[i]`
                                     guard prevents infinite swap
                                     loops when a duplicate already
                                     occupies the home slot
  ✓ Single element array?        →  n=1; if it's 1, answer is 2;
                                     otherwise answer is 1
  ✓ Values far outside [1,n]?    →  simply skipped during placement,
                                     never interfere with the result

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📊 SECTION 10 — COMPLEXITY SUMMARY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                Time      Space
  Brute Force   O(n²)     O(1)
  Better        O(n)      O(n)   (hash set)
  Optimal       O(n)      O(1)    ← use this

  Time yaake ashtu?  → prati element ಗರಿಷ್ಠ ಒಂದೇ ಸಲ ಅದರ home index
                        ಗೆ swap ಆಗುತ್ತೆ (amortized), total O(n).
                        Second scan ಕೂಡ O(n) — total O(n).
  Space yaake ashtu? → array ಅನ್ನೇ in-place rearrange ಮಾಡ್ತೀವಿ, extra
                        structure ಬೇಡ.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🎯 SECTION 11 — PATTERN LEARNED — ಇದರಿಂದ ಕಲಿತದ್ದು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Pattern Name: Array-as-Hashmap (Cyclic Sort / Index Placement)

  Ee pattern yaavaaga use maadabeeku?
  → "Find missing/duplicate number in range [1,n]" ಥರ problem, O(1)
    extra space ಕೇಳಿದಾಗ
  → Values ನ range ಗೊತ್ತಿದ್ದಾಗ (ಇಲ್ಲಿ 1..n), ಆ range ಅನ್ನೇ array
    indices ಆಗಿ map ಮಾಡ್ಬಹುದು ಅಂತ ಗುರುತಿಸಿದಾಗ
  → Hash set/map solution ಇದ್ರೂ, space constraint ಇದ್ರೆ

  Idee pattern beere problemsalli kaanisatte:
  → Find All Numbers Disappeared in an Array (LC 448) — same cyclic
    placement idea
  → Find the Duplicate Number (already solved in this repo) — related
    but uses Floyd's cycle detection instead
  → Set Mismatch (LC 645) — same in-place placement to find both a
    duplicate and a missing number

  Next time intaha problem bandre naanu modalu idannu think maadtene:
  → "'Missing number in range [1,n]' anta kanda takshana, O(1) space
      bekaadre array anne hashmap aagi use maadi, value ge home index
      ge place maadu anta modalu yochisu."

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🗣️ SECTION 12 — INTERVIEWALLI HEGE EXPLAIN MAADABEEKU
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  1. Understand:
     "I need the smallest positive integer missing from the array, in
      O(n) time and O(1) extra space."

  2. Brute force:
     "Checking each candidate against the array directly is O(n²). A
      hash set gets O(n) time but uses O(n) space, which the problem
      disallows."

  3. Optimize:
     "Since the answer must be in [1, n+1], I only care about values
      in that range. I can use the array itself as a hashmap by
      swapping each valid value to its 'home' index (value-1)."

  4. Code:
     "For each index, while its value is in range and not already at
      its home position, swap it there. Then scan once: the first
      index where value != index+1 gives the answer; if none, it's
      n+1."

  5. Complexity:
     "Time O(n) — each element reaches its home index in at most one
      swap chain overall. Space O(1) — everything happens in-place."

  Mukhya: summane kuutu code bareyabeda! Interviewer ge ninna thinking
          process kaanabeku.
"""


# ═══════════════════════════════════════════════════════════════════
# BRUTE FORCE — O(n^2) Time | O(1) Space  (Linear Search Each Candidate)
# ═══════════════════════════════════════════════════════════════════
def first_missing_positive_brute(nums):
    """Idu modala aaloochane — 1,2,3... prati candidate ge array nalli linear search maadodu"""
    candidate = 1
    while candidate in nums:
        candidate += 1
    return candidate


# ═══════════════════════════════════════════════════════════════════
# OPTIMAL — O(n) Time | O(1) Space  (Array-as-Hashmap, In-Place Placement)
# ═══════════════════════════════════════════════════════════════════
def first_missing_positive(nums):
    """Idu final answer — prati valid value annu adara home index ge place maadi scan maadu"""
    n = len(nums)

    for i in range(n):
        while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
            target = nums[i] - 1
            nums[i], nums[target] = nums[target], nums[i]

    for i in range(n):
        if nums[i] != i + 1:
            return i + 1

    return n + 1


# ═══════════════════════════════════════════════════════════════════
# TEST CASES
# ═══════════════════════════════════════════════════════════════════
if __name__ == "__main__":
    import sys
    sys.stdout.reconfigure(encoding="utf-8")

    # Test 1 — Basic example
    assert first_missing_positive([3, 4, -1, 1]) == 2

    # Test 2 — Tricky: 1..n all present (shuffled), answer is n+1
    assert first_missing_positive([1, 2, 0]) == 3

    # Test 3 — Edge case: all negative or zero
    assert first_missing_positive([-5, -3, 0]) == 1

    # Test 4 — Edge case: single element
    assert first_missing_positive([1]) == 2
    assert first_missing_positive([2]) == 1

    # Test 5 — Tricky: duplicate values present
    assert first_missing_positive([1, 1, 2, 2]) == 3

    print("All tests passed!")
