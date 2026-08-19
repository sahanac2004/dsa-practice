"""
╔════════════════════════════════════════════════════════════════════╗
║  STRING TO INTEGER (ATOI)                                          ║
║  LeetCode #8  |  Difficulty: Medium  |  Topic: Strings/Simulation  ║
║  Link: https://leetcode.com/problems/string-to-integer-atoi/       ║
╚════════════════════════════════════════════════════════════════════╝

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📘 SECTION 1 — PROBLEM UNDERSTANDING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Implement `myAtoi(s)` — convert a string to a 32-bit signed
  integer, following these rules IN ORDER:
    1. Skip any leading whitespace
    2. Read an optional '+' or '-' sign (at most one)
    3. Read digits until a non-digit character or end of string
    4. Convert those digits to an integer (ignore leading zeros)
    5. If no digits were read at all, the result is 0
    6. Clamp the final result to the 32-bit signed range:
       [-2^31, 2^31 - 1] = [-2147483648, 2147483647]

  Anything AFTER the digit sequence is simply ignored, even if
  it looks numeric later on.

  Input : s = an arbitrary string
  Output: integer — the parsed (and clamped) 32-bit signed value

  Example 1 — basic:
    Input : s = "42"
    Output: 42
    Why?  : plain digits, no sign, no surrounding noise

  Example 2 — slightly tricky (whitespace + sign + leading zero):
    Input : s = "   -042"
    Output: -42
    Why?  : leading spaces skipped, '-' sign captured, digits
            "042" → 42 (leading zero doesn't matter numerically)

  Example 3 — trailing non-digit noise:
    Input : s = "1337c0d3"
    Output: 1337
    Why?  : digit reading stops at the first non-digit 'c' —
            everything after is ignored

  Example 4 — overflow clamping:
    Input : s = "91283472332"
    Output: 2147483647
    Why?  : the parsed number exceeds INT_MAX, so it's clamped
            to the maximum 32-bit signed value

  Constraints:
    - 0 <= s.length <= 200
    - s consists of English letters, digits, ' ', '+', '-', '.'

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🧠 SECTION 2 — KANGLISH THINKING — ಹೇಗೆ ಯೋಚಿಸಬೇಕು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  Problem odi aada mele namma brain enu think maadabeeku:

  ಹಂತ 1 — Problem ಅರ್ಥ ಮಾಡಿಕೊಳ್ಳಿ
  ┌─────────────────────────────────────────────────────────┐
  │  Input ಏನು ಕೊಡ್ತಾರೆ?  →  ಯಾವುದೇ arbitrary string        │
  │  Output ಏನು ಬೇಕು?     →  ಅದರೊಳಗಿಂದ valid number extract  │
  │                           ಮಾಡಿ, 32-bit range ಗೆ clamp    │
  │  Constraints ಏನಿದೆ?   →  ಒಂದು specific ORDER ನಲ್ಲಿ ಪ್ರತಿ│
  │                           step follow ಮಾಡಬೇಕು            │
  └─────────────────────────────────────────────────────────┘

  ಹಂತ 2 — ಇದನ್ನ previous problem (#13 Roman to Integer) ಜೊತೆ
           compare ಮಾಡಿ ನೋಡಿ!
  →  ಅಲ್ಲಿ ಕೂಡ character-by-character SIMULATION ಮಾಡಿದ್ವಿ
  →  ಇಲ್ಲಿ ಕೂಡ ಅದೇ idea — ಆದ್ರೆ ಇಲ್ಲಿ rules ಜಾಸ್ತಿ (whitespace,
     sign, digits, overflow) — ಪ್ರತಿ rule ಅನ್ನ ORDER ಪ್ರಕಾರ
     apply ಮಾಡಬೇಕು

  ಹಂತ 3 — ಮೊದಲ simple idea ಏನು?
  →  Regular expression (regex) ಬಳಸಿ ಪ್ಯಾಟರ್ನ್ ಒಂದೇ ಸಲ match
     ಮಾಡಿ, ಸಿಕ್ಕ number ಅನ್ನ int() ಮಾಡಿ, ಕೊನೆಗೆ clamp ಮಾಡಿ

  ಹಂತ 4 — regex ಬೇಡ ಅಂದ್ರೆ, manual ಆಗಿ ಹೇಗೆ ಯೋಚಿಸೋದು?
  →  Problem statement ನೇ ಒಂದು STEP-BY-STEP algorithm ಆಗಿ
     ಕೊಟ್ಟಿದೆ — ಅದನ್ನೇ ನೇರವಾಗಿ code ಮಾಡಿದ್ರೆ ಆಯ್ತು!
  →  index pointer ಇಟ್ಟುಕೊಂಡು: (1) whitespace skip ಮಾಡು,
     (2) sign ಇದ್ರೆ capture ಮಾಡು, (3) digits ಸಿಗೋವರೆಗೆ read
     ಮಾಡಿ number build ಮಾಡು, (4) overflow ಆದ್ರೆ ಆಗಲೇ clamp
     ಮಾಡಿ return ಮಾಡು

  ಹಂತ 5 — Technique ಯಾಕೆ ಇಲ್ಲಿ ಕೆಲಸ ಮಾಡುತ್ತೆ?
  →  ಒಂದೇ pointer (index) ಇಂದ ಎಲ್ಲಾ steps ಸೀಕ್ವೆನ್ಶಿಯಲ್ ಆಗಿ
     ಮಾಡಬಹುದು — string ಅನ್ನ ಒಮ್ಮೆ ಮಾತ್ರ traverse ಮಾಡಿದ್ರೆ ಸಾಕು
  →  Overflow ಅನ್ನ EARLY ಆಗಿ (digit ಸೇರಿಸುವಾಗಲೇ) ಚೆಕ್ ಮಾಡಿದ್ರೆ,
     ಬಹಳ ದೊಡ್ಡ numbers build ಮಾಡೋ ಅಗತ್ಯ ಇಲ್ಲ

  💡 Interview ನಲ್ಲಿ ಹೇಗೆ ಮಾತಾಡಬೇಕು:
  →  "I'll follow the problem's own step order: skip whitespace,
      capture an optional sign, then read digits"
  →  "While building the number digit by digit, I'll check for
      32-bit overflow immediately and clamp early instead of
      building an arbitrarily large number first"
  →  "Anything after the digit sequence stops parsing — it's
      simply ignored"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🏷️ SECTION 3 — TECHNIQUE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Primary   : String Simulation — manual index-driven state machine
  Secondary : Regex pattern matching

  WHY Manual Simulation over Regex?
  → The problem statement IS already a step-by-step algorithm —
    coding it directly makes every rule (whitespace, sign,
    digits, overflow) explicit and easy to reason about, and
    lets us clamp overflow WHILE building the number instead of
    constructing a huge integer first and checking after.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 💡 SECTION 4 — INTUITION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  The key insight: this problem isn't really an "optimization"
  puzzle — it's a precise specification to SIMULATE correctly.
  The interesting design choice is WHERE to check for overflow:
  checking it AFTER building the full number risks working with
  arbitrarily huge integers first (fine in Python, but not in
  fixed-width languages); checking it INLINE, digit by digit,
  means we can clamp and return the moment the bound is crossed.

  The journey from brute to optimal:
    Brute thought   →  Use a regex to grab the whole valid
                       number pattern in one match, then int()
                       it and clamp at the end
    Problem with it →  Regex hides the step-by-step rules behind
                       a black box, and (in other languages) may
                       still require converting a large string to
                       an unbounded integer before clamping
    Better question →  "Can I check overflow WHILE reading each
                       digit, so I never need a number bigger
                       than necessary?"
    Insight         →  Compare against INT_MAX/INT_MIN as soon
                       as each digit is added — clamp immediately
    Optimal         →  One manual pass, inline overflow checks,
                       O(n) time

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🐢 SECTION 5 — APPROACH 1 — BRUTE FORCE (regex pattern match)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    Use one regex to capture "optional leading whitespace,
    optional sign, then one or more digits" from the START of
    the string. If it doesn't match, there's no valid number →
    return 0. Otherwise convert the captured group to an int and
    clamp it to the 32-bit signed range.

  Pseudocode:
    step 1: match = re.match(r'^\s*([+-]?\d+)', s)
    step 2: if not match: return 0
    step 3: num = int(match.group(1))
    step 4: clamp num into [INT_MIN, INT_MAX]
    step 5: return num

  Time  : O(n)  →  Why: regex matching this pattern is linear in
                        the matched prefix length
  Space : O(n)  →  Why: the matched substring/group is copied

  ಇದು ಯಾಕೆ ಸಾಕಾಗಲ್ಲ?
    → Works and is concise! But it hides the parsing RULES
      behind the regex engine, and builds the full integer
      before clamping — less transparent for demonstrating the
      overflow-handling logic interviewers usually want to see.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🚀 SECTION 6 — APPROACH 2 — OPTIMAL (Manual Simulation)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    Walk the string with one index pointer, applying the rules
    in order: skip spaces, capture an optional sign, then
    accumulate digits one at a time (num = num*10 + digit).
    After adding EACH digit, check if the running value has
    already exceeded the 32-bit bound for its sign — if so,
    clamp and return immediately.

  Key steps:
    1. i = 0; skip while s[i] == ' '
    2. sign = 1; if s[i] in '+-': sign = -1 if '-' else 1; i += 1
    3. num = 0
    4. while s[i] is a digit:
    5.   num = num * 10 + int(s[i]); i += 1
    6.   if sign == 1 and num > INT_MAX: return INT_MAX
    7.   if sign == -1 and -num < INT_MIN: return INT_MIN
    8. return sign * num

  ಕನ್ನಡದಲ್ಲಿ ಒಂದು ಸಲ ಹೇಳಿ:
    → "index pointer ಇಟ್ಟುಕೊಂಡು, ಮೊದಲು spaces skip ಮಾಡು. ಆಮೇಲೆ
       sign ಇದ್ರೆ capture ಮಾಡು. ಆಮೇಲೆ digits ಸಿಗೋವರೆಗೆ num ಅನ್ನ
       num*10+digit ಆಗಿ build ಮಾಡ್ತಾ ಹೋಗು. ಪ್ರತಿ digit ಸೇರಿಸಿದ
       ಮೇಲೂ, 32-bit limit ದಾಟಿದ್ಯಾ ಚೆಕ್ ಮಾಡು — ದಾಟಿದ್ರೆ ತಕ್ಷಣ
       clamp ಮಾಡಿ return ಮಾಡು!"

  Time  : O(n)  →  Why: single left-to-right pass, O(1) work
                        per character
  Space : O(1)  →  Why: just a few counters/pointers, no extra
                        data structures

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🔍 SECTION 7 — DRY RUN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Input: s = "   -042"

  Step 1 — skip whitespace: i moves from 0 to 3 (three spaces)
  Step 2 — sign: s[3] == '-' → sign = -1, i = 4
  Step 3 — digits: s[4..6] = "042"
    i=4: '0' → num = 0*10+0 = 0
    i=5: '4' → num = 0*10+4 = 4
    i=6: '2' → num = 4*10+2 = 42
    (no overflow at any step)
  Step 4: return sign * num = -1 * 42 = -42

  Output: -42 ✓

  ಇನ್ನೊಂದು example — overflow clamp:
  Input: s = "91283472332"

  Step 1: no whitespace, i = 0
  Step 2: no sign, sign = 1
  Step 3: digits accumulate: 9, 91, 912, ..., eventually num
    crosses INT_MAX (2147483647) partway through — the moment
    num > 2147483647, we return INT_MAX immediately without
    reading the remaining digits

  Output: 2147483647 ✓

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 ⚠️ SECTION 8 — EDGE CASES — ಇವನ್ನ ಮರೆಯಬೇಡ!
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  ✓ Empty string ""?               →  0 — nothing to parse
  ✓ Only whitespace "   "?         →  0 — no digits found
  ✓ No digits at all "words 987"?  →  0 — first non-space char
                                       isn't a digit or sign
  ✓ Digit stops at non-digit
    "0-1" / "1337c0d3"?            →  parsing stops at the first
                                       non-digit character
  ✓ Negative overflow
    "-91283472332"?                →  clamped to INT_MIN
                                       (-2147483648)
  ✓ Sign with no digits after "+"? →  0 — sign alone isn't a
                                       valid number

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📊 SECTION 9 — COMPLEXITY SUMMARY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                        Time    Space
  Brute (regex)         O(n)    O(n)
  Optimal (simulation)  O(n)    O(1)   ← use this ✅

  Time yaake O(n)?  → Single left-to-right pass over the string
  Space yaake O(1)? → Just an index pointer, sign, and running
                       number — no extra copies

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🎯 SECTION 10 — PATTERN LEARNED — ಇದರಿಂದ ಕಲಿತದ್ದು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Pattern Name: Index-Driven State Machine Simulation

  Ee pattern yaavaaga use maadabeeku?
  → Problem statement itself ondu STEP-BY-STEP spec kottidre
     (parsing, validation rules) → seekvenshiyal ayi ondu index
     pointer inda directly simulate madu
  → Overflow/boundary checks bekagidre, EARLY (inline) check
     madu — full value build maadi aamele check madoda bittu

  Idee pattern beere problemsalli kaanisatte:
  → Valid Number #65 (similar character-by-character state
     machine, more validation states)
  → Roman to Integer #13 (previous problem — same simulation
     style, simpler rules)
  → Reverse Integer #7 (same overflow-clamp-while-building idea)

  Next time intaha problem bandre naanu modalu idannu think maadtene:
  → "Parsing rules step-by-step kottidre → index pointer inda
     directly simulate madu. Overflow/limit checks bekagidre,
     build madtha iddaga inline check madu — clamp immediately!"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🗣️ SECTION 11 — INTERVIEWALLI HEGE EXPLAIN MAADABEEKU
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  1. Understand:
     "Parse a string into a 32-bit signed integer following
      strict rules: skip spaces, read an optional sign, read
      digits, clamp to the valid range."

  2. Brute force:
     "A regex can capture the whole valid prefix in one match,
      then int() and clamp it. Concise, but hides the rules and
      builds the full number before checking bounds."

  3. Optimize:
     "Simulate the rules directly with an index pointer: skip
      whitespace, capture sign, accumulate digits one at a time.
      Check for overflow immediately after adding each digit and
      clamp right away — no need to ever hold a huge number."

  4. Code:
     "One pass: whitespace-skip loop, sign check, digit
      accumulation loop with an inline overflow check against
      INT_MAX/INT_MIN inside the loop body."

  5. Complexity:
     "Time O(n) — single pass. Space O(1) — just a few scalar
      variables."

  Mukhya: specification-heavy problems alli, problem statement
          ne ondu algorithm — nera adhare follow madi simulate
          madidre saaku, overflow ge inline check maadi clamp
          madidre robust aaguttade!
"""

