"""
╔════════════════════════════════════════════════════════════════════╗
║  VALID ANAGRAM                                                     ║
║  LeetCode #242  |  Difficulty: Easy  |  Topic: Strings/HashMap     ║
║  Link: https://leetcode.com/problems/valid-anagram/                ║
╚════════════════════════════════════════════════════════════════════╝

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📘 SECTION 1 — PROBLEM UNDERSTANDING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Given two strings `s` and `t`, return True if `t` is an
  ANAGRAM of `s`, and False otherwise.

  An anagram is formed by rearranging all the letters of another
  word, using EVERY original letter exactly once — no adding,
  no dropping, no reordering rules, just "same multiset of
  characters."

  Input : s, t = two strings
  Output: boolean — True if t is an anagram of s

  Example 1 — basic:
    Input : s = "anagram", t = "nagaram"
    Output: True
    Why?  : both have exactly the same letters, just shuffled
            (a:3, n:1, g:1, r:1, m:1 in both)

  Example 2 — slightly tricky (same length, different letters):
    Input : s = "rat", t = "car"
    Output: False
    Why?  : 'c' appears in t but not in s — different letter
            sets, even though both are length 3

  Example 3 — different lengths (instant no):
    Input : s = "ab", t = "a"
    Output: False
    Why?  : an anagram must use ALL letters exactly once —
            different lengths make it impossible right away

  Constraints:
    - 1 <= s.length, t.length <= 5 * 10^4
    - s and t consist of lowercase English letters
    - Follow-up: what if the inputs contain Unicode characters?
      (a general hashmap handles this; a fixed 26-array doesn't)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🧠 SECTION 2 — KANGLISH THINKING — ಹೇಗೆ ಯೋಚಿಸಬೇಕು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  Problem odi aada mele namma brain enu think maadabeeku:

  ಹಂತ 1 — Problem ಅರ್ಥ ಮಾಡಿಕೊಳ್ಳಿ
  ┌─────────────────────────────────────────────────────────┐
  │  Input ಏನು ಕೊಡ್ತಾರೆ?  →  ಎರಡು strings s, t              │
  │  Output ಏನು ಬೇಕು?     →  t, s ರ letters ಅನ್ನ rearrange   │
  │                           ಮಾಡಿ ಸಿಗುತ್ಯಾ ಅಂತ ಚೆಕ್           │
  │  Constraints ಏನಿದೆ?   →  ORDER ಮ್ಯಾಟರ್ ಆಗಲ್ಲ, ಆದ್ರೆ      │
  │                           COUNT ಪ್ರತಿ letter ಗೆ ಸಮ ಇರಬೇಕು│
  └─────────────────────────────────────────────────────────┘

  ಹಂತ 2 — ಇದನ್ನ previous problem (#796 Rotation) ಜೊತೆ compare
           ಮಾಡಿ ನೋಡಿ!
  →  Rotation ನಲ್ಲಿ ORDER ಬಹಳ ಮುಖ್ಯ (specific ಆಗಿ shift ಆಗಿರಬೇಕು)
  →  ಇಲ್ಲಿ ORDER ಮ್ಯಾಟರ್ ಆಗಲ್ಲ — ಬರೀ COUNT ಸಮ ಇದ್ರೆ ಸಾಕು!
  →  ಈ ವ್ಯತ್ಯಾಸ ಗಮನಿಸಿದ್ರೆ, ಸರಿಯಾದ technique ಸಿಗುತ್ತೆ

  ಹಂತ 3 — ಮೊದಲ simple idea ಏನು?
  →  ಎರಡೂ strings ಅನ್ನ SORT ಮಾಡಿ, sorted versions compare ಮಾಡಿ
  →  Anagram ಆಗಿದ್ರೆ, sort ಮಾಡಿದ ಮೇಲೆ ಎರಡೂ ಒಂದೇ ಆಗಿ ಇರುತ್ತೆ!

  ಹಂತ 4 — Better way (sort ಬೇಡ) ಹೇಗೆ?
  →  "Sort ಬದಲು, ಪ್ರತಿ letter ಎಷ್ಟು ಸಲ ಬಂತು ಅಂತ COUNT
      ಮಾಡಿದ್ರೆ ಸಾಕಲ್ವಾ?"
  →  s ರ ಪ್ರತಿ character ಗೆ counter += 1, t ರ ಪ್ರತಿ character ಗೆ
     counter -= 1 ಮಾಡಿ
  →  ಕೊನೆಗೆ ಎಲ್ಲಾ counters 0 ಆಗಿದ್ರೆ ಸಮ frequencies — Anagram!

  ಹಂತ 5 — Technique ಯಾಕೆ ಇಲ್ಲಿ ಕೆಲಸ ಮಾಡುತ್ತೆ?
  →  Anagram ಅಂದ್ರೆ "ಪ್ರತಿ letter ಗೂ count ಸಮ ಇರಬೇಕು" — ಇದೇ
     ನಿಖರ definition
  →  Sorting O(n log n) ತಗೊಳ್ಳುತ್ತೆ, ಆದ್ರೆ counting O(n) ಸಾಕು —
     comparison based (sort) ಬದಲು direct counting ಬೇಗ ಆಗುತ್ತೆ

  💡 Interview ನಲ್ಲಿ ಹೇಗೆ ಮಾತಾಡಬೇಕು:
  →  "First check lengths — different lengths can never be
      anagrams"
  →  "Count character frequencies in s (increment), then
      subtract frequencies from t (decrement) in the same pass"
  →  "If every count ends at zero, it's a valid anagram"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🏷️ SECTION 3 — TECHNIQUE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Primary   : HashMap / Frequency Counter
  Secondary : Sorting-based comparison

  WHY Frequency Counter over Sorting?
  → Sorting forces O(n log n) comparisons just to notice "same
    multiset of characters." Counting directly captures the
    definition of an anagram — matching character frequencies —
    in a single O(n) pass, no ordering needed at all.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 💡 SECTION 4 — INTUITION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  The key insight: two strings are anagrams if and only if they
  have the IDENTICAL character frequency distribution — order is
  completely irrelevant. Sorting is one way to make that
  distribution "visible" (equal multisets sort to equal
  sequences), but it's overkill: directly counting occurrences
  answers the same question without paying the sorting cost.

  The journey from brute to optimal:
    Brute thought   →  Sort both strings, compare the sorted
                       results character by character
    Problem with it →  Sorting costs O(n log n), when checking
                       "same multiset" doesn't actually require
                       any ordering at all
    Better question →  "Can I directly compare COUNTS of each
                       character instead of ordering them?"
    Insight         →  Increment counts for s, decrement for t,
                       in the same hashmap, in one combined pass
    Optimal         →  Single pass, O(n) frequency counting

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🐢 SECTION 5 — APPROACH 1 — BRUTE FORCE (sort & compare)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    If lengths differ, immediately False. Otherwise, sort both
    strings — if they're anagrams, their sorted forms will be
    character-for-character identical.

  Pseudocode:
    step 1: if len(s) != len(t): return False
    step 2: return sorted(s) == sorted(t)

  Time  : O(n log n)  →  Why: sorting dominates; the comparison
                              itself is O(n)
  Space : O(n)         →  Why: sorted() builds new list copies

  ಇದು ಯಾಕೆ ಸಾಕಾಗಲ್ಲ?
    → Correct, but sorting does more work than necessary — we
      only need to know if character COUNTS match, and counting
      is a strictly cheaper O(n) operation than sorting.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🚀 SECTION 6 — APPROACH 2 — OPTIMAL (Frequency Counter)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    If lengths differ, immediately False. Otherwise, use one
    hashmap: walk `s` incrementing each character's count, then
    walk `t` decrementing the same counts. If every count nets
    to exactly zero, the frequency distributions matched.

  Key steps:
    1. if len(s) != len(t): return False
    2. counts = {}
    3. for ch in s: counts[ch] = counts.get(ch, 0) + 1
    4. for ch in t: counts[ch] = counts.get(ch, 0) - 1
    5. return all(v == 0 for v in counts.values())

  ಕನ್ನಡದಲ್ಲಿ ಒಂದು ಸಲ ಹೇಳಿ:
    → "ಮೊದಲು length ಸಮ ಇದ್ಯಾ ಚೆಕ್ ಮಾಡು. ಆಮೇಲೆ s ರ ಪ್ರತಿ
       character ಗೆ count += 1, t ರ ಪ್ರತಿ character ಗೆ
       count -= 1 ಮಾಡು — ಒಂದೇ hashmap ನಲ್ಲಿ. ಕೊನೆಗೆ ಎಲ್ಲಾ
       counts 0 ಆಗಿದ್ರೆ, ಎರಡೂ strings ಗೆ ಸಮ frequency —
       Anagram ಆಗಿದ್ದೇ!"

  Time  : O(n)  →  Why: two linear passes (increment, decrement),
                        each O(1) hashmap operation per character
  Space : O(k)  →  Why: k = number of distinct characters, at
                        most 26 for lowercase English letters

  📌 NOTE — array optimization for the given constraints:
    Since the problem guarantees only lowercase English letters,
    a fixed-size array of 26 integers (indexed by ord(ch)-ord('a'))
    works just as well as a hashmap and gives TRUE O(1) space
    instead of O(k). The hashmap version shown here is kept
    general so it also handles the Unicode follow-up mentioned
    in the constraints.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🔍 SECTION 7 — DRY RUN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Input: s = "anagram", t = "nagaram"

  Step 1: len(s) == len(t)? 7 == 7 → continue

  Step 2 (increment from s):
    a:3, n:1, g:1, r:1, m:1

  Step 3 (decrement from t = "nagaram"):
    n:1→0, a:3→2→1→0 (three a's in t too),
    g:1→0, r:1→0, m:1→0

  Final counts: {a:0, n:0, g:0, r:0, m:0} → all zero

  Output: True ✓

  ಇನ್ನೊಂದು example — not an anagram:
  Input: s = "rat", t = "car"

  Step 1: lengths match (3 == 3), continue
  Step 2 (increment from s): r:1, a:1, t:1
  Step 3 (decrement from t = "car"): c:-1, a:1→0, r:1→0

  Final counts: {r:0, a:0, t:1, c:-1} → t and c are NOT zero

  Output: False ✓

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 ⚠️ SECTION 8 — EDGE CASES — ಇವನ್ನ ಮರೆಯಬೇಡ!
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  ✓ Different lengths ("ab","a")?  →  False immediately, no need
                                       to even count
  ✓ Identical strings s == t?      →  True — trivially an anagram
                                       of itself
  ✓ Single character "a","a"?      →  True
  ✓ Same letters, different counts
    ("aab","abb")?                 →  False — 'a' count 2 vs 1
  ✓ All characters the same
    ("aaa","aaa")?                 →  True

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📊 SECTION 9 — COMPLEXITY SUMMARY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                        Time        Space
  Brute (sort)          O(n log n)  O(n)
  Optimal (frequency)   O(n)        O(k)   ← use this ✅

  k = number of distinct characters (≤ 26 for lowercase letters)

  Time yaake O(n)?  → Two linear passes, O(1) hashmap op each
  Space yaake O(k)? → One counts dict, at most k distinct keys

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🎯 SECTION 10 — PATTERN LEARNED — ಇದರಿಂದ ಕಲಿತದ್ದು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Pattern Name: Frequency Counter (hashmap/array)

  Ee pattern yaavaaga use maadabeeku?
  → ORDER matter aagade, only COUNT/multiset match aagbeku
     antadre → sorting bittu direct frequency counting madu
  → "Same characters, any order" type problems — anagram,
     permutation-in-string, group-anagrams family

  Idee pattern beere problemsalli kaanisatte:
  → Group Anagrams #49 (same frequency-signature idea, grouped)
  → Isomorphic Strings #205 (contrast — there ORDER mattered,
     needed bidirectional map instead of plain frequency count)
  → Sort Characters by Frequency #451 (next in curriculum's
     Medium section — frequency counting taken further)

  Next time intaha problem bandre naanu modalu idannu think maadtene:
  → "Order matter agade, count matra match aagbeku antadre →
     sort maadoda bittu, direct frequency counter (hashmap/array)
     use maadu — O(n log n) inda O(n) ge ilisabahudu!"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🗣️ SECTION 11 — INTERVIEWALLI HEGE EXPLAIN MAADABEEKU
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  1. Understand:
     "Check if t is a rearrangement of all of s's letters —
      order doesn't matter, only the multiset of characters."

  2. Brute force:
     "Sort both strings and compare. O(n log n) since sorting
      dominates."

  3. Optimize:
     "Anagram just means matching character frequencies. Count
      s's characters up, count t's characters down in the same
      hashmap — no sorting needed at all."

  4. Code:
     "Length check first. Then one dict: increment per char in
      s, decrement per char in t. All zero at the end → anagram."

  5. Complexity:
     "Time O(n) — two linear passes. Space O(k), k = distinct
      characters, capped at 26 for lowercase letters."

  Mukhya: order matter illa, count matra match aagbeku antadre —
          sorting is overkill, frequency counting is the direct hit!
"""


