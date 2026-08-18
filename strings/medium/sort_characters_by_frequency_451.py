"""
╔════════════════════════════════════════════════════════════════════╗
║  SORT CHARACTERS BY FREQUENCY                                      ║
║  LeetCode #451  |  Difficulty: Medium  |  Topic: Strings/HashMap   ║
║  Link: https://leetcode.com/problems/sort-characters-by-frequency/ ║
╚════════════════════════════════════════════════════════════════════╝

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📘 SECTION 1 — PROBLEM UNDERSTANDING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Given a string `s`, sort it in DECREASING order based on the
  frequency of characters, and return the sorted string. If
  there is more than one valid arrangement, any of them is
  acceptable.

  Input : s = a string
  Output: string with the same characters, rearranged so more
          frequent characters come before less frequent ones

  Example 1 — basic:
    Input : s = "tree"
    Output: "eert"
    Why?  : 'e' appears twice, 'r' and 't' appear once each —
            both 'e's must come before 'r' and 't' (their
            relative order doesn't matter: "eetr" is also valid)

  Example 2 — slightly tricky (a tie in frequency):
    Input : s = "cccaaa"
    Output: "aaaccc" (or "cccaaa" — both valid)
    Why?  : 'c' and 'a' are tied at 3 occurrences each — any
            order between the two GROUPS is fine, as long as
            each group's characters stay together

  Example 3 — case sensitivity matters:
    Input : s = "Aabb"
    Output: "bbAa" (or "bbaA")
    Why?  : 'A' and 'a' are DIFFERENT characters (case-sensitive)
            — 'b' has frequency 2 and must come first; 'A' and
            'a' are tied at 1 each

  Constraints:
    - 1 <= s.length <= 5 * 10^5
    - s consists of uppercase/lowercase English letters and/or
      digits

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🧠 SECTION 2 — KANGLISH THINKING — ಹೇಗೆ ಯೋಚಿಸಬೇಕು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  Problem odi aada mele namma brain enu think maadabeeku:

  ಹಂತ 1 — Problem ಅರ್ಥ ಮಾಡಿಕೊಳ್ಳಿ
  ┌─────────────────────────────────────────────────────────┐
  │  Input ಏನು ಕೊಡ್ತಾರೆ?  →  characters ಇರೋ string          │
  │  Output ಏನು ಬೇಕು?     →  ಅದೇ characters, ಆದ್ರೆ frequency │
  │                           ಜಾಸ್ತಿ ಇರೋದು ಮೊದಲು ಬರೋ ಹಾಗೆ    │
  │  Constraints ಏನಿದೆ?   →  ties ಇದ್ರೆ ಯಾವುದೇ order ಸಾಕು    │
  └─────────────────────────────────────────────────────────┘

  ಹಂತ 2 — ಇದನ್ನ previous problem (#242 Valid Anagram) ಜೊತೆ
           connect ಮಾಡಿ ನೋಡಿ!
  →  ಅಲ್ಲಿ ಕೂಡ frequency counter ಬಳಸಿದ್ವಿ — ಇಲ್ಲಿ ಕೂಡ ಅದೇ
     counting idea ಶುರುವಾಗುತ್ತೆ
  →  ಆದ್ರೆ ಇಲ್ಲಿ counts ಸಿಕ್ಕ ಮೇಲೆ, ಆ counts ಪ್ರಕಾರ characters
     ಅನ್ನ ARRANGE ಮಾಡಬೇಕು (sort ಮಾಡಬೇಕು)

  ಹಂತ 3 — ಮೊದಲ simple idea ಏನು?
  →  ಪ್ರತಿ character ಗೆ frequency count ಮಾಡಿ (hashmap)
  →  original string ಅನ್ನ, ಪ್ರತಿ character ರ frequency ಅನ್ನ
     KEY ಆಗಿ ಬಳಸಿ, decreasing order ನಲ್ಲಿ sort ಮಾಡಿ

  ಹಂತ 4 — Better way (sort ಬೇಡ) ಹೇಗೆ?
  →  "Frequency values ಯಾವಾಗಲೂ 1 ಇಂದ n ವರೆಗೆ ಮಾತ್ರ ಇರುತ್ತೆ,
      string length n ಮೀರಲ್ಲ" ಅಂತ ಗಮನಿಸಿ
  →  "ಹೀಗಿದ್ರೆ, comparison sort (O(n log n)) ಬದಲು, BUCKET
      SORT ಬಳಸಬಹುದಲ್ವಾ?" — frequency value ಅನ್ನೇ bucket
      INDEX ಆಗಿ ಬಳಸಿ!
  →  Bucket[i] = frequency i ಇರೋ ಎಲ್ಲಾ characters ರ list
  →  ಕೊನೆಗೆ buckets ಅನ್ನ ಹೆಚ್ಚಿನ frequency ಇಂದ ಕಡಿಮೆ frequency
     ಗೆ ಓಡಾಡಿ result build ಮಾಡಿದ್ರೆ ಆಯ್ತು — comparison ಬೇಡ!

  ಹಂತ 5 — Technique ಯಾಕೆ ಇಲ್ಲಿ ಕೆಲಸ ಮಾಡುತ್ತೆ?
  →  Frequency values BOUNDED ಆಗಿರೋದ್ರಿಂದ (1 ರಿಂದ n), bucket
     sort ಅನ್ನ apply ಮಾಡಬಹುದು — ಇದು comparison-based sort ಗಿಂತ
     ವೇಗ (O(n log n) ಬದಲು O(n))

  💡 Interview ನಲ್ಲಿ ಹೇಗೆ ಮಾತಾಡಬೇಕು:
  →  "Count character frequencies with a hashmap first"
  →  "Since frequencies are bounded by string length, use bucket
      sort: index buckets by frequency value directly"
  →  "Walk buckets from highest frequency to lowest, repeating
      each character by its count to build the result"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🏷️ SECTION 3 — TECHNIQUE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Primary   : Bucket Sort (frequency as bucket index)
  Secondary : HashMap frequency counting + comparison sort

  WHY Bucket Sort over Comparison Sort?
  → Frequencies are bounded integers (1 to n), which is exactly
    the situation bucket/counting sort is built for — we can
    place each character directly into the bucket matching its
    count, skipping O(n log n) comparisons entirely.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 💡 SECTION 4 — INTUITION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  The key insight: we don't actually need to COMPARE characters
  against each other to sort them by frequency — since frequency
  is just an integer from 1 to n, we can use it directly as an
  array index (bucket sort / counting sort style). Characters
  land in the right bucket automatically; we just read buckets
  off from highest index to lowest.

  The journey from brute to optimal:
    Brute thought   →  Count frequencies with a hashmap, then
                       use Python's sorted() with a custom key
                       (negative frequency) to reorder the string
    Problem with it →  sorted() is a comparison sort, O(n log n),
                       even though frequency values are tightly
                       bounded and don't need general comparison
    Better question →  "Since frequency is bounded by n, can I
                       skip comparisons and place characters
                       directly by frequency value?"
    Insight         →  Bucket sort: bucket[freq] holds all chars
                       with that exact frequency
    Optimal         →  Count (O(n)) + bucket fill (O(k)) + bucket
                       read + expand (O(n)) = O(n) overall

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🐢 SECTION 5 — APPROACH 1 — BRUTE FORCE (count + comparison sort)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    Count each character's frequency with a hashmap. Then sort
    the ENTIRE string's characters using that frequency as the
    sort key, descending.

  Pseudocode:
    step 1: freq = count occurrences of every character in s
    step 2: return "".join(sorted(s, key=lambda c: -freq[c]))

  Time  : O(n log n)  →  Why: sorting n characters dominates,
                              even though only k ≤ n distinct
                              frequency VALUES actually exist
  Space : O(n)         →  Why: sorted() builds a new list of
                              length n, plus the frequency map

  ಇದು ಯಾಕೆ ಸಾಕಾಗಲ್ಲ?
    → Correct, but pays comparison-sort cost even though the
      sort KEY (frequency) only ranges over a small bounded set
      of integers — a perfect setup for bucket sort instead.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🚀 SECTION 6 — APPROACH 2 — OPTIMAL (Bucket Sort)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    Count frequencies with a hashmap. Create `n + 1` buckets
    (index 0 to n), where bucket[i] holds every character whose
    frequency is exactly `i`. Then walk the buckets from the
    highest index down to 1, and for every character found,
    append it to the result repeated `i` times.

  Key steps:
    1. freq = {} → count each character's occurrences
    2. buckets = [[] for _ in range(len(s) + 1)]
    3. for char, count in freq.items(): buckets[count].append(char)
    4. result = []
    5. for count in range(len(s), 0, -1):
    6.   for char in buckets[count]:
    7.     result.append(char * count)
    8. return "".join(result)

  ಕನ್ನಡದಲ್ಲಿ ಒಂದು ಸಲ ಹೇಳಿ:
    → "ಪ್ರತಿ character ಗೆ frequency count ಮಾಡು. ಆಮೇಲೆ frequency
       VALUE ಅನ್ನೇ bucket index ಆಗಿ ಬಳಸಿ, characters ಅನ್ನ ಸರಿಯಾದ
       bucket ಗೆ ಹಾಕು. ಕೊನೆಗೆ ಹೆಚ್ಚಿನ frequency bucket ಇಂದ
       ಕಡಿಮೆ frequency bucket ಗೆ ಓಡಾಡಿ, ಪ್ರತಿ character ಅನ್ನ
       ಅದರ count ಸಲ repeat ಮಾಡಿ result ಗೆ ಸೇರಿಸು!"

  Time  : O(n)  →  Why: counting is O(n), filling buckets is
                        O(k) ≤ O(n), and reading buckets while
                        expanding characters touches each of the
                        n characters exactly once overall
  Space : O(n)  →  Why: buckets array (n+1 slots) + result string
                        of length n

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🔍 SECTION 7 — DRY RUN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Input: s = "tree"

  Step 1 — count frequencies: {'t': 1, 'r': 1, 'e': 2}

  Step 2 — fill buckets (size 5, index 0..4):
    bucket[1] = ['t', 'r']
    bucket[2] = ['e']
    (bucket[0], [3], [4] stay empty)

  Step 3 — read buckets from index 4 down to 1:
    index 4: empty
    index 3: empty
    index 2: ['e'] → append "e" * 2 = "ee"
    index 1: ['t', 'r'] → append "t"*1="t", "r"*1="r"

  Result: "ee" + "t" + "r" = "eetr"  (a valid answer — "eert"
  from the canonical example is just as valid, order among
  tied/lower buckets doesn't matter)

  Output: "eetr" ✓ (any arrangement with both 'e's first is correct)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 ⚠️ SECTION 8 — EDGE CASES — ಇವನ್ನ ಮರೆಯಬೇಡ!
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  ✓ Single character "a"?          →  "a" — trivially itself
  ✓ All same character "aaaa"?     →  "aaaa" — one bucket only
  ✓ All distinct characters "abc"? →  any permutation is valid
                                       (all tied at frequency 1)
  ✓ Case sensitivity ("Aabb")?     →  'A' and 'a' are different
                                       characters — must NOT merge
  ✓ Digits mixed with letters?     →  treated as regular
                                       characters, same counting

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📊 SECTION 9 — COMPLEXITY SUMMARY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                        Time        Space
  Brute (comparison)    O(n log n)  O(n)
  Optimal (bucket sort) O(n)        O(n)   ← use this ✅

  Time yaake O(n)?  → Counting O(n), bucket fill O(k), bucket
                       read + string expansion touches each of
                       the n original characters exactly once
  Space yaake O(n)? → n+1 buckets plus the O(n) result string

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🎯 SECTION 10 — PATTERN LEARNED — ಇದರಿಂದ ಕಲಿತದ್ದು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Pattern Name: Bucket Sort by Bounded Frequency

  Ee pattern yaavaaga use maadabeeku?
  → Sort key (frequency, count, distance, etc.) BOUNDED integer
     range alli iddaga → comparison sort bittu bucket/counting
     sort try maadu — O(n log n) inda O(n) ge ilisabahudu
  → "Sort by count/frequency" family problems

  Idee pattern beere problemsalli kaanisatte:
  → Top K Frequent Elements #347 (same bucket-by-frequency idea,
     applied to array elements instead of characters)
  → Sort Array By Increasing Frequency (near-identical twin)
  → Valid Anagram #242 (previous problem — same frequency
     counting step, but no sorting/rearranging needed there)

  Next time intaha problem bandre naanu modalu idannu think maadtene:
  → "Frequency/count prakara sort madabekagidre, aa count value
     BOUNDED (n varge) ideyantadre → bucket sort try maadu!
     Comparison sort (O(n log n)) beku ansalla."

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🗣️ SECTION 11 — INTERVIEWALLI HEGE EXPLAIN MAADABEEKU
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  1. Understand:
     "Rearrange the string so characters with higher frequency
      appear before characters with lower frequency."

  2. Brute force:
     "Count frequencies with a hashmap, then use a comparison
      sort with frequency as the key. O(n log n)."

  3. Optimize:
     "Frequency is bounded between 1 and n, so I can use bucket
      sort: bucket[i] holds all characters with frequency i.
      Walk buckets from n down to 1 and expand each character by
      its count — no comparisons needed."

  4. Code:
     "Count into a hashmap. Fill n+1 buckets indexed by
      frequency. Iterate buckets high-to-low, appending
      char * count for everything found."

  5. Complexity:
     "Time O(n) — counting, bucket fill, and expansion are all
      linear. Space O(n) for buckets and the result."

  Mukhya: sort key bounded integer aagidre, comparison sort
          bittu bucket sort use maadu — classic O(n log n) → O(n)
          trick!
"""


