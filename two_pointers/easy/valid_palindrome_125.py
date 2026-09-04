"""
╔════════════════════════════════════════════════════════════════════╗
║  VALID PALINDROME                                                  ║
║  LeetCode #125  |  Difficulty: Easy  |  Topic: Two Pointers        ║
║  Link: https://leetcode.com/problems/valid-palindrome/             ║
╚════════════════════════════════════════════════════════════════════╝

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📘 SECTION 1 — PROBLEM UNDERSTANDING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  A phrase is a palindrome if, after converting all uppercase
  letters to lowercase and removing all NON-ALPHANUMERIC
  characters (spaces, punctuation, etc.), it reads the same
  forwards and backwards.

  Given a string `s`, return True if it is a palindrome under
  these rules, False otherwise.

  Input : s = a string (may contain letters, digits, spaces,
          punctuation)
  Output: boolean — True if it's a valid palindrome

  Example 1 — basic:
    Input : s = "A man, a plan, a canal: Panama"
    Output: True
    Why?  : stripping punctuation/spaces and lowercasing gives
            "amanaplanacanalpanama", which reads the same
            backwards

  Example 2 — slightly tricky (fails after cleaning):
    Input : s = "race a car"
    Output: False
    Why?  : cleaned = "raceacar" — not the same reversed
            ("racaecar" ≠ "raceacar")

  Example 3 — empty after cleaning:
    Input : s = " "
    Output: True
    Why?  : after removing the non-alphanumeric space, nothing
            is left — an empty string is trivially a palindrome

  Constraints:
    - 1 <= s.length <= 2 * 10^5
    - s consists only of printable ASCII characters

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🧠 SECTION 2 — KANGLISH THINKING — ಹೇಗೆ ಯೋಚಿಸಬೇಕು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  Problem odi aada mele namma brain enu think maadabeeku:

  ಹಂತ 1 — Problem ಅರ್ಥ ಮಾಡಿಕೊಳ್ಳಿ
  ┌─────────────────────────────────────────────────────────┐
  │  Input ಏನು ಕೊಡ್ತಾರೆ?  →  letters, digits, punctuation,   │
  │                           spaces ಇರೋ string               │
  │  Output ಏನು ಬೇಕು?     →  ಸ್ವಚ್ಛ ಮಾಡಿದ ಮೇಲೆ (lowercase +  │
  │                           alphanumeric ಮಾತ್ರ) palindrome  │
  │                           ಆಗಿದ್ಯಾ ಅಂತ ಚೆಕ್                │
  │  Constraints ಏನಿದೆ?   →  punctuation/case ignore ಮಾಡಬೇಕು │
  └─────────────────────────────────────────────────────────┘

  ಹಂತ 2 — ಮೊದಲ simple idea ಏನು?
  →  string ಅನ್ನ ಸ್ವಚ್ಛ ಮಾಡಿ (ಬರೀ alphanumeric characters
     ಇಟ್ಟುಕೊಂಡು, ಎಲ್ಲಾ lowercase ಮಾಡಿ) ಹೊಸ string build ಮಾಡಿ
  →  ಆ ಹೊಸ string ಅನ್ನ reverse ಮಾಡಿ compare ಮಾಡಿ

  ಹಂತ 3 — Two-Pointer way (extra string ಬೇಡ) ಹೇಗೆ?
  →  ಎಡ pointer string ರ ಶುರುವಿಂದ, ಬಲ pointer ಕೊನೆಯಿಂದ ಶುರು
     ಮಾಡಿ
  →  ಎರಡೂ pointers ಗೂ, alphanumeric ಅಲ್ಲದ characters ಸಿಕ್ಕಾಗ
     SKIP ಮಾಡ್ತಾ ಹೋಗಿ
  →  ಎರಡೂ pointers ಗೂ valid character ಸಿಕ್ಕಾಗ, ಅವುಗಳ lowercase
     ಸಮ ಇದ್ಯಾ compare ಮಾಡಿ — ಸಮ ಇಲ್ಲಾಂದ್ರೆ False
  →  Pointers ಒಂದನ್ನೊಂದು ದಾಟೋವರೆಗೆ ಇದೇ ಮುಂದುವರಿಸಿ

  ಹಂತ 4 — Technique ಯಾಕೆ ಇಲ್ಲಿ ಕೆಲಸ ಮಾಡುತ್ತೆ?
  →  Palindrome check ಅಂದ್ರೆ ಮೂಲತಃ "ಎಡ ಮತ್ತು ಬಲ ends ಸಮ
     ಇದ್ಯಾ, ಒಳಗಡೆ ಬರ್ತಾ ಇರಿ" ಅನ್ನೋ opposite-ends comparison —
     ಇದೇ two-pointer ರ classic use case
  →  Non-alphanumeric characters ಅನ್ನ SKIP ಮಾಡ್ತಾ ಹೋಗೋದ್ರಿಂದ,
     ಹೊಸ cleaned string build ಮಾಡೋ ಅಗತ್ಯ ಇಲ್ಲ — original
     string ಮೇಲೆನೇ direct ಆಗಿ ಕೆಲಸ ಮಾಡಬಹುದು

  💡 Interview ನಲ್ಲಿ ಹೇಗೆ ಮಾತಾಡಬೇಕು:
  →  "Two pointers from opposite ends, moving inward"
  →  "Skip non-alphanumeric characters on either side before
      comparing"
  →  "Compare lowercase versions of the two valid characters —
      mismatch means not a palindrome, pointers crossing means
      it IS one"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🏷️ SECTION 3 — TECHNIQUE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Primary   : Two Pointers — opposite ends, skip-and-compare
  Secondary : Clean-then-compare (build a filtered string first)

  WHY Two Pointers (opposite ends)?
  → It avoids allocating a whole new cleaned string — we can
    walk in from both ends of the ORIGINAL string simultaneously,
    skipping junk characters as we go, and never need extra
    space proportional to the input.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 💡 SECTION 4 — INTUITION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  The key insight: checking "is this a palindrome" only ever
  needs to compare characters at MIRRORED positions — the first
  valid character against the last, the second against the
  second-last, and so on. We don't need the whole cleaned string
  in memory to do that; we just need a way to find "the next
  valid character from the left" and "the next valid character
  from the right," which two pointers do naturally as they walk
  inward.

  The journey from brute to optimal:
    Brute thought   →  Build a new string keeping only lowercase
                       alphanumeric characters, then compare it
                       to its own reverse
    Problem with it →  O(n) extra space for the cleaned string
                       (and another O(n) for its reverse)
    Better question →  "Can I compare mirrored characters
                       directly on the original string, skipping
                       junk as I go?"
    Insight         →  Two pointers from both ends, advancing
                       past non-alphanumeric characters before
                       each comparison
    Optimal         →  Single pass, O(1) extra space

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🐢 SECTION 5 — APPROACH 1 — BRUTE FORCE (clean then compare)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    Build a new string containing only the lowercased
    alphanumeric characters of `s`, in order. Then check if that
    cleaned string equals its own reverse.

  Pseudocode:
    step 1: cleaned = "".join(c.lower() for c in s if c.isalnum())
    step 2: return cleaned == cleaned[::-1]

  Time  : O(n)  →  Why: one pass to build the cleaned string,
                        one more to reverse and compare
  Space : O(n)  →  Why: the cleaned string and its reverse are
                        both new O(n) allocations

  ಇದು ಯಾಕೆ ಸಾಕಾಗಲ್ಲ?
    → Correct and still O(n) time, but allocates extra strings
      proportional to input size — two pointers can do the same
      check directly on the original string with O(1) extra space.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🚀 SECTION 6 — APPROACH 2 — OPTIMAL (Two Pointers, opposite ends)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    Keep a `left` pointer starting at index 0 and a `right`
    pointer starting at the last index. While `left < right`:
    skip `left` forward past any non-alphanumeric character,
    skip `right` backward past any non-alphanumeric character,
    then compare the lowercase versions of s[left] and s[right].
    Mismatch → not a palindrome. Otherwise, move both pointers
    inward and continue.

  Key steps:
    1. left, right = 0, len(s) - 1
    2. while left < right:
    3.   while left < right and not s[left].isalnum(): left += 1
    4.   while left < right and not s[right].isalnum(): right -= 1
    5.   if s[left].lower() != s[right].lower(): return False
    6.   left += 1; right -= 1
    7. return True

  ಕನ್ನಡದಲ್ಲಿ ಒಂದು ಸಲ ಹೇಳಿ:
    → "left pointer ಶುರುವಿಂದ, right pointer ಕೊನೆಯಿಂದ ಶುರು
       ಮಾಡು. ಎರಡೂ ಕಡೆ non-alphanumeric characters ಸಿಕ್ಕಾಗ skip
       ಮಾಡ್ತಾ ಹೋಗು. ಎರಡೂ valid character ಸಿಕ್ಕಾಗ, lowercase
       ಮಾಡಿ compare ಮಾಡು — mismatch ಆದ್ರೆ False. ಇಲ್ಲಾಂದ್ರೆ
       ಎರಡೂ pointers ಒಳಗಡೆ ಸರಿಸಿ ಮುಂದುವರಿಸು!"

  Time  : O(n)  →  Why: each pointer moves strictly inward,
                        together covering the string once
  Space : O(1)  →  Why: only two index pointers, no extra
                        strings built

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🔍 SECTION 7 — DRY RUN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Input: s = "A man, a plan, a canal: Panama"

  left=0 ('A'), right=29 ('a') → both alphanumeric →
    'a' == 'a' → match, left=1, right=28
  left=1 (' ') → skip (not alnum) → left=2 ('m')
  right=28 ('m') → alnum → 'm' == 'm' → match, left=3, right=27
  ... (continues skipping commas, spaces, colon) ...
  eventually left and right meet in the middle without any
  mismatch found

  Output: True ✓

  ಇನ್ನೊಂದು example — fails:
  Input: s = "race a car"

  left=0 ('r'), right=9 ('r') → match
  left=1 ('a'), right=8 ('a') → match
  left=2 ('c'), right=7 ('c') → match
  left=3 ('e'), right=6 (' ') → skip right → right=5 ('a')
  compare s[3]='e' vs s[5]='a' → MISMATCH

  Output: False ✓

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 ⚠️ SECTION 8 — EDGE CASES — ಇವನ್ನ ಮರೆಯಬೇಡ!
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  ✓ Single character "a"?          →  True — trivially a palindrome
  ✓ Only punctuation/spaces " "?   →  True — nothing left after
                                       cleaning, empty is a palindrome
  ✓ Mixed case "Aa"?               →  True — case-insensitive
  ✓ Digits involved "0P"?          →  False — digits count as
                                       alphanumeric, must match too
  ✓ Already clean, fails
    ("race a car")?                →  False — genuinely not a
                                       palindrome after cleaning

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📊 SECTION 9 — COMPLEXITY SUMMARY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                        Time    Space
  Brute (clean+compare)  O(n)    O(n)
  Two-Pointer            O(n)    O(1)   ← use this ✅

  Time yaake O(n)?  → Both pointers together traverse the string
                       once, each character visited a constant
                       number of times
  Space yaake O(1)? → Only two index pointers tracked, no extra
                       string allocations

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🎯 SECTION 10 — PATTERN LEARNED — ಇದರಿಂದ ಕಲಿತದ್ದು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Pattern Name: Two Pointers — Opposite Ends

  Ee pattern yaavaaga use maadabeeku?
  → Palindrome checks, reversal-style comparisons, "does this
     read the same from both sides" type problems
  → Whenever you'd otherwise build a cleaned/reversed COPY just
     to compare it — check if two pointers walking inward can
     do the same comparison directly on the original data

  Idee pattern beere problemsalli kaanisatte:
  → Two Sum II — Input Array Sorted #167 (next problem — same
     opposite-ends two-pointer shape, different goal: finding a
     target sum instead of checking symmetry)
  → Valid Palindrome II #680 (harder variant — allows deleting
     ONE character, same two-pointer skeleton with a branch)
  → Container With Most Water #11 (already done — same opposite-
     ends pointer movement, different comparison logic)

  Next time intaha problem bandre naanu modalu idannu think maadtene:
  → "Symmetry/reversal check bekagidre → two pointers opposite
     ends inda try maadu, cleaned copy build madoda bittu, junk
     characters skip maadtha directly compare madu!"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🗣️ SECTION 11 — INTERVIEWALLI HEGE EXPLAIN MAADABEEKU
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  1. Understand:
     "Check if a string is a palindrome after ignoring case and
      non-alphanumeric characters."

  2. Brute force:
     "Build a cleaned, lowercased string and compare it to its
      reverse. O(n) time, but O(n) extra space."

  3. Optimize:
     "Two pointers from both ends of the ORIGINAL string. Skip
      non-alphanumeric characters on either side, then compare
      lowercase versions. Mismatch → false; pointers crossing
      → true. No extra string needed."

  4. Code:
     "left/right pointers, two inner while-loops to skip junk
      characters, one comparison, then move both pointers inward."

  5. Complexity:
     "Time O(n) — combined pointer movement covers the string
      once. Space O(1) — just two indices."

  Mukhya: palindrome/symmetry checks are the classic opposite-
          ends two-pointer use case — skip the extra copy, compare
          directly on the original data!
"""


