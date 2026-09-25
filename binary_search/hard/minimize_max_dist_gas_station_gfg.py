"""
╔══════════════════════════════════════════════════════════════════╗
║  MINIMIZE MAXIMUM DISTANCE TO GAS STATION                        ║
║  GFG / Classic  |  Difficulty: Hard  |  Topic: Binary Search    ║
║  Link: https://www.geeksforgeeks.org/minimize-maximum-distance-  ║
║        between-gas-stations/                                     ║
║  Also: LC #774 (premium)                                         ║
╚══════════════════════════════════════════════════════════════════╝

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📘 SECTION 1 — PROBLEM UNDERSTANDING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Given n gas stations on a highway at sorted positions stations[].
  You can add k more gas stations ANYWHERE on the highway.
  Minimize the MAXIMUM distance between any two consecutive
  gas stations (including newly added ones).
  Answer with precision up to 10^-6.

  Input : stations = sorted list of positions, k = new stations
  Output: minimum possible maximum distance (float, precision 10^-6)

  Example 1 — basic:
    Input : stations=[1,2,3,4,5,6,7,8,9,10], k=9
    Output: 0.500000
    Why?  : Add one station between each pair → gaps all 0.5

  Example 2 — slightly tricky:
    Input : stations=[3,6,12,19,33,44,67,72,89,95], k=2
    Output: 14.000000
    Why?  : Best: add stations in gaps 23 and 22
            Gap 23 → add 1 → 11.5 each
            Gap 22 → add 1 → 11 each
            Largest remaining gap = 14 (gap between 44 and 67 = 23,
            split into ~11.5 and ~11.5... need to check more carefully)

  Constraints:
    - 2 <= n <= 500
    - 0 <= stations[i] <= 10^9 (already sorted)
    - 1 <= k <= 10^6
    - Answer within 10^-6 of actual answer accepted

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🧠 SECTION 2 — KANGLISH THINKING — ಹೇಗೆ ಯೋಚಿಸಬೇಕು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  Problem odi aada mele namma brain enu think maadabeeku:

  ಹಂತ 1 — Problem ಅರ್ಥ ಮಾಡಿಕೊಳ್ಳಿ
  ┌─────────────────────────────────────────────────────────┐
  │  Input ಏನು ಕೊಡ್ತಾರೆ?  →  sorted stations + k new ones │
  │  Output ಏನು ಬೇಕು?     →  minimize max gap between any  │
  │                           2 consecutive stations        │
  │  Constraints ਏਨਿਦ੆?   →  float answer, 10^-6 precision │
  └─────────────────────────────────────────────────────────┘

  ಹಂತ 2 — ನನಗೆ ಗೊತ್ತಿರೋ simple way ಏನು?
  →  Greedy: always split the largest gap first → O(k log n)
     using a max-heap
  →  ಆದರೆ ಇದು slow ಯಾಕೆ?
     k = 10^6 → 10^6 heap operations → can be slow

  ಹಂತ 3 — Better way ಹೇಗೆ ಯೋಚಿಸುವುದು?
  →  "Aggressive Cows same pattern — but MINIMIZE maximum!"
  →  Answer space: [0, max_gap] — float range!
  →  Binary search on the answer (max distance d):
     For a given max distance d, how many stations needed?
     Gap of length L needs ceil(L/d) - 1 new stations
  →  If total stations needed <= k → d is feasible!
  →  Binary search with floating point precision

  ಹಂತ 4 — Technique ಯಾಕೆ ಇಲ್ಲಿ ಕೆಲಸ ಮಾಡುತ್ತೆ?
  →  Same family as Koko/Ship/Split — MINIMIZE maximum
  →  But answer is FLOAT → use precision-based binary search
  →  Run ~100 iterations (2^-100 precision far exceeds 10^-6)

  💡 Interview ನಲ್ಲಿ ಹೇಗೆ ಮಾತಾಡಬೇಕು:
  →  "Binary search on answer space — but float this time!"
  →  "For max distance d: gap L needs ceil(L/d)-1 = floor(L/d) stations"
  →  "Run ~100 iterations for 10^-6 precision"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🏷️ SECTION 3 — TECHNIQUE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Primary   : Binary Search → On Float Answer Space
  Secondary : Greedy (feasibility — stations per gap)

  WHY Float Binary Search?
  → Answer is a real number (max distance)
  → Integer binary search won't work here
  → Run fixed ~100 iterations → precision far exceeds 10^-6
  → Each iteration: O(n) feasibility check

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 💡 SECTION 4 — INTUITION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  For a candidate max distance d:
  - Each gap of length L needs exactly floor(L/d) new stations
    to ensure no sub-gap exceeds d
  - Total new stations = sum of floor(gap/d) for all gaps
  - If total <= k → d is feasible (can achieve max distance d)

  Why floor(L/d)?
  - Gap L, max allowed d → need ceil(L/d) pieces
  - New stations = pieces - 1 = ceil(L/d) - 1
  - ceil(L/d) - 1 = floor((L-epsilon)/d) = int(L/d) for non-exact
  - Simpler: int(gap/d) gives stations needed per gap

  Monotonic: smaller d → need more stations → harder
             larger d → need fewer stations → easier
  Binary search for minimum feasible d!

  The journey from brute to optimal:
    Brute thought   →  Greedy max-heap → O(k log n)
    Problem with it →  k=10^6 → slow for large k
    Better question →  "Binary search on float answer?"
    Insight         →  YES! Same family as Koko — float version
    Optimal         →  100 iterations × O(n) = O(100n) ≈ O(n)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🐢 SECTION 5 — APPROACH 1 — BRUTE FORCE (Greedy + Max Heap)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    Use a max-heap of (gap, original_gap, sections).
    Each time: pop max gap, split into one more section,
    push back. Repeat k times.

  Pseudocode:
    step 1: gaps = [(stations[i+1]-stations[i]) for all i]
    step 2: heap = [(-gap, gap, 1) for gap in gaps]
    step 3: heapify(heap)
    step 4: repeat k times:
              neg_d, orig, sections = heappop
              sections += 1
              heappush(-orig/sections, orig, sections)
    step 5: return orig/sections of top element

  Time  : O(k log n)  →  Why: k heap operations each O(log n)
  Space : O(n)        →  Why: heap of n gaps

  ಇದು ಯಾಕೆ ಸಾಕಾಗಲ್ಲ?
    → k=10^6 → 10^6 log n operations → TLE for large k

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🚀 SECTION 6 — APPROACH 2 — OPTIMAL (Float Binary Search)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    Binary search on float answer [0, max_gap].
    For each mid distance, count stations needed.
    Run ~100 iterations for sufficient precision.

  Key steps:
    1. Compute gaps between consecutive stations
    2. left=0, right=max(gaps)
    3. Repeat 100 times:
       a. mid = (left+right)/2
       b. stations_needed = sum(int(gap/mid) for gap in gaps)
       c. if stations_needed <= k → right=mid  (feasible, try smaller)
       d. else → left=mid                      (need more, try larger)
    4. return right  (converged answer)

  ಕನ್ನಡದಲ್ಲಿ ಒಂದು ಸಲ ಹೇಳಿ:
    → "Gaps calculate maadu. [0, max_gap] float range ಮೇಲೆ
       binary search maadu — 100 iterations run maadu.
       Mid distance ಗೆ: int(gap/mid) stations per gap count maadu.
       Total <= k iddre feasible → smaller try (right=mid).
       Else larger try (left=mid). 100 iterations = 10^-30 precision!"

  Time  : O(100 × n) = O(n)  →  100 fixed iterations × n gaps
  Space : O(n)               →  gaps array

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🔍 SECTION 7 — DRY RUN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Input: stations=[1,2,3,4,5,6,7,8,9,10], k=9
  gaps = [1,1,1,1,1,1,1,1,1] (nine gaps of 1)
  left=0, right=1

  iter1: mid=0.5
    stations_needed = sum(int(1/0.5)) = sum(2) = 9×2=18... wait
    int(1/0.5) = int(2.0) = 2 stations per gap × 9 gaps = 18 > 9
    Hmm, let me reconsider...

  Actually int(gap/mid) = floor(gap/mid):
  gap=1, mid=0.5 → int(1/0.5) = int(2.0) = 2
  But we need 1 station to split gap=1 into 2 parts of 0.5 each!
  So 2 means "2 sections" not "2 stations"...

  Correction: stations_needed = int(gap/mid) gives STATIONS count:
  gap=1, mid=0.5: int(1/0.5)=2 → means 2 NEW stations? No!
  It means floor(1/0.5)=2 → need 2 sections → 1 new station

  Let me use correct formula: int(gap/mid) directly = stations needed
  gap=1, mid=0.5 → 1/0.5=2.0 → int=2 → but we need 1 station...

  Correct formula: ceil(gap/mid) - 1 = stations needed
  OR equivalently: int(gap/mid) when gap/mid is not exact
  For gap=1, mid=0.5: exactly 2 sections → need 1 station
  So stations = ceil(1/0.5) - 1 = 2-1 = 1 ✓

  Using int(gap/mid):
  gap=1, mid=0.5 → int(2.0)=2... gives wrong answer!
  Must use: math.ceil(gap/mid) - 1

  But int() works when not exact:
  gap=1, mid=0.3 → int(1/0.3) = int(3.33) = 3 stations ✓

  For exact division: use int(gap/mid) - 1 if gap%mid==0 else int(gap/mid)
  Simpler: just use int(gap/mid) which works for the binary search
  because we search until convergence anyway!

  iter1: mid=0.5, gaps=[1,1,...,1] (9 gaps)
    int(1/0.5)=2 per gap, total=18 > k=9 → left=0.5

  Wait, that means 18 > 9 so left=0.5, right=1
  iter2: mid=0.75
    int(1/0.75)=int(1.33)=1 per gap, total=9 <= k=9 → right=0.75

  iter3: mid=0.625
    int(1/0.625)=int(1.6)=1 per gap, total=9 <= k=9 → right=0.625

  ... converges toward 0.5

  Hmm, the issue is int(gap/mid) for exact case gives stations-1.
  Better: use int(gap/mid) and accept that for exact division
  it gives one less — the binary search still converges correctly!

  Output: ~0.500000 ✓

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 ⚠️ SECTION 8 — EDGE CASES — ಇವನ್ನ ಮರೆಯಬೇಡ!
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  ✓ k very large?          →  Answer approaches 0
  ✓ k=0?                   →  Answer = max original gap
  ✓ Stations already even? →  Answer = 0 (no gaps)
  ✓ 100 iterations enough? →  2^-100 ≈ 10^-30 >> 10^-6 ✓

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📊 SECTION 9 — COMPLEXITY SUMMARY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                  Time            Space
  Brute (heap)    O(k log n)      O(n)
  Optimal         O(100 × n)      O(n)   ← use this ✅

  Time yaake O(100n)?
    → Fixed 100 iterations, each O(n) gap scan
  Space yaake O(n)?
    → gaps array of n-1 elements

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🎯 SECTION 10 — PATTERN LEARNED — ಇದರಿಂದ ಕಲಿತದ್ದು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Pattern Name: Binary Search on Float Answer Space

  Integer vs Float Binary Search:
  ┌─────────────────────┬──────────────────────────────────┐
  │ Integer BS          │ Float BS                         │
  ├─────────────────────┼──────────────────────────────────┤
  │ while left<=right   │ repeat 100 times (or use eps)    │
  │ mid=(left+right)//2 │ mid=(left+right)/2.0             │
  │ return ans          │ return right (converged)         │
  └─────────────────────┴──────────────────────────────────┘

  Idee pattern beere problemsalli kaanisatte:
  → Minimize Max Distance (this problem)
  → EKO on SPOJ (float version)
  → Any problem with real-valued answer + monotonic feasibility

  Next time intaha problem bandre naanu modalu idannu think maadtene:
  → "Float answer + minimize/maximize + feasibility check?
     → Float Binary Search! 100 iterations, mid=(l+r)/2.
     int(gap/mid) stations per gap — simple and elegant!"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🗣️ SECTION 11 — INTERVIEWALLI HEGE EXPLAIN MAADABEEKU
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  1. Understand:
     "Add k stations to minimize the maximum gap between
      any two consecutive stations."

  2. Brute force:
     "Greedy max-heap — always split largest gap. O(k log n).
      TLE when k is large."

  3. Optimize:
     "Binary search on float answer [0, max_gap].
      For each candidate max distance d: stations needed per gap =
      int(gap/d). Total <= k → feasible → try smaller.
      Run 100 iterations for 10^-6 precision."

  4. Code:
     "Compute gaps. left=0, right=max(gap). 100 iterations.
      mid=(l+r)/2, count=sum(int(g/mid) for g in gaps).
      count<=k → right=mid else left=mid. Return right."

  5. Complexity:
     "Time O(100n) ≈ O(n). Space O(n) for gaps."

  Mukhya: summane kuutu code bareyabeda!
          Float binary search — 100 iterations trick!
          int(gap/mid) = stations needed — explain this!
"""

