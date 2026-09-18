"""
╔══════════════════════════════════════════════════════════════════╗
║  CAPACITY TO SHIP PACKAGES WITHIN D DAYS                         ║
║  LeetCode #1011  |  Difficulty: Medium  |  Topic: Binary Search  ║
║  Link: https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/                                            ║
╚══════════════════════════════════════════════════════════════════╝

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📘 SECTION 1 — PROBLEM UNDERSTANDING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  A conveyor belt has packages with weights[i]. We need to ship
  all packages within d days IN ORDER (cannot reorder). Each day
  we load packages onto a ship with a weight capacity. We cannot
  split a package across days. Find the MINIMUM weight capacity
  of the ship so all packages are shipped within d days.

  Input : weights = list of package weights, days = d
  Output: minimum ship capacity to ship all within d days

  Example 1 — basic:
    Input : weights=[1,2,3,4,5,6,7,8,9,10], days=5
    Output: 15
    Why?  : capacity=15 → day1:[1,2,3,4,5]=15, day2:[6,7]=13,
            day3:[8]=8, day4:[9]=9, day5:[10]=10 → 5 days ✓
            capacity=14 → cannot fit in 5 days

  Example 2 — slightly tricky (days == n):
    Input : weights=[3,2,2,4,1,4], days=3
    Output: 6
    Why?  : capacity=6 → [3,2],[2,4],[1,4] → wait 2+4=6 ✓
            Each day ships a contiguous group ≤ 6

  Constraints:
    - 1 <= days <= weights.length <= 5×10^4
    - 1 <= weights[i] <= 500

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🧠 SECTION 2 — KANGLISH THINKING — ಹೇಗೆ ಯೋಚಿಸಬೇಕು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  Problem odi aada mele namma brain enu think maadabeeku:

  ಹಂತ 1 — Problem ಅರ್ಥ ಮಾಡಿಕೊಳ್ಳಿ
  ┌─────────────────────────────────────────────────────────┐
  │  Input ಏನು ಕೊಡ್ತಾರೆ?  →  weights array + days d       │
  │  Output ಏನು ಬೇಕು?     →  minimum ship capacity to     │
  │                           ship all in d days IN ORDER  │
  │  Constraints ಏನಿದೆ?   →  order maintain maadabeeku,   │
  │                           package split ಮಾಡಲ್ಲ         │
  └─────────────────────────────────────────────────────────┘

  ಹಂತ 2 — ನನಗೆ ಗೊತ್ತಿರೋ simple way ಏನು?
  →  capacity max(weights) ಇಂದ sum(weights) ತನಕ try ಮಾಡಿ
     first valid capacity return ಮಾಡೋಣ
  →  ಆದರೆ ಇದು slow ಯಾಕೆ?
     sum can be 5×10^4 × 500 = 2.5×10^7 → each check O(n) → TLE

  ಹಂತ 3 — Better way ಹೇಗೆ ಯೋಚಿಸುವುದು?
  →  "Koko, Bouquets, Divisor same pattern ಅಲ್ಲವಾ?"
  →  Answer space [max(weights), sum(weights)] — sorted range
     min = max(weights) (must carry heaviest package)
     max = sum(weights) (ship everything in 1 day)
  →  Monotonic: capacity ಜಾಸ್ತಿ → days ಕಡಿಮೆ → always valid
  →  Binary search on capacity!

  ಹಂತ 4 — Technique ಯಾಕೆ ಇಲ್ಲಿ ಕೆಲಸ ಮಾಡುತ್ತೆ?
  →  Feasibility: greedily load packages until capacity exceeded
     → start new day → count days → check if <= d
  →  Same template — only is_feasible() changes!

  💡 Interview ನಲ್ಲಿ ಹೇಗೆ ಮಾತಾಡಬೇಕು:
  →  "4th problem in binary search on answer space series!"
  →  "Range: [max(weights), sum(weights)] — why? explain!"
  →  "Higher capacity → fewer days → monotonic → binary search"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🏷️ SECTION 3 — TECHNIQUE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Primary   : Binary Search → On Answer Space
  Secondary : Greedy (feasibility check — load greedily each day)

  WHY this answer range?
  → left = max(weights): minimum possible — must carry heaviest
  → right = sum(weights): maximum needed — ship all in 1 day
  → Any capacity < max(weights) → cannot carry heaviest package!

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 💡 SECTION 4 — INTUITION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Key difference from Koko: the answer RANGE is different!
  - Koko: [1, max(piles)]
  - This: [max(weights), sum(weights)]

  Why max(weights) as left?
  → We MUST be able to carry the heaviest package in one trip
  → If capacity < max(weights), impossible!

  Why sum(weights) as right?
  → Worst case: carry everything in one day → capacity = total

  Feasibility check (greedy):
  - Load packages one by one
  - If adding next package exceeds capacity → new day
  - Count days needed
  - If days <= d → feasible!

  The journey from brute to optimal:
    Brute thought   →  Try every capacity from max to sum → O(n×sum)
    Problem with it →  sum up to 2.5×10^7 → TLE
    Better question →  "Same as previous problems?"
    Insight         →  Yes! Monotonic + bounded range → binary search
    Optimal         →  O(n log(sum - max)) ≈ O(n log(sum))

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🐢 SECTION 5 — APPROACH 1 — BRUTE FORCE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    Try every capacity from max(weights) to sum(weights).
    Return first capacity where days needed <= d.

  Pseudocode:
    step 1: for cap in range(max(weights), sum(weights)+1):
    step 2:   if days_needed(cap) <= days: return cap

  Time  : O(n × sum(weights))  →  Why: sum capacities × n check
  Space : O(1)

  ಇದು ಯಾಕೆ ಸಾಕಾಗಲ್ಲ?
    → sum up to 2.5×10^7 iterations → TLE

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🚀 SECTION 6 — APPROACH 2 — OPTIMAL (Binary Search on Answer)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    Binary search on capacity [max(weights), sum(weights)].
    For each mid capacity, check if all packages ship in <= d days.
    If yes → try smaller capacity. If no → try larger.

  Key steps:
    1. left=max(weights), right=sum(weights), ans=right
    2. While left <= right:
       a. mid = (left+right)//2
       b. if can_ship(mid, days) → ans=mid, right=mid-1
       c. else → left=mid+1
    3. return ans

  can_ship(capacity, days):
    current_load=0, days_needed=1
    for weight in weights:
      if current_load + weight > capacity:
        days_needed += 1      # start new day
        current_load = 0
      current_load += weight
    return days_needed <= days

  ಕನ್ನಡದಲ್ಲಿ ಒಂದು ಸಲ ಹೇಳಿ:
    → "Capacity range [max(weights), sum(weights)] ಮೇಲೆ
       binary search maadu. Mid capacity ಗೆ greedy ಆಗಿ
       packages load maadu, exceed ಆದ್ರೆ new day start maadu.
       Days <= d ಆದ್ರೆ → valid! Smaller try. Else larger try.
       Koko same template — just different range and check!"

  Time  : O(n × log(sum(weights)))  →  Why: log steps × O(n) check
  Space : O(1)                      →  Why: only pointers

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🔍 SECTION 7 — DRY RUN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Input: weights=[1,2,3,4,5,6,7,8,9,10], days=5
  left=10 (max), right=55 (sum)

  mid=32 → load greedily:
    [1,2,3,4,5,6,7]=28, +8=36>32 → day2
    [8,9]=17, +10=27<=32 → day2 cont → [8,9,10]=27
    Wait: [1..7]=28, day2=[8,9,10]=27 → 2 days <= 5 ✓
    ans=32, right=31

  mid=20 → [1..6]=21>20 → [1..5]=15,day2=[6,7]=13,day3=[8]=8,
           day4=[9]=9,day5=[10]=10 → 5 days <= 5 ✓
    ans=20, right=19

  mid=14 → [1..5]=15>14 → [1..4]=10,+5=15>14 → day1=[1..4]=10
           day2=[5,6]=11,+7=18>14 → day3=[7,8]=15>14 → day3=[7]=7
           day4=[8]=8,+9=17>14 → day5=[9]=9,+10=19>14 → day6=[10]
           6 days > 5 ✗ → left=15

  mid=17 → [1..6]=21>17 → [1..5]=15,+6=21>17 → day1=[1..5]=15
           day2=[6,7]=13,+8=21>17 → day2=[6,7]=13
           day3=[8,9]=17, +10=27>17 → day4=[10]=10
           4 days <= 5 ✓ → ans=17, right=16

  mid=15 → day1=[1..5]=15, day2=[6,7]=13, day3=[8]=8,
           day4=[9]=9, day5=[10]=10 → 5 days <=5 ✓
    ans=15, right=14

  left=15 > right=14 → return 15 ✓

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 ⚠️ SECTION 8 — EDGE CASES — ಇವನ್ನ ಮರೆಯಬೇಡ!
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  ✓ days == n?        →  Each package on separate day → max(weights)
  ✓ days == 1?        →  Must ship all in one day → sum(weights)
  ✓ Single package?   →  [w], d=1 → w
  ✓ All equal weights →  [5,5,5,5], d=2 → 10

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📊 SECTION 9 — COMPLEXITY SUMMARY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                  Time                    Space
  Brute Force     O(n × sum(weights))     O(1)
  Optimal         O(n × log(sum))         O(1)   ← use this ✅

  Time yaake O(n log sum)?
    → log(sum) binary search steps on capacity range
    → Each step O(n) greedy check
  Space yaake O(1)?
    → Only left, right, mid, ans, load counters

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🎯 SECTION 10 — PATTERN LEARNED — ಇದರಿಂದ ಕಲಿತದ್ದು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Pattern Name: Binary Search on Answer Space (4th in series)

  Complete comparison table:
  ┌──────────────┬──────────────────────┬────────────────────────┐
  │ Problem      │ Answer Range         │ Feasibility Check      │
  ├──────────────┼──────────────────────┼────────────────────────┤
  │ Koko #875    │ [1, max(piles)]      │ sum(ceil(p/k)) <= h    │
  │ Bouq #1482   │ [1, max(bloom)]      │ bouquets(day) >= m     │
  │ Div  #1283   │ [1, max(nums)]       │ sum(ceil(n/d))<=thresh │
  │ Ship #1011   │ [max(w), sum(w)]     │ days_needed(cap) <= d  │
  └──────────────┴──────────────────────┴────────────────────────┘

  Key difference here: left = max(weights) not 1!
  Because we MUST be able to carry the heaviest package.

  Next time intaha problem bandre naanu modalu idannu think maadtene:
  → "Minimum capacity beeka? → Binary Search on Answer!
     left=max(weights) — must carry heaviest!
     right=sum(weights) — worst case 1 day.
     Greedy load check — days_needed <= d?"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🗣️ SECTION 11 — INTERVIEWALLI HEGE EXPLAIN MAADABEEKU
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  1. Understand:
     "Find minimum ship capacity to ship all packages in order
      within d days."

  2. Brute force:
     "Try every capacity from max(weights) to sum(weights). TLE."

  3. Optimize:
     "Binary search on answer space. Range is [max(weights),
      sum(weights)] — left is max because we must carry the
      heaviest package. Higher capacity → fewer days → monotonic.
      Feasibility: greedily load packages, count days needed."

  4. Code:
     "left=max(w), right=sum(w). For each mid, simulate loading:
      if adding next package exceeds capacity → new day.
      If days_needed <= d → feasible, save ans, try smaller."

  5. Complexity:
     "Time O(n log(sum)). Space O(1)."

  Mukhya: summane kuutu code bareyabeda!
          left=max(weights) why? — explain this clearly!
          4th in the series — show the pattern table!
"""


