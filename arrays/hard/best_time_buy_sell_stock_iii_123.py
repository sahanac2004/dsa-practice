"""
╔══════════════════════════════════════════════════════════════════╗
║  BEST TIME TO BUY AND SELL STOCK III                                ║
║  LeetCode #123  |  Difficulty: Hard  |  Topic: Arrays / DP          ║
║  Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/ ║
╚══════════════════════════════════════════════════════════════════╝

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📘 SECTION 1 — PROBLEM UNDERSTANDING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Given an array of daily stock prices, find the maximum profit
  achievable with AT MOST TWO transactions (buy then sell, buy then
  sell again). You must sell before buying again — no overlapping
  holdings.

  Input : prices = [3,3,5,0,0,3,1,4]
  Output: 6

  Example 1 — basic:
    Input : prices = [3,3,5,0,0,3,1,4]
    Output: 6
    Why?  : buy at 0, sell at 3 (profit 3), buy at 1, sell at 4
             (profit 3), total 6

  Example 2 — slightly tricky (only one transaction is best):
    Input : prices = [1,2,3,4,5]
    Output: 4
    Why?  : prices strictly increase, so a single buy-low-sell-high
             (buy at 1, sell at 5) beats splitting into two trades

  Constraints:
    - 1 <= prices.length <= 10^5
    - 0 <= prices[i] <= 10^5

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🧠 SECTION 2 — KANGLISH THINKING — ಹೇಗೆ ಯೋಚಿಸಬೇಕು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  Problem odi aada mele namma brain enu think maadabeeku:

  ಹಂತ 1 — Problem ಅರ್ಥ ಮಾಡಿಕೊಳ್ಳಿ (What are they asking?)
  ┌─────────────────────────────────────────────────────────┐
  │  Input ಏನು ಕೊಡ್ತಾರೆ?  →  ಪ್ರತಿ ದಿನದ stock price          │
  │  Output ಏನು ಬೇಕು?     →  at most 2 transactions ಇಂದ      │
  │                          max profit                       │
  │  Constraints ಏನಿದೆ?   →  n<=10^5, ಒಂದೇ ಸಲ hold ಮಾಡ್ಬೋದು, │
  │                          sell ಮಾಡ್ದೇ ಮತ್ತೊಂದು buy ಮಾಡೋಕೆ │
  │                          ಆಗಲ್ಲ                            │
  └─────────────────────────────────────────────────────────┘

  ಹಂತ 2 — ನನಗೆ ಗೊತ್ತಿರೋ simple way ಏನು? (Brute force thought)
  →  ಎಲ್ಲಾ possible pairs of transactions try ಮಾಡೋದು — first buy/sell
     day pair, second buy/sell day pair, ಎಲ್ಲಾ combinations ಗೂ profit
     ಲೆಕ್ಕ ಹಾಕಿ max ತಗೊಳ್ಳೋದು.
  →  ಆದರೆ ಇದು slow ಯಾಕೆ? → 4 nested loops (buy1,sell1,buy2,sell2)
     ಆದ್ರೆ O(n⁴), n=10^5 ಗೆ ಸಂಪೂರ್ಣ infeasible.

  ಹಂತ 3 — Better way ಹೇಗೆ ಯೋಚಿಸುವುದು? (Optimization thought)
  →  Single transaction problem ನಲ್ಲಿ (LC 121), ನಾವು running min
     price track ಮಾಡಿ, ಪ್ರತಿ ದಿನ profit = price - minSoFar ಅಂತ
     ಲೆಕ್ಕ ಹಾಕಿದ್ವಿ. ಇಲ್ಲಿ ಆ idea ಅನ್ನ "split point" concept ಜೊತೆ
     extend ಮಾಡ್ಬೋದು.
  →  ಅಹಾ moment: ಪ್ರತಿ day i ಅನ್ನ "split point" ಅಂತ ಯೋಚಿಸಿದ್ರೆ — left
     side ನಲ್ಲಿ (0 ಇಂದ i) best single transaction profit, right side
     ನಲ್ಲಿ (i ಇಂದ n-1) best single transaction profit — ಎರಡೂ ಸೇರಿಸಿದ್ರೆ
     "two transactions split at i" ನ profit! ಎಲ್ಲಾ i ಗೂ ಇದನ್ನ ಲೆಕ್ಕ
     ಹಾಕಿ max ತಗೊಂಡ್ರೆ ಸಾಕು.
  →  ಇದರಿಂದ ನಾವು DP (State Machine — 4 States: buy1, sell1, buy2,
     sell2) OR Prefix/Suffix Max Profit Split use ಮಾಡಬಹುದು!

  ಹಂತ 4 — Technique ಯಾಕೆ ಇಲ್ಲಿ ಕೆಲಸ ಮಾಡುತ್ತೆ?
  →  "At most 2 transactions" ಅಂದ್ರೆ, transactions ಯಾವಾಗ್ಲೂ time
     order ನಲ್ಲಿ ಇರುತ್ತೆ (first fully before second) — ಆದ್ದರಿಂದ ಒಂದು
     split point exist ಆಗುತ್ತೆ.
  →  Single-pass state machine (buy1,sell1,buy2,sell2 track ಮಾಡ್ತಾ)
     ಪ್ರತಿ day ಗೂ ಆ 4 states ಅನ್ನ update ಮಾಡಿದ್ರೆ, O(n) time, O(1)
     space ನಲ್ಲಿ ಸಿಗುತ್ತೆ.
  →  DP state machine ಅನ್ನ ಪ್ರತಿ transaction count k ಗೂ generalize
     ಮಾಡ್ಬಹುದು (LC 188 ಗೆ ಇದೇ idea extend ಆಗುತ್ತೆ).

  💡 Interview ನಲ್ಲಿ ಹೇಗೆ ಮಾತಾಡಬೇಕು (Think out loud):
  →  "The naive way tries every pair of buy/sell day pairs —
      O(n⁴), way too slow."
  →  "I recall that single-transaction stock problems use a running
      min-price trick — I can extend that to a state machine tracking
      4 states across one pass: first buy, first sell, second buy,
      second sell."
  →  "Each state only depends on the previous day's states, so I can
      update all 4 in a single O(n) pass with O(1) space."

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🏷️ SECTION 3 — TECHNIQUE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Primary   : DP → State Machine (buy1, sell1, buy2, sell2)
  Secondary : Greedy running-max/min (embedded in each state update)

  WHY this technique?
  → "At most 2 transactions" naturally decomposes into 4 sequential
    states, each depending only on the prior day's states
  → Single-transaction profit (LC 121) is the base case of this same
    state-machine idea with just 2 states (buy, sell)
  → A single forward pass suffices because each state's optimal value
    only needs yesterday's states, no lookahead required

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 💡 SECTION 4 — INTUITION (How to think — English)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Key observation: at most 2 transactions means the timeline splits
  into at most 2 non-overlapping buy-sell windows. Track 4 running
  quantities as you scan once: buy1 (max profit after first buy, i.e.
  -price, maximized means price minimized), sell1 (max profit after
  first sell), buy2 (max profit after second buy, using sell1's profit
  as the "budget"), sell2 (max profit after second sell — the answer).

  The journey from brute to optimal:
    Brute thought   →  try every pair of buy/sell day pairs
    Problem with it →  O(n⁴), completely infeasible
    Better question →  "can I track the best profit at each stage of
                        the transaction sequence as I scan once?"
    Insight         →  4 states (buy1,sell1,buy2,sell2), each only
                        needs the previous day's state values
    Optimal         →  single-pass state machine, O(n) time, O(1) space

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🐢 SECTION 5 — APPROACH 1 — BRUTE FORCE (Try Every Split Point + Two Single Transactions)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    For every possible split index i, compute the best single-
    transaction profit in prices[0..i] and the best single-transaction
    profit in prices[i..n-1], and add them. Take the max over all i.

  Pseudocode:
    step 1: best = 0
    step 2: for i in range(n):
    step 3:   left_profit = best_single_transaction(prices[:i+1])
    step 4:   right_profit = best_single_transaction(prices[i:])
    step 5:   best = max(best, left_profit + right_profit)
    step 6: return best

  Time  : O(n²)  →  Why: for each split point, an O(n) scan on each side
  Space : O(1)   →  Why: no extra arrays if computed inline

  ಇದು ಯಾಕೆ ಸಾಕಾಗಲ್ಲ? (Why is this not enough?)
    → n=10^5 ಆದ್ರೆ n² = 10^10 — TLE ಆಗತ್ತೆ, precompute ಮಾಡಿ improve
      ಮಾಡ್ಬಹುದು.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🚶 SECTION 6 — APPROACH 2 — BETTER (Precomputed Prefix/Suffix Max Profit)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    Precompute left[i] = best single-transaction profit using
    prices[0..i], and right[i] = best single-transaction profit using
    prices[i..n-1], each in one O(n) pass. Then scan once more to find
    max(left[i] + right[i]) over all split points i.

  Time  : O(n)  →  three linear passes (left, right, combine)
  Space : O(n)  →  two auxiliary arrays of size n

  ಇನ್ನೂ better ಮಾಡಬಹುದಾ? → ಹೌದು — DP state machine ಇಂದ, ಈ ಎರಡು arrays
  ಬೇಡ ಆಗುತ್ತೆ, O(1) space ನಲ್ಲಿ single pass ನಲ್ಲೇ ಆಗುತ್ತೆ.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🚀 SECTION 7 — APPROACH 3 — OPTIMAL   (DP State Machine — 4 States)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    Track 4 running values in one pass: buy1 (best "profit" after
    first buy — negative, so maximize means minimize price paid),
    sell1 (best profit after first sell), buy2 (best profit after
    second buy, spending from sell1's proceeds), sell2 (best profit
    after second sell — the final answer).

  Key steps:
    1. buy1 = sell1 = buy2 = sell2 = -infinity, 0, -infinity, 0 (init)
    2. for price in prices:
         buy1  = max(buy1, -price)
         sell1 = max(sell1, buy1 + price)
         buy2  = max(buy2, sell1 - price)
         sell2 = max(sell2, buy2 + price)
    3. return sell2

  ಕನ್ನಡದಲ್ಲಿ ಒಂದು ಸಲ ಹೇಳಿ (Kanglish one-liner so it sticks):
    → "buy1, sell1, buy2, sell2 ಅಂತ 4 states ಇಟ್ಕೊಂಡು, ಪ್ರತಿ price ಗೂ:
        buy1 = max(buy1, -price), sell1 = max(sell1, buy1+price),
        buy2 = max(buy2, sell1-price), sell2 = max(sell2, buy2+price)
        ಅಂತ update ಮಾಡ್ತಾ ಹೋಗು — ಕೊನೆಗೆ sell2 ಯೇ answer!"

  Time  : O(n)  →  Why: single pass, constant work per day
  Space : O(1)  →  Why: only 4 running variables tracked

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🔍 SECTION 8 — DRY RUN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Input: prices = [3,3,5,0,0,3,1,4]

  Init: buy1=-inf, sell1=0, buy2=-inf, sell2=0

  price=3: buy1=max(-inf,-3)=-3; sell1=max(0,-3+3)=0;
           buy2=max(-inf,0-3)=-3; sell2=max(0,-3+3)=0
  price=3: buy1=max(-3,-3)=-3; sell1=max(0,-3+3)=0;
           buy2=max(-3,0-3)=-3; sell2=max(0,-3+3)=0
  price=5: buy1=max(-3,-5)=-3; sell1=max(0,-3+5)=2;
           buy2=max(-3,2-5)=-3; sell2=max(0,-3+5)=2
  price=0: buy1=max(-3,0)=0; sell1=max(2,0+0)=2;
           buy2=max(-3,2-0)=2; sell2=max(2,2+0)=2
  price=0: buy1=max(0,0)=0; sell1=max(2,0+0)=2;
           buy2=max(2,2-0)=2; sell2=max(2,2+0)=2
  price=3: buy1=max(0,-3)=0; sell1=max(2,0+3)=3;
           buy2=max(2,3-3)=2; sell2=max(2,2+3)=5
  price=1: buy1=max(0,-1)=0; sell1=max(3,0+1)=3;
           buy2=max(2,3-1)=2; sell2=max(5,2+1)=5
  price=4: buy1=max(0,-4)=0; sell1=max(3,0+4)=4;
           buy2=max(2,4-4)=2; sell2=max(5,2+4)=6

  Output: sell2 = 6   matches expected

  ಇನ್ನೊಂದು example — tricky case (strictly increasing, one trade best):
  Input: prices = [1,2,3,4,5]

  Tracing shows sell1 grows to 4 (buy at 1, sell at 5), and buy2/sell2
  never find a profitable second trade worth taking (buying again
  after selling only loses ground since prices keep rising) — sell2
  ends up equal to sell1 = 4, since the state machine naturally allows
  "not taking" the second transaction (buy2 = sell1 - price stays
  close to sell1, and immediately re-selling at the same or better
  price keeps sell2 == sell1 when a second trade isn't beneficial).

  Output: 4   matches expected

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 ⚠️ SECTION 9 — EDGE CASES — ಇವನ್ನ ಮರೆಯಬೇಡ!
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  ✓ Single day (can't trade)?     →  sell2 stays 0, no transaction possible
  ✓ Strictly decreasing prices?   →  every state stays at its initial
                                     "no profitable trade" value, answer 0
  ✓ All same price?               →  buying and selling at the same
                                     price yields 0 profit throughout
  ✓ Only one profitable trade      →  state machine naturally uses
    exists (rest is flat/losing)?    only 1 transaction's worth of gain,
                                     second stays a no-op
  ✓ Best split uses only 1 trade   →  covered automatically since the
    instead of 2?                    state machine doesn't force a
                                     second real transaction to occur

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📊 SECTION 10 — COMPLEXITY SUMMARY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                Time      Space
  Brute Force   O(n²)     O(1)
  Better        O(n)      O(n)   (prefix/suffix profit arrays)
  Optimal       O(n)      O(1)    ← use this

  Time yaake ashtu?  → ಒಂದೇ pass ನಲ್ಲಿ 4 states update ಮಾಡ್ತೀವಿ,
                        ಪ್ರತಿ day ಗೂ constant work — O(n).
  Space yaake ashtu? → 4 running variables ಮಾತ್ರ, extra array ಬೇಡ.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🎯 SECTION 11 — PATTERN LEARNED — ಇದರಿಂದ ಕಲಿತದ್ದು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Pattern Name: DP State Machine (Buy/Sell Stages)

  Ee pattern yaavaaga use maadabeeku?
  → "At most k transactions" ಥರ stock problems ಕೇಳಿದಾಗ
  → Sequential stages ಇರೋ decision problems (state depends only on
    previous state, not full history)
  → Single pass + O(1) space ಬೇಕಾದಾಗ, DP array ಬದ್ಲು few variables

  Idee pattern beere problemsalli kaanisatte:
  → Best Time to Buy/Sell Stock (LC 121) — same idea, 2 states (buy,sell)
  → Best Time to Buy/Sell Stock IV (LC 188) — same idea generalized to
    k states/transactions
  → Best Time to Buy/Sell Stock with Cooldown/Fee — same state machine
    family with extra state transitions

  Next time intaha problem bandre naanu modalu idannu think maadtene:
  → "'At most k transactions' anta kanda takshana, k jodi states
      (buyI, sellI) track maadi, ondde pass nalli update maadu anta
      modalu yochisu."

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🗣️ SECTION 12 — INTERVIEWALLI HEGE EXPLAIN MAADABEEKU
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  1. Understand:
     "I need the max profit from at most 2 non-overlapping buy-sell
      transactions over the price sequence."

  2. Brute force:
     "Try every pair of buy/sell day pairs — O(n⁴), or find the best
      split point with recomputed single-transaction profits each
      time — O(n²). Both too slow for n up to 10^5."

  3. Optimize:
     "I can extend the single-transaction running-min trick into a
      4-state machine: first buy, first sell, second buy, second
      sell — each state only needs yesterday's values."

  4. Code:
     "Initialize buy1/buy2 to -infinity and sell1/sell2 to 0. For each
      price, update buy1 = max(buy1, -price), sell1 = max(sell1,
      buy1+price), buy2 = max(buy2, sell1-price), sell2 = max(sell2,
      buy2+price). Return sell2."

  5. Complexity:
     "Time O(n) — single pass. Space O(1) — just 4 running variables."

  Mukhya: summane kuutu code bareyabeda! Interviewer ge ninna thinking
          process kaanabeku.
"""


