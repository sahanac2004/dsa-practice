"""
╔══════════════════════════════════════════════════════════════════╗
║  CONTAINER WITH MOST WATER                                       ║
║  LeetCode #11  |  Difficulty: Medium  |  Topic: Arrays / Two Ptr  ║
║  Link: https://leetcode.com/problems/container-with-most-water/   ║
╚══════════════════════════════════════════════════════════════════╝

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📘 SECTION 1 — PROBLEM UNDERSTANDING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Given an array of heights (each index is a vertical line), pick
  two lines that, together with the x-axis, form a container that
  holds the MOST water. Return the maximum water area possible.

  Area between lines at i and j = min(height[i], height[j]) * (j - i)
  (limited by the shorter line, since water spills over the shorter side)

  Input : height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
  Output: 49

  Example 1 — basic:
    Input : height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    Output: 49
    Why?  : lines at index 1 (height 8) and index 8 (height 7) give
             min(8,7) * (8-1) = 7 * 7 = 49, the maximum possible

  Example 2 — slightly tricky (all same height):
    Input : height = [4, 4, 4, 4]
    Output: 12
    Why?  : any pair gives min(4,4) * distance; the widest pair
             (index 0 and 3) wins: 4 * 3 = 12

  Constraints:
    - 2 <= height.length <= 10^5
    - 0 <= height[i] <= 10^4
    - Must find the answer efficiently — brute force checking every
      pair is too slow for n up to 10^5

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🧠 SECTION 2 — KANGLISH THINKING — ಹೇಗೆ ಯೋಚಿಸಬೇಕು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  ಮೊದಲು problem odidaga ನಮ್ಮ brain ಏನು think ಮಾಡಬೇಕು:

  ಹಂತ 1 — Problem ಅರ್ಥ ಮಾಡಿಕೊಳ್ಳಿ (What are they asking?)
  ┌─────────────────────────────────────────────────────────┐
  │  Input ಏನು ಕೊಡ್ತಾರೆ?  →  ಪ್ರತಿ index ಗೆ ಒಂದು height     │
  │                          (vertical line) ಇರೋ array        │
  │  Output ಏನು ಬೇಕು?     →  ಎರಡು lines pick ಮಾಡಿ, ಅವುಗಳ    │
  │                          ನಡುವೆ ಹಿಡಿಯೋ ಗರಿಷ್ಠ water area   │
  │  Constraints ಏನಿದೆ?   →  n=10^5 ಇರ್ಬೋದು, O(n²) TLE ಆಗುತ್ತೆ│
  └─────────────────────────────────────────────────────────┘

  ಹಂತ 2 — ನನಗೆ ಗೊತ್ತಿರೋ simple way ಏನು? (Brute force thought)
  →  ಪ್ರತಿ pair (i, j) ಗೂ area = min(h[i],h[j]) * (j-i) ಲೆಕ್ಕ ಹಾಕಿ,
     max ಇಟ್ಟುಕೊಳ್ಳೋದು.
  →  ಆದರೆ ಇದು slow ಯಾಕೆ? → O(n²) pairs, n=10^5 ಗೆ 10^10 operations,
     TLE ಗ್ಯಾರಂಟಿ.

  ಹಂತ 3 — Better way ಹೇಗೆ ಯೋಚಿಸುವುದು? (Optimization thought)
  →  "ಎಲ್ಲಾ pairs check ಮಾಡೋ ಬದ್ಲು, ಅತ್ಯಂತ WIDE pair (index 0 ಮತ್ತು
     n-1) ಇಂದ ಶುರು ಮಾಡಿದ್ರೆ ಏನಾಗುತ್ತೆ?"
  →  ಅಹಾ moment: ಎರಡು ಪಕ್ಕ L, R pointers ಇಟ್ಟುಕೊಂಡು, ಚಿಕ್ಕ height
     ಇರೋ side ಅನ್ನ ಮಾತ್ರ ಒಳಗೆ move ಮಾಡಬೇಕು — ಯಾಕಂದ್ರೆ ದೊಡ್ಡ side
     move ಮಾಡಿದ್ರೆ width ಕಡಿಮೆ ಆಗುತ್ತೆ, height ಕೂಡ (min ಇಂದಾಗಿ)
     ಹೆಚ್ಚಾಗಲ್ಲ — area ಕಡಿಮೆ ಆಗೋದೇ ಗ್ಯಾರಂಟಿ. ಚಿಕ್ಕ side move
     ಮಾಡಿದ್ರೆ ಮಾತ್ರ ದೊಡ್ಡ height ಸಿಗೋ possibility ಇರುತ್ತೆ.
  →  ಇದರಿಂದ ನಾವು Two Pointers → Opposite Ends (greedy shrink) use
     ಮಾಡಬಹುದು!

  ಹಂತ 4 — Technique ಯಾಕೆ ಇಲ್ಲಿ ಕೆಲಸ ಮಾಡುತ್ತೆ?
  →  Area = min(height) × width. Width ಯಾವಾಗ್ಲೂ L,R ಒಳಗೆ ಬಂದಂತೆ
     ಕಡಿಮೆ ಆಗುತ್ತೆ — ಆದ್ದರಿಂದ ಪ್ರತಿ step ನಲ್ಲೂ height ಹೆಚ್ಚಿಸೋ
     ಪ್ರಯತ್ನ ಮಾಡಬೇಕು.
  →  ಚಿಕ್ಕ line ಅನ್ನೇ move ಮಾಡಿದ್ರೆ, ಒಂದೋ ದೊಡ್ಡ height ಸಿಗುತ್ತೆ
     (area ಜಾಸ್ತಿ ಆಗೋ ಚಾನ್ಸ್), ಇಲ್ಲಾಂದ್ರೆ ಚಿಕ್ಕದೇ ಆಗುತ್ತೆ (ಆದ್ರೂ
     ಬೇರೆ option ಕಳ್ಕೋಬಾರ್ದು ಅಂತ ಇದನ್ನೇ move ಮಾಡ್ಬೇಕು).
  →  ಪ್ರತಿ step ನಲ್ಲೂ current area track ಮಾಡ್ತಾ, L,R ಹತ್ತಿರ ಆಗೋ
     ತನಕ (L<R) continue ಮಾಡೋದ್ರಿಂದ ಎಲ್ಲಾ optimal candidates
     ಮಿಸ್ ಆಗಲ್ಲ.

  💡 Interview ನಲ್ಲಿ ಹೇಗೆ ಮಾತಾಡಬೇಕು (Think out loud):
  →  "The brute force checks every pair of lines — O(n²), too slow
      for n up to 10^5."
  →  "I notice area is limited by the shorter line and the distance
      between the lines. Starting from the widest possible pair and
      moving the shorter side inward only ever has a chance of
      increasing the area — moving the taller side can only shrink it."
  →  "So I can use two pointers from both ends, always moving the
      pointer at the shorter line, giving O(n)."

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🏷️ SECTION 3 — TECHNIQUE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Primary   : Two Pointers → Opposite Ends (greedy shrink toward center)
  Secondary : —

  WHY this technique?
  → Area = min(left, right) height × width — shrinking width can
    only help if it also grows the limiting (shorter) height
  → Moving the taller pointer can never improve the area, so the
    greedy rule (always move the shorter side) is provably safe
  → Single pass with two pointers converging gives O(n)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 💡 SECTION 4 — INTUITION (How to think)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Key observation: start with the widest container (both ends).
  From there, width only shrinks as the pointers move inward, so
  the only way to ever beat the current area is to find a taller
  limiting line. Moving the taller of the two pointers can never
  help (width shrinks, and the limiting height is still capped by
  the shorter side) — so always move the shorter one.

  The journey from brute to optimal:
    Brute thought   →  check every pair (i, j), O(n²)
    Problem with it →  too slow for n=10^5
    Better question →  "does moving the taller pointer ever help?"
    Insight         →  no — only moving the shorter pointer can
                        possibly increase the limiting height
    Optimal         →  two pointers from both ends, always move the
                        shorter one, track the best area seen

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🐢 SECTION 5 — APPROACH 1 — BRUTE FORCE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    Check every pair of lines (i, j), compute the area, keep the max.

  Pseudocode:
    step 1: best = 0
    step 2: for i in range(n): for j in range(i+1, n):
    step 3:   best = max(best, min(height[i], height[j]) * (j - i))
    step 4: return best

  Time  : O(n²)  →  Why: nested loop over all index pairs
  Space : O(1)   →  Why: only a running best value tracked

  ಇದು ಯಾಕೆ ಸಾಕಾಗಲ್ಲ? (Why is this not enough?)
    → n=10^5 ಆದ್ರೆ n² = 10^10 operations — TLE ಗ್ಯಾರಂಟಿ.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🚶 SECTION 6 — APPROACH 2 — BETTER (skip — brute jumps straight to optimal)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  ಇಲ್ಲಿ intermediate approach ಇಲ್ಲ — greedy two-pointer insight
  ಸಿಕ್ಕ ತಕ್ಷಣ ನೇರವಾಗಿ optimal ಗೆ ಹೋಗಬಹುದು.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🚀 SECTION 7 — APPROACH 3 — OPTIMAL   (Two Pointers, greedy shrink)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    Start with L=0, R=n-1 (the widest container). Compute the area,
    update the best seen so far, then move whichever pointer points
    to the SHORTER line inward (moving the taller one can never
    increase the area). Repeat until L meets R.

  Key steps:
    1. L, R = 0, n-1; best = 0
    2. While L < R:
         area = min(height[L], height[R]) * (R - L)
         best = max(best, area)
         if height[L] < height[R]: L += 1
         else: R -= 1
    3. Return best.

  ಕನ್ನಡದಲ್ಲಿ ಒಂದು ಸಲ ಹೇಳಿ (Say it once in Kanglish so it sticks):
    → "L=0, R=n-1 ಇಟ್ಟುಕೊಂಡು area = min(height[L],height[R]) * (R-L)
        ಲೆಕ್ಕ ಹಾಕಿ best update ಮಾಡು. height[L] < height[R] ಆದ್ರೆ
        L++ ಮಾಡು (ಚಿಕ್ಕ side move ಮಾಡು), ಇಲ್ಲಾಂದ್ರೆ R-- ಮಾಡು.
        L,R ಸೇರೋ ತನಕ ಇದನ್ನ repeat ಮಾಡು!"

  Time  : O(n)  →  Why: single pass, L and R together cover each index once
  Space : O(1)  →  Why: only a few scalar trackers (L, R, best)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🔍 SECTION 8 — DRY RUN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Input: height = [1, 8, 6, 2, 5, 4, 8, 3, 7]  (indices 0..8)

  L=0,R=8 → area=min(1,7)*8=8  → best=8  → height[0]=1<height[8]=7 → L=1
  L=1,R=8 → area=min(8,7)*7=49 → best=49 → height[1]=8>height[8]=7 → R=7
  L=1,R=7 → area=min(8,3)*6=18 → best=49 → height[1]=8>height[7]=3 → R=6
  L=1,R=6 → area=min(8,8)*5=40 → best=49 → equal → R=5 (else-branch moves R)
  L=1,R=5 → area=min(8,4)*4=16 → best=49 → height[1]=8>height[5]=4 → R=4
  L=1,R=4 → area=min(8,5)*3=15 → best=49 → height[1]=8>height[4]=5 → R=3
  L=1,R=3 → area=min(8,2)*2=4  → best=49 → height[1]=8>height[3]=2 → R=2
  L=1,R=2 → area=min(8,6)*1=6  → best=49 → height[1]=8>height[2]=6 → R=1, loop ends

  Output: 49 (matches expected)

  ಇನ್ನೊಂದು example — tricky case (all same height):
  Input: height = [4, 4, 4, 4]  (indices 0..3)
  L=0,R=3 → area=min(4,4)*3=12 → best=12 → equal → R=2
  L=0,R=2 → area=min(4,4)*2=8  → best=12 → equal → R=1
  L=0,R=1 → area=min(4,4)*1=4  → best=12 → equal → R=0, loop ends
  Output: 12

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 ⚠️ SECTION 9 — EDGE CASES — ಇವನ್ನ ಮರೆಯಬೇಡ!
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  ✓ Exactly 2 elements?           →  only one pair possible, returned directly as the answer
  ✓ All same height?              →  every pair area shrinks as width shrinks, widest pair wins
  ✓ Strictly increasing/decreasing heights? → two-pointer still finds the true max in one pass
  ✓ Height of 0 somewhere?        →  that line contributes 0 area whenever it's the limiting side, handled naturally
  ✓ Two equal tallest lines at the ends? → widest pair itself is often the answer (as in Example 2)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📊 SECTION 10 — COMPLEXITY SUMMARY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                Time      Space
  Brute Force   O(n²)     O(1)
  Optimal       O(n)      O(1)    ← use this ✅

  Time ಯಾಕೆ ಅಷ್ಟು?  → L ಮತ್ತು R ಒಟ್ಟಿಗೆ ಸೇರಿ ಪ್ರತಿ index ಅನ್ನ
                        ಒಂದೇ ಸಲ visit ಮಾಡ್ತಾರೆ — O(n).
  Space ಯಾಕೆ ಅಷ್ಟು? → L, R, best ಬಿಟ್ಟು ಬೇರೆ extra structure ಬೇಡ.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🎯 SECTION 11 — PATTERN LEARNED — ಇದರಿಂದ ಕಲಿತದ್ದು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Pattern Name: Two Pointers — Greedy Shrink from Widest

  ಈ pattern ಯಾವಾಗ use ಮಾಡಬೇಕು?
  → "width × min(height)" ಥರದ area/capacity maximize ಮಾಡೋ problem
    ಬಂದಾಗ
  → Widest option ಇಂದ ಶುರು ಮಾಡಿ, ಒಂದು side ಮಾತ್ರ move ಮಾಡಿದ್ರೆ
    improve ಆಗೋ possibility ಇದೆ ಅಂತ prove ಮಾಡ್ಬೋದಾಗ (greedy safe)

  ಇದೇ pattern ಬೇರೆ problems ನಲ್ಲಿ ಕಾಣಿಸುತ್ತೆ:
  → Trapping Rain Water (#42) — similar two-pointer, tracks max seen from both sides
  → 3Sum / 3Sum Closest (#15, #16) — same opposite-ends convergence idea
  → Largest Rectangle in Histogram (#84) — different technique, but same "shorter side limits" intuition

  Next time ಇಂತಹ problem ಬಂದ್ರೆ ನಾನು ಮೊದಲು ಇದನ್ನ think ಮಾಡ್ತೇನೆ:
  → "'ಎರಡು lines ಇಂದ area/capacity maximize ಮಾಡು' ಅಂದ್ರೆ, widest
      pair ಇಂದ ಶುರು ಮಾಡಿ, ಚಿಕ್ಕ side ಅನ್ನ ಮಾತ್ರ move ಮಾಡ್ತಾ
      ಹೋಗೋ two-pointer greedy ಯೋಚಿಸು."

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🗣️ SECTION 12 — INTERVIEW ನಲ್ಲಿ ಹೇಗೆ EXPLAIN ಮಾಡಬೇಕು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  1. Understand:
     "I need to pick two lines that, with the x-axis, form the
      container holding the most water — area is min(height) times
      the distance between them."

  2. Brute force:
     "Check every pair of lines and compute the area — O(n²), too
      slow for n up to 10^5."

  3. Optimize:
     "Starting from the widest possible container (both ends), width
      only shrinks as I move inward, so I should only move a pointer
      if it has a chance of increasing the limiting height. Moving
      the taller pointer never helps — only moving the shorter one
      can find something taller."

  4. Code:
     "Two pointers L=0, R=n-1. At each step compute the area, update
      the best, then move whichever pointer is at the shorter line
      inward. Stop when L meets R."

  5. Complexity:
     "Time O(n) — L and R together scan every index once. Space
      O(1) — just a few scalar trackers."

  ಮುಖ್ಯ: ಸುಮ್ಮನೆ ಕೂತು code ಬರೆಯಬೇಡ!
         Interviewer ಗೆ ನಿನ್ನ thinking process ಕಾಣಬೇಕು.
"""


