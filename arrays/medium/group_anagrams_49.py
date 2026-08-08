"""
╔══════════════════════════════════════════════════════════════════╗
║  GROUP ANAGRAMS                                                  ║
║  LeetCode #49  |  Difficulty: Medium  |  Topic: Arrays/HashMap  ║
║  Link: https://leetcode.com/problems/group-anagrams/            ║
╚══════════════════════════════════════════════════════════════════╝

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📘 SECTION 1 — PROBLEM UNDERSTANDING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Given an array of strings, group all strings that are anagrams
  of each other together and return the groups.
  Two strings are anagrams if they have the same characters
  in the same frequency (order doesn't matter).

  Input : strs = list of strings
  Output: list of groups, each group = list of anagram strings

  Example 1 — basic:
    Input : ["eat","tea","tan","ate","nat","bat"]
    Output: [["eat","tea","ate"], ["tan","nat"], ["bat"]]
    Why?  : eat/tea/ate all have same chars {a,e,t}
            tan/nat have same chars {a,n,t}
            bat is alone {a,b,t}

  Example 2 — slightly tricky (empty string):
    Input : [""]
    Output: [[""]]
    Why?  : single empty string forms its own group

  Constraints:
    - 1 <= strs.length <= 10^4
    - 0 <= strs[i].length <= 100
    - strs[i] consists of lowercase English letters only

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🧠 SECTION 2 — KANGLISH THINKING — ಹೇಗೆ ಯೋಚಿಸಬೇಕು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  Problem odi aada mele namma brain enu think maadabeeku:

  ಹಂತ 1 — Problem ಅರ್ಥ ಮಾಡಿಕೊಳ್ಳಿ
  ┌─────────────────────────────────────────────────────────┐
  │  Input ಏನು ಕೊಡ್ತಾರೆ?  →  strings array               │
  │  Output ಏನು ಬೇಕು?     →  anagram strings ನ groups     │
  │                           ಆಗಿ group ಮಾಡಬೇಕು           │
  │  Constraints ಏನಿದೆ?   →  lowercase only, n=10^4       │
  └─────────────────────────────────────────────────────────┘

  ಹಂತ 2 — ನನಗೆ ಗೊತ್ತಿರೋ simple way ಏನು?
  →  ಪ್ರತಿ pair (i,j) compare ಮಾಡಿ anagram ಆ ಅಂತ check ಮಾಡೋಣ
  →  ಆದರೆ ಇದು slow ಯಾಕೆ?
     n=10^4, each string length=100 → O(n² × k) → TLE!

  ಹಂತ 3 — Better way ಹೇಗೆ ಯೋಚಿಸುವುದು?
  →  "Anagrams ಗೆ ಒಂದು common key ಏನಾದ್ರೂ ಇದ್ಯಾ?"
  →  YES! Sort ಮಾಡಿದ್ರೆ "eat", "tea", "ate" ಎಲ್ಲ "aet" ಆಗತ್ತೆ!
  →  Sorted string = key, HashMap ಲ್ಲಿ group ಮಾಡಬಹುದು!
  →  ಇದರಿಂದ ನಾವು HashMap + Sort Key use ಮಾಡಬಹুದು!

  ಹಂತ 4 — Technique ಯಾಕೆ ಇಲ್ಲಿ ಕೆಲಸ ಮಾಡುತ್ತೆ?
  →  Anagrams sort ಮಾಡಿದ್ರೆ identical ಆಗತ್ತೆ — perfect key!
  →  HashMap {sorted_str: [original strings]} group ಮಾಡತ್ತೆ
  →  Single pass ಲ್ಲಿ O(n × k log k) ಲ್ಲಿ solve ಆಗತ್ತೆ

  💡 Interview ನಲ್ಲಿ ಹೇಗೆ ಮಾತಾಡಬೇಕು:
  →  "Anagrams share the same sorted form — use that as HashMap key"
  →  "Brute force compares all pairs — O(n² × k), too slow"
  →  "Sort each string, group by sorted key — O(n × k log k)"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🏷️ SECTION 3 — TECHNIQUE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Primary   : HashMap → Sort Key Grouping
  Secondary : Frequency Count Key (alternative)

  WHY Sort Key?
  → All anagrams sort to the same string
  → That sorted string becomes a unique key
  → HashMap groups all strings with same key together

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 💡 SECTION 4 — INTUITION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Anagrams are just rearrangements of the same characters.
  If we sort any anagram, they all produce the same string.
  "eat" → "aet", "tea" → "aet", "ate" → "aet" — same key!

  The journey from brute to optimal:
    Brute thought   →  Compare every pair, check if anagram
    Problem with it →  O(n² × k) — TLE for n=10^4
    Better question →  "What do all anagrams have in common?"
    Insight         →  Sorted form is identical for all anagrams
    Optimal         →  HashMap with sorted string as key O(n × k log k)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🐢 SECTION 5 — APPROACH 1 — BRUTE FORCE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    Compare every pair of strings. If they are anagrams,
    group them together. Track which strings already grouped.

  Pseudocode:
    step 1: visited = set()
    step 2: for each i, if not visited:
    step 3:   group = [strs[i]]
    step 4:   for each j > i: if anagram(i,j) → add to group
    step 5:   result.append(group)

  Time  : O(n² × k)  →  Why: n² pairs, each comparison O(k)
  Space : O(n × k)   →  Why: storing all strings in groups

  ಇದು ಯಾಕೆ ಸಾಕಾಗಲ್ಲ?
    → n=10^4, k=100 → 10^10 operations → TLE aagatte

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🚀 SECTION 6 — APPROACH 2 — OPTIMAL (Sort Key)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    Sort each string to get its key. All anagrams produce the
    same key. Group strings by their sorted key using a HashMap.

  Key steps:
    1. HashMap: {sorted_string: [list of original strings]}
    2. For each string, sort it → get key
    3. Append original string to HashMap[key]
    4. Return all values of HashMap

  ಕನ್ನಡದಲ್ಲಿ ಒಂದು ಸಲ ಹೇಳಿ:
    → "ಪ್ರತಿ string sort ಮಾಡು → key ಸಿಗತ್ತೆ. HashMap ಲ್ಲಿ
       key → [strings] ಆಗಿ group ಮಾಡು. Same key = same anagram group.
       ಕೊನೆಗೆ HashMap values return ಮಾಡು!"

  Time  : O(n × k log k)  →  Why: n strings, each sorted in k log k
  Space : O(n × k)        →  Why: storing all strings in HashMap

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🚀 SECTION 7 — APPROACH 3 — OPTIMAL V2 (Frequency Count Key)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    Instead of sorting, use character frequency count as key.
    A tuple of 26 counts uniquely identifies an anagram group.
    Avoids sorting cost → O(n × k) instead of O(n × k log k)

  Key steps:
    1. For each string, build count array of size 26
    2. Convert to tuple → use as HashMap key
    3. Group strings by this tuple key

  ಕನ್ನಡದಲ್ಲಿ ಒಂದು ಸಲ ಹೇಳಿ:
    → "Sort ಬದಲು 26 letters frequency count tuple ಮಾಡು.
       Same anagrams = same counts = same tuple key.
       O(n×k) — sort ಗಿಂತ faster!"

  Time  : O(n × k)   →  Why: n strings, each counted in O(k)
  Space : O(n × k)   →  Why: storing all strings in HashMap

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🔍 SECTION 8 — DRY RUN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Input: ["eat","tea","tan","ate","nat","bat"]

  "eat" → sorted → "aet"  → map={"aet":["eat"]}
  "tea" → sorted → "aet"  → map={"aet":["eat","tea"]}
  "tan" → sorted → "ant"  → map={"aet":["eat","tea"], "ant":["tan"]}
  "ate" → sorted → "aet"  → map={"aet":["eat","tea","ate"], "ant":["tan"]}
  "nat" → sorted → "ant"  → map={"aet":[...], "ant":["tan","nat"]}
  "bat" → sorted → "abt"  → map={"aet":[...], "ant":[...], "abt":["bat"]}

  Output: [["eat","tea","ate"], ["tan","nat"], ["bat"]] ✓

  ಇನ್ನೊಂದು example — single empty string:
  Input: [""]
  "" → sorted → ""  → map={"": [""]}
  Output: [[""]] ✓

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 ⚠️ SECTION 9 — EDGE CASES — ಇವನ್ನ ಮರೆಯಬೇಡ!
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  ✓ Empty string?          →  [""] → [[""]] works fine
  ✓ Single string?         →  ["abc"] → [["abc"]]
  ✓ All same anagrams?     →  ["abc","bca","cab"] → [["abc","bca","cab"]]
  ✓ No anagrams at all?    →  ["abc","def"] → [["abc"],["def"]]
  ✓ Single character strs? →  ["a","b","a"] → [["a","a"],["b"]]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📊 SECTION 10 — COMPLEXITY SUMMARY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                  Time            Space
  Brute Force     O(n² × k)       O(n × k)
  Sort Key        O(n × k log k)  O(n × k)   ← good ✅
  Frequency Key   O(n × k)        O(n × k)   ← best ✅

  Time yaake O(n × k log k)? → n strings, each sort costs k log k
  Space yaake O(n × k)?      → HashMap stores all strings

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🎯 SECTION 11 — PATTERN LEARNED — ಇದರಿಂದ ಕಲಿತದ್ದು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Pattern Name: HashMap Sort Key Grouping

  Ee pattern yaavaaga use maadabeeku?
  → "Group elements that are transformations of each other"
  → Need a canonical form that all variants share
  → Sort or frequency count gives that canonical form

  Idee pattern beere problemsalli kaanisatte:
  → Valid Anagram #242 (simpler version — just check two strings)
  → Find All Anagrams in String #438 (sliding window + anagram)
  → Group Shifted Strings (shift all chars by same amount)

  Next time intaha problem bandre naanu modalu idannu think maadtene:
  → "Group maadabekittu → common key enu? → sort maadu,
     HashMap alli group maadu — O(n k log k) alli solve!"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🗣️ SECTION 12 — INTERVIEWALLI HEGE EXPLAIN MAADABEEKU
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  1. Understand:
     "Group all strings that are anagrams of each other."

  2. Brute force:
     "Compare every pair — O(n² × k), TLE for large inputs."

  3. Optimize:
     "Key insight: all anagrams sort to the same string.
      Use sorted string as HashMap key to group them."

  4. Code:
     "defaultdict(list), for each string sort it, append
      original to HashMap[sorted_key], return values."

  5. Complexity:
     "Time O(n × k log k) — n strings each sorted in k log k.
      Space O(n × k) — storing all strings."

  Mukhya: summane kuutu code bareyabeda!
          Sort key trick — simple but very elegant solution!
"""

