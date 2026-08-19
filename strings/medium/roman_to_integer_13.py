"""
╔════════════════════════════════════════════════════════════════════╗
║  ROMAN TO INTEGER                                                  ║
║  LeetCode #13  |  Difficulty: Easy/Medium  |  Topic: Strings/HashMap║
║  Link: https://leetcode.com/problems/roman-to-integer/             ║
╚════════════════════════════════════════════════════════════════════╝

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📘 SECTION 1 — PROBLEM UNDERSTANDING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Roman numerals use seven symbols:
    I=1, V=5, X=10, L=50, C=100, D=500, M=1000

  Normally symbols are written largest-to-smallest left to right
  and their values simply ADD UP (e.g. "III" = 1+1+1 = 3). But
  six special SUBTRACTIVE pairs exist, where a smaller symbol
  placed BEFORE a larger one means "subtract the smaller":
    IV=4, IX=9, XL=40, XC=90, CD=400, CM=900

  Given a valid roman numeral string `s`, convert it to an
  integer.

  Input : s = a valid roman numeral string
  Output: integer value it represents

  Example 1 — basic (pure addition):
    Input : s = "III"
    Output: 3
    Why?  : I + I + I = 1 + 1 + 1 = 3, no subtractive pairs

  Example 2 — slightly tricky (mix of add & subtract):
    Input : s = "LVIII"
    Output: 58
    Why?  : L=50, V=5, III=3 → 50 + 5 + 1 + 1 + 1 = 58

  Example 3 — several subtractive pairs together:
    Input : s = "MCMXCIV"
    Output: 1994
    Why?  : M=1000, CM=900 (subtractive!), XC=90 (subtractive!),
            IV=4 (subtractive!) → 1000+900+90+4 = 1994

  Constraints:
    - 1 <= s.length <= 15
    - s consists only of 'I','V','X','L','C','D','M'
    - It is guaranteed that s is a valid roman numeral in the
      range [1, 3999]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🧠 SECTION 2 — KANGLISH THINKING — ಹೇಗೆ ಯೋಚಿಸಬೇಕು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  Problem odi aada mele namma brain enu think maadabeeku:

  ಹಂತ 1 — Problem ಅರ್ಥ ಮಾಡಿಕೊಳ್ಳಿ
  ┌─────────────────────────────────────────────────────────┐
  │  Input ಏನು ಕೊಡ್ತಾರೆ?  →  Roman numeral string           │
  │  Output ಏನು ಬೇಕು?     →  ಅದರ integer value               │
  │  Constraints ಏನಿದೆ?   →  ಕೆಲವು ಕಡೆ SUBTRACT ಮಾಡಬೇಕು     │
  │                           (small symbol, large ಗಿಂತ ಮುಂಚೆ)│
  └─────────────────────────────────────────────────────────┘

  ಹಂತ 2 — ಮೊದಲ simple idea ಏನು?
  →  6 special pairs (IV, IX, XL, XC, CD, CM) ಗೆ ಒಂದು ಪ್ರತ್ಯೇಕ
     lookup table ಇಟ್ಟುಕೊಳ್ಳಿ
  →  string ಅನ್ನ scan ಮಾಡ್ತಾ, ಮೊದಲು 2-character pair special
     ಇದ್ಯಾ ಚೆಕ್ ಮಾಡಿ, ಇದ್ರೆ ಆ value add ಮಾಡಿ 2 index ಮುಂದೆ ಹೋಗಿ
  →  ಇಲ್ಲಾಂದ್ರೆ single character value add ಮಾಡಿ 1 index ಮುಂದೆ ಹೋಗಿ

  ಹಂತ 3 — ಎರಡು separate lookup tables ಬೇಕಾ, ಅಥವಾ general
           RULE ಸಿಗುತ್ತಾ?
  →  Subtractive pair ಅಂದ್ರೆ ಏನು ಗಮನಿಸಿ: "small symbol,
      ದೊಡ್ಡ symbol ಗಿಂತ ಮುಂಚೆ ಬಂದ್ರೆ ಮಾತ್ರ subtract!"
  →  ಇದೇ general rule ಆಗುತ್ತೆ: current symbol value < NEXT
     symbol value ಆಗಿದ್ರೆ → SUBTRACT current value
     ಇಲ್ಲಾಂದ್ರೆ → ADD current value
  →  ಈ ಒಂದೇ rule 6 special cases ಕೂಡ automatically ಸರಿಯಾಗಿ
     handle ಮಾಡುತ್ತೆ — ಪ್ರತ್ಯೇಕ table ಬೇಕಿಲ್ಲ!

  ಹಂತ 4 — Technique ಯಾಕೆ ಇಲ್ಲಿ ಕೆಲಸ ಮಾಡುತ್ತೆ?
  →  ಒಂದೇ hashmap (symbol → value) ಸಾಕು
  →  ಪ್ರತಿ index ನಲ್ಲಿ, ಮುಂದಿನ symbol ಜೊತೆ compare ಮಾಡಿದ್ರೆ
     ಸಾಕು — ಇದೇ compare, subtractive pair ಇದ್ಯಾ ಇಲ್ವಾ ಅಂತ
     ತಾನಾಗೇ ಗೊತ್ತಾಗುತ್ತೆ

  💡 Interview ನಲ್ಲಿ ಹೇಗೆ ಮಾತಾಡಬೇಕು:
  →  "Map each symbol to its value with one hashmap"
  →  "Walk left to right — if the current symbol's value is
      LESS than the next symbol's value, it's part of a
      subtractive pair, so subtract it"
  →  "Otherwise, just add it — this single rule covers every
      subtractive case without a separate lookup table"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🏷️ SECTION 3 — TECHNIQUE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Primary   : HashMap — single value lookup + "compare with next" rule
  Secondary : HashMap with a separate subtractive-pair table

  WHY "compare with next" over a separate pair table?
  → It's the same underlying rule that DEFINES a subtractive
    pair — smaller value immediately before a larger one — so
    checking it directly avoids hardcoding all six special
    two-character combinations by hand.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 💡 SECTION 4 — INTUITION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  The key insight: a symbol should be SUBTRACTED exactly when a
  bigger symbol comes right after it — that's the literal
  definition of a subtractive pair. Rather than memorizing all
  six special two-letter combinations (IV, IX, XL, XC, CD, CM),
  we can just compare each symbol's value to its neighbor's
  value and let the "smaller-before-bigger" rule decide.

  The journey from brute to optimal:
    Brute thought   →  Keep TWO lookup tables: one for single
                       symbols, one for the six subtractive
                       pairs. Scan two characters at a time,
                       checking the pair table first.
    Problem with it →  Duplicates information — the pair table
                       is really just "smaller value before
                       bigger value," which is already derivable
                       from the single-symbol table
    Better question →  "Can I detect a subtractive pair just by
                       comparing adjacent values, without a
                       separate table?"
    Insight         →  current < next → subtract current;
                       otherwise → add current
    Optimal         →  One hashmap, one linear pass, O(n) time

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🐢 SECTION 5 — APPROACH 1 — BRUTE FORCE (separate pair table)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    Keep a table of single symbol values AND a table of the six
    known subtractive two-character pairs. Walk the string; at
    each position, first check if the NEXT two characters form a
    known pair — if so, add its value and skip two characters;
    otherwise add the single symbol's value and skip one.

  Pseudocode:
    step 1: values = {I:1, V:5, X:10, L:50, C:100, D:500, M:1000}
    step 2: pairs = {IV:4, IX:9, XL:40, XC:90, CD:400, CM:900}
    step 3: i = 0, total = 0
    step 4: while i < len(s):
    step 5:   if s[i:i+2] in pairs: total += pairs[s[i:i+2]]; i += 2
    step 6:   else: total += values[s[i]]; i += 1
    step 7: return total

  Time  : O(n)  →  Why: single pass, each step advances i by 1 or 2
  Space : O(1)  →  Why: two small fixed-size lookup tables

  ಇದು ಯಾಕೆ ಸಾಕಾಗಲ್ಲ?
    → Works fine and is O(n)! But maintaining a whole SEPARATE
      table for subtractive pairs duplicates logic that's
      already implied by comparing adjacent symbol values —
      more to memorize/maintain than necessary.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🚀 SECTION 6 — APPROACH 2 — OPTIMAL (Compare-with-next rule)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    Use just ONE hashmap of symbol values. Walk left to right;
    at each index, compare the current symbol's value to the
    NEXT symbol's value. If current < next, it's part of a
    subtractive pair — subtract it. Otherwise, add it normally.

  Key steps:
    1. values = {I:1, V:5, X:10, L:50, C:100, D:500, M:1000}
    2. total = 0
    3. for i in range(len(s)):
    4.   curr = values[s[i]]
    5.   if i+1 < len(s) and curr < values[s[i+1]]:
    6.     total -= curr
    7.   else:
    8.     total += curr
    9. return total

  ಕನ್ನಡದಲ್ಲಿ ಒಂದು ಸಲ ಹೇಳಿ:
    → "ಒಂದೇ hashmap ಇಟ್ಕೊಳ್ಳಿ. ಪ್ರತಿ symbol ಗೆ, ಅದರ ಮುಂದಿನ
       symbol value ಜೊತೆ compare ಮಾಡು. ಈಗಿನದು ಚಿಕ್ಕದಿದ್ರೆ
       (ಮುಂದಿನದಕ್ಕಿಂತ) → subtract ಮಾಡು, ಇಲ್ಲಾಂದ್ರೆ add ಮಾಡು.
       ಇದೇ single rule ಎಲ್ಲಾ subtractive cases ಕೂಡ ಸರಿಯಾಗಿ
       handle ಮಾಡುತ್ತೆ!"

  Time  : O(n)  →  Why: single linear pass, O(1) hashmap lookup
                        per character
  Space : O(1)  →  Why: one small fixed-size (7-entry) hashmap

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🔍 SECTION 7 — DRY RUN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Input: s = "MCMXCIV"

  i  s[i]  curr  next   curr<next?  action        total
  0  'M'   1000  'C'=100  No         total+=1000   1000
  1  'C'   100   'M'=1000 Yes        total-=100    900
  2  'M'   1000  'X'=10   No         total+=1000   1900
  3  'X'   10    'C'=100  Yes        total-=10     1890
  4  'C'   100   'I'=1    No         total+=100    1990
  5  'I'   1     'V'=5    Yes        total-=1      1989
  6  'V'   5     (none)   No         total+=5      1994

  Output: 1994 ✓

  ಇನ್ನೊಂದು example — pure addition:
  Input: s = "III"

  i  s[i]  curr  next     curr<next?  action       total
  0  'I'   1     'I'=1    No          total+=1     1
  1  'I'   1     'I'=1    No          total+=1     2
  2  'I'   1     (none)   No          total+=1     3

  Output: 3 ✓

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 ⚠️ SECTION 8 — EDGE CASES — ಇವನ್ನ ಮರೆಯಬೇಡ!
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  ✓ Single symbol "V"?             →  5 — trivially itself
  ✓ Pure addition "LVIII"?         →  58 — no subtractive pairs
  ✓ All subtractive pairs "CMXCIV"? →  1994 (C M X C I V → wait,
                                       this is "MCMXCIV" reordered
                                       example above) — multiple
                                       subtractive pairs chained
  ✓ Largest value "MMMCMXCIX"?     →  3999 — max representable
                                       value in the constraint range
  ✓ Smallest value "I"?            →  1

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📊 SECTION 9 — COMPLEXITY SUMMARY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                          Time    Space
  Brute (pair table)      O(n)    O(1)
  Optimal (compare-next)  O(n)    O(1)   ← use this ✅ (simpler, 1 table)

  Time yaake O(n)?  → Single left-to-right pass, O(1) work per
                       character (hashmap lookup + comparison)
  Space yaake O(1)? → Fixed-size 7-entry symbol table only

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🎯 SECTION 10 — PATTERN LEARNED — ಇದರಿಂದ ಕಲಿತದ್ದು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Pattern Name: Adjacent-Comparison Simulation

  Ee pattern yaavaaga use maadabeeku?
  → "Special-case pairs" ideyantha problems alli, aa special
     case ondu SIMPLE comparison rule inda derive aagutte
     antadre → separate lookup table bittu, adjacent elements
     compare madu
  → Symbol/value simulation problems — Roman numerals, custom
     number systems

  Idee pattern beere problemsalli kaanisatte:
  → Integer to Roman #12 (reverse direction — same value table,
     greedy subtraction instead)
  → String to Integer (atoi) #8 (next problem — another
     character-by-character simulation, different rules)

  Next time intaha problem bandre naanu modalu idannu think maadtene:
  → "Special-case pairs kanda tanaka, aa pattern ondu simple
     RULE (comparison) inda cover aaguttaa antha yochane madu —
     hardcoded table bittu general rule hudku!"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🗣️ SECTION 11 — INTERVIEWALLI HEGE EXPLAIN MAADABEEKU
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  1. Understand:
     "Convert a roman numeral string to its integer value,
      handling six special subtractive two-symbol pairs."

  2. Brute force:
     "One table for single symbols, one for the six subtractive
      pairs. Check two characters at a time. O(n), but two
      tables to maintain."

  3. Optimize:
     "A subtractive pair is just 'smaller value immediately
      before a bigger one.' So with ONE table, I compare each
      symbol's value to the next symbol's value — subtract if
      smaller, add otherwise."

  4. Code:
     "One hashmap. Loop with index, compare values[s[i]] against
      values[s[i+1]] when it exists; subtract or add accordingly."

  5. Complexity:
     "Time O(n) — one linear pass. Space O(1) — fixed 7-entry
      table."

  Mukhya: hardcoded special-case pairs kanda tanaka, aa
          "specialness" simple comparison rule inda derive
          aaguttadeyantha yochane madu!
"""


