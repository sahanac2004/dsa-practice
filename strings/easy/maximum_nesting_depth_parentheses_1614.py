"""
╔════════════════════════════════════════════════════════════════════╗
║  MAXIMUM NESTING DEPTH OF THE PARENTHESES                          ║
║  LeetCode #1614  |  Difficulty: Easy  |  Topic: Strings/Stack      ║
║  Link: https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/ ║
╚════════════════════════════════════════════════════════════════════╝

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📘 SECTION 1 — PROBLEM UNDERSTANDING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  A string is a valid parentheses string (VPS) if either:
    - It is an empty string "", or
    - It can be written as AB, where A and B are VPS's, or
    - It can be written as (A), where A is a VPS.

  The nesting depth of a VPS is defined as:
    depth("")    = 0
    depth(A + B) = max(depth(A), depth(B))   where A, B are VPS
    depth("(" + A + ")") = 1 + depth(A)       where A is a VPS

  Note: LeetCode's actual `s` also contains digits and operators
  ('0'-'9', '+', '-', '*', '/') mixed in with the brackets — only
  '(' and ')' affect depth, everything else must be ignored.

  Input : s = valid parentheses string (with or without digits/ops)
  Output: integer — the maximum nesting depth

  Example 1 — basic (digits/operators mixed in, as on LeetCode):
    Input : s = "(1+(2*3)+((8)/4))+1"
    Output: 3
    Why?  : deepest nesting reaches 3 levels of '(' before closing —
            digits and '+', '*', '/' are just noise, not brackets

  Example 2 — slightly tricky (multiple separate groups):
    Input : s = "(()(()))"
    Output: 3
    Why?  : "(()(()))" → depth goes 1,2,1,2,3,2,1,0 → max is 3

  Example 3 — simplest case:
    Input : s = "()()"
    Output: 1
    Why?  : each pair only ever reaches depth 1, never nested

  Constraints:
    - 1 <= s.length <= 100
    - s is a valid parentheses string (for our version, only '(' and ')')

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🧠 SECTION 2 — KANGLISH THINKING — ಹೇಗೆ ಯೋಚಿಸಬೇಕು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  Problem odi aada mele namma brain enu think maadabeeku:

  ಹಂತ 1 — Problem ಅರ್ಥ ಮಾಡಿಕೊಳ್ಳಿ
  ┌─────────────────────────────────────────────────────────┐
  │  Input ಏನು ಕೊಡ್ತಾರೆ?  →  valid parentheses string     │
  │  Output ಏನು ಬೇಕು?     →  ಎಷ್ಟು ಆಳ (depth) ಗೆ           │
  │                           brackets nest ಆಗಿವೆ ಅನ್ನೋ     │
  │                           maximum number                │
  │  Constraints ಏನಿದೆ?   →  always valid string,          │
  │                           only '(' and ')' chars         │
  └─────────────────────────────────────────────────────────┘

  ಹಂತ 2 — ಇದು previous problem (Remove Outermost Parentheses) ಗೆ
           ಎಷ್ಟು close ಆಗಿದೆ ಅಂತ ಗಮನಿಸಿ!
  →  ಆ problem ನಲ್ಲಿ ನಾವು depth counter track ಮಾಡಿ
     outermost brackets skip ಮಾಡಿದ್ವಿ
  →  ಇಲ್ಲಿ ಕೂಡ depth counter track ಮಾಡಬೇಕು,
     ಆದ್ರೆ skip ಮಾಡುವ ಬದಲು — just maximum depth track ಮಾಡಬೇಕು!

  ಹಂತ 3 — Simple way ಏನು?
  →  '(' ಬಂದ್ರೆ → depth += 1
  →  ')' ಬಂದ್ರೆ → depth -= 1
  →  ಪ್ರತಿ step ನಲ್ಲೂ max_depth = max(max_depth, depth) update ಮಾಡು
  →  Single pass ಸಾಕು — extra stack ಕೂಡ ಬೇಕಿಲ್ಲ!

  ಹಂತ 4 — Technique ಯಾಕೆ ಇಲ್ಲಿ ಕೆಲಸ ಮಾಡುತ್ತೆ?
  →  '(' ಯಾವಾಗಲೂ depth ಒಂದು level ಹೆಚ್ಚಿಸುತ್ತೆ — so ಅಲ್ಲಿ
     max reach ಆಗಬಹುದು
  →  ')' depth ಕಡಿಮೆ ಮಾಡುತ್ತೆ — max ಗೆ ಸಂಬಂಧ ಇಲ್ಲ
  →  So '(' ನ ನಂತರವೇ max_depth check ಮಾಡಿದ್ರೆ ಸಾಕು

  💡 Interview ನಲ್ಲಿ ಹೇಗೆ ಮಾತಾಡಬೇಕು:
  →  "Track running depth with a counter — increment on '(',
      decrement on ')'"
  →  "Nesting depth can only increase right after an opening
      bracket, so update the max there"
  →  "No stack needed — we don't need to know WHAT's nested,
      only HOW deep — a counter is enough"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🏷️ SECTION 3 — TECHNIQUE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Primary   : Depth Counter — single pass
  Secondary : Running maximum

  WHY Depth Counter (no stack needed)?
  → We only need to know HOW DEEP we are, not what's on top
  → A stack of matching brackets would only ever hold '(' chars —
    its SIZE is literally the depth, so a plain integer counter
    gives us the same information with O(1) space

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 💡 SECTION 4 — INTUITION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  The key insight: depth only ever CHANGES by ±1 per character,
  and it can only reach a NEW maximum right when we open a
  bracket ('('). Closing brackets ')' can never create a new
  peak — they only bring us back down.

  The journey from brute to optimal:
    Brute thought   →  Use an actual stack, push '(' pop ')',
                       track max(len(stack))
    Problem with it →  We never use the stack's contents,
                       only its size → wasted space
    Better question →  "Do I need to know WHAT is nested,
                       or just HOW DEEP?"
    Insight         →  Just the depth NUMBER matters →
                       replace stack with a simple counter
    Optimal         →  Single pass, integer counter, O(1) space

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🐢 SECTION 5 — APPROACH 1 — BRUTE FORCE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    Use an actual stack. Push every '(' onto it, pop on every ')'.
    After every push, the stack's current size IS the current
    depth — track the maximum size ever seen.

  Pseudocode:
    step 1: stack = [], max_depth = 0
    step 2: for each char in s:
    step 3:   if '(' → push to stack
                       max_depth = max(max_depth, len(stack))
    step 4:   if ')' → pop from stack
    step 5: return max_depth

  Time  : O(n)  →  Why: single pass through string
  Space : O(n)  →  Why: stack can hold up to n/2 '(' characters

  ಇದು ಯಾಕೆ ಸಾಕಾಗಲ್ಲ?
    → Actually correct! But we never READ the stack's contents,
      only its size — so keeping the whole stack wastes O(n)
      space when a single counter would do

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🚀 SECTION 6 — APPROACH 2 — OPTIMAL (Depth Counter)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    Replace the stack with a plain integer `depth`. Increment on
    '(' and immediately update `max_depth`. Decrement on ')'
    (never a new peak, so no max update needed there).

  Key steps:
    1. depth = 0, max_depth = 0
    2. For each char:
       If '(' → depth += 1 → max_depth = max(max_depth, depth)
       If ')' → depth -= 1
    3. return max_depth

  ಕನ್ನಡದಲ್ಲಿ ಒಂದು ಸಲ ಹೇಳಿ:
    → "'(' ನೋಡಿದ್ರೆ: depth++ ಮಾಡು, ಆಮೇಲೆ max_depth update ಮಾಡು.
       ')' ನೋಡಿದ್ರೆ: depth-- ಮಾಡು, max update ಬೇಕಿಲ್ಲ ಯಾಕಂದ್ರೆ
       depth ಕಡಿಮೆ ಆಗ್ತಿದೆ, ಹೊಸ peak ಆಗಲ್ಲ."

  Time  : O(n)  →  Why: single pass, each char processed once
  Space : O(1)  →  Why: only two integer variables used

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🔍 SECTION 7 — DRY RUN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Input: s = "(()(()))"

  char  depth_before  action                depth_after  max_depth
  '('   0             depth++ → max update  1            1
  '('   1             depth++ → max update  2            2
  ')'   2             depth--                1            2
  '('   1             depth++ → max update  2            2
  '('   2             depth++ → max update  3            3
  ')'   3             depth--                2            3
  ')'   2             depth--                1            3
  ')'   1             depth--                0            3

  Output: 3 ✓

  ಇನ್ನೊಂದು example — simplest:
  Input: s = "()()"

  char  depth_before  action                depth_after  max_depth
  '('   0             depth++ → max update  1            1
  ')'   1             depth--                0            1
  '('   0             depth++ → max update  1            1
  ')'   1             depth--                0            1

  Output: 1 ✓

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 ⚠️ SECTION 8 — EDGE CASES — ಇವನ್ನ ಮರೆಯಬೇಡ!
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  ✓ Single pair "()"?              →  1 — one level of nesting
  ✓ Deeply nested "((()))"?        →  3 — every bracket nests deeper
  ✓ All separate "()()()"          →  1 — never nests, always depth 1
  ✓ Empty string ""?               →  0 — no brackets at all
  ✓ Digits/operators mixed in?     →  ignore them completely — only
                                       '(' / ')' may change depth
                                       (e.g. "(1+(2*3)+((8)/4))+1" → 3)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📊 SECTION 9 — COMPLEXITY SUMMARY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                Time    Space
  Brute Force   O(n)    O(n)
  Optimal       O(n)    O(1)   ← use this ✅

  Time yaake O(n)?  → String ಒಮ್ಮೆ ಮಾತ್ರ traverse, each char O(1)
  Space yaake O(1)? → Depth ಮತ್ತು max_depth — ಎರಡು int variables ಮಾತ್ರ

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🎯 SECTION 10 — PATTERN LEARNED — ಇದರಿಂದ ಕಲಿತದ್ದು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Pattern Name: Depth Counter for Parentheses (space-optimized)

  Ee pattern yaavaaga use maadabeeku?
  → Stack ba varigaagi content ಬೇಕಾಗದೇ ಇದ್ದಾಗ, ಕೇವಲ SIZE
     (depth/level) ಮಾತ್ರ ಬೇಕಾದಾಗ → plain counter use ಮಾಡು
  → "Maximum depth", "current level", "nesting" type problems

  Idee pattern beere problemsalli kaanisatte:
  → Remove Outermost Parentheses #1021 (previous problem)
  → Valid Parentheses #20 (needs real stack — multiple bracket types)
  → Score of Parentheses #856 (next problem!)

  Next time intaha problem bandre naanu modalu idannu think maadtene:
  → "Parentheses problem → depth counter think maadu!
     Content nodabekagide → real stack.
     Level/size mattra bekagide → plain int counter saaku!"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🗣️ SECTION 11 — INTERVIEWALLI HEGE EXPLAIN MAADABEEKU
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  1. Understand:
     "Find the maximum nesting depth of a valid parentheses
      string — how many levels deep does it ever go."

  2. Brute force:
     "Use a real stack, push '(' pop ')', track max stack size.
      O(n) time, O(n) space."

  3. Optimize:
     "I never look INSIDE the stack, only its size — so replace
      it with a plain integer counter. Same logic, O(1) space."

  4. Code:
     "depth counter. For '(': depth++, then update max_depth.
      For ')': depth--, no max update needed."

  5. Complexity:
     "Time O(n) — single pass. Space O(1) — two integers only."

  Mukhya: stack size mattra bekagidre, stack replace maadi
          counter use maadu — space save aagatte!
"""


