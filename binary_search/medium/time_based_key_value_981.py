"""
╔══════════════════════════════════════════════════════════════════╗
║  TIME BASED KEY-VALUE STORE                                      ║
║  LeetCode #981  |  Difficulty: Medium  |  Topic: Binary Search  ║
║  Link: https://leetcode.com/problems/time-based-key-value-store/ ║
╚══════════════════════════════════════════════════════════════════╝

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📘 SECTION 1 — PROBLEM UNDERSTANDING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Design a time-based key-value data structure that can store
  multiple values for the same key at different timestamps and
  retrieve the key's value at a certain timestamp.

  Implement TimeMap class:
    set(key, value, timestamp): stores key→value at timestamp
    get(key, timestamp): returns value stored at the largest
                         timestamp <= given timestamp
                         returns "" if no such timestamp exists

  Input : set/get operations with key, value, timestamp
  Output: get returns most recent value at or before timestamp

  Example 1 — basic:
    set("foo","bar",1) → store foo=bar at t=1
    get("foo",1)       → "bar"   (exact match t=1)
    get("foo",3)       → "bar"   (latest at or before t=3 is t=1)
    set("foo","bar2",4)→ store foo=bar2 at t=4
    get("foo",4)       → "bar2"  (exact match t=4)
    get("foo",5)       → "bar2"  (latest at or before t=5 is t=4)

  Example 2 — slightly tricky (no valid timestamp):
    set("love","high",10)
    set("love","low",20)
    get("love",5)  → ""    (no timestamp <= 5 exists)
    get("love",10) → "high"
    get("love",15) → "high" (latest at or before 15 is 10)
    get("love",20) → "low"
    get("love",25) → "low"

  Constraints:
    - 1 <= key.length, value.length <= 100
    - 1 <= timestamp <= 10^7
    - All timestamps in set() are strictly increasing
    - At most 2×10^5 calls to set and get

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🧠 SECTION 2 — KANGLISH THINKING — ಹೇಗೆ ಯೋಚಿಸಬೇಕು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  Problem odi aada mele namma brain enu think maadabeeku:

  ಹಂತ 1 — Problem ಅರ್ಥ ಮಾಡಿಕೊಳ್ಳಿ
  ┌─────────────────────────────────────────────────────────┐
  │  Input ಏನು ಕೊಡ್ತಾರೆ?  →  key, value, timestamp        │
  │  Output ಏನು ಬೇಕು?     →  get(key, t) → value at       │
  │                           largest timestamp <= t        │
  │  Constraints ಏನಿದೆ?   →  timestamps strictly increasing│
  │                           in set() calls               │
  └─────────────────────────────────────────────────────────┘

  ಹಂತ 2 — ನನಗೆ ಗೊತ್ತಿರೋ simple way ಏನು?
  →  HashMap ಲ್ಲಿ key → [(timestamp, value)] store ಮಾಡೋಣ
     get() ಲ್ಲಿ list ಅನ್ನು scan ಮಾಡಿ largest t <= timestamp
     ಆದ value return ಮಾಡೋಣ → O(n) per get
  →  ಆದರೆ ಇದು slow ಯಾಕೆ?
     2×10^5 get calls, each O(n) → TLE possible

  ಹಂತ 3 — Better way ಹೇಗೆ ಯೋಚಿಸುವುದು?
  →  "Timestamps strictly increasing ಅಂದ್ರೆ list sorted!"
  →  Sorted list ಲ್ಲಿ "largest t <= timestamp" find ಮಾಡಲು
     binary search = upper bound - 1!
  →  bisect_right(timestamps, t) - 1 gives the answer index!

  ಹಂತ 4 — Technique ಯಾಕೆ ಇಲ್ಲಿ ಕೆಲಸ ಮಾಡುತ್ತೆ?
  →  timestamps always increasing → list always sorted
  →  "Largest timestamp <= t" = upper_bound(t) - 1
  →  Python bisect_right() does this in O(log n)

  💡 Interview ನಲ್ಲಿ ಹೇಗೆ ಮಾತಾಡಬೇಕು:
  →  "Since timestamps are strictly increasing, stored list is sorted"
  →  "get() = find largest timestamp <= t = upper bound - 1"
  →  "Binary search with bisect_right → O(log n) per get"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🏷️ SECTION 3 — TECHNIQUE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Primary   : Binary Search → Upper Bound (bisect_right)
  Secondary : HashMap + sorted list storage

  WHY Binary Search?
  → Timestamps always increasing → stored list is always sorted
  → "Largest timestamp <= t" = classic upper bound - 1
  → bisect_right(timestamps, t) - 1 → O(log n) per get

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 💡 SECTION 4 — INTUITION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Key observation: the problem says timestamps in set() are
  STRICTLY INCREASING. This means if we store (timestamp, value)
  pairs per key, the timestamps list is always sorted!

  get(key, t) → find largest stored_timestamp <= t
  This is the UPPER BOUND problem:
  → bisect_right(timestamps, t) gives first index where timestamp > t
  → So index-1 is the largest timestamp <= t
  → If index == 0 → no valid timestamp → return ""

  The journey from brute to optimal:
    Brute thought   →  Linear scan per get → O(n) per call
    Problem with it →  2×10^5 calls → too slow
    Better question →  "Are stored timestamps sorted?"
    Insight         →  YES! Strictly increasing → always sorted
                       → binary search for upper bound!
    Optimal         →  O(log n) per get using bisect_right

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🐢 SECTION 5 — APPROACH 1 — BRUTE FORCE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    Store key → [(timestamp, value)] in HashMap.
    For get(), scan all pairs and find largest timestamp <= t.

  Time  : set O(1), get O(n)
  Space : O(n) total stored pairs

  ಇದು ಯಾಕೆ ಸಾಕಾಗಲ್ಲ?
    → get() O(n) per call, 2×10^5 calls → O(n²) worst case → TLE

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🚀 SECTION 6 — APPROACH 2 — OPTIMAL (Binary Search)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    Store key → (timestamps_list, values_list) in HashMap.
    set(): append to both lists → O(1)
    get(): binary search for largest timestamp <= t → O(log n)

  Key steps for get(key, timestamp):
    1. If key not in store → return ""
    2. timestamps = store[key][0]
    3. idx = bisect_right(timestamps, timestamp) - 1
    4. If idx < 0 → no valid timestamp → return ""
    5. return store[key][1][idx]

  ಕನ್ನಡದಲ್ಲಿ ಒಂದು ಸಲ ಹೇಳಿ:
    → "HashMap ಲ್ಲಿ key → ([timestamps], [values]) store maadu.
       set() ಲ್ಲಿ append maadu — O(1).
       get() ಲ್ಲಿ bisect_right(timestamps, t)-1 maadu.
       -1 ಬಂದ್ರೆ '' return maadu, else values[idx] return maadu.
       Timestamps always sorted! O(log n) per get!"

  Time  : set O(1), get O(log n)
  Space : O(n) total

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🔍 SECTION 7 — DRY RUN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  set("foo","bar",1)  → store["foo"] = ([1],["bar"])
  set("foo","bar2",4) → store["foo"] = ([1,4],["bar","bar2"])

  get("foo",1):
    timestamps=[1,4], bisect_right([1,4],1)=1, idx=1-1=0
    values[0]="bar" ✓

  get("foo",3):
    timestamps=[1,4], bisect_right([1,4],3)=1, idx=1-1=0
    values[0]="bar" ✓  (t=3 not in store, use t=1)

  get("foo",4):
    timestamps=[1,4], bisect_right([1,4],4)=2, idx=2-1=1
    values[1]="bar2" ✓

  get("foo",5):
    timestamps=[1,4], bisect_right([1,4],5)=2, idx=2-1=1
    values[1]="bar2" ✓

  ಇನ್ನೊಂದు — no valid timestamp:
  set("love","high",10) → store["love"]=([10],["high"])
  get("love",5):
    bisect_right([10],5)=0, idx=0-1=-1
    idx < 0 → return "" ✓

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 ⚠️ SECTION 8 — EDGE CASES — ಇವನ್ನ ಮರೆಯಬೇಡ!
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  ✓ Key not set yet?          →  return ""
  ✓ t < smallest timestamp?   →  idx=-1 → return ""
  ✓ t exactly matches?        →  bisect_right gives exact index
  ✓ t > largest timestamp?    →  idx=last → return last value
  ✓ Multiple keys?            →  each key has own list in HashMap

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📊 SECTION 9 — COMPLEXITY SUMMARY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                set       get       Space
  Brute Force   O(1)      O(n)      O(n)
  Optimal       O(1)      O(log n)  O(n)   ← use this ✅

  Time yaake O(log n) get?
    → bisect_right on sorted timestamps list
  Space yaake O(n)?
    → Store all (timestamp, value) pairs

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🎯 SECTION 10 — PATTERN LEARNED — ಇದರಿಂದ ಕಲಿತದ್ದು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Pattern Name: Binary Search — Upper Bound on Sorted List

  bisect_right(arr, target):
    → Returns first index where arr[index] > target
    → So arr[index-1] is the LARGEST element <= target
    → This is the "floor" or "upper bound - 1" pattern

  bisect_left(arr, target):
    → Returns first index where arr[index] >= target
    → This is the "lower bound" or "ceiling" pattern

  Ee pattern yaavaaga use maadabeeku?
  → "Find largest value <= target in sorted list"
  → "Find floor of target in sorted array"
  → Design problems with time-versioned data

  Idee pattern beere problemsalli kaanisatte:
  → Find First and Last Position #34 (bisect_left + bisect_right)
  → Kth Missing Positive #1539 (binary search on missing count)
  → Search Insert Position #35 (bisect_left)

  Next time intaha problem bandre naanu modalu idannu think maadtene:
  → "Sorted list alli largest element <= t beeka?
     → bisect_right(list, t) - 1 → that's the index!
     idx < 0 iddre no valid answer!"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🗣️ SECTION 11 — INTERVIEWALLI HEGE EXPLAIN MAADABEEKU
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  1. Understand:
     "Design key-value store. get() returns value at largest
      stored timestamp <= given timestamp."

  2. Brute force:
     "Store list per key, scan linearly for get → O(n) per get."

  3. Optimize:
     "Since timestamps in set() are strictly increasing, the
      stored list per key is always sorted! So get() becomes
      a binary search — find largest timestamp <= t using
      bisect_right(timestamps, t) - 1."

  4. Code:
     "HashMap key → ([timestamps], [values]). set() appends.
      get() uses bisect_right, checks idx >= 0, returns value."

  5. Complexity:
     "set O(1). get O(log n). Space O(n) total."

  Mukhya: summane kuutu code bareyabeda!
          bisect_right - 1 = upper bound - 1 = floor — explain clearly!
          "timestamps strictly increasing → always sorted" — key insight!
"""

