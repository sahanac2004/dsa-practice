"""
╔════════════════════════════════════════════════════════════════════╗
║  REVERSE WORDS IN A STRING III (REVERSE EVERY WORD)                ║
║  LeetCode #557  |  Difficulty: Easy  |  Topic: Strings/Two Pointers║
║  Link: https://leetcode.com/problems/reverse-words-in-a-string-iii/║
╚════════════════════════════════════════════════════════════════════╝

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📘 SECTION 1 — PROBLEM UNDERSTANDING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Given a string `s`, reverse the CHARACTERS of every word in
  the string, while still preserving whitespace and the
  ORIGINAL order of the words themselves.

  A word is a sequence of non-space characters. Unlike #151
  (Reverse Words in a Given String), here the words separated by
  single spaces, with NO leading/trailing/extra spaces to worry
  about — only the letters INSIDE each word get flipped.

  Input : s = a string of single-space-separated words
  Output: string with each word's characters reversed, word
          order and spacing unchanged

  Example 1 — basic:
    Input : s = "Let's take LeetCode contest"
    Output: "s'teL ekat edoCteeL tsetnoc"
    Why?  : each word is reversed in place — "Let's" → "s'teL",
            "take" → "ekat", etc. — but the WORD ORDER stays
            exactly the same

  Example 2 — slightly tricky (single word):
    Input : s = "God Ding"
    Output: "doG gniD"
    Why?  : two words, each reversed independently; word order
            ("God" then "Ding") is preserved

  Example 3 — simplest case:
    Input : s = "hello"
    Output: "olleh"
    Why?  : a single word is just reversed on its own

  Constraints:
    - 1 <= s.length <= 5 * 10^4
    - s consists of printable ASCII characters
    - s does not contain any leading or trailing spaces
    - Words in s are separated by a single space
    - s contains at least one word

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🧠 SECTION 2 — KANGLISH THINKING — ಹೇಗೆ ಯೋಚಿಸಬೇಕು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  Problem odi aada mele namma brain enu think maadabeeku:

  ಹಂತ 1 — Problem ಅರ್ಥ ಮಾಡಿಕೊಳ್ಳಿ
  ┌─────────────────────────────────────────────────────────┐
  │  Input ಏನು ಕೊಡ್ತಾರೆ?  →  single-space separated words    │
  │  Output ಏನು ಬೇಕು?     →  ಪ್ರತಿ WORD ರ letters reverse    │
  │                           ಮಾಡಿ, WORD order ಹಾಗೆಯೇ ಇಡಿ    │
  │  Constraints ಏನಿದೆ?   →  leading/trailing spaces ಇಲ್ಲ,    │
  │                           single space ಮಾತ್ರ words ನಡುವೆ │
  └─────────────────────────────────────────────────────────┘

  ಹಂತ 2 — ಇದನ್ನ previous problem (#151 Reverse Words) ಜೊತೆ
           compare ಮಾಡಿ ನೋಡಿ — ಇದೇ ಸರಿಯಾದ CONTRAST!
  →  #151 ರಲ್ಲಿ: WORD ORDER reverse ಮಾಡಿದ್ವಿ, letters ಸರಿಯಾಗಿ
     ಇಟ್ಟಿದ್ವಿ (ಇಡೀ array reverse + ಪ್ರತಿ word reverse ಮಾಡಿ
     letters fix ಮಾಡಿದ್ವಿ)
  →  ಇಲ್ಲಿ: WORD ORDER ಹಾಗೆಯೇ ಇಡಬೇಕು, letters ಮಾತ್ರ reverse
     ಮಾಡಬೇಕು — ಸರಿ ಎದುರು (opposite) ಟಾಸ್ಕ್!
  →  So ಇಲ್ಲಿ ಬರೀ "ಪ್ರತಿ word reverse ಮಾಡು" step ಸಾಕು —
     ಇಡೀ array reverse ಮಾಡೋ ಅಗತ್ಯ ಇಲ್ಲ!

  ಹಂತ 3 — ಮೊದಲ simple idea ಏನು?
  →  Space ಪ್ರಕಾರ split ಮಾಡಿ, ಪ್ರತಿ word ಅನ್ನ Python slicing
     [::-1] ಬಳಸಿ reverse ಮಾಡಿ, space ಇಟ್ಟು join ಮಾಡಿ

  ಹಂತ 4 — Two-Pointer way (in-place style) ಹೇಗೆ?
  →  string ಅನ್ನ char list ಆಗಿ ಪರಿವರ್ತಿಸಿ
  →  space boundary ಪ್ರತಿ ಸಲ ಸಿಕ್ಕಾಗ, ಆ word ರ start ಮತ್ತು end
     indices ಅನ್ನ two pointers ಬಳಸಿ swap ಮಾಡ್ತಾ reverse ಮಾಡು
     (ಇದೇ #151 ರಲ್ಲಿ ಬಳಸಿದ reverse() helper!)
  →  Space characters ಅನ್ನ touch ಮಾಡೋ ಅಗತ್ಯ ಇಲ್ಲ — ಅವು
     ಹಾಗೇ ಇರುತ್ತೆ, ಪ್ರತಿ word ಮಾತ್ರ ತನ್ನ boundary ಒಳಗೆ reverse
     ಆಗುತ್ತೆ

  💡 Interview ನಲ್ಲಿ ಹೇಗೆ ಮಾತಾಡಬೇಕು:
  →  "Since word ORDER stays the same, I only need to reverse
      each word's characters in place — no full-array reversal
      needed like the word-reordering variant of this problem"
  →  "Walk the string, find each space-delimited word's [start,
      end) boundary, and reverse just that segment with two
      pointers"
  →  "Spaces themselves are left untouched — they're already in
      the right place"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🏷️ SECTION 3 — TECHNIQUE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Primary   : Two Pointers — reverse each word in place
  Secondary : Split, reverse via slicing, rejoin

  WHY Two Pointers over split/reverse/join?
  → It demonstrates the same in-place reverse(l, r) helper
    used for the full "reverse word order" variant (#151),
    just applied WITHOUT the full-array reversal step — a clean
    illustration of how the two problems relate.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 💡 SECTION 4 — INTUITION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  The key insight: this is the DIRECT mirror of "reverse word
  order, keep letters correct." Here we keep word order and
  reverse the letters — so we only need HALF of the #151
  technique: no full-string reversal, just find each word's
  boundaries and reverse within them.

  The journey from brute to optimal:
    Brute thought   →  s.split(" ") → reverse each word with
                       slicing → " ".join(...)
    Problem with it →  Works fine and is O(n), but relies on
                       built-ins that hide the underlying
                       two-pointer mechanics
    Better question →  "Can I reverse each word's characters
                       directly, in place, using the same
                       swap-based technique from #151?"
    Insight         →  Track word boundaries via space
                       positions; reverse(start, end) each
                       segment with two pointers
    Optimal         →  Single pass, two-pointer reversal per
                       word, O(n) time

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🐢 SECTION 5 — APPROACH 1 — BRUTE FORCE (split / reverse / join)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    Split the string on single spaces (safe here since the
    constraints guarantee no leading/trailing/extra spaces),
    reverse each word using slicing, then rejoin with spaces.

  Pseudocode:
    step 1: words = s.split(" ")
    step 2: reversed_words = [w[::-1] for w in words]
    step 3: return " ".join(reversed_words)

  Time  : O(n)  →  Why: split, reverse-each, join each scan the
                        data once
  Space : O(n)  →  Why: new list of reversed words + result string

  ಇದು ಯಾಕೆ ಸಾಕಾಗಲ್ಲ?
    → Perfectly valid and O(n)! But it hides the two-pointer
      swap mechanic behind Python's slicing — less useful for
      demonstrating the in-place technique interviewers often
      want to see (and the direct link back to #151).

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🚀 SECTION 6 — APPROACH 2 — OPTIMAL (Two-Pointer in-place reverse)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    Convert the string to a mutable character list. Walk through
    it tracking the start of the current word; whenever a space
    (or the end of the string) is hit, that marks the word's end
    — reverse that [start, end) segment in place with two
    pointers, then move on to the next word.

  Key steps:
    1. chars = list(s)
    2. start = 0
    3. for end in range(len(chars) + 1):
    4.   if end == len(chars) or chars[end] == ' ':
    5.     reverse chars[start:end] in place (two pointers)
    6.     start = end + 1
    7. return "".join(chars)

  ಕನ್ನಡದಲ್ಲಿ ಒಂದು ಸಲ ಹೇಳಿ:
    → "String ಅನ್ನ char list ಆಗಿ ಪರಿವರ್ತಿಸು. space ಅಥವಾ string
       ಮುಗಿದ ಕಡೆ ಸಿಕ್ಕಾಗ, ಆ word ರ [start, end) segment ಅನ್ನ
       two pointers ಬಳಸಿ reverse ಮಾಡು. ಆಮೇಲೆ next word ಗೆ
       start ಅನ್ನ ಸರಿಸು — space characters ಅನ್ನ touch ಮಾಡಬೇಡ!"

  Time  : O(n)  →  Why: single pass; every character is visited
                        a constant number of times total across
                        all word reversals
  Space : O(n)  →  Why: Python strings immutable → need a list
                        copy; the algorithm itself needs only
                        O(1) extra space on a true mutable array

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🔍 SECTION 7 — DRY RUN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Input: s = "Let's take LeetCode contest"

  Word boundaries found (via spaces): "Let's", "take",
  "LeetCode", "contest"

  Reverse each word in place:
    "Let's"    → "s'teL"
    "take"     → "ekat"
    "LeetCode" → "edoCteeL"
    "contest"  → "tsetnoc"

  Spaces stay exactly where they were — join everything back:
    "s'teL" + " " + "ekat" + " " + "edoCteeL" + " " + "tsetnoc"

  Output: "s'teL ekat edoCteeL tsetnoc" ✓

  ಇನ್ನೊಂದು example — simplest:
  Input: s = "hello"

  Only one word, no spaces at all → reverse the whole thing:
  "hello" → "olleh"

  Output: "olleh" ✓

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 ⚠️ SECTION 8 — EDGE CASES — ಇವನ್ನ ಮರೆಯಬೇಡ!
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  ✓ Single word "hello"?           →  "olleh" — whole string
                                       reversed, no spaces involved
  ✓ Two words "God Ding"?          →  "doG gniD" — order kept,
                                       letters flipped per word
  ✓ Single-character words "a b c"? →  "a b c" — each 1-char
                                       "word" reverses to itself
  ✓ Palindromic word "level up"?   →  "level pu" — "level" reads
                                       the same reversed, "up"
                                       becomes "pu"
  ✓ Word with punctuation "Let's"? →  "s'teL" — punctuation is
                                       just another character,
                                       reversed along with letters

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📊 SECTION 9 — COMPLEXITY SUMMARY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                        Time    Space
  Brute (split/join)    O(n)    O(n)
  Two-Pointer           O(n)    O(n)*  ← use this ✅ (see note)

  * O(1) EXTRA space on a true mutable char array (C++/Java
    style); Python needs O(n) for the list(s) copy since strings
    are immutable — same caveat as #151

  Time yaake O(n)?  → Single pass; each character is part of
                       exactly one word-reversal operation

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🎯 SECTION 10 — PATTERN LEARNED — ಇದರಿಂದ ಕಲಿತದ್ದು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Pattern Name: Segment-wise In-Place Reversal (two pointers)

  Ee pattern yaavaaga use maadabeeku?
  → "Reverse CONTENT within boundaries, but keep boundary ORDER
     unchanged" type problems — the opposite half of "reverse
     ORDER, keep content correct" (#151)
  → Any "reverse each chunk between delimiters" task

  Idee pattern beere problemsalli kaanisatte:
  → Reverse Words in a Given String #151 (previous problem — the
     mirror-image task: reverse word ORDER, keep letters correct)
  → Reverse String II #541 (reverse every k characters — same
     segment-reversal idea, fixed-size chunks instead of words)

  Next time intaha problem bandre naanu modalu idannu think maadtene:
  → "Reverse ORDER matra bekagidre → #151 style (reverse-all +
     reverse-each-part). Reverse CONTENT matra bekagidre, order
     hage ide beku antadre → seedha ide problem style — just
     reverse each segment in place, order touch madabeda!"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🗣️ SECTION 11 — INTERVIEWALLI HEGE EXPLAIN MAADABEEKU
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  1. Understand:
     "Reverse the characters WITHIN each word, but keep the
      words in their original order and spacing untouched."

  2. Brute force:
     "split(' ') → reverse each word with slicing → join with
      spaces. O(n), but hides the swap mechanics."

  3. Optimize:
     "Since word order doesn't change, I don't need the full
      reverse-all step from #151 — just walk the string, find
      each word's [start, end) boundary via spaces, and reverse
      that segment in place with two pointers."

  4. Code:
     "Convert to a char list. Track word start; on hitting a
      space or end-of-string, reverse chars[start:end] with a
      two-pointer swap, then advance start past the space."

  5. Complexity:
     "Time O(n) — single pass, each char touched a constant
      number of times. Space O(n) in Python (immutable strings),
      O(1) extra on a true mutable array."

  Mukhya: this is the exact mirror of #151 — reverse ORDER vs
          reverse CONTENT are two different halves of the same
          reverse-all-then-fix-parts toolkit!
"""


