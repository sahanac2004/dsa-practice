"""
╔══════════════════════════════════════════════════════════════════╗
║  BEST TIME TO BUY AND SELL STOCK                                 ║
║  LeetCode #121  |  Difficulty: Easy  |  Topic: Arrays / Greedy   ║
║  Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/ ║
╚══════════════════════════════════════════════════════════════════╝

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🧠 KANGLISH THINKING — ಹೇಗೆ ಯೋಚಿಸಬೇಕು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  ಮೊದಲು problem odidaga ನಮ್ಮ brain ಏನು think ಮಾಡಬೇಕು:

  ಹಂತ 1 — Problem ಅರ್ಥ ಮಾಡಿಕೊಳ್ಳಿ (What are they asking?)
  ┌─────────────────────────────────────────────────────────┐
  │  Input ಏನು ಕೊಡ್ತಾರೆ?  →  ಪ್ರತಿ day ಗೆ stock price     │
  │                          ಇರೋ array                      │
  │  Output ಏನು ಬೇಕು?     →  ಒಂದೇ buy + ಒಂದೇ sell ಮಾಡಿ    │
  │                          ಸಿಗುವ max profit                │
  │  Constraints ಏನಿದೆ?   →  buy ಮೊದಲು, sell ಆಮೇಲೆ         │
  │                          (sell day > buy day ಇರಬೇಕು)    │
  └─────────────────────────────────────────────────────────┘

  ಹಂತ 2 — ನನಗೆ ಗೊತ್ತಿರೋ simple way ಏನು? (Brute force thought)
  →  ಪ್ರತಿ buy day i ಗೂ, ಅದರ ಆಮೇಲಿನ ಎಲ್ಲಾ sell day j ಗೂ profit
     ಎಷ್ಟು ಅಂತ check ಮಾಡಿ, max ಎಷ್ಟು ಅಂತ track ಮಾಡೋದು.
  →  ಆದರೆ ಇದು slow ಯಾಕೆ? → n=10^5 ಆದ್ರೆ n² operations ಆಗುತ್ತೆ,
     TLE ಗ್ಯಾರಂಟಿ.

  ಹಂತ 3 — Better way ಹೇಗೆ ಯೋಚಿಸುವುದು? (Optimization thought)
  →  "ನಾನು day j ನಲ್ಲಿ sell ಮಾಡ್ಬೇಕು ಅಂದ್ರೆ, ಅದಕ್ಕಿಂತ ಮುಂಚೆ
     ಇರೋ LOWEST price ದಿನ buy ಮಾಡಿದ್ರೆ ಸಾಕಲ್ವಾ?"
  →  ಅಹಾ moment: ಪ್ರತಿ j ಗೂ ಹಿಂದೆ ಹೋಗಿ min ಹುಡುಕೋ ಬದ್ಲು, ಮುಂದೆ
     ಹೋಗ್ತಾ min_price ಅನ್ನ ಒಂದೇ variable ನಲ್ಲಿ carry ಮಾಡಿದ್ರೆ ಸಾಕು.
  →  ಇದರಿಂದ ನಾವು Greedy — Running Minimum use ಮಾಡಬಹುದು!

  ಹಂತ 4 — Technique ಯಾಕೆ ಇಲ್ಲಿ ಕೆಲಸ ಮಾಡುತ್ತೆ?
  →  "Buy before sell" ಅನ್ನೋ one-directional constraint ಇರೋದ್ರಿಂದ,
     single left-to-right scan ಸಾಕಾಗುತ್ತೆ.
  →  ಇವತ್ತು sell ಮಾಡಿದ್ರೆ profit = today - min_so_far, ಅಷ್ಟೇ ಸಾಕು —
     future prices ಗೊತ್ತಿರೋ ಅಗತ್ಯ ಇಲ್ಲ.
  →  O(1) extra space ಸಾಕಾಗುತ್ತೆ ಅಂದ್ರೆ, greedy running-min
     signal ಸಿಗುತ್ತೆ.

  💡 Interview ನಲ್ಲಿ ಹೇಗೆ ಮಾತಾಡಬೇಕು (Think out loud):
  →  "So I'm seeing that I need one buy and one sell, buy before sell."
  →  "The brute force would check every (buy, sell) pair — O(n²)."
  →  "I notice that for any sell day, the best buy day is just the
      minimum price seen so far, so I can track that in one pass."

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🏷️ TECHNIQUE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Primary   : Greedy → Track Minimum So Far
  Secondary : Sliding Window (variable, conceptually)

  WHY this technique?
  → Must BUY before SELL — min price must come from strictly
    before the sell index (one-directional scan)
  → Best profit if selling TODAY only depends on lowest price seen
    so far — no need to look ahead
  → Single pass, O(1) extra state → classic greedy "running min"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📘 PROBLEM UNDERSTANDING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  You're given prices[i] = stock price on day i. Buy on one day,
  sell on a LATER day (one transaction only). Return max profit,
  or 0 if no profit is possible.

  Input : prices = [7, 1, 5, 3, 6, 4]
  Output: 5

  Example 1 — basic:
    Input : prices = [7, 1, 5, 3, 6, 4]
    Output: 5
    Why?  : buy day1 (price=1), sell day4 (price=6), profit = 5

  Example 2 — slightly tricky:
    Input : prices = [7, 6, 4, 3, 1]
    Output: 0
    Why?  : strictly decreasing — no profitable buy/sell exists

  Constraints:
    - Must buy BEFORE you sell (sell index > buy index)
    - Only one buy + one sell transaction total

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 💡 INTUITION (How to think)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  If I'm standing on day j deciding to SELL, the best day to have
  bought is whichever day BEFORE j had the lowest price.

  The journey from brute to optimal:
    Brute thought   →  check every (buy, sell) pair
    Problem with it →  O(n²), TLE for n=10⁵
    Better question →  "what's the best buy day for THIS sell day?"
    Insight         →  it's just the running minimum price so far
    Optimal         →  single pass, carry min_price forward

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🐢 APPROACH 1 — BRUTE FORCE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    Try every (buy day, sell day) pair where sell > buy.

  Pseudocode:
    step 1: max_profit = 0
    step 2: for i in range(n): for j in range(i+1, n):
    step 3:     max_profit = max(max_profit, prices[j] - prices[i])

  Time  : O(n²)  →  Why: nested loops over all pairs
  Space : O(1)   →  Why: no extra data structure used

  ಇದು ಯಾಕೆ ಸಾಕಾಗಲ್ಲ? (Why is this not enough?)
    → n = 10⁵ ಆದ್ರೆ 10¹⁰ operations → definite TLE.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🚶 APPROACH 2 — BETTER (skip — brute jumps straight to optimal)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  ಇಲ್ಲಿ intermediate approach ಇಲ್ಲ — running-min insight ಸಿಕ್ಕ
  ತಕ್ಷಣ ನೇರವಾಗಿ O(n) optimal ಗೆ ಹೋಗಬಹುದು.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🚀 APPROACH 3 — OPTIMAL  
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    Single pass, track min price seen so far + best profit.

  Key steps:
    1. min_price = prices[0], max_profit = 0
    2. For each price starting from index 1:
         a. profit if selling today = price - min_price
         b. max_profit = max(max_profit, profit)
         c. min_price  = min(min_price, price)   ← update AFTER
    3. Return max_profit

  ಕನ್ನಡದಲ್ಲಿ ಒಂದು ಸಲ ಹೇಳಿ (Say it once in Kanglish so it sticks):
    → "Array ಅನ್ನ ಒಮ್ಮೆ scan ಮಾಡ್ತಾ, ಇಲ್ಲಿಯವರೆಗೆ ಕಂಡ ಕಡಿಮೆ price
        ಅನ್ನ min_price ನಲ್ಲಿ track ಮಾಡು. ಪ್ರತಿ day ಗೂ 'ಇವತ್ತು sell
        ಮಾಡಿದ್ರೆ profit ಎಷ್ಟು' ಅಂತ (today - min_price) calculate
        ಮಾಡಿ best ಜೊತೆ compare ಮಾಡು. ಆಮೇಲೆ min_price ಅನ್ನ update
        ಮಾಡು."

  Time  : O(n)  →  Why: single pass
  Space : O(1)  →  Why: just two variables

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🔍 DRY RUN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Input: prices = [7, 1, 5, 3, 6, 4]

  Start: min_price=7, max_profit=0

  price=1  →  variables: min_price=7  →  profit=1-7=-6, max_profit stays 0, min_price→1
  price=5  →  variables: min_price=1  →  profit=5-1=4,  max_profit=4
  price=3  →  variables: min_price=1  →  profit=3-1=2,  max_profit stays 4
  price=6  →  variables: min_price=1  →  profit=6-1=5,  max_profit=5
  price=4  →  variables: min_price=1  →  profit=4-1=3,  max_profit stays 5

  Output: 5 (buy@1, sell@6)

  ಇನ್ನೊಂದು example — tricky case:
  Input: prices = [7, 6, 4, 3, 1]
  Every next price is LOWER than min_price so far → profit always
  negative or zero → max_profit never updates from 0.
  Output: 0

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 ⚠️ EDGE CASES — ಇವನ್ನ ಮರೆಯಬೇಡ!
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  ✓ Strictly decreasing prices?  →  [7,6,4,3,1] → 0 (never buy+sell)
  ✓ Single day?                 →  [5] → 0 (can't transact, no second day)
  ✓ Strictly increasing prices? →  [1,2,3,4,5] → 4 (buy day0, sell last)
  ✓ All same price?             →  [3,3,3] → 0
  ✓ Two elements?                →  [2,4] → 2

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📊 COMPLEXITY SUMMARY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                Time      Space
  Brute Force   O(n²)     O(1)
  Optimal       O(n)      O(1)    ← use this  

  Time ಯಾಕೆ O(n)?  → Array ಒಮ್ಮೆ ಮಾತ್ರ traverse ಮಾಡ್ತೇವೆ.
  Space ಯಾಕೆ O(1)? → min_price, max_profit ಎರಡು variables ಸಾಕು.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🎯 PATTERN LEARNED — ಇದರಿಂದ ಕಲಿತದ್ದು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Pattern Name: Greedy Running Minimum/Maximum

  ಈ pattern ಯಾವಾಗ use ಮಾಡಬೇಕು?
  → Answer "best pair where one side must come BEFORE the other"
    ಅಂತ ಇದ್ದಾಗ
  → O(n) time, O(1) space ಬೇಕು ಅಂದಾಗ
  → Re-scanning ಮಾಡೋ ಬದ್ಲು, ಒಂದು running best variable carry
    ಮಾಡಿದ್ರೆ ಸಾಕಾಗುತ್ತೆ ಅಂತ ಗೊತ್ತಾದಾಗ

  ಇದೇ pattern ಬೇರೆ problems ನಲ್ಲಿ ಕಾಣಿಸುತ್ತೆ:
  → Maximum Subarray / Kadane's (#53) — running best sum
  → Best Time to Buy/Sell Stock III/IV — DP state machine extension
  → Container With Most Water — running best area

  Next time ಇಂತಹ problem ಬಂದ್ರೆ ನಾನು ಮೊದಲು ಇದನ್ನ think ಮಾಡ್ತೇನೆ:
  → "Before/after ordering constraint ಇದ್ಯಾ? ಇದ್ರೆ, ಒಂದೇ pass ಲ್ಲಿ
      running min/max carry ಮಾಡಕ್ಕಾಗುತ್ತಾ ಅಂತ ಮೊದಲು ಯೋಚಿಸು."

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🗣️ INTERVIEW ನಲ್ಲಿ ಹೇಗೆ EXPLAIN ಮಾಡಬೇಕು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  1. Understand:
     "So I need to find one buy day and one later sell day that
      maximizes profit."

  2. Brute force:
     "The naive approach checks every (buy, sell) pair — O(n²),
      which would TLE for n up to 10⁵."

  3. Optimize:
     "I notice that for any sell day, the best buy day is just the
      minimum price seen before it — so I can track that minimum
      as I scan forward, no need to re-scan."

  4. Code:
     "I'll keep min_price and max_profit, updating both in a
      single left-to-right pass."

  5. Complexity:
     "Time O(n) — one pass. Space O(1) — two variables."

  ಮುಖ್ಯ: ಸುಮ್ಮನೆ ಕೂತು code ಬರೆಯಬೇಡ!
         Interviewer ಗೆ ನಿನ್ನ thinking process ಕಾಣಬೇಕು.
"""