# ═══════════════════════════════════════════════════════════════════
# BRUTE FORCE — O(n × sum) Time | O(1) Space
# ═══════════════════════════════════════════════════════════════════
def ship_within_days_brute(weights, days):
    """Idu modala aaloochane — try every capacity linearly"""
    def days_needed(cap):
        d = 1
        load = 0
        for w in weights:
            if load + w > cap:
                d += 1
                load = 0
            load += w
        return d

    for cap in range(max(weights), sum(weights) + 1):
        if days_needed(cap) <= days:
            return cap


# ═══════════════════════════════════════════════════════════════════
# OPTIMAL — O(n log(sum)) Time | O(1) Space
# ═══════════════════════════════════════════════════════════════════
def ship_within_days(weights, days):
    """
    Idu final answer — binary search on [max(weights), sum(weights)]
    left=max because must carry heaviest package in one trip!
    Greedy feasibility: load until exceed, start new day
    """
    def can_ship(capacity):
        days_needed = 1
        current_load = 0
        for w in weights:
            if current_load + w > capacity:
                days_needed += 1      # start fresh day
                current_load = 0
            current_load += w
        return days_needed <= days

    left  = max(weights)    # must carry heaviest package
    right = sum(weights)    # ship everything in 1 day
    ans   = right

    while left <= right:
        mid = (left + right) // 2

        if can_ship(mid):
            ans = mid               # feasible! try smaller cap
            right = mid - 1
        else:
            left = mid + 1         # not enough, need bigger cap

    return ans


# ═══════════════════════════════════════════════════════════════════
# TEST CASES
# ═══════════════════════════════════════════════════════════════════
if __name__ == "__main__":
    # Test 1 — Basic
    assert ship_within_days([1,2,3,4,5,6,7,8,9,10], 5) == 15

    # Test 2 — Second example
    assert ship_within_days([3,2,2,4,1,4], 3) == 6

    # Test 3 — Third example
    assert ship_within_days([1,2,3,1,1], 4) == 3

    # Test 4 — days == n (one package per day)
    assert ship_within_days([5,5,5,5], 4) == 5

    # Test 5 — days == 1 (all in one day)
    assert ship_within_days([1,2,3], 1) == 6

    # Test 6 — Single package
    assert ship_within_days([10], 1) == 10

    print("All tests passed!")
