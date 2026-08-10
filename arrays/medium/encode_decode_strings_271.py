"""
╔══════════════════════════════════════════════════════════════════╗
║  ENCODE AND DECODE STRINGS                                       ║
║  LeetCode #271  |  Difficulty: Medium  |  Topic: Arrays/Strings ║
║  Link: https://leetcode.com/problems/encode-and-decode-strings/ ║
╚══════════════════════════════════════════════════════════════════╝

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📘 SECTION 1 — PROBLEM UNDERSTANDING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Design an algorithm to encode a list of strings into a single
  string. The encoded string is then sent over the network and
  decoded back to the original list of strings.
  The tricky part: strings can contain ANY character including
  the delimiter you choose — so a simple separator like ',' fails!

  Input  (encode): strs = list of strings
  Output (encode): single encoded string

  Input  (decode): encoded single string
  Output (decode): original list of strings

  Example 1 — basic:
    Input : ["hello", "world"]
    Encoded: "5#hello5#world"
    Decoded: ["hello", "world"]
    Why?  : length prefix tells us exactly where each word ends

  Example 2 — slightly tricky (delimiter in string):
    Input : ["hello#world", "test"]
    Encoded: "11#hello#world4#test"
    Decoded: ["hello#world", "test"]
    Why?  : length prefix = 11 tells us to read 11 chars,
            so the '#' inside the string is not confused as delimiter

  Constraints:
    - 0 <= strs.length <= 200
    - 0 <= strs[i].length <= 200
    - strs[i] can contain ANY Unicode character

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🧠 SECTION 2 — KANGLISH THINKING — ಹೇಗೆ ಯೋಚಿಸಬೇಕು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  Problem odi aada mele namma brain enu think maadabeeku:

  ಹಂತ 1 — Problem ಅರ್ಥ ಮಾಡಿಕೊಳ್ಳಿ
  ┌─────────────────────────────────────────────────────────┐
  │  Input ಏನು ಕೊಡ್ತಾರೆ?  →  strings list                 │
  │  Output ಏನು ಬೇಕು?     →  encode: one string,          │
  │                           decode: original list back    │
  │  Constraints ಏನಿದೆ?   →  strings ಲ್ಲಿ ANY character   │
  │                           ಇರಬಹುದು — delimiter ಕೆಲಸ    │
  │                           ಮಾಡಲ್ಲ!                      │
  └─────────────────────────────────────────────────────────┘

  ಹಂತ 2 — ನನಗೆ ಗೊತ್ತಿರೋ simple way ಏನು?
  →  ',' or '#' ಯಾವುದಾದ್ರೂ delimiter use ಮಾಡೋಣ
  →  ಆದರೆ ಇದು work ಆಗಲ್ಲ ಯಾಕೆ?
     String ಲ್ಲೇ '#' ಇದ್ರೆ decode ತಪ್ಪಾಗತ್ತೆ!
     "he#llo" → split by '#' → ["he", "llo"] → WRONG!

  ಹಂತ 3 — Better way ಹೇಗೆ ಯೋಚಿಸುವುದು?
  →  "Delimiter ambiguity ತಪ್ಪಿಸಲು ಏನು ಮಾಡಬಹುದು?"
  →  Length prefix! ಪ್ರತಿ word ಮೊದಲು length ಹೇಳಿದ್ರೆ
     exactly ಎಷ್ಟು characters read ಮಾಡಬೇಕು ಅಂತ ಗೊತ್ತಾಗತ್ತೆ
  →  Format: "5#hello5#world" → length + '#' + word
  →  ಇದರಿಂದ ನಾವು Length Prefix Encoding use ಮಾಡಬಹuದು!

  ಹಂತ 4 — Technique ಯಾಕೆ ಇಲ್ಲಿ ಕೆಲಸ ಮಾಡುತ್ತೆ?
  →  Length ಮೊದಲು ಓದಿದ್ರೆ exactly ಆ many chars skip ಮಾಡಬಹুದು
  →  String ಲ್ಲಿ '#' ಇದ್ರೂ confuse ಆಗಲ್ಲ — length tells the truth
  →  '#' separator ಆಗಿ use ಮಾಡಿದ್ದು length ಮತ್ತು word ನ separate ಮಾಡಲು

  💡 Interview ನಲ್ಲಿ ಹೇಗೆ ಮಾತಾಡಬೇಕು:
  →  "Simple delimiter fails because strings can contain any char"
  →  "Length prefix solves it — encode as len(s) + '#' + s"
  →  "Decode: read until '#', get length, read that many chars"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🏷️ SECTION 3 — TECHNIQUE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Primary   : Length Prefix Encoding
  Secondary : String/Design

  WHY Length Prefix?
  → Any delimiter-based approach fails with arbitrary characters
  → Length prefix is unambiguous — number is always numeric
  → Decode knows exactly how many chars to read — no guessing

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 💡 SECTION 4 — INTUITION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  The challenge: any character can appear in the string, so no
  single character can safely serve as a delimiter.

  Solution: instead of marking END of word, mark the LENGTH of word.
  If I know the length upfront, I can read exactly that many chars —
  whatever they are — without ambiguity.

  The journey from brute to optimal:
    Brute thought   →  Join with a special delimiter like ','
    Problem with it →  Strings can CONTAIN the delimiter — breaks!
    Better question →  "What information removes all ambiguity?"
    Insight         →  Length of string! Read length, then read
                       exactly that many chars — works for any content
    Optimal         →  Format: "len#string" for each word

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🐢 SECTION 5 — APPROACH 1 — BRUTE FORCE (Naive Delimiter)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    Join strings with a rare delimiter like chr(257) (non-ASCII)
    or escape the delimiter inside strings before joining.

  Pseudocode:
    encode: return DELIM.join(strs)
    decode: return s.split(DELIM)

  Time  : O(n × k)  →  Why: n strings each of length k
  Space : O(n × k)  →  Why: encoded string total length

  ಇದು ಯಾಕೆ ಸಾಕಾಗಲ್ಲ?
    → "Any Unicode character" constraint iddare — even chr(257)
       can appear in string! Not truly safe. Escaping = complex.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🚀 SECTION 6 — APPROACH 2 — OPTIMAL (Length Prefix)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    ENCODE: for each string, prepend its length + '#' separator
    DECODE: read until '#' to get length, then read that many chars

  Key steps:
    Encode:
      1. For each s in strs: add str(len(s)) + '#' + s
      2. Join all → single encoded string

    Decode:
      1. i = 0 (pointer into encoded string)
      2. Find '#' from position i → extract length
      3. Read length chars after '#' → that is the word
      4. Move i forward, repeat until end

  ಕನ್ನಡದಲ್ಲಿ ಒಂದು ಸಲ ಹೇಳಿ:
    → "Encode: ಪ್ರತಿ word ಮೊದಲು length + '#' + word ಬರೆ.
       Decode: '#' ವರೆಗೆ ಓದಿ length ತಿಳ್ಕೋ, ಆ ಮೇಲೆ
       exactly ಅಷ್ಟು characters ಓದು — word ಸಿಗತ್ತೆ!
       Length ಸುಳ್ಳು ಹೇಳಲ್ಲ — content ಏನೇ ಇರಲಿ!"

  Time  : O(n × k)  →  Why: encode/decode each char once
  Space : O(n × k)  →  Why: encoded string length = sum of all

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🔍 SECTION 7 — DRY RUN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Input: ["hello", "world"]

  ENCODE:
    "hello" → len=5 → "5#hello"
    "world" → len=5 → "5#world"
    encoded = "5#hello5#world"

  DECODE: s = "5#hello5#world"
    i=0 → find '#' from i → '#' at index 1 → length = s[0:1] = "5" = 5
    word = s[2 : 2+5] = s[2:7] = "hello"
    i = 2 + 5 = 7

    i=7 → find '#' from 7 → '#' at index 8 → length = s[7:8] = "5" = 5
    word = s[9 : 9+5] = s[9:14] = "world"
    i = 9 + 5 = 14 → end of string

    result = ["hello", "world"] ✓

  ಇನ್ನೊಂದು example — '#' inside string:
  Input: ["he#llo", "world"]

  ENCODE:
    "he#llo" → len=6 → "6#he#llo"
    "world"  → len=5 → "5#world"
    encoded = "6#he#llo5#world"

  DECODE: s = "6#he#llo5#world"
    i=0 → '#' at index 1 → length=6
    word = s[2:8] = "he#llo"   ← '#' inside is safely included!
    i = 8

    i=8 → '#' at index 9 → length=5
    word = s[10:15] = "world"
    result = ["he#llo", "world"] ✓

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 ⚠️ SECTION 8 — EDGE CASES — ಇವನ್ನ ಮರೆಯಬೇಡ!
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  ✓ Empty list?               →  [] → encode="" → decode=[]
  ✓ Empty string in list?     →  [""] → "0#" → [""]
  ✓ String with '#' inside?   →  ["a#b"] → "3#a#b" → ["a#b"] ✓
  ✓ String with digits?       →  ["123"] → "3#123" → ["123"] ✓
  ✓ Single character strings? →  ["a","b"] → "1#a1#b" → ["a","b"] ✓
  ✓ Very long strings?        →  length can be multi-digit like "100#..."

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📊 SECTION 9 — COMPLEXITY SUMMARY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                Time        Space
  Naive Delim   O(n × k)    O(n × k)   fragile
  Length Prefix O(n × k)    O(n × k)   ← use this ✅

  Time yaake O(n × k)?  → n strings, each of avg length k, one pass
  Space yaake O(n × k)? → encoded string = sum of all string lengths

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🎯 SECTION 10 — PATTERN LEARNED — ಇದರಿಂದ ಕಲಿತದ್ದು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Pattern Name: Length Prefix Encoding

  Ee pattern yaavaaga use maadabeeku?
  → Serialize/deserialize data with arbitrary content
  → When no safe delimiter exists
  → Network protocol design, file format design

  Idee pattern beere problemsalli kaanisatte:
  → Serialize and Deserialize Binary Tree #297
  → Serialize and Deserialize BST #449
  → Design-based questions about data serialization

  Next time intaha problem bandre naanu modalu idannu think maadtene:
  → "Delimiter use maadidre fail aagatte → length prefix use maadu!
     len(s) + '#' + s → decode alli '#' find maadi length odi,
     exactly aastu chars read maadu — safe and simple!"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🗣️ SECTION 12 — INTERVIEWALLI HEGE EXPLAIN MAADABEEKU
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  1. Understand:
     "Encode a list of strings to one string and decode it back.
      Strings can contain any character."

  2. Brute force:
     "Simple delimiter like comma fails — strings can contain commas."

  3. Optimize:
     "Use length prefix: for each string, encode as len(s)+'#'+s.
      During decode, read until '#' to get length, then read
      exactly that many characters. Works for any content."

  4. Code:
     "Encode: join all len+#+ string.
      Decode: pointer i, find '#', read length, slice word, advance."

  5. Complexity:
     "Time O(n×k) — one pass each direction.
      Space O(n×k) — total length of encoded string."

  Mukhya: summane kuutu code bareyabeda!
          Length prefix trick — elegant and interviewer loves it!
          Real world protocol design concept — shows depth!
"""


