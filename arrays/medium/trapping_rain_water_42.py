"""
╔══════════════════════════════════════════════════════════════════╗
║  TRAPPING RAIN WATER                                                ║
║  LeetCode #42  |  Difficulty: Hard  |  Topic: Arrays / Two Pointers ║
║  Link: https://leetcode.com/problems/trapping-rain-water/           ║
╚══════════════════════════════════════════════════════════════════╝

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📘 SECTION 1 — PROBLEM UNDERSTANDING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Given n non-negative integers representing an elevation map where
  the width of each bar is 1, compute how much rainwater it can trap
  after raining. Water sits above a bar only if there's a taller (or
  equal) bar on both its left and right somewhere in the array.

  Input : height = [0,1,0,2,1,0,1,3,2,1,2,1]
  Output: 6

  Example 1 — basic:
    Input : height = [0,1,0,2,1,0,1,3,2,1,2,1]
    Output: 6
    Why?  : water pools in the dips between taller bars, totalling 6 units

  Example 2 — slightly tricky (strictly increasing, no water trapped):
    Input : height = [1, 2, 3, 4, 5]
    Output: 0
    Why?  : no bar has a taller bar to its right, so nothing can pool
             above it

  Constraints:
    - n == height.length
    - 1 <= n <= 2 * 10^4
    - 0 <= height[i] <= 10^5

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🧠 SECTION 2 — KANGLISH THINKING — ಹೇಗೆ ಯೋಚಿಸಬೇಕು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  ಮೊದಲು problem odidaga ನಮ್ಮ brain ಏನು think ಮಾಡಬೇಕು:

  ಹಂತ 1 — Problem ಅರ್ಥ ಮಾಡಿಕೊಳ್ಳಿ (What are they asking?)
  ┌─────────────────────────────────────────────────────────┐
  │  Input ಏನು ಕೊಡ್ತಾರೆ?  →  bar heights ನ array (width=1)   │
  │  Output ಏನು ಬೇಕು?     →  total trapped water units       │
  │  Constraints ಏನಿದೆ?   →  n<=2*10^4, heights>=0           │
  └─────────────────────────────────────────────────────────┘

  ಹಂತ 2 — ನನಗೆ ಗೊತ್ತಿರೋ simple way ಏನು? (Brute force thought)
  →  ಪ್ರತಿ bar i ಗೂ, ಅದರ ಎಡಗಡೆ ಇರೋ tallest bar ಮತ್ತು ಬಲಗಡೆ ಇರೋ
     tallest bar ಹುಡುಕಿ, water = min(leftMax, rightMax) - height[i]
     (positive ಆದ್ರೆ ಮಾತ್ರ) ಅಂತ ಲೆಕ್ಕ ಹಾಕಿ ಎಲ್ಲಾ ಸೇರಿಸೋದು.
  →  ಆದರೆ ಇದು slow ಯಾಕೆ? → ಪ್ರತಿ bar ಗೂ ಎಡ ಮತ್ತು ಬಲ scan ಮಾಡಿದ್ರೆ
     O(n²).

  ಹಂತ 3 — Better way ಹೇಗೆ ಯೋಚಿಸುವುದು? (Optimization thought)
  →  leftMax ಮತ್ತು rightMax ಅನ್ನ ಪ್ರತಿ bar ಗೂ ಮತ್ತೆ ಮತ್ತೆ ಹುಡುಕೋ ಬದ್ಲು,
     precompute ಮಾಡಿ store ಮಾಡ್ಬೋದು — prefix max array (ಎಡಗಡೆ ಇಂದ) ಮತ್ತು
     suffix max array (ಬಲಗಡೆ ಇಂದ).
  →  ಅಹಾ moment: ಇನ್ನೂ ಒಂದು step ಮುಂದೆ ಹೋಗಿ ಯೋಚಿಸಿದ್ರೆ — leftMax ಮತ್ತು
     rightMax ಅನ್ನ two pointers (L, R) ಇಟ್ಕೊಂಡು, ಚಿಕ್ಕದಾಗಿರೋ side ಇಂದ
     ಮುಂದೆ ಹೋದ್ರೆ, extra arrays ಬೇಡ! ಯಾಕಂದ್ರೆ ಚಿಕ್ಕ side ನ max ಯಾವಾಗ್ಲೂ
     bottleneck ಆಗಿರುತ್ತೆ, ಅದೇ trapped water decide ಮಾಡುತ್ತೆ.
  →  ಇದರಿಂದ ನಾವು Two-Pointer (Shrinking from Both Ends, Track
     Left/Right Max) use ಮಾಡಬಹುದು!

  ಹಂತ 4 — Technique ಯಾಕೆ ಇಲ್ಲಿ ಕೆಲಸ ಮಾಡುತ್ತೆ?
  →  ಒಂದು bar ಮೇಲೆ trapped water = min(leftMax, rightMax) - height[i]
     — ಯಾವಾಗ್ಲೂ ಚಿಕ್ಕ side ಯೇ limiting factor.
  →  L ಮತ್ತು R pointers ಇಂದ, height[L] < height[R] ಆದ್ರೆ leftMax ಗೊತ್ತಿದ್ರೆ
     ಸಾಕು (rightMax ಎಷ್ಟೇ ಇರ್ಲಿ, height[L] side ಇಂದ decide ಆಗುತ್ತೆ,
     ಯಾಕಂದ್ರೆ ಎಲ್ಲೋ ಬಲಗಡೆ height[R] >= height[L] ಇರೋ bar ಇದ್ದೇ ಇರುತ್ತೆ).
  →  ಇದೇ symmetric logic ಬಲಗಡೆಗೂ ಅನ್ವಯ ಆಗುತ್ತೆ — ಆದ್ದರಿಂದ ಎರಡು extra
     arrays ಬೇಡ, ಒಂದೇ pass ಸಾಕು.

  💡 Interview ನಲ್ಲಿ ಹೇಗೆ ಮಾತಾಡಬೇಕು (Think out loud):
  →  "The naive way finds the left-max and right-max for every bar by
      rescanning — O(n²), too slow for n up to 2*10^4."
  →  "I can precompute left-max and right-max arrays in two passes to
      avoid rescanning — O(n) time but O(n) extra space."
  →  "I notice that whichever side has the smaller max is always the
      bottleneck for that pointer's water level, so I can shrink two
      pointers inward tracking running maxes, needing no extra arrays."

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🏷️ SECTION 3 — TECHNIQUE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Primary   : Two-Pointer → Opposite Ends (Shrinking Inward)
  Secondary : Running Max Tracking (leftMax / rightMax)

  WHY this technique?
  → Water above any bar is capped by the SMALLER of its left-max and
    right-max, so the smaller-max side can always be resolved safely
  → Moving the pointer on the smaller-max side guarantees correctness:
    the other side's true max (even if unknown yet) is always >= current
  → Eliminates the need for separate O(n) prefix/suffix max arrays,
    cutting space from O(n) to O(1)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 💡 SECTION 4 — INTUITION (How to think — English)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Key observation: the water level at any position is
  min(leftMax, rightMax) - height[i]. If leftMax < rightMax at a given
  pointer position, then the current bar's water is fully determined
  by leftMax alone — whatever rightMax turns out to be, it's already
  known to be >= leftMax, so it can't be the limiting factor. This
  lets two pointers close in from both ends, always processing the
  side with the smaller running max.

  The journey from brute to optimal:
    Brute thought   →  for each bar, rescan left and right for the max
    Problem with it →  O(n²), repeated rescanning
    Better question →  "can I precompute the maxes instead of
                        rescanning every time?"
    Insight         →  the smaller of leftMax/rightMax is always the
                        bottleneck — no need to know the exact other
                        max, just that it's >= the smaller one
    Optimal         →  two pointers from both ends, track running
                        leftMax/rightMax, O(n) time, O(1) space

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🐢 SECTION 5 — APPROACH 1 — BRUTE FORCE (Rescan Left/Right Per Bar)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    For each index i, scan leftward for the max height and rightward
    for the max height; add min(leftMax, rightMax) - height[i] to the
    total if positive.

  Pseudocode:
    step 1: total = 0
    step 2: for i in range(n):
    step 3:   leftMax = max(height[0..i])
    step 4:   rightMax = max(height[i..n-1])
    step 5:   total += max(0, min(leftMax, rightMax) - height[i])
    step 6: return total

  Time  : O(n²)  →  Why: for each of n bars, an O(n) scan in each direction
  Space : O(1)   →  Why: no extra arrays, just running scan variables

  ಇದು ಯಾಕೆ ಸಾಕಾಗಲ್ಲ? (Why is this not enough?)
    → n=2*10^4 ಆದ್ರೆ n² = 4*10^8 — TLE ಆಗ್ಬೋದು.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🚶 SECTION 6 — APPROACH 2 — BETTER (Prefix/Suffix Max Arrays)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    Precompute leftMax[i] = max height from 0..i, and rightMax[i] =
    max height from i..n-1, in two linear passes. Then a third pass
    computes min(leftMax[i], rightMax[i]) - height[i] for each bar.

  Time  : O(n)  →  three linear passes (left pass, right pass, sum pass)
  Space : O(n)  →  two extra arrays of size n

  ಇನ್ನೂ better ಮಾಡಬಹುದಾ? → ಹೌದು — two-pointer ಇಂದ, ಈ ಎರಡು arrays
  ಬೇಡ ಆಗುತ್ತೆ, running leftMax/rightMax variables ಮಾತ್ರ ಸಾಕು, O(1)
  space ಗೆ ಇಳಿಸ್ಬೋದು.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🚀 SECTION 7 — APPROACH 3 — OPTIMAL   (Two-Pointer, Track Running Max)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    Start L=0, R=n-1, leftMax=0, rightMax=0. At each step, move the
    pointer on the side with the smaller height, updating that side's
    running max and adding (runningMax - height[pointer]) to the total
    (only positive contributions occur since runningMax >= height at
    that pointer by construction).

  Key steps:
    1. L, R = 0, n-1; leftMax = rightMax = 0; total = 0
    2. while L < R:
    3.   if height[L] <= height[R]:
    4.     leftMax = max(leftMax, height[L])
    5.     total += leftMax - height[L]; L += 1
    6.   else:
    7.     rightMax = max(rightMax, height[R])
    8.     total += rightMax - height[R]; R -= 1
    9. return total

  ಕನ್ನಡದಲ್ಲಿ ಒಂದು ಸಲ ಹೇಳಿ (Say it once in Kanglish so it sticks):
    → "L ಮತ್ತು R ಅನ್ನ ಎರಡು ends ಇಂದ ಇಟ್ಕೊಂಡು, height[L] <= height[R]
        ಆದ್ರೆ leftMax update ಮಾಡಿ leftMax - height[L] ಅನ್ನ total ಗೆ
        ಸೇರಿಸಿ L++ ಮಾಡು. ಇಲ್ಲಾಂದ್ರೆ rightMax update ಮಾಡಿ rightMax -
        height[R] ಸೇರಿಸಿ R-- ಮಾಡು. L ಮತ್ತು R ಸೇರೋ ತನಕ repeat ಮಾಡು!"

  Time  : O(n)  →  Why: single pass, L and R together cover each index once
  Space : O(1)  →  Why: only pointers and two running max variables

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🔍 SECTION 8 — DRY RUN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]  (n=12)

  L=0,R=11: height[0]=0 <= height[11]=1 → leftMax=max(0,0)=0,
            total += 0-0=0 → total=0, L=1
  L=1,R=11: height[1]=1 <= height[11]=1 → leftMax=max(0,1)=1,
            total += 1-1=0 → total=0, L=2
  L=2,R=11: height[2]=0 <= height[11]=1 → leftMax=max(1,0)=1,
            total += 1-0=1 → total=1, L=3
  L=3,R=11: height[3]=2 > height[11]=1 → rightMax=max(0,1)=1,
            total += 1-1=0 → total=1, R=10
  L=3,R=10: height[3]=2 > height[10]=2 → equal→ take height[L]<=height[R]
            branch (2<=2 true) → leftMax=max(1,2)=2, total += 2-2=0
            → total=1, L=4
  L=4,R=10: height[4]=1 <= height[10]=2 → leftMax=max(2,1)=2,
            total += 2-1=1 → total=2, L=5
  L=5,R=10: height[5]=0 <= height[10]=2 → leftMax=max(2,0)=2,
            total += 2-0=2 → total=4, L=6
  L=6,R=10: height[6]=1 <= height[10]=2 → leftMax=max(2,1)=2,
            total += 2-1=1 → total=5, L=7
  L=7,R=10: height[7]=3 > height[10]=2 → rightMax=max(1,2)=2,
            total += 2-2=0 → total=5, R=9
  L=7,R=9: height[7]=3 > height[9]=1 → rightMax=max(2,1)=2,
           total += 2-1=1 → total=6, R=8
  L=7,R=8: height[7]=3 > height[8]=2 → rightMax=max(2,2)=2,
           total += 2-2=0 → total=6, R=7
  L=7,R=7: loop ends (L < R false)

  Output: 6   matches expected

  ಇನ್ನೊಂದು example — tricky case (strictly increasing):
  Input: height = [1, 2, 3, 4, 5]

  ಪ್ರತಿ step ನಲ್ಲೂ height[L] <= height[R] ಆಗಿರುತ್ತೆ (L side ಯಾವಾಗ್ಲೂ
  ಚಿಕ್ಕದು ಅಥವಾ equal), ಆದ್ರೆ leftMax ಯಾವಾಗ್ಲೂ height[L] ಗೆ ಸೇಮ್
  ಆಗಿರೋದ್ರಿಂದ (strictly increasing), total += 0 ಪ್ರತಿ ಸಲ.

  Output: 0   matches expected — no water can pool

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 ⚠️ SECTION 9 — EDGE CASES — ಇವನ್ನ ಮರೆಯಬೇಡ!
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  ✓ Single bar or empty array?   →  L>=R immediately, loop never
                                     runs, total stays 0
  ✓ Strictly increasing/          →  no bar has both sides taller,
    decreasing heights?              total remains 0
  ✓ All bars same height?        →  leftMax/rightMax always equal
                                     current height, total stays 0
  ✓ Single tall spike in middle? →  bars around it trap water up to
                                     their own surrounding max, spike
                                     itself contributes nothing
  ✓ Heights include 0s (valleys)? →  0-height bars can trap the full
                                     min(leftMax, rightMax) as water

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📊 SECTION 10 — COMPLEXITY SUMMARY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                Time      Space
  Brute Force   O(n²)     O(1)
  Better        O(n)      O(n)   (prefix/suffix max arrays)
  Optimal       O(n)      O(1)    ← use this

  Time ಯಾಕೆ ಅಷ್ಟು?  → L ಮತ್ತು R ಒಟ್ಟಿಗೆ ಸೇರಿ ಪ್ರತಿ index ಅನ್ನ ಒಮ್ಮೆ
                        ಮಾತ್ರ visit ಮಾಡ್ತಾವೆ — single pass, O(n).
  Space ಯಾಕೆ ಅಷ್ಟು? → leftMax, rightMax, L, R, total ಬಿಟ್ಟು ಬೇರೆ
                        ಏನೂ store ಮಾಡಲ್ಲ.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🎯 SECTION 11 — PATTERN LEARNED — ಇದರಿಂದ ಕಲಿತದ್ದು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Pattern Name: Two-Pointer with Running Max/Min (Smaller-Side-First)

  ಈ pattern ಯಾವಾಗ use ಮಾಡಬೇಕು?
  → Answer at each position depends on min/max of "everything to the
    left" and "everything to the right"
  → Prefix/suffix precompute arrays feel like O(n) space overkill —
    check if the smaller running value always safely decides the
    current answer
  → Two ends closing inward naturally applies (array-based, no
    ordering requirement beyond position)

  ಇದೇ pattern ಬೇರೆ problems ನಲ್ಲಿ ಕಾಣಿಸುತ್ತೆ:
  → Container With Most Water — same two-pointer-from-ends family
    (already solved in this repo)
  → Product of Array Except Self — prefix/suffix idea, different
    resolution (no two-pointer needed there)
  → Candy / Trapping Rain Water II (2D version) — same core idea
    extended to a grid

  Next time ಇಂತಹ problem ಬಂದ್ರೆ ನಾನು ಮೊದಲು ಇದನ್ನ think ಮಾಡ್ತೇನೆ:
  → "min(leftMax, rightMax) ಥರ formula ಕಂಡ ತಕ್ಷಣ, ಚಿಕ್ಕದಾಗಿರೋ side
      ಯಾವಾಗ್ಲೂ safe ಆಗಿ decide ಮಾಡುತ್ತೆ ಅಂತ ಗುರುತಿಸಿ, prefix/suffix
      arrays ಬದ್ಲು two-pointer ಇಂದ O(1) space ಗೆ ಇಳಿಸೋಕೆ ಆಗುತ್ತಾ ಅಂತ
      ಮೊದಲು ಯೋಚಿಸು."

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🗣️ SECTION 12 — INTERVIEWALLI HEGE EXPLAIN MAADABEEKU
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  1. Understand:
     "For each bar, water above it equals min(leftMax, rightMax) minus
      its own height, and I need the sum across the whole array."

  2. Brute force:
     "For each bar, rescan left and right for the max — O(n²), too
      slow for n up to 2*10^4."

  3. Optimize:
     "Precomputing prefix/suffix max arrays gets it to O(n) time but
      costs O(n) space. I can do better: whichever side has the
      smaller running max is always the bottleneck for that pointer,
      regardless of what the other side's exact max turns out to be."

  4. Code:
     "Use two pointers from both ends with running leftMax and
      rightMax. Move whichever pointer points to the smaller height,
      updating that side's max and adding the trapped water at that
      position, until the pointers meet."

  5. Complexity:
     "Time O(n) — L and R together visit each index once. Space
      O(1) — just a couple of running max variables and two pointers."

  ಮುಖ್ಯ: ಸುಮ್ಮನೆ ಕೂತು code ಬರೆಯಬೇಡ!
         Interviewer ಗೆ ನಿನ್ನ thinking process ಕಾಣಬೇಕು.
"""