# ═══════════════════════════════════════════════════════════════════
# BRUTE FORCE — O(n) Time | O(n) Space (split / reverse / join)
# ═══════════════════════════════════════════════════════════════════
def reverse_every_word_brute(s):
    """
    Idu modala aaloochane — space prakara split madi, prati
    word na slicing bhalasi reverse madi, join madu
    """
    return " ".join(word[::-1] for word in s.split(" "))


# ═══════════════════════════════════════════════════════════════════
# OPTIMAL — O(n) Time | O(n) Space (two-pointer in-place reverse)
# ═══════════════════════════════════════════════════════════════════
def reverse_every_word(s):
    """
    Idu final answer — prati word na [start,end) boundary
    kandukondu, two pointers bhalasi in-place reverse madu
    """
    chars = list(s)
    n = len(chars)

    def reverse(left, right):
        while left < right:
            chars[left], chars[right] = chars[right], chars[left]
            left += 1
            right -= 1

    start = 0
    for end in range(n + 1):
        if end == n or chars[end] == ' ':
            reverse(start, end - 1)
            start = end + 1

    return "".join(chars)


# ═══════════════════════════════════════════════════════════════════
# TEST CASES
# ═══════════════════════════════════════════════════════════════════
if __name__ == "__main__":
    # Test 1 — Basic
    assert reverse_every_word("Let's take LeetCode contest") == "s'teL ekat edoCteeL tsetnoc"

    # Test 2 — Two words
    assert reverse_every_word("God Ding") == "doG gniD"

    # Test 3 — Single word
    assert reverse_every_word("hello") == "olleh"

    # Test 4 — Single-character words
    assert reverse_every_word("a b c") == "a b c"

    # Test 5 — Mix of palindromic and non-palindromic words
    assert reverse_every_word("level up") == "level pu"

    # Cross-check: brute force must agree on all of the above
    assert reverse_every_word_brute("Let's take LeetCode contest") == "s'teL ekat edoCteeL tsetnoc"
    assert reverse_every_word_brute("God Ding") == "doG gniD"
    assert reverse_every_word_brute("hello") == "olleh"
    assert reverse_every_word_brute("a b c") == "a b c"
    assert reverse_every_word_brute("level up") == "level pu"

    print("All tests passed!")