INT_MAX = 2 ** 31 - 1       # 2147483647
INT_MIN = -2 ** 31          # -2147483648


# ═══════════════════════════════════════════════════════════════════
# BRUTE FORCE — O(n) Time | O(n) Space (regex pattern match)
# ═══════════════════════════════════════════════════════════════════
def my_atoi_brute(s):
    """
    Idu modala aaloochane — regex ondu sala match madi valid
    number prefix extract madi, int() madi clamp madu
    """
    import re

    match = re.match(r'^\s*([+-]?\d+)', s)
    if not match:
        return 0

    num = int(match.group(1))

    if num > INT_MAX:
        return INT_MAX
    if num < INT_MIN:
        return INT_MIN
    return num


# ═══════════════════════════════════════════════════════════════════
# OPTIMAL — O(n) Time | O(1) Space (manual index-driven simulation)
# ═══════════════════════════════════════════════════════════════════
def my_atoi(s):
    """
    Idu final answer — index pointer inda whitespace skip, sign
    capture, digit accumulate madi, prati digit mele inline
    overflow check madi clamp madu
    """
    i = 0
    n = len(s)

    # Step 1: skip leading whitespace
    while i < n and s[i] == ' ':
        i += 1

    if i == n:
        return 0

    # Step 2: optional sign
    sign = 1
    if s[i] in ('+', '-'):
        if s[i] == '-':
            sign = -1
        i += 1

    # Step 3: accumulate digits, with inline overflow clamping
    num = 0
    while i < n and s[i].isdigit():
        num = num * 10 + int(s[i])
        i += 1

        if sign == 1 and num > INT_MAX:
            return INT_MAX
        if sign == -1 and -num < INT_MIN:
            return INT_MIN

    return sign * num