# ═══════════════════════════════════════════════════════════════════
# BRUTE FORCE — O(n^2) Time | O(1) Space  (Best Split Point, Recomputed)
# ═══════════════════════════════════════════════════════════════════
def max_profit_iii_brute(prices):
    """Idu modala aaloochane — every split point ge left/right best single trade recompute maadodu"""
    n = len(prices)

    def best_single(arr):
        if not arr:
            return 0
        min_price = arr[0]
        profit = 0
        for p in arr:
            min_price = min(min_price, p)
            profit = max(profit, p - min_price)
        return profit

    best = 0
    for i in range(n):
        left_profit = best_single(prices[:i + 1])
        right_profit = best_single(prices[i:])
        best = max(best, left_profit + right_profit)
    return best


# ═══════════════════════════════════════════════════════════════════
# OPTIMAL — O(n) Time | O(1) Space  (DP State Machine — 4 States)
# ═══════════════════════════════════════════════════════════════════
def max_profit_iii(prices):
    """Idu final answer — buy1,sell1,buy2,sell2 states track maadi single pass nalli solve maadu"""
    buy1 = buy2 = float('-inf')
    sell1 = sell2 = 0

    for price in prices:
        buy1 = max(buy1, -price)
        sell1 = max(sell1, buy1 + price)
        buy2 = max(buy2, sell1 - price)
        sell2 = max(sell2, buy2 + price)

    return sell2


# ═══════════════════════════════════════════════════════════════════
# TEST CASES
# ═══════════════════════════════════════════════════════════════════
if __name__ == "__main__":
    import sys
    sys.stdout.reconfigure(encoding="utf-8")

    # Test 1 — Basic example
    assert max_profit_iii([3, 3, 5, 0, 0, 3, 1, 4]) == 6

    # Test 2 — Edge case: single day, no transaction possible
    assert max_profit_iii([5]) == 0

    # Test 3 — Edge case: all same price
    assert max_profit_iii([4, 4, 4, 4]) == 0

    # Test 4 — Tricky: strictly increasing, one trade is optimal
    assert max_profit_iii([1, 2, 3, 4, 5]) == 4

    # Test 5 — Tricky: strictly decreasing, no profit possible
    assert max_profit_iii([9, 7, 5, 3, 1]) == 0

    print("All tests passed!")
