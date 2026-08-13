"""
╔════════════════════════════════════════════════════════════════════╗
║  SCORE OF PARENTHESES                                              ║
║  LeetCode #856  |  Difficulty: Medium  |  Topic: Strings/Stack     ║
║  Link: https://leetcode.com/problems/score-of-parentheses/         ║
╚════════════════════════════════════════════════════════════════════╝

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📘 SECTION 1 — PROBLEM UNDERSTANDING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Given a balanced parentheses string `s`, compute its score based
  on these rules:
    - "()" has score 1
    - AB has score A + B, where A and B are balanced parentheses
      strings placed one after another (concatenation)
    - (A) has score 2 * A, where A is a balanced parentheses string

  Input : s = balanced parentheses string
  Output: integer — the computed score

  Example 1 — basic:
    Input : s = "()"
    Output: 1
    Why?  : the base rule — a single pair scores 1

  Example 2 — slightly tricky (nesting doubles the score):
    Input : s = "(())"
    Output: 2
    Why?  : inner "()" = 1, wrapped in one more pair → 2 * 1 = 2

  Example 3 — concatenation (scores just add):
    Input : s = "()()"
    Output: 2
    Why?  : "()" + "()" = 1 + 1 = 2  (side by side, not nested)

  Example 4 — mix of both rules:
    Input : s = "(()(()))"
    Output: 6
    Why?  : inside the outer pair: "()" + "(())" = 1 + 2 = 3
            outer pair doubles it → 2 * 3 = 6

  Constraints:
    - 2 <= s.length <= 50
    - s consists of only '(' and ')'
    - s is a balanced parentheses string

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🧠 SECTION 2 — KANGLISH THINKING — ಹೇಗೆ ಯೋಚಿಸಬೇಕು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  Problem odi aada mele namma brain enu think maadabeeku:

  ಹಂತ 1 — Problem ಅರ್ಥ ಮಾಡಿಕೊಳ್ಳಿ
  ┌─────────────────────────────────────────────────────────┐
  │  Input ಏನು ಕೊಡ್ತಾರೆ?  →  balanced parentheses string   │
  │  Output ಏನು ಬೇಕು?     →  rules ಪ್ರಕಾರ score compute    │
  │                           ಮಾಡಿ integer return ಮಾಡಬೇಕು  │
  │  Constraints ಏನಿದೆ?   →  always balanced,               │
  │                           only '(' and ')' chars          │
  └─────────────────────────────────────────────────────────┘

  ಹಂತ 2 — ಇದು previous 2 problems (#1021, #1614) ಗೆ ಹೇಗೆ
           connect ಆಗುತ್ತೆ ಅಂತ ಗಮನಿಸಿ!
  →  ಎಲ್ಲಾ 3 problems ಕೂಡ depth/nesting track ಮಾಡೋದ್ರ ಮೇಲೆ ನಿಂತಿದೆ
  →  ಆದ್ರೆ ಇಲ್ಲಿ ಒಂದು twist ಇದೆ — "()" pair depth d ನಲ್ಲಿ ಸಿಕ್ಕಿದ್ರೆ
     ಅದರ contribution 2^d ಆಗಿರುತ್ತೆ (nesting = doubling!)

  ಹಂತ 3 — Simple way ಏನು?
  →  Recursive ಆಗಿ ಯೋಚಿಸಿ: string ಅನ್ನು depth-0 boundary ನಲ್ಲಿ
     ಚೂರುಗಳಾಗಿ split ಮಾಡಿ, ಪ್ರತಿ chunk ಗೆ rule apply ಮಾಡಿ
  →  "()" ಆದ್ರೆ 1, "(A)" ಆದ್ರೆ 2*score(A), "AB" ಆದ್ರೆ score(A)+score(B)

  ಹಂತ 4 — Better way ಹೇಗೆ ಯೋಚಿಸೋದು?
  →  "ಪ್ರತಿ '()' pair ಗೆ ಅದು ಎಷ್ಟು depth ನಲ್ಲಿ ಇದೆ ಅಂತ ಗೊತ್ತಾದ್ರೆ
      ಅದರ contribution 2^depth ಅಂತ direct ಆಗಿ ಗೊತ್ತಾಗುತ್ತಲ್ಲ?"
  →  ಯಾಕಂದ್ರೆ ಪ್ರತಿ ಸುತ್ತುವ '(' ಸುತ್ತೋಣಂ score ನ ಡಬಲ್ ಮಾಡುತ್ತೆ
  →  So: depth counter track ಮಾಡಿ, "()" ಸಿಕ್ಕಾಗ 2^depth score ಗೆ add ಮಾಡು!

  ಹಂತ 5 — Technique ಯಾಕೆ ಇಲ್ಲಿ ಕೆಲಸ ಮಾಡುತ್ತೆ?
  →  ಪ್ರತಿ nesting level ಒಂದು extra "×2" add ಮಾಡುತ್ತೆ (rule (A)=2A ಪ್ರಕಾರ)
  →  So base "()" leaf pair depth d ನಲ್ಲಿ ಇದ್ದಾಗ, ಅದರ 1 score
     d ಸಲ ಡಬಲ್ ಆಗಿ 2^d ಆಗಿರುತ್ತೆ — recursion ಬೇಡ, direct formula!

  💡 Interview ನಲ್ಲಿ ಹೇಗೆ ಮಾತಾಡಬೇಕು:
  →  "Every '()' leaf pair contributes 1, doubled once per
      enclosing pair — so its score is 2^depth"
  →  "Track depth like before. When I see '()' (an opening
      immediately followed by a closing), add 2^depth to score"
  →  "No stack, no recursion needed — a running depth counter
      plus a bit-shift is enough"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🏷️ SECTION 3 — TECHNIQUE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Primary   : Stack (bottom-up score folding)
  Secondary : Depth Counter + bit-shift (space-optimized)

  WHY Stack first?
  → Natural way to handle nested "2 * A" and concatenated "A + B"
    without writing actual recursion — push a 0 on '(', and on
    ')' fold the top value into its parent

  WHY Depth Counter beats it?
  → We don't actually need to store partial sums per level —
    only "()" leaf pairs ever add anything, and their contribution
    is fully determined by their depth: 2^depth. So a single
    depth counter (no stack) is enough.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 💡 SECTION 4 — INTUITION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  The key insight: only "()" leaf pairs ever create score — a
  lone '(' or ')' does nothing by itself. Every enclosing pair
  around a leaf just DOUBLES whatever is inside it. So a leaf
  pair sitting at nesting depth d contributes exactly 2^d.

  The journey from brute to optimal:
    Brute thought   →  Recursively split into balanced chunks at
                       depth-0 boundaries, apply rules per chunk
    Problem with it →  Finding split points repeatedly can cost
                       O(n) each time → O(n^2) worst case
    Better question →  "Do I need the actual recursive structure,
                       or just WHERE each leaf pair sits?"
    Insight         →  Use a stack to fold values bottom-up in
                       one pass → O(n). Then notice: only leaf
                       "()" pairs matter, and their score is a
                       pure function of depth → drop the stack
                       entirely, use 2^depth in a single counter
    Optimal         →  Single pass, depth counter, O(1) space

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🐢 SECTION 5 — APPROACH 1 — STACK (bottom-up folding)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    Keep a stack of partial scores, one per open nesting level,
    starting with a 0 for the outermost level. On '(' push a
    fresh 0 (new level starts with no score yet). On ')' pop the
    completed level's value `v`; if it was a leaf pair v == 0, so
    this pair scores 1; otherwise it was a wrapped group, so it
    scores 2*v. Add that result into the new top (its parent).

  Pseudocode:
    step 1: stack = [0]
    step 2: for each char in s:
    step 3:   if '(' → push 0 (start new level)
    step 4:   if ')' → v = pop()
                        stack[-1] += 1 if v == 0 else 2 * v
    step 5: return stack[0]

  Time  : O(n)  →  Why: single pass, each char processed once
  Space : O(n)  →  Why: stack can hold up to n/2 levels deep

  ಇದು ಯಾಕೆ optimal ಅಲ್ಲ?
    → Correct and already O(n) time! But we're storing an entire
      stack of partial sums when really only the CURRENT depth
      number matters for scoring a leaf pair — O(n) space wasted.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🚀 SECTION 6 — APPROACH 2 — OPTIMAL (Depth Counter + bit-shift)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    Track depth like in #1021 / #1614. Whenever we see a ')'
    that immediately follows a '(' (i.e. s[i-1] == '(' — a leaf
    "()" pair), its contribution is 2^depth, where depth is the
    nesting level AFTER stepping into that pair. Add that to the
    running score. Depth changes are the only bookkeeping needed.

  Key steps:
    1. depth = 0, score = 0
    2. For each index i, char in s:
       If '(' → depth += 1
       If ')' → depth -= 1
                 if s[i-1] == '(' → score += 2 ** depth
                                     (leaf pair found — depth here
                                      is the level just closed)
    3. return score

  ಕನ್ನಡದಲ್ಲಿ ಒಂದು ಸಲ ಹೇಳಿ:
    → "'(' ನೋಡಿದ್ರೆ: depth++ ಮಾಡು.
       ')' ನೋಡಿದ್ರೆ: depth-- ಮಾಡು, ಆಮೇಲೆ ಹಿಂದಿನ char '(' ಆಗಿದ್ರೆ
       (ಅಂದ್ರೆ ಇದು leaf '()' pair) → score += 2^depth ಮಾಡು.
       ಪ್ರತಿ leaf pair ತನ್ನ depth ಗೆ ಸರಿಯಾಗಿ 2^depth score ಕೊಡುತ್ತೆ!"

  Time  : O(n)  →  Why: single pass, each char processed once
  Space : O(1)  →  Why: only depth and score integers used
                        (ignoring the O(1)-sized int for 2**depth)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🔍 SECTION 7 — DRY RUN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Input: s = "(()(()))"     (indices: 0..7)

  APPROACH 2 — Depth Counter:
  i  char  depth_before  action                          depth_after  score
  0  '('   0             depth++                          1           0
  1  '('   1             depth++                          2           0
  2  ')'   2             depth-- ; s[1]=='(' → leaf!       1           0 + 2^1 = 2
                          score += 2^1 = 2
  3  '('   1             depth++                          2           2
  4  '('   2             depth++                          3           2
  5  ')'   3             depth-- ; s[4]=='(' → leaf!       2           2 + 2^2 = 6
                          score += 2^2 = 4
  6  ')'   2             depth-- ; s[5]==')' → not leaf    1           6
  7  ')'   1             depth-- ; s[6]==')' → not leaf    0           6

  Output: 6 ✓  (matches Example 4 above)

  APPROACH 1 — Stack (same input, for comparison):
  stack starts [0]
  '('→[0,0]  '('→[0,0,0]  ')'→pop 0(leaf,+1)→[0,1]
  '('→[0,1,0]  '('→[0,1,0,0]  ')'→pop 0(leaf,+1)→[0,1,1]
  ')'→pop 1(wrap,2*1=2)→[0,3]   ')'→pop 3(wrap,2*3=6)→[6]
  Output: 6 ✓  (same answer, more space used)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 ⚠️ SECTION 8 — EDGE CASES — ಇವನ್ನ ಮರೆಯಬೇಡ!
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  ✓ Single pair "()"?              →  1 — leaf pair at depth 1 → 2^0
                                       (note: score uses depth AFTER
                                       closing, i.e. 0, not 1 — see code)
  ✓ Simple nesting "(())"?         →  2 — leaf at depth 1 (post-close)
  ✓ Concatenation "()()"           →  2 — two leaf pairs, each 2^0 = 1
  ✓ Deep nesting "((()))"          →  4 — one leaf pair, 2^2 = 4
  ✓ Minimum length "()"?           →  handled same as any leaf pair

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📊 SECTION 9 — COMPLEXITY SUMMARY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                Time    Space
  Stack         O(n)    O(n)
  Optimal       O(n)    O(1)   ← use this ✅

  Time yaake O(n)?  → String ಒಮ್ಮೆ ಮಾತ್ರ traverse, each char O(1)
  Space yaake O(1)? → depth ಮತ್ತು score — ಎರಡು int variables ಮಾತ್ರ

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🎯 SECTION 10 — PATTERN LEARNED — ಇದರಿಂದ ಕಲಿತದ್ದು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Pattern Name: Depth Counter with Weighted Contribution (2^depth)

  Ee pattern yaavaaga use maadabeeku?
  → Nested structure alli, "each level DOUBLES/multiplies"
     type rule ಇದ್ದಾಗ → depth counter + weight formula use ಮಾಡು
  → Recursion ಬರೆಯೋ ಬದಲು, "leaf ಅಂದ್ರೆ ಏನಾಗುತ್ತೆ, depth ಗೆ
     ಸಂಬಂಧ ಹೇಗಿದೆ" ಅಂತ ಕೇಳಿಕೊಳ್ಳಿ — formula ಸಿಗಬಹುದು

  Idee pattern beere problemsalli kaanisatte:
  → Remove Outermost Parentheses #1021 (depth counter basics)
  → Maximum Nesting Depth of Parentheses #1614 (running max depth)
  → Decode String #394 (nested multiplier — similar doubling idea!)

  Next time intaha problem bandre naanu modalu idannu think maadtene:
  → "Nested structure + multiply-per-level rule → depth counter
     ಮೊದಲು try ಮಾಡು. Stack ಆಗಿದ್ರೂ ಸರಿ, ಆದ್ರೆ formula ಸಿಕ್ಕಿದ್ರೆ
     O(1) space ಗೆ ಇಳಿಸಬಹುದು!"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🗣️ SECTION 11 — INTERVIEWALLI HEGE EXPLAIN MAADABEEKU
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  1. Understand:
     "Compute a score for a balanced parentheses string: '()' is
      1, side-by-side scores add, and wrapping in one more pair
      doubles the inner score."

  2. Brute/Stack:
     "Use a stack of partial sums, one per nesting level. On ')',
      fold the completed level (1 if it was empty/leaf, else
      double it) into its parent. O(n) time, O(n) space."

  3. Optimize:
     "Only leaf '()' pairs actually create score, and each
      enclosing pair just doubles it — so a leaf at depth d is
      worth exactly 2^d. Track depth with a counter, detect leaf
      pairs (s[i-1]=='('), add 2^depth directly. O(1) space."

  4. Code:
     "depth counter. '(' → depth++. ')' → depth--, and if the
      previous char was '(', add 2**depth to score."

  5. Complexity:
     "Time O(n) — single pass. Space O(1) — two integers only."

  Mukhya: "multiply per nesting level" rule kanda kooda — recursion
          bittu depth-to-weight formula hudku, O(1) space sigatte!
"""


