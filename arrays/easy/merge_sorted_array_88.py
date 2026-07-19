"""
╔══════════════════════════════════════════════════════════════════╗
║  MERGE SORTED ARRAY                                              ║
║  LeetCode #88  |  Difficulty: Easy  |  Topic: Arrays / Two Pointers ║
║  Link: https://leetcode.com/problems/merge-sorted-array/         ║
╚══════════════════════════════════════════════════════════════════╝

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📘 PROBLEM UNDERSTANDING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Two sorted arrays nums1 (m real elements, n trailing zero
  placeholders) and nums2 (n elements). Merge nums2 INTO nums1
  in-place so nums1 becomes one sorted array.

  Input : nums1 = [1,2,3,0,0,0], m=3, nums2 = [2,5,6], n=3
  Output: nums1 = [1,2,2,3,5,6]

  Example 1 — basic:
    Input : nums1=[1,2,3,0,0,0], m=3, nums2=[2,5,6], n=3
    Output: [1,2,2,3,5,6]
    Why?  : merging [1,2,3] and [2,5,6] gives this sorted result

  Example 2 — slightly tricky:
    Input : nums1=[0,0,0], m=0, nums2=[2,5,6], n=3
    Output: [2,5,6]
    Why?  : nums1 has no real elements — result is exactly nums2

  Constraints:
    - nums1 has exactly m + n total slots (trailing zeros are filler)
    - Must merge IN-PLACE into nums1

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🧠 KANGLISH THINKING — ಹೇಗೆ ಯೋಚಿಸಬೇಕು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  ಮೊದಲು problem odidaga ನಮ್ಮ brain ಏನು think ಮಾಡಬೇಕು:

  ಹಂತ 1 — Problem ಅರ್ಥ ಮಾಡಿಕೊಳ್ಳಿ (What are they asking?)
  ┌─────────────────────────────────────────────────────────┐
  │  Input ಏನು ಕೊಡ್ತಾರೆ?  →  nums1 (m real + n trailing 0)  │
  │                          ಮತ್ತು nums2 (n elements)         │
  │  Output ಏನು ಬೇಕು?     →  nums1 ಒಳಗೇ merge ಆದ sorted     │
  │                          array (in-place)                 │
  │  Constraints ಏನಿದೆ?   →  nums1 ಗೆ IN-PLACE merge         │
  │                          ಮಾಡ್ಬೇಕು, extra array ಬೇಡ        │
  └─────────────────────────────────────────────────────────┘

  ಹಂತ 2 — ನನಗೆ ಗೊತ್ತಿರೋ simple way ಏನು? (Brute force thought)
  →  nums1 ನ real values ಅನ್ನ ಒಂದು temp copy ಗೆ ತಗೊಂಡು, temp
     ಮತ್ತು nums2 ಅನ್ನ front ಇಂದ merge ಮಾಡಿ nums1 ಗೆ ಬರೀಯೋದು.
  →  ಆದರೆ ಇದು ಯಾಕೆ enough ಅಲ್ಲ? → temp copy ಗೆ O(m) extra space
     ಬೇಕಾಗುತ್ತೆ.

  ಹಂತ 3 — Better way ಹೇಗೆ ಯೋಚಿಸುವುದು? (Optimization thought)
  →  "Front ಇಂದ merge ಮಾಡಿದ್ರೆ, nums1 ನ still-unread values ಅನ್ನ
     overwrite ಮಾಡಿಬಿಡ್ತೀನಿ. BACK ಇಂದ merge ಮಾಡಿದ್ರೆ ಹೇಗಿರುತ್ತೆ?"
  →  ಅಹಾ moment: nums1 ಕೊನೇಲಿ ಈಗಾಗಲೇ empty space ಇದೆ (m+n
     length ಇದೆ, ಆದ್ರೆ m ಮಾತ್ರ real). ದೊಡ್ಡ value ಗಳನ್ನ ಮೊದಲು
     ಆ ಕೊನೇ empty slots ಗೆ ಇಟ್ಟುಕೊಂಡ್ರೆ, ನಮಗೆ ಇನ್ನೂ ಬೇಕಾದ data
     ಅನ್ನ ಎಂದೂ overwrite ಮಾಡಲ್ಲ.
  →  ಇದರಿಂದ ನಾವು Two Pointers — Merge from the Back use ಮಾಡಬಹುದು!

  ಹಂತ 4 — Technique ಯಾಕೆ ಇಲ್ಲಿ ಕೆಲಸ ಮಾಡುತ್ತೆ?
  →  nums1 ಗೆ ಕೊನೇಲಿ ಸಾಕಷ್ಟು extra room ಇರೋದ್ರಿಂದ, ಆ room ಅನ್ನ
     ಬಳಸಿ ಹಿಂದೆ ಇಂದ ಬರೆಯಬಹುದು.
  →  Merge sort ನ classic merge step ಗೆ ಇದೇ reverse version.
  →  In-place constraint ಇದ್ರಿಂದ, "write ಮಾಡೋಕ್ಕೆ ಮುಂಚೆ read
     ಮಾಡಿ ಆಗಿರ್ಬೇಕು" ಅನ್ನೋ order ಕಾಪಾಡೋಕ್ಕೆ back-to-front ಅಗತ್ಯ.

  💡 Interview ನಲ್ಲಿ ಹೇಗೆ ಮಾತಾಡಬೇಕು (Think out loud):
  →  "So I need to merge nums2 into nums1 in-place, and nums1 has
      trailing empty space sized exactly for the merge."
  →  "Merging from the front would overwrite unread nums1 values."
  →  "I notice merging from the BACK never overwrites data I still
      need, since I always place into the highest empty slot."

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🏷️ TECHNIQUE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Primary   : Two Pointers → Opposite Ends (Merge from the BACK)
  Secondary : In-place merge (merge-sort's merge step, reversed)

  WHY this technique?
  → nums1 has trailing empty space sized for the merge
  → Writing from the BACK never overwrites data still needed
  → Classic merge step, run in reverse to respect in-place space

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 💡 INTUITION (How to think)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  If I merge from the FRONT, I'd overwrite unread nums1 values.
  What if I merge from the BACK instead?

  The journey from brute to optimal:
    Brute thought   →  copy nums1's real part to temp, merge normally
    Problem with it →  O(m) extra space
    Better question →  "can the empty space at the END help?"
    Insight         →  place largest remaining value into the last
                        empty slot, working backward
    Optimal         →  three pointers (i, j, k), merge from the back

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🐢 APPROACH 1 — BRUTE FORCE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    Copy nums1's real values out, then merge two arrays normally.

  Pseudocode:
    step 1: temp = nums1[:m]
    step 2: merge temp and nums2 front-to-back into nums1
    step 3: copy any remaining elements

  Time  : O(m + n)  →  Why: each element placed once
  Space : O(m)  →  Why: temp copy of nums1's real values

  ಇದು ಯಾಕೆ ಸಾಕಾಗಲ್ಲ? (Why is this not enough?)
    → Extra O(m) space ಬಳಸುತ್ತೆ; problem true in-place merge ಬಯಸುತ್ತೆ.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🚶 APPROACH 2 — BETTER (skip — brute jumps straight to optimal)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  ಇಲ್ಲಿ intermediate approach ಇಲ್ಲ — merge-from-back insight
  ಸಿಕ್ಕ ತಕ್ಷಣ ನೇರವಾಗಿ O(1) space optimal ಗೆ ಹೋಗಬಹುದು.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🚀 APPROACH 3 — OPTIMAL  
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    Three pointers, merge from the back, largest values first.

  Key steps:
    1. i = m-1 (last real nums1), j = n-1 (last nums2),
       k = m+n-1 (last slot, write position)
    2. While i >= 0 and j >= 0:
         if nums1[i] > nums2[j]: nums1[k] = nums1[i]; i -= 1
         else:                    nums1[k] = nums2[j]; j -= 1
         k -= 1
    3. If nums2 still has leftovers (j >= 0), copy them in
       (leftover nums1 values are already correctly positioned)

  ಕನ್ನಡದಲ್ಲಿ ಒಂದು ಸಲ ಹೇಳಿ (Say it once in Kanglish so it sticks):
    → "ಮೂರು pointers — i (nums1 ಕೊನೆ real element), j (nums2
        ಕೊನೆ element), k (nums1 ಕೊನೆ empty slot). i, j ಎರಡರ
        values compare ಮಾಡಿ, ಯಾವುದು ದೊಡ್ಡದೋ ಅದನ್ನ k ಗೆ ಇಟ್ಟು,
        ಆ pointer ಅನ್ನ ಎಡಕ್ಕೆ ಸರಿಸು. ಕೊನೆಗೆ nums2 ಲ್ಲಿ ಏನಾದ್ರೂ
        ಉಳಿದಿದ್ರೆ ಅದನ್ನ ಕಾಪಿ ಮಾಡು."

  Time  : O(m + n)  →  Why: each element placed once
  Space : O(1)  →  Why: true in-place, no extra array

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🔍 DRY RUN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Input: nums1 = [1,2,3,0,0,0], m=3, nums2 = [2,5,6], n=3

  i=2(val=3) j=2(val=6) k=5

  →  variables: nums1[i]=3, nums2[j]=6  →  6 bigger → nums1[5]=6, j=1, k=4
     nums1 = [1,2,3,0,0,6]
  →  variables: nums1[i]=3, nums2[j]=5  →  5 bigger → nums1[4]=5, j=0, k=3
     nums1 = [1,2,3,0,5,6]
  →  variables: nums1[i]=3, nums2[j]=2  →  3 bigger → nums1[3]=3, i=1, k=2
     nums1 = [1,2,3,3,5,6]
  →  variables: nums1[i]=2, nums2[j]=2  →  tie, take nums2 → nums1[2]=2, j=-1, k=1
     nums1 = [1,2,2,3,5,6]

  j < 0 → loop ends. No leftover nums2 to copy.
  Output: [1,2,2,3,5,6]

  ಇನ್ನೊಂದು example — tricky case:
  Input: nums1=[0,0,0], m=0, nums2=[2,5,6], n=3
  i=-1 immediately (m=0), loop with i>=0 never runs
  j copies leftovers: nums1 becomes [2,5,6]
  Output: [2,5,6]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 ⚠️ EDGE CASES — ಇವನ್ನ ಮರೆಯಬೇಡ!
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  ✓ nums2 empty (n=0)?          →  nums1 unchanged, loop never runs
  ✓ nums1 real part empty (m=0)?  →  nums1 becomes exactly nums2
  ✓ All of nums2 smaller?       →  nums2 ends up at front
  ✓ Duplicate values across arrays?  →  [2] and [2] → both kept
  ✓ nums2 has leftovers after loop?  →  must explicitly copy them
    (most common bug in this pattern if forgotten!)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📊 COMPLEXITY SUMMARY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                Time      Space
  Brute Force   O(m+n)    O(m)
  Optimal       O(m+n)    O(1)    ← use this  

  Time ಯಾಕೆ O(m+n)?  → ಪ್ರತಿ element ಒಂದೇ ಸಲ place ಆಗುತ್ತೆ.
  Space ಯಾಕೆ O(1)?   → i, j, k ಮೂರು pointer variables ಸಾಕು.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🎯 PATTERN LEARNED — ಇದರಿಂದ ಕಲಿತದ್ದು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Pattern Name: Two Pointers — Merge From the Back

  ಈ pattern ಯಾವಾಗ use ಮಾಡಬೇಕು?
  → In-place merge ಮಾಡ್ಬೇಕಾದ buffer ಕೊನೇಲಿ extra room ಇದ್ದಾಗ
    (front ಅಲ್ಲ) — largest values ಮೊದಲು, backward ಆಗಿ ಬರೆಯಿರಿ
  → ಒಂದು pointer ಮೊದಲು ಖಾಲಿ ಆದ್ರೆ, ಇನ್ನೊಂದರ LEFTOVER ಅನ್ನ
    explicit ಆಗಿ copy ಮಾಡೋದನ್ನ ಮರೀಬೇಡಿ

  ಇದೇ pattern ಬೇರೆ problems ನಲ್ಲಿ ಕಾಣಿಸುತ್ತೆ:
  → Merge Sort ನ merge step (front-to-back version)
  → Sort a nearly-sorted array with limited extra buffer problems

  Next time ಇಂತಹ problem ಬಂದ್ರೆ ನಾನು ಮೊದಲು ಇದನ್ನ think ಮಾಡ್ತೇನೆ:
  → "In-place merge, extra room ಕೊನೇಲಿ ಇದ್ಯಾ? ಇದ್ರೆ back ಇಂದ
      merge ಮಾಡು, front ಇಂದ ಅಲ್ಲ."

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🗣️ INTERVIEW ನಲ್ಲಿ ಹೇಗೆ EXPLAIN ಮಾಡಬೇಕು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  1. Understand:
     "So I need to merge nums2 into nums1 in-place, and nums1
      already has trailing empty room sized exactly for nums2."

  2. Brute force:
     "I could copy nums1's real part to a temp array and merge
      normally, but that costs O(m) extra space."

  3. Optimize:
     "Merging from the front risks overwriting nums1 values I
      haven't read yet. If I merge from the BACK instead, placing
      the largest remaining value into the last empty slot, I
      never overwrite data I still need."

  4. Code:
     "Three pointers: i for nums1's last real element, j for
      nums2's last element, k for the last write slot. Whichever
      of nums1[i]/nums2[j] is bigger goes to nums1[k]."

  5. Complexity:
     "Time O(m+n) — each element placed once. Space O(1) — true
      in-place."

  ಮುಖ್ಯ: ಸುಮ್ಮನೆ ಕೂತು code ಬರೆಯಬೇಡ!
         Interviewer ಗೆ ನಿನ್ನ thinking process ಕಾಣಬೇಕು.
"""


