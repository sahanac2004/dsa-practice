"""
╔══════════════════════════════════════════════════════════════════╗
║  PROBLEM NAME                                                    ║
║  LeetCode #   |  Difficulty: Easy/Medium/Hard  |  Topic:        ║
║  Link: https://leetcode.com/problems/...                         ║
╚══════════════════════════════════════════════════════════════════╝

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🧠 KANGLISH THINKING — ಹೇಗೆ ಯೋಚಿಸಬೇಕು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  ಮೊದಲು problem odidaga ನಮ್ಮ brain ಏನು think ಮಾಡಬೇಕು:

  ಹಂತ 1 — Problem ಅರ್ಥ ಮಾಡಿಕೊಳ್ಳಿ (What are they asking?)
  ┌─────────────────────────────────────────────────────────┐
  │  Input ಏನು ಕೊಡ್ತಾರೆ?  →  <fill here>                  │
  │  Output ಏನು ಬೇಕು?     →  <fill here>                  │
  │  Constraints ಏನಿದೆ?   →  <fill here>                  │
  └─────────────────────────────────────────────────────────┘

  ಹಂತ 2 — ನನಗೆ ಗೊತ್ತಿರೋ simple way ಏನು? (Brute force thought)
  →  <Kanglish explanation of obvious first approach>
  →  ಆದರೆ ಇದು slow ಯಾಕೆ? → <why it's not good enough>

  ಹಂತ 3 — Better way ಹೇಗೆ ಯೋಚಿಸುವುದು? (Optimization thought)
  →  <Key question you ask yourself>
  →  <The aha moment in Kanglish>
  →  ಇದರಿಂದ ನಾವು <technique name> use ಮಾಡಬಹುದು!

  ಹಂತ 4 — Technique ಯಾಕೆ ಇಲ್ಲಿ ಕೆಲಸ ಮಾಡುತ್ತೆ?
  →  <Signal 1 from problem that tells you which technique>
  →  <Signal 2>
  →  <Signal 3>

  💡 Interview ನಲ್ಲಿ ಹೇಗೆ ಮಾತಾಡಬೇಕು (Think out loud):
  →  "So I'm seeing that... <observation>"
  →  "The brute force would be... but that's O(n²)"
  →  "I notice that if I... then I can reduce it to O(n)"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🏷️ TECHNIQUE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Primary   : <e.g. Sliding Window → Variable Size>
  Secondary : <e.g. HashMap (frequency count)>

  WHY this technique?
  → <signal 1 from problem that told you>
  → <signal 2 from problem that told you>
  → <signal 3 from problem that told you>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📘 PROBLEM UNDERSTANDING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  <Explain the problem in your own simple words — 2 to 3 lines>

  Input :
  Output:

  Example 1:
    Input : 
    Output: 
    Why?  : 

  Example 2 (slightly tricky):
    Input : 
    Output: 
    Why?  : 

  Constraints:
    -
    -

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 💡 INTUITION (How to think — English)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  <What is the KEY observation that unlocks this problem?>
  <What pattern did you notice in the input/output?>
  <What question did you ask yourself that led to the optimal approach?>

  The journey from brute to optimal:
    Brute thought   →  <what first comes to mind>
    Problem with it →  <why it is slow>
    Better question →  <what you ask yourself>
    Insight         →  <the aha moment>
    Optimal         →  <what technique to use and why>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🐢 APPROACH 1 — BRUTE FORCE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    <Explain in plain English, no code yet>

  Pseudocode:
    step 1:
    step 2:
    step 3:

  Time  : O( )  →  Why: <explain>
  Space : O( )  →  Why: <explain>

  ಇದು ಯಾಕೆ ಸಾಕಾಗಲ್ಲ? (Why is this not enough?)
    → <Kanglish explanation — e.g. n=10^5 ಆದ್ರೆ 10^10 operations, TLE ಆಗತ್ತೆ>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🚶 APPROACH 2 — BETTER (if exists)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    <What improvement did you make over brute force?>

  Time  : O( )
  Space : O( )

  ಇನ್ನೂ better ಮಾಡಬಹುದಾ? → <yes/no and why>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🚀 APPROACH 3 — OPTIMAL
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    <Explain the optimal approach clearly in plain English>

  Key steps:
    1. 
    2. 
    3. 

  ಕನ್ನಡದಲ್ಲಿ ಒಂದು ಸಲ ಹೇಳಿ (Say it once in Kanglish so it sticks):
    → <e.g. "Array sort ಮಾಡಿ, ಆಮೇಲೆ L ಮತ್ತು R pointers ಇಟ್ಟು
              sum < target ಆದ್ರೆ L++ ಮಾಡು, sum > target ಆದ್ರೆ R-- ಮಾಡು,
              equal ಆದ್ರೆ answer ಸಿಕ್ಕಿತು!">

  Time  : O( )  →  Why: <explain>
  Space : O( )  →  Why: <explain>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🔍 DRY RUN — Step by step trace
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Input: 

  i=0  →  variables: <state>  →  <what happened and why>
  i=1  →  variables: <state>  →  <what happened and why>
  i=2  →  variables: <state>  →  <what happened and why>

  Output: 

  ಇನ್ನೊಂದು example — tricky case:
  Input: 
  <trace>
  Output: 

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 ⚠️ EDGE CASES — ಇವನ್ನ ಮರೆಯಬೇಡ!
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  ✓ Empty array/string?           →  <how handled>
  ✓ Single element?               →  <how handled>
  ✓ All same elements?            →  <how handled>
  ✓ Negative numbers?             →  <how handled>
  ✓ <problem specific edge case>  →  <how handled>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📊 COMPLEXITY SUMMARY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                Time      Space     Notes
  Brute Force   O( )      O( )
  Better        O( )      O( )      [if applicable]
  Optimal       O( )      O( )      use this

  Time ಯಾಕೆ ಅಷ್ಟು?  → <plain reason — e.g. "array ಒಮ್ಮೆ traverse ಮಾಡ್ತೇವೆ">
  Space ಯಾಕೆ ಅಷ್ಟು? → <plain reason — e.g. "HashMap ನಲ್ಲಿ n elements store ಮಾಡ್ತೇವೆ">

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🎯 PATTERN LEARNED — ಇದರಿಂದ ಕಲಿತದ್ದು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Pattern Name: <e.g. HashMap Complement Lookup>

  ಈ pattern ಯಾವಾಗ use ಮಾಡಬೇಕು?
  → <Signal 1: what kind of problem hints at this pattern>
  → <Signal 2>
  → <Signal 3>

  ಇದೇ pattern ಬೇರೆ problems ನಲ್ಲಿ ಕಾಣಿಸುತ್ತೆ:
  → <Related problem 1>
  → <Related problem 2>
  → <Related problem 3>

  Next time ಇಂತಹ problem ಬಂದ್ರೆ ನಾನು ಮೊದಲು ಇದನ್ನ think ಮಾಡ್ತೇನೆ:
  → "<One line reminder to future self in Kanglish>"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🗣️ INTERVIEW ನಲ್ಲಿ ಹೇಗೆ EXPLAIN ಮಾಡಬೇಕು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  (Interviewer ಮುಂದೆ ಇದನ್ನ ಹೀಗೆ ಹೇಳು — think out loud)

  1. Understand:
     "So the problem is asking me to <restate in own words>..."

  2. Brute force:
     "The naive approach would be to <brute idea>...
      which gives O(...) time, but that might TLE for large inputs."

  3. Optimize:
     "I notice that <key observation>...
      so instead of doing X, I can do Y using <technique>."

  4. Code:
     "I'll use a <HashMap/Two Pointer/etc> because <reason>."

  5. Complexity:
     "Time complexity is O(...) because <reason>.
      Space complexity is O(...) because <reason>."

  ಮುಖ್ಯ: ಸುಮ್ಮನೆ ಕೂತು code ಬರೆಯಬೇಡ — always think out loud!
         Interviewer ಗೆ ನಿನ್ನ thinking process ಕಾಣಬೇಕು.
"""


# ═══════════════════════════════════════════════════════════════════
# BRUTE FORCE — O( ) Time | O( ) Space
# ═══════════════════════════════════════════════════════════════════
def solution_brute():
    """
    ಇದು ಮೊದಲ ಆಲೋಚನೆ — simple but slow
    """
    pass


# ═══════════════════════════════════════════════════════════════════
# OPTIMAL — O( ) Time | O( ) Space
# ═══════════════════════════════════════════════════════════════════
def solution():
    """
    ಇದು final answer — fast and clean
    """
    pass


# ═══════════════════════════════════════════════════════════════════
# TEST CASES
# ═══════════════════════════════════════════════════════════════════
if __name__ == "__main__":
    # Test 1 — Basic example
    
    # Test 2 — Edge case: empty / single element
    
    # Test 3 — Edge case: all same elements
    
    # Test 4 — Tricky / negative numbers
    
    print("All tests passed!  ")
