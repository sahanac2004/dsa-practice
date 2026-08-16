"""
╔════════════════════════════════════════════════════════════════════╗
║  ISOMORPHIC STRINGS                                                ║
║  LeetCode #205  |  Difficulty: Easy  |  Topic: Strings/HashMap     ║
║  Link: https://leetcode.com/problems/isomorphic-strings/           ║
╚════════════════════════════════════════════════════════════════════╝

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📘 SECTION 1 — PROBLEM UNDERSTANDING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Given two strings `s` and `t`, determine if they are isomorphic.

  Two strings are isomorphic if the characters in `s` can be
  replaced to get `t`, such that:
    - All occurrences of a character in `s` must map to the SAME
      character in `t` (consistent mapping)
    - No two different characters in `s` may map to the SAME
      character in `t` (mapping must be one-to-one, a bijection)
    - A character may map to itself
    - Order/position of characters must be preserved (no reordering)

  Input : s, t = two strings of equal length
  Output: boolean — True if isomorphic, False otherwise

  Example 1 — basic:
    Input : s = "egg", t = "add"
    Output: True
    Why?  : e→a, g→d — consistent both directions, no clashes

  Example 2 — slightly tricky (one char, two mappings):
    Input : s = "foo", t = "bar"
    Output: False
    Why?  : f→b, first o→a, but second o would need →r —
            'o' can't map to two different characters

  Example 3 — the "sneaky" false case (many-to-one):
    Input : s = "ab", t = "aa"
    Output: False
    Why?  : a→a and b→a — TWO different source characters both
            map to the same target 'a', which breaks the
            one-to-one requirement (even though each individual
            mapping looks "consistent")

  Constraints:
    - 1 <= s.length <= 5 * 10^4
    - t.length == s.length
    - s and t consist of any valid ASCII character

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🧠 SECTION 2 — KANGLISH THINKING — ಹೇಗೆ ಯೋಚಿಸಬೇಕು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  Problem odi aada mele namma brain enu think maadabeeku:

  ಹಂತ 1 — Problem ಅರ್ಥ ಮಾಡಿಕೊಳ್ಳಿ
  ┌─────────────────────────────────────────────────────────┐
  │  Input ಏನು ಕೊಡ್ತಾರೆ?  →  ಎರಡು same-length strings s, t  │
  │  Output ಏನು ಬೇಕು?     →  s ರ characters ಅನ್ನ t ಆಗಿ       │
  │                           consistent ಆಗಿ map ಮಾಡಬಹುದಾ?  │
  │  Constraints ಏನಿದೆ?   →  ಒಂದು character ಎರಡು ಕಡೆ map    │
  │                           ಆಗಬಾರದು (bijection ಇರಬೇಕು)     │
  └─────────────────────────────────────────────────────────┘

  ಹಂತ 2 — ಮೊದಲ simple idea ಏನು?
  →  s ಇಂದ t ಗೆ ಒಂದು hashmap ಇಟ್ಟುಕೊಳ್ಳಿ (char → char mapping)
  →  ಪ್ರತಿ position ನಲ್ಲಿ mapping consistent ಆಗಿದ್ಯಾ ಚೆಕ್ ಮಾಡಿ

  ಹಂತ 3 — ಆದ್ರೆ ಒಂದೇ hashmap ಸಾಕಾ? Example "ab"→"aa" ಟ್ರೈ ಮಾಡಿ!
  →  a→a (fine), b→a (map ನಲ್ಲಿ 'b' ಇರಲಿಲ್ಲ, so add ಮಾಡ್ತೀವಿ)
  →  ಆದ್ರೆ ಇಲ್ಲಿ 'a' ಮತ್ತು 'b' ಎರಡೂ 'a' ಗೆ map ಆಗ್ತಿದೆ — ಇದು
     ILLEGAL! ಯಾಕಂದ್ರೆ ಎರಡು ಬೇರೆ source characters ಒಂದೇ
     target character ಗೆ map ಆಗಬಾರದು
  →  ಒಂದೇ hashmap (s→t) ಇದನ್ನ catch ಮಾಡಲ್ಲ! ಇನ್ನೊಂದು hashmap
     (t→s) ಕೂಡ ಬೇಕು — REVERSE mapping ಕೂಡ consistent ಆಗಿರಬೇಕು

  ಹಂತ 4 — Technique ಯಾಕೆ ಇಲ್ಲಿ ಕೆಲಸ ಮಾಡುತ್ತೆ?
  →  ಎರಡು hashmaps (forward s→t ಮತ್ತು backward t→s) ಒಟ್ಟಿಗೆ
     track ಮಾಡಿದ್ರೆ, TRUE bijection (one-to-one AND onto)
     guarantee ಆಗುತ್ತೆ
  →  Single pass ಸಾಕು — ಪ್ರತಿ index ನಲ್ಲಿ ಎರಡೂ mapping check/set
     ಮಾಡ್ತಾ ಹೋಗಬಹುದು

  💡 Interview ನಲ್ಲಿ ಹೇಗೆ ಮಾತಾಡಬೇಕು:
  →  "I need a mapping from s→t AND a mapping from t→s — a
      single direction isn't enough to guarantee a true
      one-to-one correspondence"
  →  "At each index, if a mapping already exists, verify it's
      consistent; if not, create it in BOTH directions"
  →  "Any inconsistency in either direction → not isomorphic"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🏷️ SECTION 3 — TECHNIQUE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Primary   : HashMap — bidirectional character mapping
  Secondary : Pattern encoding (first-occurrence index)

  WHY Bidirectional HashMap?
  → A one-way map (s→t) only catches "same source char, two
    different targets." It misses "two different source chars,
    same target char." Tracking BOTH directions in one pass
    catches every violation of the one-to-one requirement.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 💡 SECTION 4 — INTUITION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  The key insight: "isomorphic" really means s and t have the
  EXACT SAME STRUCTURE of repeated characters — if you replaced
  every character with "the index where its value first
  appeared," s and t would produce identical patterns. A
  bidirectional hashmap enforces this structural equality
  directly, without needing to build and compare separate
  pattern arrays.

  The journey from brute to optimal:
    Brute thought   →  Encode both strings into a "pattern":
                       for each position, note the index of that
                       character's FIRST occurrence. Compare the
                       two pattern lists.
    Problem with it →  Finding "first occurrence" naively with
                       something like list.index() re-scans from
                       the start each time → O(n^2)
    Better question →  "Can I check consistency in a single
                       linear pass instead of rebuilding patterns?"
    Insight         →  Track s→t and t→s mappings simultaneously;
                       any mismatch in either direction fails fast
    Optimal         →  Single pass, two hashmaps, O(n) time

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🐢 SECTION 5 — APPROACH 1 — BRUTE FORCE (pattern encoding)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    Convert each string into a list where every character is
    replaced by the index of its FIRST occurrence in that
    string. Two strings are isomorphic exactly when their
    "pattern" lists match.

  Pseudocode:
    step 1: def pattern(str):
    step 2:   return [str.index(c) for c in str]
    step 3: return pattern(s) == pattern(t)

  Time  : O(n^2)  →  Why: str.index(c) re-scans from the start
                          for every character → O(n) per lookup,
                          O(n) lookups → O(n^2) total
  Space : O(n)     →  Why: two pattern lists of length n

  ಇದು ಯಾಕೆ ಸಾಕಾಗಲ್ಲ?
    → Correct, but str.index() repeatedly rescans the string —
      wasteful. We can get the SAME structural check in one
      linear pass using hashmaps instead of rebuilding patterns.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🚀 SECTION 6 — APPROACH 2 — OPTIMAL (Bidirectional HashMap)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    Walk both strings together, index by index. Maintain two
    dictionaries: `s_to_t` and `t_to_s`. At each position, if a
    mapping already exists for either character, it MUST match
    what we see now; otherwise, record a fresh mapping in BOTH
    directions.

  Key steps:
    1. s_to_t = {}, t_to_s = {}
    2. for cs, ct in zip(s, t):
    3.   if cs in s_to_t and s_to_t[cs] != ct: return False
    4.   if ct in t_to_s and t_to_s[ct] != cs: return False
    5.   s_to_t[cs] = ct
    6.   t_to_s[ct] = cs
    7. return True

  ಕನ್ನಡದಲ್ಲಿ ಒಂದು ಸಲ ಹೇಳಿ:
    → "s ಇಂದ t ಗೆ ಒಂದು map, t ಇಂದ s ಗೆ ಇನ್ನೊಂದು map ಇಟ್ಕೊಳಿ.
       ಪ್ರತಿ character pair ನೋಡುವಾಗ: ಈಗಾಗಲೇ mapping ಇದ್ರೆ
       ಅದು match ಆಗಬೇಕು, ಇಲ್ಲಾಂದ್ರೆ False. ಇಲ್ಲಾಂದ್ರೆ ಎರಡೂ
       map ಗಳಲ್ಲಿ ಹೊಸ entry ಸೇರಿಸಿ. ಕೊನೆವರೆಗೂ ಸಮಸ್ಯೆ ಇಲ್ಲಾಂದ್ರೆ True!"

  Time  : O(n)  →  Why: single pass, O(1) hashmap lookups/inserts
  Space : O(k)  →  Why: k = number of distinct characters, bounded
                        by alphabet size (at most n in worst case)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🔍 SECTION 7 — DRY RUN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Input: s = "egg", t = "add"

  i  cs   ct   s_to_t before   t_to_s before   action
  0  'e'  'a'  {}              {}              new: s_to_t[e]=a, t_to_s[a]=e
  1  'g'  'd'  {e:a}           {a:e}           new: s_to_t[g]=d, t_to_s[d]=g
  2  'g'  'd'  {e:a,g:d}       {a:e,d:g}       check: s_to_t[g]==d ✓, t_to_s[d]==g ✓

  Output: True ✓

  ಇನ್ನೊಂದು example — many-to-one violation:
  Input: s = "ab", t = "aa"

  i  cs   ct   s_to_t before   t_to_s before   action
  0  'a'  'a'  {}              {}              new: s_to_t[a]=a, t_to_s[a]=a
  1  'b'  'a'  {a:a}           {a:a}           check t_to_s: 'a' already
                                                maps to 'a', but current
                                                cs is 'b' ≠ 'a' → MISMATCH

  Output: False ✓  (caught by the REVERSE map check)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 ⚠️ SECTION 8 — EDGE CASES — ಇವನ್ನ ಮರೆಯಬೇಡ!
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  ✓ Same string twice "abc","abc"? →  True — identity mapping
  ✓ Many-to-one "ab" → "aa"?       →  False — caught by reverse map
  ✓ One-to-many "foo" → "bar"?     →  False — caught by forward map
  ✓ Single character "a","b"?      →  True — trivial 1-char mapping
  ✓ All same char "aaa","bbb"?     →  True — consistent both ways

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📊 SECTION 9 — COMPLEXITY SUMMARY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                      Time     Space
  Brute (pattern)     O(n^2)   O(n)
  Optimal (2 maps)    O(n)     O(k)   ← use this ✅

  k = number of distinct characters involved (≤ n)

  Time yaake O(n)?  → Single pass through both strings together,
                       O(1) hashmap operations per index
  Space yaake O(k)? → Two hashmaps hold at most one entry per
                       distinct character seen

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🎯 SECTION 10 — PATTERN LEARNED — ಇದರಿಂದ ಕಲಿತದ್ದು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Pattern Name: Bidirectional HashMap Mapping

  Ee pattern yaavaaga use maadabeeku?
  → "One-to-one correspondence / bijection" check bekagidre —
     ondu direction map saaladu, RIVERSE map koota bekagutte
  → Structural equality (same repetition pattern) check
     madabekagidre

  Idee pattern beere problemsalli kaanisatte:
  → Check if String is Rotation of Another #796 (next problem!)
  → Word Pattern #290 (same bidirectional mapping idea, words↔chars)
  → Valid Anagram #242 (single hashmap, frequency-based — good
     contrast to see when ONE map is enough vs when TWO are needed)

  Next time intaha problem bandre naanu modalu idannu think maadtene:
  → "Two sequences ge character-by-character mapping/bijection
     bekagidre → bidirectional hashmap try maadu! Ondu direction
     matra saaladu — reverse map illade sneaky many-to-one
     violations miss aagatte!"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🗣️ SECTION 11 — INTERVIEWALLI HEGE EXPLAIN MAADABEEKU
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  1. Understand:
     "Check if characters of s can be consistently, one-to-one
      replaced to produce t — same repetition structure."

  2. Brute force:
     "Encode each string as first-occurrence-index patterns and
      compare them. Correct, but O(n^2) due to repeated index()
      scans."

  3. Optimize:
     "Track s→t and t→s mappings simultaneously in one pass. A
      single direction only catches one kind of violation — I
      need both to guarantee a true bijection."

  4. Code:
     "Two dicts. At each index, verify existing mappings agree
      in both directions, or create fresh entries in both."

  5. Complexity:
     "Time O(n) — one pass, O(1) hashmap ops. Space O(k) for the
      two maps, k = distinct characters."

  Mukhya: bijection check bekagidre — ONE map alone is a trap,
          always verify BOTH directions!
"""


