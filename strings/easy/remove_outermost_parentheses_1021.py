"""
╔════════════════════════════════════════════════════════════════════╗
║  REMOVE OUTERMOST PARENTHESES                                      ║
║  LeetCode #1021  |  Difficulty: Easy  |  Topic: Strings/Stack      ║
║  Link: https://leetcode.com/problems/remove-outermost-parentheses/ ║
╚════════════════════════════════════════════════════════════════════╝

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📘 SECTION 1 — PROBLEM UNDERSTANDING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  A valid parentheses string is either:
    - Empty ""
    - "(" + A + ")" where A is valid
    - A + B where A and B are valid

  A primitive string is a valid parentheses string that CANNOT
  be split into two non-empty valid strings.

  Given a valid parentheses string, remove the outermost
  parentheses of every primitive substring and return the result.

  Input : s = valid parentheses string
  Output: string with outermost parentheses of each primitive removed

  Example 1 — basic:
    Input : s = "(()())(())"
    Output: "()()()"
    Why?  : primitives are "(()())" and "(())"
            remove outermost → "()()" + "()" = "()()()"

  Example 2 — slightly tricky (nested deeply):
    Input : s = "(()())(())(()(()))"
    Output: "()()()()(())"
    Why?  : primitives = "(()())", "(())", "(()(()))"
            → "()()" + "()" + "()(())" = "()()()()(())"

  Example 3 — simplest case:
    Input : s = "()()"
    Output: ""
    Why?  : primitives = "()" and "()"
            remove both outermost → "" + "" = ""

  Constraints:
    - 1 <= s.length <= 10^5
    - s is a valid parentheses string
    - s consists of '(' and ')' only

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🧠 SECTION 2 — KANGLISH THINKING — ಹೇಗೆ ಯೋಚಿಸಬೇಕು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  Problem odi aada mele namma brain enu think maadabeeku:

  ಹಂತ 1 — Problem ಅರ್ಥ ಮಾಡಿಕೊಳ್ಳಿ
  ┌─────────────────────────────────────────────────────────┐
  │  Input ಏನು ಕೊಡ್ತಾರೆ?  →  valid parentheses string     │
  │  Output ಏನು ಬೇಕು?     →  ಪ್ರತಿ primitive group ರ      │
  │                           outermost brackets remove     │
  │                           ಮಾಡಿದ string                 │
  │  Constraints ಏನಿದೆ?   →  always valid string,         │
  │                           only '(' and ')' chars        │
  └─────────────────────────────────────────────────────────┘

  ಹಂತ 2 — ನನಗೆ ಗೊತ್ತಿರೋ simple way ಏನು?
  →  ಮೊದಲು primitives find ಮಾಡೋಣ, ಆಮೇಲೆ ಪ್ರತಿದರ
     first '(' ಮತ್ತು last ')' remove ಮಾಡೋಣ
  →  Stack use ಮಾಡಿ primitives identify ಮಾಡಬಹುದು
  →  ಆದರೆ ಇದು slow ಯಾಕೆ? → 2 passes ಬೇಕಾಗತ್ತೆ

  ಹಂತ 3 — Better way ಹೇಗೆ ಯೋಚಿಸುವುದು?
  →  "Outermost bracket ಅಂದ್ರೆ ಏನು?"
  →  '(' → depth 0 ಇದ್ದಾಗ ಬಂದ್ರೆ → outermost opening!
  →  ')' → depth 1 ಇದ್ದಾಗ ಬಂದ್ರೆ → outermost closing!
  →  So: depth > 0 ಇದ್ದಾಗ ಮಾತ್ರ '(' add ಮಾಡು
         depth > 1 ಇದ್ದಾಗ ಮಾತ್ರ ')' add ಮಾಡು
  →  ಇದರಿಂದ ನಾವು Depth Counter — single pass use ಮಾಡಬಹুದು!

  ಹಂತ 4 — Technique ಯಾಕೆ ಇಲ್ಲಿ ಕೆಲಸ ಮಾಡುತ್ತೆ?
  →  depth == 0 ಅಂದ್ರೆ ನಾವು primitive ರ outside ಇದ್ದೇವೆ
  →  depth > 0 ಅಂದ್ರೆ outermost bracket ನ inside ಇದ್ದೇವೆ
  →  Only inside characters ಬೇಕು → depth check ಮಾಡಿ add ಮಾಡು

  💡 Interview ನಲ್ಲಿ ಹೇಗೆ ಮಾತಾಡಬೇಕು:
  →  "Outermost '(' is the one that takes depth from 0 to 1"
  →  "Outermost ')' is the one that takes depth from 1 to 0"
  →  "So skip those — only add chars when depth > 0 for '('
      and depth > 1 for ')'"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🏷️ SECTION 3 — TECHNIQUE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Primary   : Stack / Depth Counter — single pass
  Secondary : String building

  WHY Depth Counter?
  → Outermost bracket = depth changes between 0 and 1
  → Track depth to know if current char is outermost or inner
  → depth > 0 for '(' and depth > 1 for ')' → skip outermost

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 💡 SECTION 4 — INTUITION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  The key insight: the outermost '(' of a primitive is the one
  that transitions depth from 0 → 1.
  The outermost ')' of a primitive is the one that transitions
  depth from 1 → 0.
  So we just skip these and include everything else!

  The journey from brute to optimal:
    Brute thought   →  Find primitives with stack, slice, remove ends
    Problem with it →  Two passes, extra slicing operations
    Better question →  "Which brackets are outermost exactly?"
    Insight         →  Outermost = depth boundary (0↔1 transitions)
                       Everything at depth > 0 = inner = keep it!
    Optimal         →  Single pass, depth counter, conditional append

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🐢 SECTION 5 — APPROACH 1 — BRUTE FORCE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    Use a stack to find each primitive. When stack becomes empty,
    we have found one complete primitive. Slice off first and last
    char (outermost brackets), add inner part to result.

  Pseudocode:
    step 1: stack = [], start = 0, result = ""
    step 2: for each char:
    step 3:   if '(' → push to stack
    step 4:   if ')' → pop from stack
    step 5:   if stack empty → found primitive s[start:i+1]
                               result += s[start+1 : i]  (skip outer)
                               start = i + 1
    step 6: return result

  Time  : O(n)  →  Why: single pass through string
  Space : O(n)  →  Why: stack can hold up to n/2 elements

  ಇದು ಯಾಕೆ ಸಾಕಾಗಲ್ಲ?
    → Actually valid! But slightly more code. Depth counter cleaner.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🚀 SECTION 6 — APPROACH 2 — OPTIMAL (Depth Counter)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    Track depth. Add '(' only if depth > 0 (not outermost).
    Add ')' only if depth > 1 (not outermost).
    Update depth after decision for ')' and before for '('.

  Key steps:
    1. depth = 0, result = []
    2. For each char:
       If '(' → if depth > 0: add to result → depth += 1
       If ')' → depth -= 1 → if depth > 0: add to result
    3. return "".join(result)

  ಕನ್ನಡದಲ್ಲಿ ಒಂದು ಸಲ ಹೇಳಿ:
    → "'(' ನೋಡಿದ್ರೆ: depth > 0 ಆದ್ರೆ ಮಾತ್ರ add ಮಾಡು,
       ಆಮೇಲೆ depth++.
       ')' ನೋಡಿದ್ರೆ: depth-- ಮಾಡು, depth > 0 ಆದ್ರೆ ಮಾತ್ರ add ಮಾಡು.
       ಹೀಗೆ outermost brackets automatically skip ಆಗತ್ತೆ!"

  Time  : O(n)  →  Why: single pass, each char processed once
  Space : O(n)  →  Why: result list holds at most n chars

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🔍 SECTION 7 — DRY RUN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Input: s = "(()())(())"

  char  depth_before  action              depth_after  result
  '('   0             depth>0? NO→skip    1            ""
  '('   1             depth>0? YES→add    2            "("
  ')'   2             depth-- →1>0?YES→add 1           "()"
  '('   1             depth>0? YES→add    2            "()("
  ')'   2             depth-- →1>0?YES→add 1           "()()"
  ')'   1             depth-- →0>0?NO→skip 0           "()()"
  '('   0             depth>0? NO→skip    1            "()()"
  '('   1             depth>0? YES→add    2            "()()("
  ')'   2             depth-- →1>0?YES→add 1           "()()()"
  ')'   1             depth-- →0>0?NO→skip 0           "()()()"

  Output: "()()()" ✓

  ಇನ್ನೊಂದು example — simplest:
  Input: s = "()()"

  char  depth_before  action              depth_after  result
  '('   0             depth>0? NO→skip    1            ""
  ')'   1             depth-- →0>0?NO→skip 0           ""
  '('   0             depth>0? NO→skip    1            ""
  ')'   1             depth-- →0>0?NO→skip 0           ""

  Output: "" ✓

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 ⚠️ SECTION 8 — EDGE CASES — ಇವನ್ನ ಮರೆಯಬೇಡ!
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  ✓ Single primitive "()"?         →  "" — both chars are outermost
  ✓ Deeply nested "((()))"?        →  "(())" — only outer pair removed
  ✓ Multiple simple "()()()"?      →  "" — all are outermost pairs
  ✓ Long nested "((()())())"?      →  "(()())()" — one primitive only

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📊 SECTION 9 — COMPLEXITY SUMMARY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                Time    Space
  Brute Force   O(n)    O(n)
  Optimal       O(n)    O(n)   ← use this ✅

  Time yaake O(n)?  → String ಒಮ್ಮೆ ಮಾತ್ರ traverse, each char O(1)
  Space yaake O(n)? → Result list atmost n chars store maadatte

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🎯 SECTION 10 — PATTERN LEARNED — ಇದರಿಂದ ಕಲಿತದ್ದು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Pattern Name: Depth Counter for Parentheses

  Ee pattern yaavaaga use maadabeeku?
  → Parentheses string alli depth track maadabekaagidraga
  → "Outermost", "innermost", "level k" brackets find maadabekaagidraga
  → Valid parentheses structure problems

  Idee pattern beere problemsalli kaanisatte:
  → Maximum Nesting Depth of Parentheses #1614 (next problem!)
  → Valid Parentheses #20 (classic stack)
  → Longest Valid Parentheses #32 (hard version)

  Next time intaha problem bandre naanu modalu idannu think maadtene:
  → "Parentheses problem → depth counter think maadu!
     Outermost = depth 0↔1 boundary. Inner = depth > 0.
     Ek pass alli O(n) alli solve!"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🗣️ SECTION 11 — INTERVIEWALLI HEGE EXPLAIN MAADABEEKU
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  1. Understand:
     "Remove the outermost parentheses of every primitive
      decomposition of the string."

  2. Brute force:
     "Use a stack to find each primitive, then slice off first
      and last character of each. O(n) but two passes."

  3. Optimize:
     "The outermost '(' transitions depth 0→1.
      The outermost ')' transitions depth 1→0.
      So I just skip chars at those transitions — single pass!"

  4. Code:
     "depth counter. For '(': add if depth>0, then depth++.
      For ')': depth--, add if depth>0."

  5. Complexity:
     "Time O(n) — single pass. Space O(n) — result string."

  Mukhya: summane kuutu code bareyabeda!
          depth 0↔1 boundary = outermost — clean insight!
"""