from collections import defaultdict


# ═══════════════════════════════════════════════════════════════════
# BRUTE FORCE — O(n² × k) Time | O(n × k) Space
# ═══════════════════════════════════════════════════════════════════
def group_anagrams_brute(strs):
    """Idu modala aaloochane — compare every pair O(n²)"""
    n = len(strs)
    visited = [False] * n
    result = []

    for i in range(n):
        if visited[i]:
            continue
        group = [strs[i]]
        visited[i] = True
        for j in range(i + 1, n):
            if not visited[j] and sorted(strs[i]) == sorted(strs[j]):
                group.append(strs[j])
                visited[j] = True
        result.append(group)

    return result


# ═══════════════════════════════════════════════════════════════════
# OPTIMAL V1 — O(n × k log k) Time | O(n × k) Space (Sort Key)
# ═══════════════════════════════════════════════════════════════════
def group_anagrams(strs):
    """Idu final answer — sorted string as HashMap key"""
    groups = defaultdict(list)

    for s in strs:
        key = ''.join(sorted(s))    # "eat" → "aet"
        groups[key].append(s)

    return list(groups.values())


# ═══════════════════════════════════════════════════════════════════
# OPTIMAL V2 — O(n × k) Time | O(n × k) Space (Frequency Key)
# ═══════════════════════════════════════════════════════════════════
def group_anagrams_v2(strs):
    """Even faster — frequency count tuple as key, no sorting"""
    groups = defaultdict(list)

    for s in strs:
        count = [0] * 26
        for ch in s:
            count[ord(ch) - ord('a')] += 1
        key = tuple(count)          # (1,0,0,...1,...1,...) unique per anagram group
        groups[key].append(s)

    return list(groups.values())


# ═══════════════════════════════════════════════════════════════════
# TEST CASES
# ═══════════════════════════════════════════════════════════════════
if __name__ == "__main__":
    # Test 1 — Basic (sort output for comparison)
    result = group_anagrams(["eat","tea","tan","ate","nat","bat"])
    result_sorted = sorted([sorted(g) for g in result])
    assert result_sorted == [["bat"], ["ate","eat","tea"], ["nat","tan"]]

    # Test 2 — Empty string
    assert group_anagrams([""]) == [[""]]

    # Test 3 — Single char
    assert group_anagrams(["a"]) == [["a"]]

    # Test 4 — No anagrams
    result = group_anagrams(["abc", "def"])
    assert len(result) == 2

    print("All tests passed!")

