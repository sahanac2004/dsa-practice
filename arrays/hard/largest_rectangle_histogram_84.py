"""
╔══════════════════════════════════════════════════════════════════╗
║  LARGEST RECTANGLE IN HISTOGRAM                                     ║
║  LeetCode #84  |  Difficulty: Hard  |  Topic: Arrays / Monotonic Stack ║
║  Link: https://leetcode.com/problems/largest-rectangle-in-histogram/ ║
╚══════════════════════════════════════════════════════════════════╝

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📘 SECTION 1 — PROBLEM UNDERSTANDING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Given an array of bar heights forming a histogram (each bar has
  width 1), find the area of the largest rectangle that can be formed
  using contiguous bars.

  Input : heights = [2,1,5,6,2,3]
  Output: 10

  Example 1 — basic:
    Input : heights = [2,1,5,6,2,3]
    Output: 10
    Why?  : bars at indices 2,3 (heights 5,6) form a rectangle of
             height 5 and width 2 → area 10

  Example 2 — slightly tricky (all same height):
    Input : heights = [4,4,4,4]
    Output: 16
    Why?  : the entire histogram is one rectangle, height 4, width 4

  Constraints:
    - 1 <= heights.length <= 10^5
    - 0 <= heights[i] <= 10^4

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🧠 SECTION 2 — KANGLISH THINKING — ಹೇಗೆ ಯೋಚಿಸಬೇಕು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  Problem odi aada mele namma brain enu think maadabeeku:

  ಹಂತ 1 — Problem ಅರ್ಥ ಮಾಡಿಕೊಳ್ಳಿ (What are they asking?)
  ┌─────────────────────────────────────────────────────────┐
  │  Input ಏನು ಕೊಡ್ತಾರೆ?  →  bar heights (width=1 ಪ್ರತಿಯೊಂದೂ)│
  │  Output ಏನು ಬೇಕು?     →  ಅತ್ಯಂತ ದೊಡ್ಡ rectangle area,     │
  │                          contiguous bars use ಮಾಡಿ         │
  │  Constraints ಏನಿದೆ?   →  n<=10^5, height 0 ಆಗ್ಬೋದು        │
  └─────────────────────────────────────────────────────────┘

  ಹಂತ 2 — ನನಗೆ ಗೊತ್ತಿರೋ simple way ಏನು? (Brute force thought)
  →  ಪ್ರತಿ bar i ಗೂ, ಅದನ್ನ "shortest bar" ಆಗಿ ಇಟ್ಕೊಂಡು, ಎಡ ಮತ್ತು
     ಬಲಗಡೆ ಎಷ್ಟು ದೂರ ವಿಸ್ತಾರ ಆಗ್ಬೋದು (height[i] ಗಿಂತ ಕಡಿಮೆ ಬಾರ್ ಸಿಗೋ
     ತನಕ) ಅಂತ ಹುಡುಕಿ area = height[i] * width ಲೆಕ್ಕ ಹಾಕಿ max ತಗೊಳ್ಳೋದು.
  →  ಆದರೆ ಇದು slow ಯಾಕೆ? → ಪ್ರತಿ bar ಗೂ ಎಡ/ಬಲ scan ಮಾಡಿದ್ರೆ O(n²),
     n=10^5 ಗೆ TLE.

  ಹಂತ 3 — Better way ಹೇಗೆ ಯೋಚಿಸುವುದು? (Optimization thought)
  →  ಪ್ರತಿ bar i ಗೆ, "ಎಡಗಡೆ ಎಷ್ಟು ದೂರ height[i] ಗಿಂತ ಕಡಿಮೆ bar ಇಲ್ಲ"
     ಮತ್ತು "ಬಲಗಡೆ ಎಷ್ಟು ದೂರ height[i] ಗಿಂತ ಕಡಿಮೆ bar ಇಲ್ಲ" ಅಂತ ಮೊದಲೇ
     ಗೊತ್ತಿದ್ರೆ, area ನೇರ ಲೆಕ್ಕ ಹಾಕ್ಬೋದು — "next smaller element"
     problem ಥರ ಕಾಣುತ್ತೆ!
  →  ಅಹಾ moment: Monotonic increasing stack ಇಟ್ಕೊಂಡು, ಒಂದು bar
     height ಗಿಂತ ಕಡಿಮೆ ಬಂದಾಗ, stack ಇಂದ pop ಮಾಡ್ತಾ ಆ popped bar
     "smallest bar" ಆಗಿರೋ rectangle area ಲೆಕ್ಕ ಹಾಕ್ಬೋದು — width =
     current index - (new stack top index) - 1 (ಅಥವಾ current index,
     stack empty ಆದ್ರೆ).
  →  ಇದರಿಂದ ನಾವು Monotonic Stack (Increasing — Find Left/Right
     Smaller Boundary) use ಮಾಡಬಹುದು!

  ಹಂತ 4 — Technique ಯಾಕೆ ಇಲ್ಲಿ ಕೆಲಸ ಮಾಡುತ್ತೆ?
  →  ಒಂದು bar ನ rectangle ಅನ್ನ ಎಷ್ಟು ವಿಸ್ತಾರ ಮಾಡ್ಬೋದು ಅನ್ನೋದು, ಅದರ
     ಎಡ ಮತ್ತು ಬಲಗಡೆ ಇರೋ "ಮೊದಲ ಕಡಿಮೆ height" ಇಂದ decide ಆಗುತ್ತೆ —
     classic "next smaller/previous smaller element" pattern.
  →  Monotonic increasing stack ಇಂದ, ಒಂದು ಸಲ pop ಆದ bar ಗೆ, ಅದರ
     right boundary (current index) ಮತ್ತು left boundary (new top)
     ಎರಡೂ ಒಟ್ಟಿಗೆ ಗೊತ್ತಾಗುತ್ತೆ — O(1) amortized per element.
  →  ಪ್ರತಿ index ಗೂ push+pop ಒಂದು ಸಲ ಮಾತ್ರ ಆಗೋದ್ರಿಂದ, total O(n).

  💡 Interview ನಲ್ಲಿ ಹೇಗೆ ಮಾತಾಡಬೇಕು (Think out loud):
  →  "The naive way expands left/right from every bar directly —
      O(n²), too slow for n up to 10^5."
  →  "This resembles the 'next smaller element' pattern — for each
      bar, I need to know how far it can extend before hitting a
      shorter bar on either side."
  →  "A monotonic increasing stack finds exactly that boundary: when
      a shorter bar arrives, everything taller on the stack gets
      popped and its rectangle area finalized in O(1) amortized time."

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🏷️ SECTION 3 — TECHNIQUE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Primary   : Monotonic Stack → Increasing (Next Smaller Element Boundary)
  Secondary : None

  WHY this technique?
  → Each bar's maximal rectangle width is bounded by the nearest
    shorter bar on the left and right — a "next smaller element" query
  → A monotonic increasing stack finds both boundaries for a bar in a
    single amortized O(1) operation, when it gets popped
  → Every index is pushed and popped at most once, guaranteeing O(n)
    total work despite the nested-looking pop loop

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 💡 SECTION 4 — INTUITION (How to think — English)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Key observation: for any bar, the widest rectangle with that bar's
  height as the limiting height extends exactly until a shorter bar
  appears on each side. Maintaining a stack of indices with
  increasing heights means: whenever the current bar is shorter than
  the stack's top, the top bar can't extend any further right — pop
  it and compute its area using the current index as the right
  boundary and the new stack top as the left boundary.

  The journey from brute to optimal:
    Brute thought   →  expand left/right from every bar individually
    Problem with it →  O(n²), too slow for large n
    Better question →  "can I precompute, for every bar, the nearest
                        shorter bar on each side in one pass?"
    Insight         →  a monotonic increasing stack naturally reveals
                        both boundaries the moment a bar gets popped
    Optimal         →  single pass with a stack, O(n) time, O(n) space

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🐢 SECTION 5 — APPROACH 1 — BRUTE FORCE (Expand Left/Right Per Bar)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    For each bar i, expand left and right as far as possible while
    the bars are at least as tall as heights[i], and compute the
    area with that width.

  Pseudocode:
    step 1: best = 0
    step 2: for i in range(n):
    step 3:   left = i; while left > 0 and heights[left-1] >= heights[i]: left -= 1
    step 4:   right = i; while right < n-1 and heights[right+1] >= heights[i]: right += 1
    step 5:   best = max(best, heights[i] * (right - left + 1))
    step 6: return best

  Time  : O(n²)  →  Why: for each bar, an O(n) expansion in the worst case
  Space : O(1)   →  Why: no extra structures beyond loop variables

  ಇದು ಯಾಕೆ ಸಾಕಾಗಲ್ಲ? (Why is this not enough?)
    → n=10^5 ಆದ್ರೆ n² = 10^10 — TLE ಆಗತ್ತೆ.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🚶 SECTION 6 — APPROACH 2 — BETTER (if exists)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    No natural polynomial-but-not-optimal middle step — the moment
    you recognize the "next smaller element" structure, the monotonic
    stack approach is the direct optimal solution.

  Time  : —
  Space : —

  ಇನ್ನೂ better ಮಾಡಬಹುದಾ? → ಇದೇ optimal, directly SECTION 7 ಗೆ ಹೋಗೋಣ.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🚀 SECTION 7 — APPROACH 3 — OPTIMAL   (Monotonic Increasing Stack)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    Maintain a stack of indices with strictly increasing bar heights.
    For each bar, while the stack's top has a height >= current
    height, pop it and compute its area (height = popped bar's
    height, width = current index - new top index - 1, or current
    index if the stack is now empty). After the main pass, process
    any bars still left on the stack using n as the right boundary.

  Key steps:
    1. stack = []; best = 0
    2. for i in range(n) [with an extra pass using height 0 at the end
       to flush the stack, or handle the leftover stack explicitly]:
         while stack and heights[stack[-1]] >= heights[i]:
           top_height = heights[stack.pop()]
           width = i - stack[-1] - 1 if stack else i
           best = max(best, top_height * width)
         stack.append(i)
    3. flush remaining stack entries using n as the right boundary
    4. return best

  ಕನ್ನಡದಲ್ಲಿ ಒಂದು ಸಲ ಹೇಳಿ (Kanglish one-liner so it sticks):
    → "Increasing heights ನ stack (indices) ಇಟ್ಕೊಂಡು, current bar
        stack top ಗಿಂತ ಕಡಿಮೆ ಆದ್ರೆ pop ಮಾಡಿ, ಆ popped bar ನ height ಇಂದ
        area = height * (current_i - new_top_i - 1) ಲೆಕ್ಕ ಹಾಕು.
        ಕೊನೆಗೆ ಉಳಿದ stack ಅನ್ನ n ಅನ್ನ right boundary ಆಗಿ ಇಟ್ಕೊಂಡು
        ಅದೇ ಥರ flush ಮಾಡು!"

  Time  : O(n)  →  Why: each index is pushed and popped at most once
                    (amortized), total work bounded by O(n)
  Space : O(n)  →  Why: stack can hold up to n indices in the worst case
                    (strictly increasing heights)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🔍 SECTION 8 — DRY RUN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Input: heights = [2,1,5,6,2,3]  (n=6)

  i=0 (h=2): stack empty → push 0 → stack=[0]
  i=1 (h=1): heights[stack top=0]=2 >= 1 → pop 0, top_height=2,
             stack empty → width=1 → area=2*1=2 → best=2
             stack empty → push 1 → stack=[1]
  i=2 (h=5): heights[1]=1 < 5 → no pop → push 2 → stack=[1,2]
  i=3 (h=6): heights[2]=5 < 6 → no pop → push 3 → stack=[1,2,3]
  i=4 (h=2): heights[3]=6 >= 2 → pop 3, top_height=6, new top=2,
             width=4-2-1=1 → area=6*1=6 → best=6
             heights[2]=5 >= 2 → pop 2, top_height=5, new top=1,
             width=4-1-1=2 → area=5*2=10 → best=10
             heights[1]=1 < 2 → no more pop → push 4 → stack=[1,4]
  i=5 (h=3): heights[4]=2 < 3 → no pop → push 5 → stack=[1,4,5]

  Flush remaining stack with right boundary n=6:
    pop 5, top_height=3, new top=4, width=6-4-1=1 → area=3*1=3 → best stays 10
    pop 4, top_height=2, new top=1, width=6-1-1=4 → area=2*4=8 → best stays 10
    pop 1, top_height=1, stack empty, width=6 → area=1*6=6 → best stays 10

  Output: 10   matches expected

  ಇನ್ನೊಂದು example — tricky case (all same height):
  Input: heights = [4,4,4,4]

  Since heights are non-decreasing (equal, not strictly less), the
  `>=` comparison pops earlier-equal bars only once true equality
  triggers — each bar pushed without popping until the flush phase,
  where the leftmost bar ends up covering the full width 4 at height
  4 → area = 16.

  Output: 16   matches expected

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 ⚠️ SECTION 9 — EDGE CASES — ಇವನ್ನ ಮರೆಯಬೇಡ!
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  ✓ Single bar?                  →  area = that bar's height * 1,
                                     trivially correct
  ✓ All same height?             →  entire array becomes one
                                     rectangle at the flush step
  ✓ Strictly increasing heights? →  nothing pops during the main
                                     loop; the flush phase handles
                                     all bars, each getting its full
                                     leftward extent
  ✓ Strictly decreasing heights? →  every bar pops almost
                                     immediately, forming n small
                                     rectangles compared for the max
  ✓ Height 0 present?            →  contributes area 0 wherever it
                                     appears, never wins the max but
                                     doesn't break the stack logic

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📊 SECTION 10 — COMPLEXITY SUMMARY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                Time      Space
  Brute Force   O(n²)     O(1)
  Optimal       O(n)      O(n)    ← use this

  Time yaake ashtu?  → ಪ್ರತಿ index ಒಂದೇ ಸಲ push ಆಗುತ್ತೆ, ಒಂದೇ ಸಲ pop
                        ಆಗುತ್ತೆ — amortized O(1) per element, total O(n).
  Space yaake ashtu? → worst case (strictly increasing heights)
                        stack ನಲ್ಲಿ ಎಲ್ಲಾ n indices ಇರ್ಬೋದು.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🎯 SECTION 11 — PATTERN LEARNED — ಇದರಿಂದ ಕಲಿತದ್ದು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Pattern Name: Monotonic Stack — Next Smaller Element Boundary

  Ee pattern yaavaaga use maadabeeku?
  → "Largest rectangle/area bounded by shorter neighbors" ಥರ problem
    ಕೇಳಿದಾಗ
  → "Next/previous smaller (or greater) element" ಥರ boundary-finding
    problem ಆಗಿ reframe ಮಾಡ್ಬಹುದಾ ಅಂತ ಗುರುತಿಸಿದಾಗ
  → O(n²) brute force ಇದ್ರೆ, ಮತ್ತೆ ಮತ್ತೆ ಎಡ/ಬಲ scan ಮಾಡ್ತಿದ್ರೆ

  Idee pattern beere problemsalli kaanisatte:
  → Maximal Rectangle (LC 85) — extends this exact idea to a 2D binary matrix
  → Trapping Rain Water (already solved in this repo) — related but
    uses two-pointer instead of monotonic stack
  → Next Greater Element I/II (LC 496/503) — same monotonic stack
    mechanics, different boundary condition

  Next time intaha problem bandre naanu modalu idannu think maadtene:
  → "'Bounded by shorter/smaller neighbor' anta kanda takshana,
      monotonic stack track maadi, pop aadaga area/answer calculate
      maadu anta modalu yochisu."

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🗣️ SECTION 12 — INTERVIEWALLI HEGE EXPLAIN MAADABEEKU
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  1. Understand:
     "I need the largest rectangle area formable from contiguous bars
      in a histogram, where the rectangle's height is limited by the
      shortest bar it spans."

  2. Brute force:
     "For each bar, expand left and right until a shorter bar is hit
      — O(n²), too slow for n up to 10^5."

  3. Optimize:
     "This is a 'next smaller element' boundary problem — I can find,
      for every bar, the nearest shorter bar on each side using a
      monotonic increasing stack, in one linear pass."

  4. Code:
     "Push indices onto a stack while heights are increasing. When a
      shorter bar arrives, pop the taller ones, computing each
      popped bar's area using the current index as the right bound
      and the new stack top as the left bound. Flush any leftovers
      at the end using n as the right bound."

  5. Complexity:
     "Time O(n) — each index is pushed and popped once. Space O(n)
      — the stack in the worst case holds every index."

  Mukhya: summane kuutu code bareyabeda! Interviewer ge ninna thinking
          process kaanabeku.
"""