# ═══════════════════════════════════════════════════════════════════
# BRUTE FORCE — O(n log n) Time | O(n) Space (count + comparison sort)
# ═══════════════════════════════════════════════════════════════════
def frequency_sort_brute(s):
    """
    Idu modala aaloochane — frequency count madi, aa count ge
    key aagi comparison sort use madu
    """
    freq = {}
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1

    return "".join(sorted(s, key=lambda c: -freq[c]))


# ═══════════════════════════════════════════════════════════════════
# OPTIMAL — O(n) Time | O(n) Space (bucket sort by frequency)
# ═══════════════════════════════════════════════════════════════════
def frequency_sort(s):
    """
    Idu final answer — frequency value ondu bucket index aagi
    bally madi, high count inda low count ge result build madu
    """
    freq = {}
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1

    buckets = [[] for _ in range(len(s) + 1)]
    for ch, count in freq.items():
        buckets[count].append(ch)

    result = []
    for count in range(len(s), 0, -1):
        for ch in buckets[count]:
            result.append(ch * count)

    return "".join(result)


# ═══════════════════════════════════════════════════════════════════
# TEST CASES
# ═══════════════════════════════════════════════════════════════════
def _char_counts(string):
    counts = {}
    for ch in string:
        counts[ch] = counts.get(ch, 0) + 1
    return counts