# ═══════════════════════════════════════════════════════════════════
# BRUTE FORCE — O(n) Time | O(n) Space (clean then compare)
# ═══════════════════════════════════════════════════════════════════
def is_palindrome_brute(s):
    """
    Idu modala aaloochane — alphanumeric characters matra ittu
    lowercase string build madi, reverse jothe compare madu
    """
    cleaned = "".join(ch.lower() for ch in s if ch.isalnum())
    return cleaned == cleaned[::-1]


# ═══════════════════════════════════════════════════════════════════
# OPTIMAL — O(n) Time | O(1) Space (two pointers, opposite ends)
# ═══════════════════════════════════════════════════════════════════
def is_palindrome(s):
    """
    Idu final answer — left mattu right pointers opposite ends
    inda, junk characters skip madtha directly compare madu
    """
    left, right = 0, len(s) - 1

    while left < right:
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1

        if s[left].lower() != s[right].lower():
            return False

        left += 1
        right -= 1

    return True


# ═══════════════════════════════════════════════════════════════════
# TEST CASES
# ═══════════════════════════════════════════════════════════════════
if __name__ == "__main__":
    # Test 1 — Basic
    assert is_palindrome("A man, a plan, a canal: Panama") is True

    # Test 2 — Fails after cleaning
    assert is_palindrome("race a car") is False

    # Test 3 — Empty after cleaning
    assert is_palindrome(" ") is True

    # Test 4 — Single character
    assert is_palindrome("a") is True

    # Test 5 — Digits involved, fails
    assert is_palindrome("0P") is False

    # Cross-check: brute force must agree on all of the above
    assert is_palindrome_brute("A man, a plan, a canal: Panama") is True
    assert is_palindrome_brute("race a car") is False
    assert is_palindrome_brute(" ") is True
    assert is_palindrome_brute("a") is True
    assert is_palindrome_brute("0P") is False

    print("All tests passed!")