# ═══════════════════════════════════════════════════════════════════
# BRUTE FORCE — O(n) Time | O(n) Space (Stack approach)
# ═══════════════════════════════════════════════════════════════════
def remove_outer_parentheses_brute(s):
    """
    Idu modala aaloochane — stack use maadi primitives find maadu,
    aamel outermost remove maadu
    """
    result = []
    stack = []
    start = 0

    for i, char in enumerate(s):
        if char == '(':
            stack.append(char)
        else:
            stack.pop()

        if not stack:
            # found one complete primitive s[start:i+1]
            # add inner part only (skip first and last char)
            result.append(s[start + 1 : i])
            start = i + 1

    return "".join(result)


# ═══════════════════════════════════════════════════════════════════
# OPTIMAL — O(n) Time | O(n) Space (Depth Counter)
# ═══════════════════════════════════════════════════════════════════
def remove_outer_parentheses(s):
    """
    Idu final answer — depth counter, outermost skip maadu
    depth > 0 alli '(' add maadu
    depth > 0 alli ')' add maadu (after decrement)
    """
    result = []
    depth = 0

    for char in s:
        if char == '(':
            if depth > 0:        # not outermost → add it
                result.append(char)
            depth += 1           # always increase depth

        else:                    # char == ')'
            depth -= 1           # always decrease depth first
            if depth > 0:        # not outermost → add it
                result.append(char)

    return "".join(result)


# ═══════════════════════════════════════════════════════════════════
# TEST CASES
# ═══════════════════════════════════════════════════════════════════
if __name__ == "__main__":
    # Test 1 — Basic
    assert remove_outer_parentheses("(()())(())") == "()()()"

    # Test 2 — Nested
    assert remove_outer_parentheses("(()())(())(()(()))") == "()()()()(())"

    # Test 3 — Simple pairs (all outermost)
    assert remove_outer_parentheses("()()") == ""

    # Test 4 — Single primitive
    assert remove_outer_parentheses("()") == ""

    # Test 5 — Deeply nested
    assert remove_outer_parentheses("((()))") == "(())"

    print("All tests passed!")