def _is_valid_frequency_sort(original, candidate):
    """A valid answer: same multiset of chars, non-increasing frequency order."""
    if _char_counts(original) != _char_counts(candidate):
        return False

    freq = _char_counts(original)
    prev_freq = float("inf")
    for ch in candidate:
        if freq[ch] > prev_freq:
            return False
        prev_freq = freq[ch]
    return True


if __name__ == "__main__":
    # Test 1 — Basic
    assert _is_valid_frequency_sort("tree", frequency_sort("tree"))

    # Test 2 — Tied frequencies
    assert _is_valid_frequency_sort("cccaaa", frequency_sort("cccaaa"))

    # Test 3 — Case sensitivity
    assert _is_valid_frequency_sort("Aabb", frequency_sort("Aabb"))

    # Test 4 — Single character
    assert _is_valid_frequency_sort("a", frequency_sort("a"))

    # Test 5 — All distinct characters
    assert _is_valid_frequency_sort("abc", frequency_sort("abc"))

    # Cross-check: brute force must also produce valid answers
    assert _is_valid_frequency_sort("tree", frequency_sort_brute("tree"))
    assert _is_valid_frequency_sort("cccaaa", frequency_sort_brute("cccaaa"))
    assert _is_valid_frequency_sort("Aabb", frequency_sort_brute("Aabb"))
    assert _is_valid_frequency_sort("a", frequency_sort_brute("a"))
    assert _is_valid_frequency_sort("abc", frequency_sort_brute("abc"))

    print("All tests passed!")