# ═══════════════════════════════════════════════════════════════════
# BRUTE FORCE — O(n) Time | O(n) Space (Actual stack)
# ═══════════════════════════════════════════════════════════════════
def max_depth_brute(s):
    """
    Idu modala aaloochane — real stack use maadi, size track maadu
    Digits/operators are NOT brackets — only '(' and ')' affect the stack
    """
    stack = []
    max_depth = 0

    for char in s:
        if char == '(':
            stack.append(char)
            max_depth = max(max_depth, len(stack))
        elif char == ')':
            stack.pop()
        # any other char (digit, '+', '*', '/', etc.) → ignore, not a bracket

    return max_depth


# ═══════════════════════════════════════════════════════════════════
# OPTIMAL — O(n) Time | O(1) Space (Depth Counter)
# ═══════════════════════════════════════════════════════════════════
def max_depth(s):
    """
    Idu final answer — stack ge badalu plain int counter,
    depth ondu level jaasti aadaga max_depth update maadu
    Digits/operators are NOT brackets — only '(' and ')' change depth
    """
    depth = 0
    max_depth_seen = 0

    for char in s:
        if char == '(':
            depth += 1                                # nest one level deeper
            max_depth_seen = max(max_depth_seen, depth)  # new peak? check
        elif char == ')':                              # only real closers
            depth -= 1                                 # unwind one level
        # any other char (digit, '+', '*', '/', etc.) → depth unchanged

    return max_depth_seen


# ═══════════════════════════════════════════════════════════════════
# TEST CASES
# ═══════════════════════════════════════════════════════════════════
if __name__ == "__main__":
    # Test 1 — Basic
    assert max_depth("(()(()))") == 3

    # Test 2 — All separate pairs (never nests)
    assert max_depth("()()") == 1

    # Test 3 — Single pair
    assert max_depth("()") == 1

    # Test 4 — Deeply nested
    assert max_depth("((()))") == 3

    # Test 5 — Empty string
    assert max_depth("") == 0

    # Test 6 — Real LeetCode-style input with digits and operators
    assert max_depth("(1+(2*3)+((8)/4))+1") == 3

    # Test 7 — Brute force must agree too
    assert max_depth_brute("(1+(2*3)+((8)/4))+1") == 3

    print("All tests passed!")
