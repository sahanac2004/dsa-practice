"""
╔══════════════════════════════════════════════════════════════════╗
║  BEST TIME TO BUY AND SELL STOCK IV                                 ║
║  LeetCode #188  |  Difficulty: Hard  |  Topic: Arrays / DP          ║
║  Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/ ║
╚══════════════════════════════════════════════════════════════════╝

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📘 SECTION 1 — PROBLEM UNDERSTANDING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Given daily stock prices and an integer k, find the maximum profit
  achievable with AT MOST k transactions. Same rule as before — must
  sell before buying again.

  Input : k = 2, prices = [3,2,6,5,0,3]
  Output: 7

  Example 1 — basic:
    Input : k = 2, prices = [3,2,6,5,0,3]
    Output: 7
    Why?  : buy at 2, sell at 6 (profit 4), buy at 0, sell at 3
             (profit 3), total 7

  Example 2 — slightly tricky (k very large — more than needed):
    Input : k = 100, prices = [1,2,3,4,5]
    Output: 4
    Why?  : k=100 way exceeds n/2, so it behaves like unlimited
             transactions — but prices only ever rise, so just one
             continuous trade (buy 1, sell 5) is optimal

  Constraints:
    - 0 <= k <= 100
    - 0 <= prices.length <= 1000
    - 0 <= prices[i] <= 1000

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🧠 SECTION 2 — KANGLISH THINKING — ಹೇಗೆ ಯೋಚಿಸಬೇಕು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  Problem odi aada mele namma brain enu think maadabeeku:

  ಹಂತ 1 — Problem ಅರ್ಥ ಮಾಡಿಕೊಳ್ಳಿ (What are they asking?)
  ┌─────────────────────────────────────────────────────────┐
  │  Input ಏನು ಕೊಡ್ತಾರೆ?  →  prices + k (max transactions)   │
  │  Output ಏನು ಬೇಕು?     →  at most k transactions ಇಂದ      │
  │                          max profit                       │
  │  Constraints ಏನಿದೆ?   →  k<=100, n<=1000, k ಬಹಳ ಜಾಸ್ತಿ    │
  │                          ಆಗ್ಬೋದು (unlimited ಗೆ equivalent)│
  └─────────────────────────────────────────────────────────┘

  ಹಂತ 2 — ನನಗೆ ಗೊತ್ತಿರೋ simple way ಏನು? (Brute force thought)
  →  LC 123 (at most 2) ಗೆ 4 states use ಮಾಡಿದ್ವಿ — ಇಲ್ಲಿ k transactions
     ಗೆ 2k states ಬೇಕಾಗುತ್ತೆ. Recursive backtracking ಇಂದ ಎಲ್ಲಾ possible
     buy/sell day combinations try ಮಾಡ್ಬೋದು.
  →  ಆದರೆ ಇದು slow ಯಾಕೆ? → Exponential — ಪ್ರತಿ day ಗೂ buy/sell/skip
     3 choices, O(3^n) ಆಗ್ಬೋದು.

  ಹಂತ 3 — Better way ಹೇಗೆ ಯೋಚಿಸುವುದು? (Optimization thought)
  →  LC 123 ನ 4-state trick ಅನ್ನ generalize ಮಾಡಿದ್ರೆ — buy[0..k-1]
     ಮತ್ತು sell[0..k-1] ಅಂತ 2k arrays ಇಟ್ಕೊಂಡು, ಪ್ರತಿ price ಗೂ, ಪ್ರತಿ
     transaction index j ಗೂ update ಮಾಡ್ಬೋದು.
  →  ಅಹಾ moment: k ಬಹಳ ದೊಡ್ಡ ಆಗಿದ್ರೆ (k >= n/2), ಪ್ರತಿ profitable
     day pair ಅನ್ನ separate transaction ಆಗಿ ತಗೊಳ್ಳೋಕೆ ಆಗುತ್ತೆ — ಅದೇ
     "unlimited transactions" problem (LC 122), greedy sum of positive
     differences ಇಂದ solve ಆಗುತ್ತೆ! ಇದನ್ನ special case ಆಗಿ handle
     ಮಾಡಿದ್ರೆ, k*n DP time ಇಂದ avoid ಆಗುತ್ತೆ (k ಬಹಳ ದೊಡ್ಡ ಆಗಿದ್ರೆ).
  →  ಇದರಿಂದ ನಾವು DP (Generalized State Machine, k transactions) +
     Greedy Special Case (k >= n/2) use ಮಾಡಬಹುದು!

  ಹಂತ 4 — Technique ಯಾಕೆ ಇಲ್ಲಿ ಕೆಲಸ ಮಾಡುತ್ತೆ?
  →  "At most k transactions" ಅಂದ್ರೆ, LC 123 ನ 4-state idea ಅನ್ನ k
     ಸಲ repeat ಮಾಡಿದ್ರೆ ಸಾಕು — buy[j] depends on sell[j-1], sell[j]
     depends on buy[j].
  →  k >= n/2 ಆದ್ರೆ, n days ನಲ್ಲಿ ಗರಿಷ್ಠ n/2 transactions ಮಾತ್ರ
     ಸಾಧ್ಯ (ಪ್ರತಿ transaction ಗೆ ಕಡಿಮೆ 2 days ಬೇಕು) — ಆದ್ದರಿಂದ k
     restriction ಯಾವತ್ತೂ bind ಆಗಲ್ಲ, unlimited transactions ಆಗುತ್ತೆ.
  →  ಈ special case ಬಿಟ್ಟ್ರೆ, O(n*k) DP time acceptable (n,k <= 1000
     ಆದ್ರೆ 10^6, fine).

  💡 Interview ನಲ್ಲಿ ಹೇಗೆ ಮಾತಾಡಬೇಕು (Think out loud):
  →  "The naive way is exponential backtracking over buy/sell/skip
      choices each day — completely infeasible."
  →  "I recall the 4-state trick from 'at most 2 transactions' — I
      can generalize that to 2k states for k transactions."
  →  "I also notice that if k is at least n/2, the transaction limit
      never actually binds, so it reduces to the unlimited-
      transactions greedy problem — handling that separately avoids
      unnecessary O(n*k) work when k is huge."

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🏷️ SECTION 3 — TECHNIQUE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Primary   : DP → Generalized State Machine (buy[j], sell[j] for j in 0..k-1)
  Secondary : Greedy Special Case (k >= n/2 → unlimited transactions)

  WHY this technique?
  → Generalizing LC 123's 4-state trick to 2k states directly extends
    the same reasoning: each transaction's states depend only on the
    previous transaction's sell state and the previous day
  → The n/2 bound on max possible transactions makes large k
    equivalent to unlimited transactions — a much simpler greedy
  → Avoids O(n*k) work with unnecessarily large k, which could
    otherwise dominate runtime for no added benefit

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 💡 SECTION 4 — INTUITION (How to think — English)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Key observation: this is LC 123 generalized. Maintain buy[j] = best
  profit after the j-th buy, sell[j] = best profit after the j-th
  sell, for j from 0 to k-1. Each day, update all j in order:
  buy[j] = max(buy[j], sell[j-1] - price), sell[j] = max(sell[j],
  buy[j] + price) (with sell[-1] treated as 0). Additionally, since
  each transaction needs at least 2 days, k >= n/2 means the k-limit
  never restricts anything — treat it as unlimited transactions.

  The journey from brute to optimal:
    Brute thought   →  exponential backtracking over buy/sell/skip choices
    Problem with it →  O(3^n), totally infeasible
    Better question →  "how did the at-most-2 case generalize its
                        4-state trick — can I do it for general k?"
    Insight         →  2k running states, updated once per day, plus
                        a greedy shortcut when k is large enough to
                        never bind
    Optimal         →  O(n*k) DP (or O(n) greedy when k >= n/2)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🐢 SECTION 5 — APPROACH 1 — BRUTE FORCE (Exponential Backtracking)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    At each day, recursively try: do nothing, or buy (if not holding
    and transactions remain), or sell (if holding). Track the best
    profit across all valid sequences.

  Pseudocode:
    step 1: def rec(day, holding, transactions_left):
    step 2:   if day == n or transactions_left == 0: return 0
    step 3:   skip = rec(day+1, holding, transactions_left)
    step 4:   if not holding: act = -prices[day] + rec(day+1, True, transactions_left)
    step 5:   else: act = prices[day] + rec(day+1, False, transactions_left-1)
    step 6:   return max(skip, act)

  Time  : O(3^n)  →  Why: 2-3 branching choices per day, no memoization
  Space : O(n)    →  Why: recursion depth

  ಇದು ಯಾಕೆ ಸಾಕಾಗಲ್ಲ? (Why is this not enough?)
    → n=1000 ಆದ್ರೆ 3^1000 — astronomically large, ಸಂಪೂರ್ಣ infeasible.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🚶 SECTION 6 — APPROACH 2 — BETTER (Memoized DP — 3D State)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    Memoize the recursive brute force on (day, holding, transactions_
    left) so each state is computed once instead of exponentially
    many times.

  Time  : O(n*k)   →  n days * 2 holding states * k transaction counts
  Space : O(n*k)   →  memo table of that same size, plus recursion stack

  ಇನ್ನೂ better ಮಾಡಬಹುದಾ? → ಹೌದು — iterative state machine ಇಂದ, recursion
  overhead ಮತ್ತು O(n*k) space (memo table) ಅನ್ನ O(k) space ಗೆ ಇಳಿಸ್ಬೋದು
  (rolling states instead of full table), ಮತ್ತು k ದೊಡ್ಡ ಆದ್ರೆ greedy
  shortcut use ಮಾಡ್ಬಹುದು.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🚀 SECTION 7 — APPROACH 3 — OPTIMAL   (Generalized State Machine + Greedy Shortcut)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    If k >= n // 2, the transaction limit never binds — solve as
    unlimited transactions greedily (sum all positive consecutive
    differences). Otherwise, maintain buy[0..k-1] and sell[0..k-1]
    arrays, updating them once per day in transaction order.

  Key steps:
    1. if k >= n // 2: return sum(max(0, prices[i]-prices[i-1]) for i in 1..n-1)
    2. buy = [-infinity] * k; sell = [0] * k
    3. for price in prices:
         for j in range(k):
           buy[j] = max(buy[j], (sell[j-1] if j > 0 else 0) - price)
           sell[j] = max(sell[j], buy[j] + price)
    4. return sell[k-1] if k > 0 else 0

  ಕನ್ನಡದಲ್ಲಿ ಒಂದು ಸಲ ಹೇಳಿ (Kanglish one-liner so it sticks):
    → "k >= n/2 ಆದ್ರೆ, unlimited transactions greedy (consecutive
        positive differences sum) use ಮಾಡು. ಇಲ್ಲಾಂದ್ರೆ, buy[j] ಮತ್ತು
        sell[j] ಅಂತ k pairs ಇಟ್ಕೊಂಡು, ಪ್ರತಿ price ಗೂ, j=0 ಇಂದ k-1
        ತನಕ order ನಲ್ಲಿ update ಮಾಡ್ತಾ ಹೋಗು — ಕೊನೆಗೆ sell[k-1] ಯೇ
        answer!"

  Time  : O(n*k)  →  Why: for each of n days, update k transaction states
  Space : O(k)    →  Why: only buy[] and sell[] arrays of size k

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🔍 SECTION 8 — DRY RUN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Input: k=2, prices = [3,2,6,5,0,3]  (n=6, n//2=3, k=2 < 3, DP path)

  Init: buy=[-inf,-inf], sell=[0,0]

  price=3: j=0: buy[0]=max(-inf,0-3)=-3; sell[0]=max(0,-3+3)=0
           j=1: buy[1]=max(-inf,sell[0]-3)=max(-inf,0-3)=-3;
                sell[1]=max(0,-3+3)=0
  price=2: j=0: buy[0]=max(-3,0-2)=-2; sell[0]=max(0,-2+2)=0
           j=1: buy[1]=max(-3,sell[0]-2)=max(-3,0-2)=-2;
                sell[1]=max(0,-2+2)=0
  price=6: j=0: buy[0]=max(-2,0-6)=-2; sell[0]=max(0,-2+6)=4
           j=1: buy[1]=max(-2,sell[0]-6)=max(-2,4-6)=-2;
                sell[1]=max(0,-2+6)=4
  price=5: j=0: buy[0]=max(-2,0-5)=-2; sell[0]=max(4,-2+5)=4
           j=1: buy[1]=max(-2,sell[0]-5)=max(-2,4-5)=-2;
                sell[1]=max(4,-2+5)=4
  price=0: j=0: buy[0]=max(-2,0-0)=0; sell[0]=max(4,0+0)=4
           j=1: buy[1]=max(-2,sell[0]-0)=max(-2,4-0)=4;
                sell[1]=max(4,4+0)=4
  price=3: j=0: buy[0]=max(0,0-3)=0; sell[0]=max(4,0+3)=4
           j=1: buy[1]=max(4,sell[0]-3)=max(4,4-3)=4;
                sell[1]=max(4,4+3)=7

  Output: sell[1] = 7   matches expected

  ಇನ್ನೊಂದು example — tricky case (k huge, becomes unlimited):
  Input: k=100, prices=[1,2,3,4,5]  (n=5, n//2=2, k=100 >= 2 → greedy path)

  Greedy: sum of positive consecutive diffs = (2-1)+(3-2)+(4-3)+(5-4) = 4

  Output: 4   matches expected

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 ⚠️ SECTION 9 — EDGE CASES — ಇವನ್ನ ಮರೆಯಬೇಡ!
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  ✓ k == 0?                      →  no transactions allowed, answer 0
                                     (guard before entering DP/greedy)
  ✓ Empty prices array?          →  n=0, no trades possible, answer 0
  ✓ k >= n/2 (large k)?          →  greedy shortcut avoids wasted
                                     O(n*k) work with an oversized k
  ✓ Strictly decreasing prices?  →  every state stays at its "no
                                     profitable trade" baseline, answer 0
  ✓ k == 1?                      →  DP path degenerates correctly to
                                     the LC 121 single-transaction case

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📊 SECTION 10 — COMPLEXITY SUMMARY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                Time      Space
  Brute Force   O(3^n)    O(n)
  Better        O(n*k)    O(n*k)  (memoized 3D DP)
  Optimal       O(n*k)    O(k)    ← use this (or O(n) via greedy when k>=n/2)

  Time yaake ashtu?  → ಪ್ರತಿ day ಗೂ, k transaction states update
                        ಮಾಡ್ಬೇಕು — O(n*k). k >= n/2 ಆದ್ರೆ greedy
                        O(n) ಗೆ ಇಳಿಯುತ್ತೆ.
  Space yaake ashtu? → buy[] ಮತ್ತು sell[] arrays ಮಾತ್ರ, size k —
                        memo table ಬೇಡ.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🎯 SECTION 11 — PATTERN LEARNED — ಇದರಿಂದ ಕಲಿತದ್ದು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Pattern Name: Generalized DP State Machine (k Transactions) + Bound-Based Greedy Shortcut

  Ee pattern yaavaaga use maadabeeku?
  → "At most k transactions/operations" ಥರ problem ಕೇಳಿದಾಗ
  → A smaller-k version of the same problem (LC 121, LC 123) ಆಗಲೇ
    state-machine ಇಂದ solve ಆಗಿದ್ರೆ, ಅದನ್ನ k ಗೆ generalize ಮಾಡ್ಬಹುದಾ
    ಅಂತ ಯೋಚಿಸಿದಾಗ
  → k ನ theoretical maximum (ಇಲ್ಲಿ n/2) ಗಿಂತ input k ಜಾಸ್ತಿ ಇದ್ರೆ,
    constraint ಎಂದೂ bind ಆಗಲ್ಲ ಅಂತ ಗುರುತಿಸಿ simpler greedy ಗೆ ಇಳಿಸೋದು

  Idee pattern beere problemsalli kaanisatte:
  → Best Time to Buy/Sell Stock (LC 121) — base case, k=1
  → Best Time to Buy/Sell Stock III (LC 123) — base case, k=2
  → Best Time to Buy/Sell Stock with Cooldown/Fee — same family with
    extra state transitions

  Next time intaha problem bandre naanu modalu idannu think maadtene:
  → "'At most k' anta kanda takshana, chikka-k version already known
      idre adannu generalize maadu, mattu k ge upper bound edaadru
      ideye antha check maadi greedy shortcut sigutta anta noodu."

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🗣️ SECTION 12 — INTERVIEWALLI HEGE EXPLAIN MAADABEEKU
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  1. Understand:
     "I need max profit from at most k non-overlapping buy-sell
      transactions, given the daily price sequence."

  2. Brute force:
     "Recursive backtracking over buy/sell/skip choices per day is
      O(3^n) — infeasible. Memoizing on (day, holding, transactions
      left) gets it to O(n*k) time but O(n*k) space."

  3. Optimize:
     "I generalize the at-most-2 4-state trick to 2k states: buy[j]
      and sell[j] for each transaction index j, updated once per day.
      I also note that if k >= n/2, the limit never binds since each
      transaction needs at least 2 days — so I can just use the
      unlimited-transactions greedy instead."

  4. Code:
     "Check k >= n//2 first and use the greedy sum of positive
      consecutive differences if so. Otherwise maintain buy[] and
      sell[] arrays of size k, updating buy[j] from sell[j-1] and
      sell[j] from buy[j] for each day, in transaction order."

  5. Complexity:
     "Time O(n*k) for the DP path (or O(n) for the greedy shortcut).
      Space O(k) — just the buy/sell arrays."

  Mukhya: summane kuutu code bareyabeda! Interviewer ge ninna thinking
          process kaanabeku.
"""