# ═══════════════════════════════════════════════════════════════════
# BRUTE FORCE — O(m+n) Time | O(m) Space
# ═══════════════════════════════════════════════════════════════════
def merge_brute(nums1, m, nums2, n):
    """ಇದು ಮೊದಲ ಆಲೋಚನೆ — temp copy ಮಾಡಿ front-to-back merge"""
    temp = nums1[:m]
    i = j = k = 0
    while i < m and j < n:
        if temp[i] <= nums2[j]:
            nums1[k] = temp[i]
            i += 1
        else:
            nums1[k] = nums2[j]
            j += 1
        k += 1
    while i < m:
        nums1[k] = temp[i]
        i += 1
        k += 1
    while j < n:
        nums1[k] = nums2[j]
        j += 1
        k += 1
    return nums1


# ═══════════════════════════════════════════════════════════════════
# OPTIMAL — O(m+n) Time | O(1) Space
# ═══════════════════════════════════════════════════════════════════
def merge(nums1, m, nums2, n):
    """ಇದು final answer — three pointers, merge from the back"""
    i = m - 1
    j = n - 1
    k = m + n - 1

    while i >= 0 and j >= 0:
        if nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
        k -= 1

    while j >= 0:
        nums1[k] = nums2[j]
        j -= 1
        k -= 1

    return nums1


# ═══════════════════════════════════════════════════════════════════
# TEST CASES
# ═══════════════════════════════════════════════════════════════════
if __name__ == "__main__":
    import sys
    sys.stdout.reconfigure(encoding="utf-8")   # Windows cp1252 can't print   otherwise

    # Test 1 — Basic example
    assert merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3) == [1, 2, 2, 3, 5, 6]

    # Test 2 — Edge case: nums2 empty
    assert merge([1, 2, 3], 3, [], 0) == [1, 2, 3]

    # Test 3 — Edge case: nums1 real part empty
    assert merge([0, 0, 0], 0, [2, 5, 6], 3) == [2, 5, 6]

    # Test 4 — Tricky: nums2 all smaller
    assert merge([4, 5, 6, 0, 0, 0], 3, [1, 2, 3], 3) == [1, 2, 3, 4, 5, 6]

    print("All tests passed!  ")