# ═══════════════════════════════════════════════════════════════════
# APPROACH 1 — Stack (bottom-up folding) — O(n) Time | O(n) Space
# ═══════════════════════════════════════════════════════════════════
def score_of_parentheses_stack(s):
    """
    Idu modala aaloochane — stack of partial sums, one per level
    ')' sikkaaga: leaf (v==0) aadre 1, wrap aadre 2*v parent ge add
    """
    stack = [0]

    for char in s:
        if char == '(':
            stack.append(0)
        else:
            v = stack.pop()
            stack[-1] += 1 if v == 0 else 2 * v

    return stack[0]


# ═══════════════════════════════════════════════════════════════════
# APPROACH 2 — OPTIMAL — Depth Counter + bit-shift — O(n) Time | O(1) Space
# ═══════════════════════════════════════════════════════════════════
def score_of_parentheses(s):
    """
    Idu final answer — leaf '()' pair depth d nalli sikkidre
    adara contribution nera 2^d, stack/recursion yaavudu bekilla
    """
    depth = 0
    score = 0

    for i, char in enumerate(s):
        if char == '(':
            depth += 1                        # entering one level deeper
        else:                                  # char == ')'
            depth -= 1                         # leaving this level
            if s[i - 1] == '(':                # leaf "()" pair found
                score += 1 << depth            # contributes 2^depth

    return score


# ═══════════════════════════════════════════════════════════════════
# TEST CASES
# ═══════════════════════════════════════════════════════════════════
if __name__ == "__main__":
    # Test 1 — Base case
    assert score_of_parentheses("()") == 1

    # Test 2 — Simple nesting
    assert score_of_parentheses("(())") == 2

    # Test 3 — Concatenation
    assert score_of_parentheses("()()") == 2

    # Test 4 — Mix of nesting and concatenation
    assert score_of_parentheses("(()(()))") == 6

    # Test 5 — Deep nesting
    assert score_of_parentheses("((()))") == 4

    # Cross-check: stack approach must agree on all of the above
    assert score_of_parentheses_stack("()") == 1
    assert score_of_parentheses_stack("(())") == 2
    assert score_of_parentheses_stack("()()") == 2
    assert score_of_parentheses_stack("(()(()))") == 6
    assert score_of_parentheses_stack("((()))") == 4

    print("All tests passed!")