# ═══════════════════════════════════════════════════════════════════
# OPTIMAL — O(n × k) Time | O(n × k) Space
# Length Prefix Encoding — works for any characters
# ═══════════════════════════════════════════════════════════════════
class Codec:

    def encode(self, strs):
        """
        Idu encode — length + '#' + word format use maadu
        ["hello","world"] → "5#hello5#world"
        """
        encoded = ""
        for s in strs:
            encoded += str(len(s)) + '#' + s
        return encoded

    def decode(self, s):
        """
        Idu decode — '#' find maadi length odi, word extract maadu
        "5#hello5#world" → ["hello","world"]
        """
        result = []
        i = 0

        while i < len(s):
            # find the '#' separator from current position
            j = i
            while s[j] != '#':
                j += 1

            # extract length
            length = int(s[i:j])

            # extract word (j+1 skips the '#')
            word = s[j + 1 : j + 1 + length]
            result.append(word)

            # move pointer past this word
            i = j + 1 + length

        return result


# ═══════════════════════════════════════════════════════════════════
# TEST CASES
# ═══════════════════════════════════════════════════════════════════
if __name__ == "__main__":
    codec = Codec()

    # Test 1 — Basic
    strs = ["hello", "world"]
    assert codec.decode(codec.encode(strs)) == strs

    # Test 2 — String with '#' inside
    strs = ["he#llo", "world"]
    assert codec.decode(codec.encode(strs)) == strs

    # Test 3 — Empty string in list
    strs = [""]
    assert codec.decode(codec.encode(strs)) == strs

    # Test 4 — Empty list
    strs = []
    assert codec.decode(codec.encode(strs)) == strs

    # Test 5 — Single character strings
    strs = ["a", "b", "c"]
    assert codec.decode(codec.encode(strs)) == strs

    # Test 6 — String with digits and special chars
    strs = ["123", "abc#def", "hello world"]
    assert codec.decode(codec.encode(strs)) == strs

    print("All tests passed!")
