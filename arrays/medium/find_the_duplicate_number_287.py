"""
╔══════════════════════════════════════════════════════════════════╗
║  FIND THE DUPLICATE NUMBER                                        ║
║  LeetCode #287  |  Difficulty: Medium  |  Topic: Arrays / Two Pointers ║
║  Link: https://leetcode.com/problems/find-the-duplicate-number/   ║
╚══════════════════════════════════════════════════════════════════╝

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📘 SECTION 1 — PROBLEM UNDERSTANDING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Given an array of n+1 integers where every value is in range
  [1, n], there is exactly ONE number that repeats (possibly more
  than twice). Find that duplicate — WITHOUT modifying the array, and
  using O(1) extra space.

  Input : nums = [1, 3, 4, 2, 2]
  Output: 2

  Example 1 — basic:
    Input : nums = [1, 3, 4, 2, 2]
    Output: 2
    Why?  : n=4, values should be a permutation of [1,2,3,4], but 2
             appears twice and 4's "slot" pattern reveals the collision

  Example 2 — slightly tricky (duplicate appears many times):
    Input : nums = [3, 1, 3, 4, 2]
    Output: 3
    Why?  : 3 repeats — must find it purely via value/index
             relationships, not sorting or extra storage

  Constraints:
    - 1 <= n <= 10^5
    - nums.length == n + 1
    - 1 <= nums[i] <= n
    - All integers appear once EXCEPT one, which appears 2+ times
    - Must NOT modify the array; O(1) extra space required (follow-up)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🧠 SECTION 2 — KANGLISH THINKING — ಹೇಗೆ ಯೋಚಿಸಬೇಕು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  ಮೊದಲು problem odidaga ನಮ್ಮ brain ಏನು think ಮಾಡಬೇಕು:

  ಹಂತ 1 — Problem ಅರ್ಥ ಮಾಡಿಕೊಳ್ಳಿ (What are they asking?)
  ┌─────────────────────────────────────────────────────────┐
  │  Input ಏನು ಕೊಡ್ತಾರೆ?  →  n+1 integers, values [1,n] range   │
  │  Output ಏನು ಬೇಕು?     →  ಒಂದೇ ಒಂದು repeat ಆಗಿರೋ number     │
  │  Constraints ಏನಿದೆ?   →  array modify ಮಾಡ್ಬಾರ್ದು, O(1)     │
  │                          space (follow-up), sort/hashset ಬೇಡ │
  └─────────────────────────────────────────────────────────┘

  ಹಂತ 2 — ನನಗೆ ಗೊತ್ತಿರೋ simple way ಏನು? (Brute force thought)
  →  HashSet ಇಟ್ಕೊಂಡು, ಪ್ರತಿ number ಗೂ set ನಲ್ಲಿ ಆಗ್ಲೇ ಇದ್ಯಾ ಅಂತ ಚೆಕ್
     ಮಾಡೋದು.
  →  ಆದರೆ ಇದು slow ಯಾಕೆ? → Correct, ಆದ್ರೆ O(n) extra space ಬೇಕಾಗುತ್ತೆ —
     follow-up O(1) space ಕೇಳ್ತಾ ಇದೆ. Sort ಮಾಡಿದ್ರೂ array modify
     ಆಗುತ್ತೆ (ಅಥವಾ copy ಬೇಕಾಗುತ್ತೆ) — ಅದೂ constraint violate ಮಾಡುತ್ತೆ.

  ಹಂತ 3 — Better way ಹೇಗೆ ಯೋಚಿಸುವುದು? (Optimization thought)
  →  "values [1,n] range ನಲ್ಲಿ ಇರೋದ್ರಿಂದ, ಪ್ರತಿ index i ಇಂದ
     nums[i] ಗೆ ಒಂದು 'pointer' ಅಂತ ಯೋಚಿಸಿದ್ರೆ (i -> nums[i]), ಇದು
     ಒಂದು linked list ಥರ ಆಗುತ್ತೆ! ಒಂದೇ number ಎರಡು ಸಲ ಇರೋದ್ರಿಂದ,
     ಎರಡು ಬೇರೆ indices ಇಂದ ಒಂದೇ next value ಗೆ ಪಾಯಿಂಟ್ ಆಗುತ್ತೆ — ಇದೇ
     'cycle' ಸೃಷ್ಟಿ ಆಗುತ್ತೆ, floyd's cycle detection use ಮಾಡ್ಬಹುದಾ?"
  →  ಅಹಾ moment: nums ಅನ್ನ implicit linked list ಆಗಿ ಪರಿಗಣಿಸಿದ್ರೆ
     (node i -> node nums[i]), duplicate ಇರೋದ್ರಿಂದ ಈ "list" ನಲ್ಲಿ
     ಖಂಡಿತ ಒಂದು cycle ಇರುತ್ತೆ (ಯಾಕಂದ್ರೆ ಎರಡು indices ಒಂದೇ value ಗೆ
     ಪಾಯಿಂಟ್ ಮಾಡ್ತಾವೆ, ಆ value ಗೆ ಇಬ್ಬರು "in-edges" ಬರುತ್ತೆ). ಆ cycle ನ
     entry point ಯೇ duplicate number! Floyd's Tortoise & Hare ಇಂದ
     O(1) space ನಲ್ಲಿ cycle entry point ಕಂಡುಹಿಡಿಬಹುದು.
  →  ಇದರಿಂದ ನಾವು Two Pointers → Slow-Fast (Floyd's Cycle Detection on
     Implicit Linked List) use ಮಾಡಬಹುದು!

  ಹಂತ 4 — Technique ಯಾಕೆ ಇಲ್ಲಿ ಕೆಲಸ ಮಾಡುತ್ತೆ?
  →  Values [1,n] range ನಲ್ಲಿ ಇರೋದ್ರಿಂದ, array ಅನ್ನ node-to-node
     mapping (i -> nums[i]) ಆಗಿ ನೋಡ್ಬಹುದು — ಇದೇ implicit linked list.
  →  Duplicate ಇರೋದ್ರಿಂದ ಆ "list" ಗೆ ಖಂಡಿತ ಒಂದು cycle ಇರುತ್ತೆ — ಈ
     structural guarantee Floyd's algorithm apply ಮಾಡೋಕೆ ಅಗತ್ಯ.
  →  Floyd's ಇಂದ array modify ಮಾಡ್ದೇ, extra space ಬಳಸ್ದೇ (bare ಆಗಿ
     slow/fast pointers ಇಂದ) duplicate ಸಿಗುತ್ತೆ.

  💡 Interview ನಲ್ಲಿ ಹೇಗೆ ಮಾತಾಡಬೇಕು (Think out loud):
  →  "A hash set would find the duplicate easily, but that's O(n)
      extra space, which violates the follow-up constraint."
  →  "The key insight is that since every value is in [1, n], I can
      treat the array as an implicit linked list: index i points to
      index nums[i]."
  →  "Because there's a duplicate, two different indices point to the
      same value, creating a cycle in this implicit list — and the
      entry point of that cycle is exactly the duplicate number,
      found with Floyd's Tortoise and Hare in O(1) space."

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🏷️ SECTION 3 — TECHNIQUE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Primary   : Two Pointers → Slow-Fast (Floyd's Cycle Detection)
  Secondary : None

  WHY this technique?
  → Values constrained to [1, n] let us treat the array as function
    f(i) = nums[i], an implicit linked list on indices
  → A duplicate value guarantees two indices point to the same node,
    which structurally forces a cycle to exist in this implicit list
  → Floyd's algorithm finds the cycle entry point (= the duplicate)
    in O(n) time and O(1) space, without modifying the array

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 💡 SECTION 4 — INTUITION (How to think — English)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Key observation: think of the array as defining a function
  f(x) = nums[x], starting from x = 0 (a value outside the cycle,
  since values are in [1,n] and never point back to index 0). Because
  one value repeats, two positions "feed into" the same next value —
  exactly the condition that creates a cycle in a functional graph.
  This is now structurally identical to "Linked List Cycle II" — find
  where the cycle begins.

  The journey from brute to optimal:
    Brute thought   →  track seen values in a hash set
    Problem with it →  O(n) extra space, violates the O(1) follow-up
    Better question →  "can the array's own value-index relationship
                        encode the answer, like a linked list?"
    Insight         →  treating index->nums[index] as a linked list,
                        the duplicate creates a provable cycle
    Optimal         →  Floyd's Tortoise and Hare to find the cycle's
                        entry point, O(n) time, O(1) space

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🐢 SECTION 5 — APPROACH 1 — BRUTE FORCE (HashSet)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    Walk through the array, adding each value to a set. The moment a
    value is already in the set, that's the duplicate.

  Pseudocode:
    step 1: seen = set()
    step 2: for num in nums:
    step 3:   if num in seen: return num
    step 4:   seen.add(num)

  Time  : O(n)  →  Why: single pass, O(1) average set operations
  Space : O(n)  →  Why: set can hold up to n distinct values

  ಇದು ಯಾಕೆ ಸಾಕಾಗಲ್ಲ? (Why is this not enough?)
    → Follow-up ಸ್ಪಷ್ಟವಾಗಿ O(1) extra space ಕೇಳ್ತಾ ಇದೆ, array modify
      ಮಾಡ್ಬಾರ್ದು ಅಂತ ಸಹ ಕೇಳ್ತಾ ಇದೆ — Floyd's cycle detection ಇಂದ
      ಎರಡೂ ಗುರಿ ಮುಟ್ಟಿಸ್ಬೋದು.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🚶 SECTION 6 — APPROACH 2 — BETTER (skip — brute jumps straight to optimal)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  ಇಲ್ಲಿ intermediate approach ಇಲ್ಲ — HashSet brute force ಇಂದ ನೇರವಾಗಿ
  Floyd's cycle detection optimal ಗೆ ಹೋಗಬಹುದು (Binary search on
  answer-space O(n log n) ಸಹ ಇದೆ, ಆದ್ರೆ Floyd's ಇಂದ O(n) ಇನ್ನೂ fast).

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🚀 SECTION 7 — APPROACH 3 — OPTIMAL   (Floyd's Cycle Detection — Slow/Fast Pointers)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    Treat nums as a function: from any index/value x, "next" is
    nums[x]. Phase 1 — start slow and fast both at nums[0], move
    slow one step (slow = nums[slow]) and fast two steps
    (fast = nums[nums[fast]]) until they meet inside the cycle.
    Phase 2 — reset slow to nums[0]-position-equivalent (actually
    reset one pointer to the start value nums[0]... using the
    standard "reset to head" trick), then move both one step at a
    time; where they meet again is the cycle's entry point — the
    duplicate number.

  Key steps:
    1. slow = fast = nums[0]
    2. Phase 1 (find meeting point inside cycle):
         while True:
           slow = nums[slow]
           fast = nums[nums[fast]]
           if slow == fast: break
    3. Phase 2 (find cycle entry = duplicate):
         slow2 = nums[0]
         while slow2 != slow:
           slow2 = nums[slow2]
           slow = nums[slow]
    4. Return slow (== slow2, the duplicate)

  ಕನ್ನಡದಲ್ಲಿ ಒಂದು ಸಲ ಹೇಳಿ (Say it once in Kanglish so it sticks):
    → "slow, fast ಎರಡೂ nums[0] ಇಂದ start ಮಾಡು. slow ಒಂದು step,
        fast ಎರಡು step ಮುಂದೆ ಹೋಗ್ತಾ ಇರ್ಲಿ (nums[x] ಅನ್ನೇ 'next' ಅಂತ),
        ಇಬ್ಬರೂ meet ಆಗೋ ತನಕ. ಆಮೇಲೆ ಒಂದು ಹೊಸ pointer nums[0] ಇಂದ
        start ಮಾಡಿ, ಅದು ಮತ್ತು slow ಇಬ್ಬರೂ ಒಂದೊಂದೇ step ಮುಂದೆ ಹೋಗ್ತಾ
        ಇರ್ಲಿ — ಎಲ್ಲಿ meet ಆಗುತ್ತೋ ಅದೇ duplicate number!"

  Time  : O(n)  →  Why: both phases are linear in the number of
                    elements traversed (standard Floyd's bound)
  Space : O(1)  →  Why: only two/three pointer variables, no extra
                    structures, array untouched

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🔍 SECTION 8 — DRY RUN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Input: nums = [1, 3, 4, 2, 2]  (index: 0  1  2  3  4)

  Phase 1 — find meeting point:
    slow=fast=nums[0]=1
    step1: slow=nums[1]=3, fast=nums[nums[1]]=nums[3]=2
    step2: slow=nums[3]=2, fast=nums[nums[2]]=nums[4]=2
    slow==fast==2 → meeting point found, break

  Phase 2 — find cycle entry:
    slow2 = nums[0] = 1
    slow2(1) != slow(2)? Yes, keep going
    slow2 = nums[1] = 3, slow = nums[2] = 4
    slow2(3) != slow(4)? Yes, keep going
    slow2 = nums[3] = 2, slow = nums[4] = 2
    slow2(2) == slow(2) → stop

  Output: 2   matches expected

  ಇನ್ನೊಂದು example — tricky case (duplicate appears many times):
  Input: nums = [3, 1, 3, 4, 2]  (index: 0  1  2  3  4)

  Phase 1:
    slow=fast=nums[0]=3
    step1: slow=nums[3]=4, fast=nums[nums[3]]=nums[4]=2
    step2: slow=nums[4]=2, fast=nums[nums[2]]=nums[3]=4
    step3: slow=nums[2]=3, fast=nums[nums[4]]=nums[2]=3
    slow==fast==3 → break

  Phase 2:
    slow2 = nums[0] = 3
    slow2(3) == slow(3) → stop immediately

  Output: 3   matches expected

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 ⚠️ SECTION 9 — EDGE CASES — ಇವನ್ನ ಮರೆಯಬೇಡ!
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  ✓ Smallest input (n=1, array=[1,1])? →  slow=fast=nums[0]=1 already
                                   equal in phase 1's first check
                                   pattern, correctly resolves to 1
  ✓ Duplicate appears many times (3+)? →  Floyd's still finds the
                                   single cycle entry correctly (see
                                   Example 2 dry run above)
  ✓ Duplicate is the smallest value (1)? →  works identically, no
                                   special-casing needed for value 1
  ✓ Duplicate is the largest value (n)? →  works identically, cycle
                                   structure doesn't depend on which
                                   value repeats
  ✓ Array must stay unmodified?  →  Floyd's only reads nums[x], never
                                   writes to the array

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📊 SECTION 10 — COMPLEXITY SUMMARY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                Time      Space
  Brute Force   O(n)      O(n)   (hashset)
  Optimal       O(n)      O(1)    ← use this  (Floyd's, no modification)

  Time ಯಾಕೆ ಅಷ್ಟು?  → ಎರಡೂ phases linear — fast pointer meets slow
                        within cycle-length bound, ಆಮೇಲೆ entry point
                        ಗೆ ಮತ್ತೊಂದು linear walk.
  Space ಯಾಕೆ ಅಷ್ಟು? → slow, fast, slow2 — ಬರೀ pointer variables, array
                        untouched, ಬೇರೆ extra structure ಬೇಡ.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🎯 SECTION 11 — PATTERN LEARNED — ಇದರಿಂದ ಕಲಿತದ್ದು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Pattern Name: Floyd's Cycle Detection on Implicit Linked List (Array as Graph)

  ಈ pattern ಯಾವಾಗ use ಮಾಡಬೇಕು?
  → Array values ಒಂದು range [1,n] (ಅಥವಾ [0,n-1]) ಒಳಗೆ ಇದ್ದು, ಅದನ್ನ
    index->value mapping/function ಆಗಿ ನೋಡ್ಬಹುದು ಅಂತ ಗೊತ್ತಾದಾಗ
  → Duplicate ಅಥವಾ repeated element ಇರೋದ್ರಿಂದ structurally cycle
    ಗ್ಯಾರಂಟಿ ಆಗಿದೆ ಅಂತ ಗೊತ್ತಾದಾಗ
  → O(1) space + no modification constraint ಇದ್ದಾಗ (hashset/sort
    ಎರಡೂ ruled out ಆಗಿದ್ದಾಗ)

  ಇದೇ pattern ಬೇರೆ problems ನಲ್ಲಿ ಕಾಣಿಸುತ್ತೆ:
  → Linked List Cycle II (#142) — the original Floyd's cycle-entry problem
  → Circular Array Loop — same functional-graph cycle detection idea
  → Happy Number (#202) — same slow/fast pointer trick on a different function

  Next time ಇಂತಹ problem ಬಂದ್ರೆ ನಾನು ಮೊದಲು ಇದನ್ನ think ಮಾಡ್ತೇನೆ:
  → "Array values ಒಂದು bounded range ಒಳಗೆ ಇದ್ದು, duplicate ಹುಡುಕ್ಬೇಕು,
      O(1) space ಬೇಕು ಅಂತ ಕೇಳಿದ ತಕ್ಷಣ, array ಅನ್ನ implicit linked
      list ಆಗಿ ನೋಡಿ Floyd's slow/fast ಬಳಸು ಅಂತ ಮೊದಲು ಯೋಚಿಸು."

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🗣️ SECTION 12 — INTERVIEWALLI HEGE EXPLAIN MAADABEEKU
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  1. Understand:
     "I need to find the one duplicate value in an array of n+1
      integers all in range [1,n], without modifying the array and
      ideally using O(1) extra space."

  2. Brute force:
     "A hash set tracking seen values finds the duplicate in O(n)
      time, but uses O(n) extra space, which violates the follow-up."

  3. Optimize:
     "Since every value is in [1,n], I can treat the array as a
      function f(x) = nums[x] — an implicit linked list. The
      duplicate value means two indices point to the same next node,
      which guarantees a cycle exists — turning this into 'find the
      cycle's entry point,' just like Linked List Cycle II."

  4. Code:
     "I will use Floyd's Tortoise and Hare: first find a meeting
      point inside the cycle with slow/fast pointers, then reset one
      pointer to the start and advance both one step at a time until
      they meet again — that meeting point is the duplicate."

  5. Complexity:
     "Time O(n) — both phases are linear. Space O(1) — just pointer
      variables, and the array is never modified."

  ಮುಖ್ಯ: ಸುಮ್ಮನೆ ಕೂತು code ಬರೆಯಬೇಡ!
         Interviewer ಗೆ ನಿನ್ನ thinking process ಕಾಣಬೇಕು.
"""