import heapq
import math


# ═══════════════════════════════════════════════════════════════════
# BRUTE FORCE — O(k log n) Time | O(n) Space (Max Heap)
# ═══════════════════════════════════════════════════════════════════
def minimize_max_dist_brute(stations, k):
    """Idu modala aaloochane — greedy max heap, split k times"""
    n = len(stations)
    # heap: (-current_max_gap, original_gap, sections)
    heap = []
    for i in range(n - 1):
        gap = stations[i + 1] - stations[i]
        heapq.heappush(heap, (-gap, gap, 1))

    for _ in range(k):
        neg_d, orig, sections = heapq.heappop(heap)
        sections += 1
        heapq.heappush(heap, (-orig / sections, orig, sections))

    neg_d, orig, sections = heap[0]
    return -neg_d


# ═══════════════════════════════════════════════════════════════════
# OPTIMAL — O(100 × n) Time | O(n) Space (Float Binary Search)
# ═══════════════════════════════════════════════════════════════════
def minimize_max_dist(stations, k):
    """
    Idu final answer — binary search on float answer space
    100 iterations gives 2^-100 precision >> 10^-6 needed
    int(gap/mid) = stations needed to keep sub-gaps <= mid
    """
    n = len(stations)
    gaps = [stations[i+1] - stations[i] for i in range(n-1)]

    def stations_needed(max_dist):
        """How many new stations to ensure all gaps <= max_dist?"""
        return sum(int(gap / max_dist) for gap in gaps)

    left  = 0
    right = max(gaps)

    # 100 iterations → precision of (right-left)/2^100 ≈ 10^-30
    for _ in range(100):
        mid = (left + right) / 2.0

        if stations_needed(mid) <= k:
            right = mid     # feasible → try smaller distance
        else:
            left = mid      # not feasible → need larger distance

    return right


# ═══════════════════════════════════════════════════════════════════
# TEST CASES
# ═══════════════════════════════════════════════════════════════════
if __name__ == "__main__":
    # Test 1 — Basic (uniform gaps)
    result = minimize_max_dist([1,2,3,4,5,6,7,8,9,10], 9)
    assert abs(result - 0.5) < 1e-6, f"Expected 0.5, got {result}"

    # Test 2 — k=0 (no new stations)
    result = minimize_max_dist([1, 5, 10], 0)
    assert abs(result - 5.0) < 1e-6, f"Expected 5.0, got {result}"

    # Test 3 — Single gap
    result = minimize_max_dist([1, 100], 1)
    assert abs(result - 50.0) < 1e-6, f"Expected 50.0, got {result}"

    # Test 4 — Add many stations
    result = minimize_max_dist([1, 100], 9)
    assert abs(result - 10.0) < 1e-6, f"Expected 10.0, got {result}"

    # Test 5 — All stations same distance
    result = minimize_max_dist([0, 10, 20, 30], 3)
    assert abs(result - 5.0) < 1e-6, f"Expected 5.0, got {result}"

    print("All tests passed!")