# ═══════════════════════════════════════════════════════════════════
# BRUTE FORCE — O(3^n) Time | O(n) Space  (Exponential Backtracking)
# ═══════════════════════════════════════════════════════════════════
def max_profit_iv_brute(k, prices):
    """Idu modala aaloochane — prati day ge buy/sell/skip try maadi best profit hudukodu"""
    n = len(prices)

    def rec(day, holding, txn_left):
        if day == n or txn_left == 0:
            return 0
        skip = rec(day + 1, holding, txn_left)
        if not holding:
            act = -prices[day] + rec(day + 1, True, txn_left)
        else:
            act = prices[day] + rec(day + 1, False, txn_left - 1)
        return max(skip, act)

    return rec(0, False, k)


# ═══════════════════════════════════════════════════════════════════
# OPTIMAL — O(n*k) Time | O(k) Space  (Generalized State Machine + Greedy Shortcut)
# ═══════════════════════════════════════════════════════════════════
def max_profit_iv(k, prices):
    """Idu final answer — k >= n/2 aadre greedy, illaandre 2k-state DP"""
    n = len(prices)
    if n == 0 or k == 0:
        return 0

    if k >= n // 2:
        return sum(max(0, prices[i] - prices[i - 1]) for i in range(1, n))

    buy = [float('-inf')] * k
    sell = [0] * k

    for price in prices:
        for j in range(k):
            prev_sell = sell[j - 1] if j > 0 else 0
            buy[j] = max(buy[j], prev_sell - price)
            sell[j] = max(sell[j], buy[j] + price)

    return sell[k - 1]


# ═══════════════════════════════════════════════════════════════════
# TEST CASES
# ═══════════════════════════════════════════════════════════════════
if __name__ == "__main__":
    import sys
    sys.stdout.reconfigure(encoding="utf-8")

    # Test 1 — Basic example
    assert max_profit_iv(2, [3, 2, 6, 5, 0, 3]) == 7

    # Test 2 — Edge case: k == 0
    assert max_profit_iv(0, [1, 2, 3]) == 0

    # Test 3 — Edge case: empty prices
    assert max_profit_iv(2, []) == 0

    # Test 4 — Tricky: k huge, becomes unlimited transactions
    assert max_profit_iv(100, [1, 2, 3, 4, 5]) == 4

    # Test 5 — Tricky: strictly decreasing, no profit possible
    assert max_profit_iv(2, [9, 7, 5, 3, 1]) == 0

    # Test 6 — k == 1 degenerates to single transaction
    assert max_profit_iv(1, [7, 1, 5, 3, 6, 4]) == 5

    print("All tests passed!")