from collections import defaultdict
from bisect import bisect_right


# ═══════════════════════════════════════════════════════════════════
# BRUTE FORCE — set O(1), get O(n) per call
# ═══════════════════════════════════════════════════════════════════
class TimeMapBrute:
    """Idu modala aaloochane — linear scan for get"""

    def __init__(self):
        self.store = defaultdict(list)   # key → [(timestamp, value)]

    def set(self, key, value, timestamp):
        self.store[key].append((timestamp, value))

    def get(self, key, timestamp):
        if key not in self.store:
            return ""
        result = ""
        for t, v in self.store[key]:
            if t <= timestamp:
                result = v      # keep updating — last valid wins
        return result


# ═══════════════════════════════════════════════════════════════════
# OPTIMAL — set O(1), get O(log n) per call
# ═══════════════════════════════════════════════════════════════════
class TimeMap:
    """
    Idu final answer — separate timestamps and values lists
    bisect_right on timestamps → O(log n) per get
    """

    def __init__(self):
        # key → ([timestamps], [values])
        # timestamps always sorted since set() called with increasing t
        self.store = defaultdict(lambda: [[], []])

    def set(self, key, value, timestamp):
        """O(1) — just append to both lists"""
        self.store[key][0].append(timestamp)
        self.store[key][1].append(value)

    def get(self, key, timestamp):
        """
        O(log n) — binary search for largest timestamp <= given t
        bisect_right gives first index where timestamps[idx] > t
        So idx-1 is the largest timestamp <= t
        """
        if key not in self.store:
            return ""

        timestamps = self.store[key][0]
        values     = self.store[key][1]

        # bisect_right: first position where timestamps[pos] > timestamp
        idx = bisect_right(timestamps, timestamp) - 1

        if idx < 0:
            return ""          # no timestamp <= given timestamp

        return values[idx]