# ═══════════════════════════════════════════════════════════════════
# BRUTE FORCE — O(n^2) Time | O(n) Space (pattern encoding)
# ═══════════════════════════════════════════════════════════════════
def is_isomorphic_brute(s, t):
    """
    Idu modala aaloochane — prati string ge first-occurrence-index
    pattern build madi, compare madu
    """
    def pattern(string):
        return [string.index(c) for c in string]

    return pattern(s) == pattern(t)


# ═══════════════════════════════════════════════════════════════════
# OPTIMAL — O(n) Time | O(k) Space (bidirectional hashmap)
# ═══════════════════════════════════════════════════════════════════
def is_isomorphic(s, t):
    """
    Idu final answer — s_to_t mattu t_to_s eradu maps track madi,
    ondu single pass alli bijection check madu
    """
    s_to_t = {}
    t_to_s = {}

    for cs, ct in zip(s, t):
        if cs in s_to_t and s_to_t[cs] != ct:
            return False
        if ct in t_to_s and t_to_s[ct] != cs:
            return False

        s_to_t[cs] = ct
        t_to_s[ct] = cs

    return True


# ═══════════════════════════════════════════════════════════════════
# TEST CASES
# ═══════════════════════════════════════════════════════════════════
if __name__ == "__main__":
    # Test 1 — Basic isomorphic
    assert is_isomorphic("egg", "add") is True

    # Test 2 — One-to-many violation
    assert is_isomorphic("foo", "bar") is False

    # Test 3 — Longer isomorphic string
    assert is_isomorphic("paper", "title") is True

    # Test 4 — Many-to-one violation (the sneaky case)
    assert is_isomorphic("ab", "aa") is False

    # Test 5 — All same character
    assert is_isomorphic("aaa", "bbb") is True

    # Cross-check: brute force must agree on all of the above
    assert is_isomorphic_brute("egg", "add") is True
    assert is_isomorphic_brute("foo", "bar") is False
    assert is_isomorphic_brute("paper", "title") is True
    assert is_isomorphic_brute("ab", "aa") is False
    assert is_isomorphic_brute("aaa", "bbb") is True

    print("All tests passed!")