# ═══════════════════════════════════════════════════════════════════
# BRUTE FORCE — O(n) Time | O(1) Space (separate subtractive-pair table)
# ═══════════════════════════════════════════════════════════════════
def roman_to_int_brute(s):
    """
    Idu modala aaloochane — single symbols ge ondu table,
    subtractive pairs ge inolo ondu table, 2-char check madtha hogu
    """
    values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    pairs = {'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}

    total = 0
    i = 0
    while i < len(s):
        if s[i:i + 2] in pairs:
            total += pairs[s[i:i + 2]]
            i += 2
        else:
            total += values[s[i]]
            i += 1

    return total


# ═══════════════════════════════════════════════════════════════════
# OPTIMAL — O(n) Time | O(1) Space (compare-with-next rule)
# ═══════════════════════════════════════════════════════════════════
def roman_to_int(s):
    """
    Idu final answer — ondu hashmap saaku, prati symbol na next
    symbol jothe compare madi subtract/add decide madu
    """
    values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    total = 0
    n = len(s)

    for i in range(n):
        curr = values[s[i]]
        if i + 1 < n and curr < values[s[i + 1]]:
            total -= curr          # part of a subtractive pair
        else:
            total += curr          # normal addition

    return total


# ═══════════════════════════════════════════════════════════════════
# TEST CASES
# ═══════════════════════════════════════════════════════════════════
if __name__ == "__main__":
    # Test 1 — Pure addition
    assert roman_to_int("III") == 3

    # Test 2 — Mix of add and subtract
    assert roman_to_int("LVIII") == 58

    # Test 3 — Multiple chained subtractive pairs
    assert roman_to_int("MCMXCIV") == 1994

    # Test 4 — Single symbol
    assert roman_to_int("V") == 5

    # Test 5 — Maximum value in valid range
    assert roman_to_int("MMMCMXCIX") == 3999

    # Cross-check: brute force must agree on all of the above
    assert roman_to_int_brute("III") == 3
    assert roman_to_int_brute("LVIII") == 58
    assert roman_to_int_brute("MCMXCIV") == 1994
    assert roman_to_int_brute("V") == 5
    assert roman_to_int_brute("MMMCMXCIX") == 3999

    print("All tests passed!")