# ═══════════════════════════════════════════════════════════════════
# TEST CASES
# ═══════════════════════════════════════════════════════════════════
if __name__ == "__main__":
    # Test 1 — Basic example from problem
    tm = TimeMap()
    tm.set("foo", "bar", 1)
    assert tm.get("foo", 1) == "bar"
    assert tm.get("foo", 3) == "bar"   # no t=3, use t=1
    tm.set("foo", "bar2", 4)
    assert tm.get("foo", 4) == "bar2"
    assert tm.get("foo", 5) == "bar2"

    # Test 2 — No valid timestamp (t before all stored)
    tm2 = TimeMap()
    tm2.set("love", "high", 10)
    tm2.set("love", "low", 20)
    assert tm2.get("love", 5)  == ""      # before any stored t
    assert tm2.get("love", 10) == "high"
    assert tm2.get("love", 15) == "high"  # between 10 and 20
    assert tm2.get("love", 20) == "low"
    assert tm2.get("love", 25) == "low"   # after all stored t

    # Test 3 — Key not set
    tm3 = TimeMap()
    assert tm3.get("missing", 5) == ""

    # Test 4 — Exact timestamp match
    tm4 = TimeMap()
    tm4.set("a", "1", 5)
    tm4.set("a", "2", 10)
    tm4.set("a", "3", 15)
    assert tm4.get("a", 5)  == "1"
    assert tm4.get("a", 10) == "2"
    assert tm4.get("a", 15) == "3"
    assert tm4.get("a", 12) == "2"   # between 10 and 15

    print("All tests passed!")