# ═══════════════════════════════════════════════════════════════════
# BRUTE FORCE — O(n²) Time | O(1) Space
# ═══════════════════════════════════════════════════════════════════
def max_profit_brute(prices):
    """ಇದು ಮೊದಲ ಆಲೋಚನೆ — every (buy, sell) pair check, simple but slow"""
    n = len(prices)
    max_profit = 0
    for i in range(n):
        for j in range(i + 1, n):
            profit = prices[j] - prices[i]
            max_profit = max(max_profit, profit)
    return max_profit


# ═══════════════════════════════════════════════════════════════════
# OPTIMAL — O(n) Time | O(1) Space
# ═══════════════════════════════════════════════════════════════════
def max_profit(prices):
    """ಇದು final answer — running minimum price tracked in one pass"""
    if not prices:
        return 0

    min_price = prices[0]
    best_profit = 0

    for price in prices[1:]:
        best_profit = max(best_profit, price - min_price)
        min_price = min(min_price, price)

    return best_profit


# ═══════════════════════════════════════════════════════════════════
# TEST CASES
# ═══════════════════════════════════════════════════════════════════
if __name__ == "__main__":
    import sys
    sys.stdout.reconfigure(encoding="utf-8")   # Windows cp1252 can't print   otherwise

    # Test 1 — Basic example
    assert max_profit([7, 1, 5, 3, 6, 4]) == 5

    # Test 2 — Edge case: strictly decreasing, no profit
    assert max_profit([7, 6, 4, 3, 1]) == 0

    # Test 3 — Edge case: single day
    assert max_profit([5]) == 0

    # Test 4 — Tricky: all same price
    assert max_profit([3, 3, 3]) == 0

    print("All tests passed!  ")