# ═══════════════════════════════════════════════════════════════════
# BRUTE FORCE — O(n^2) Time | O(1) Space  (Expand Left/Right Per Bar)
# ═══════════════════════════════════════════════════════════════════
def largest_rectangle_brute(heights):
    """Idu modala aaloochane — prati bar geeu edaa/balagade expand maadi area lekka haakodu"""
    n = len(heights)
    best = 0
    for i in range(n):
        left = i
        while left > 0 and heights[left - 1] >= heights[i]:
            left -= 1
        right = i
        while right < n - 1 and heights[right + 1] >= heights[i]:
            right += 1
        best = max(best, heights[i] * (right - left + 1))
    return best


# ═══════════════════════════════════════════════════════════════════
# OPTIMAL — O(n) Time | O(n) Space  (Monotonic Increasing Stack)
# ═══════════════════════════════════════════════════════════════════
def largest_rectangle(heights):
    """Idu final answer — increasing stack ittukondu, pop aadaga area calculate maadu"""
    n = len(heights)
    stack = []
    best = 0

    for i in range(n + 1):
        current_height = heights[i] if i < n else 0
        while stack and heights[stack[-1]] >= current_height:
            top_height = heights[stack.pop()]
            width = i - stack[-1] - 1 if stack else i
            best = max(best, top_height * width)
        stack.append(i)

    return best


# ═══════════════════════════════════════════════════════════════════
# TEST CASES
# ═══════════════════════════════════════════════════════════════════
if __name__ == "__main__":
    import sys
    sys.stdout.reconfigure(encoding="utf-8")

    # Test 1 — Basic example
    assert largest_rectangle([2, 1, 5, 6, 2, 3]) == 10

    # Test 2 — Edge case: single bar
    assert largest_rectangle([5]) == 5

    # Test 3 — Edge case: all same height
    assert largest_rectangle([4, 4, 4, 4]) == 16

    # Test 4 — Tricky: strictly increasing
    assert largest_rectangle([1, 2, 3, 4, 5]) == 9  # bars [3,4,5] -> 3*3

    # Test 5 — Tricky: strictly decreasing
    assert largest_rectangle([5, 4, 3, 2, 1]) == 9  # bars [5,4,3] -> 3*3

    # Test 6 — Edge case: height 0 present
    assert largest_rectangle([2, 0, 2]) == 2

    print("All tests passed!")
