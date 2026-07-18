"""
╔═══════════════════════════════════════════════════════════════════════╗
║  BEST TIME TO BUY AND SELL STOCK                                      ║
║  LeetCode #121  |  Difficulty: Easy  |  Topic: Arrays / Greedy        ║
║  Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/ ║
╚═══════════════════════════════════════════════════════════════════════╝

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 TECHNIQUE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Primary   : Greedy → Track Minimum So Far
  Secondary : Sliding Window (variable, conceptually)

  WHY this technique?
  → You must BUY before you SELL — the min price must come from
    an index strictly before the sell index (one-directional scan).
  → At every day, the best possible profit if selling TODAY only
    depends on the lowest price seen so far → no need to look ahead.
  → Single pass, O(1) extra state → classic greedy "running min" pattern.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 PROBLEM UNDERSTANDING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  You're given an array `prices` where prices[i] = price of the
  stock on day i. You may buy on one day and sell on a LATER day
  (only one transaction allowed). Return the max profit possible.
  If no profit is possible, return 0.

  Input : prices = [7, 1, 5, 3, 6, 4]
  Output: 5
  Why?  : Buy on day 1 (price=1), sell on day 4 (price=6)
          profit = 6 - 1 = 5 (max possible)

  Constraints:
    - Must buy BEFORE you sell (sell index > buy index)
    - Only one buy + one sell transaction total
    - If prices are strictly decreasing → answer is 0 (don't transact)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 HOW TO THINK (Intuition)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Brute force asks: "for every pair (i, j) with j > i, what's the
  max prices[j] - prices[i]?" That's O(n²) — too slow.

  Key question to move brute → optimal:
  "If I'm standing on day j deciding to SELL, what's the best day
   to have bought?" → Obviously the day with the LOWEST price
   among all days BEFORE j.

  So instead of re-scanning backward for every j, just carry the
  minimum price seen so far as you move forward. At each day,
  compute profit = price_today - min_so_far, and track the best.

  This is the same "track running best while scanning once" idea
  used in Kadane's algorithm for Maximum Subarray.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 APPROACH 1 — BRUTE FORCE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea: Try every (buy day, sell day) pair where sell > buy

  Pseudocode:
    max_profit = 0
    for i in range(n):
        for j in range(i+1, n):
            profit = prices[j] - prices[i]
            max_profit = max(max_profit, profit)

  Time  : O(n²)  — nested loops over all pairs
  Space : O(1)

  Why not enough?
    → For n = 10⁵ (LeetCode constraint), 10¹⁰ operations → TLE

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 APPROACH 2 — OPTIMAL 
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea: Single pass, track min price seen so far + best profit

  Key steps:
    1. min_price = prices[0], max_profit = 0
    2. For each price starting from index 1:
         a. profit if selling today = price - min_price
         b. max_profit = max(max_profit, profit)
         c. min_price  = min(min_price, price)   ← update AFTER
            (so today's price can't be its own buy day)
    3. Return max_profit

  Time  : O(n)  — single pass
  Space : O(1)  — just two variables

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 DRY RUN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Input: prices = [7, 1, 5, 3, 6, 4]

  Start: min_price=7, max_profit=0

  price=1  profit=1-7=-6 → max_profit stays 0   min_price=min(7,1)=1
  price=5  profit=5-1=4  → max_profit=4         min_price=min(1,5)=1
  price=3  profit=3-1=2  → max_profit stays 4   min_price=min(1,3)=1
  price=6  profit=6-1=5  → max_profit=5         min_price=min(1,6)=1
  price=4  profit=4-1=3  → max_profit stays 5   min_price=min(1,4)=1

  Final: max_profit = 5 ✓ (buy@1, sell@6)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 EDGE CASES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  ✓ Strictly decreasing prices: [7,6,4,3,1] → 0 (never buy+sell)
  ✓ Single day: [5] → 0 (can't transact, no second day)
  ✓ Strictly increasing prices: [1,2,3,4,5] → 4 (buy day0, sell last)
  ✓ Two elements: [2,4] → 2
  ✓ All same price: [3,3,3] → 0

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 COMPLEXITY SUMMARY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                Time      Space
  Brute Force   O(n²)     O(1)
  Optimal       O(n)      O(1)    ← use this 

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 PATTERN LEARNED
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Greedy "Running Minimum / Maximum" while scanning once:
  → Whenever the answer depends on "best pair where one side must
    come BEFORE the other", don't re-scan for every index — just
    carry forward the best candidate seen so far (min price here).
  → This is the seed pattern for Kadane's Algorithm (Max Subarray)
    and later generalizes into DP state machines for Stock III/IV
    (buy/sell with multiple transactions, cooldowns, fees).
"""


# ─── BRUTE FORCE  O(n²) ───────────────────────────────────────────
def max_profit_brute(prices):
    n = len(prices)
    max_profit = 0
    for i in range(n):
        for j in range(i + 1, n):
            profit = prices[j] - prices[i]
            max_profit = max(max_profit, profit)
    return max_profit


# ─── OPTIMAL  O(n) ────────────────────────────────────────────────
def max_profit(prices):
    if not prices:
        return 0

    min_price = prices[0]
    max_profit = 0

    for price in prices[1:]:
        profit = price - min_price
        max_profit = max(max_profit, profit)
        min_price = min(min_price, price)

    return max_profit


# ─── TEST ─────────────────────────────────────────────────────────
if __name__ == "__main__":
    # Basic — profit exists
    print(max_profit([7, 1, 5, 3, 6, 4]))   # 5
    # Strictly decreasing — no profit
    print(max_profit([7, 6, 4, 3, 1]))       # 0
    # Strictly increasing — buy day0, sell last
    print(max_profit([1, 2, 3, 4, 5]))       # 4
    # Single day — no transaction possible
    print(max_profit([5]))                   # 0
    # All same price
    print(max_profit([3, 3, 3]))             # 0