# ═══════════════════════════════════════════════════════════════════
# BRUTE FORCE — O(n^2) Time | O(1) Space
# ═══════════════════════════════════════════════════════════════════
def max_area_brute(height):
    """ಇದು ಮೊದಲ ಆಲೋಚನೆ — every pair (i, j) check ಮಾಡಿ max area track"""
    n = len(height)
    best = 0
    for i in range(n):
        for j in range(i + 1, n):
            area = min(height[i], height[j]) * (j - i)
            best = max(best, area)
    return best


# ═══════════════════════════════════════════════════════════════════
# OPTIMAL — O(n) Time | O(1) Space  (Two Pointers, greedy shrink)
# ═══════════════════════════════════════════════════════════════════
def max_area(height):
    """ಇದು final answer — L,R widest ಇಂದ ಶುರು ಮಾಡಿ, ಚಿಕ್ಕ side move ಮಾಡ್ತಾ ಹೋಗೋದು"""
    left, right = 0, len(height) - 1
    best = 0

    while left < right:
        area = min(height[left], height[right]) * (right - left)
        best = max(best, area)
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return best


# ═══════════════════════════════════════════════════════════════════
# TEST CASES
# ═══════════════════════════════════════════════════════════════════
if __name__ == "__main__":
    import sys
    sys.stdout.reconfigure(encoding="utf-8")   # Windows cp1252 can't print emoji otherwise

    # Test 1 — Basic example
    assert max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49

    # Test 2 — Edge case: exactly 2 elements
    assert max_area([1, 1]) == 1

    # Test 3 — Edge case: all same height
    assert max_area([4, 4, 4, 4]) == 12

    # Test 4 — Tricky: a zero-height line in the middle should be skipped over
    assert max_area([1, 0, 1]) == 2

    print("All tests passed! ✅")