# ═══════════════════════════════════════════════════════════════════
# BRUTE FORCE — O(n^2) Time | O(1) Space  (Rescan Left/Right Per Bar)
# ═══════════════════════════════════════════════════════════════════
def trap_brute(height):
    """ಇದು ಮೊದಲ ಆಲೋಚನೆ — ಪ್ರತಿ bar ಗೂ ಎಡ/ಬಲ rescan ಮಾಡಿ max ಹುಡುಕೋದು"""
    n = len(height)
    total = 0
    for i in range(n):
        left_max = max(height[:i + 1])
        right_max = max(height[i:])
        total += max(0, min(left_max, right_max) - height[i])
    return total


# ═══════════════════════════════════════════════════════════════════
# OPTIMAL — O(n) Time | O(1) Space  (Two-Pointer, Track Running Max)
# ═══════════════════════════════════════════════════════════════════
def trap(height):
    """ಇದು final answer — L,R two pointers ಇಂದ running max track ಮಾಡಿ trap ಮಾಡು"""
    if not height:
        return 0

    L, R = 0, len(height) - 1
    left_max = right_max = 0
    total = 0

    while L < R:
        if height[L] <= height[R]:
            left_max = max(left_max, height[L])
            total += left_max - height[L]
            L += 1
        else:
            right_max = max(right_max, height[R])
            total += right_max - height[R]
            R -= 1

    return total


# ═══════════════════════════════════════════════════════════════════
# TEST CASES
# ═══════════════════════════════════════════════════════════════════
if __name__ == "__main__":
    import sys
    sys.stdout.reconfigure(encoding="utf-8")   # Windows cp1252 can't print emoji otherwise

    # Test 1 — Basic example
    assert trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) == 6

    # Test 2 — Edge case: strictly increasing, no water trapped
    assert trap([1, 2, 3, 4, 5]) == 0

    # Test 3 — Edge case: single element / empty
    assert trap([5]) == 0
    assert trap([]) == 0

    # Test 4 — Tricky: all same height
    assert trap([3, 3, 3, 3]) == 0

    # Test 5 — Tricky: valley between two tall walls
    assert trap([5, 0, 0, 0, 5]) == 15

    print("All tests passed! ")