# ═══════════════════════════════════════════════════════════════════
# BRUTE FORCE — O(n) Time | O(n) Space  (HashSet)
# ═══════════════════════════════════════════════════════════════════
def find_duplicate_brute(nums):
    """ಇದು ಮೊದಲ ಆಲೋಚನೆ — hashset ಇಟ್ಕೊಂಡು ಆಗ್ಲೇ seen ಆಗಿರೋ value ಹುಡುಕೋದು"""
    seen = set()
    for num in nums:
        if num in seen:
            return num
        seen.add(num)
    return -1


# ═══════════════════════════════════════════════════════════════════
# OPTIMAL — O(n) Time | O(1) Space  (Floyd's Cycle Detection)
# ═══════════════════════════════════════════════════════════════════
def find_duplicate(nums):
    """ಇದು final answer — array ಅನ್ನ implicit linked list ಆಗಿ ನೋಡಿ Floyd's slow/fast ಬಳಸು"""
    slow = fast = nums[0]

    # Phase 1 — find a meeting point inside the cycle
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break

    # Phase 2 — find the cycle's entry point (the duplicate)
    slow2 = nums[0]
    while slow2 != slow:
        slow2 = nums[slow2]
        slow = nums[slow]

    return slow


# ═══════════════════════════════════════════════════════════════════
# TEST CASES
# ═══════════════════════════════════════════════════════════════════
if __name__ == "__main__":
    import sys
    sys.stdout.reconfigure(encoding="utf-8")   # Windows cp1252 can't print emoji otherwise

    # Test 1 — Basic example
    assert find_duplicate([1, 3, 4, 2, 2]) == 2

    # Test 2 — Edge case: smallest possible input
    assert find_duplicate([1, 1]) == 1

    # Test 3 — Edge case: duplicate appears many times
    assert find_duplicate([2, 2, 2, 2, 2]) == 2

    # Test 4 — Tricky: duplicate is the largest value, appears 3 times
    assert find_duplicate([3, 1, 3, 4, 2]) == 3

    print("All tests passed! ")