# ═══════════════════════════════════════════════════════════════════
# BRUTE FORCE — O(n log n) Time | O(n) Space (sort & compare)
# ═══════════════════════════════════════════════════════════════════
def is_anagram_brute(s, t):
    """
    Idu modala aaloochane — eradu strings sort madi compare madu
    """
    if len(s) != len(t):
        return False

    return sorted(s) == sorted(t)


# ═══════════════════════════════════════════════════════════════════
# OPTIMAL — O(n) Time | O(k) Space (frequency counter)
# ═══════════════════════════════════════════════════════════════════
def is_anagram(s, t):
    """
    Idu final answer — s ge count increment, t ge count decrement,
    ondu single hashmap alli — kadege ella zero aadre anagram
    """
    if len(s) != len(t):
        return False

    counts = {}

    for ch in s:
        counts[ch] = counts.get(ch, 0) + 1

    for ch in t:
        counts[ch] = counts.get(ch, 0) - 1

    return all(v == 0 for v in counts.values())


# ═══════════════════════════════════════════════════════════════════
# TEST CASES
# ═══════════════════════════════════════════════════════════════════
if __name__ == "__main__":
    # Test 1 — Basic anagram
    assert is_anagram("anagram", "nagaram") is True

    # Test 2 — Same length, different letters
    assert is_anagram("rat", "car") is False

    # Test 3 — Different lengths
    assert is_anagram("ab", "a") is False

    # Test 4 — Identical strings
    assert is_anagram("listen", "listen") is True

    # Test 5 — Same letters, different counts
    assert is_anagram("aab", "abb") is False

    # Cross-check: brute force must agree on all of the above
    assert is_anagram_brute("anagram", "nagaram") is True
    assert is_anagram_brute("rat", "car") is False
    assert is_anagram_brute("ab", "a") is False
    assert is_anagram_brute("listen", "listen") is True
    assert is_anagram_brute("aab", "abb") is False

    print("All tests passed!")