# ═══════════════════════════════════════════════════════════════════
# TEST CASES
# ═══════════════════════════════════════════════════════════════════
if __name__ == "__main__":
    # Test 1 — Basic
    assert my_atoi("42") == 42

    # Test 2 — Whitespace, sign, leading zero
    assert my_atoi("   -042") == -42

    # Test 3 — Trailing non-digit noise
    assert my_atoi("1337c0d3") == 1337

    # Test 4 — Positive overflow clamp
    assert my_atoi("91283472332") == 2147483647

    # Test 5 — No valid number at all
    assert my_atoi("words and 987") == 0

    # Test 6 — Digit stops at first non-digit right away
    assert my_atoi("0-1") == 0

    # Test 7 — Negative overflow clamp
    assert my_atoi("-91283472332") == -2147483648

    # Test 8 — Empty string
    assert my_atoi("") == 0

    # Cross-check: brute force must agree on all of the above
    assert my_atoi_brute("42") == 42
    assert my_atoi_brute("   -042") == -42
    assert my_atoi_brute("1337c0d3") == 1337
    assert my_atoi_brute("91283472332") == 2147483647
    assert my_atoi_brute("words and 987") == 0
    assert my_atoi_brute("0-1") == 0
    assert my_atoi_brute("-91283472332") == -2147483648
    assert my_atoi_brute("") == 0

    print("All tests passed!")
