"""
╔══════════════════════════════════════════════════════════════════╗
║  REMOVE DUPLICATES FROM SORTED LIST                              ║
║  LeetCode #83  |  Difficulty: Easy  |  Topic: Linked Lists      ║
║  Link: https://leetcode.com/problems/remove-duplicates-from-    ║
║        sorted-list/                                              ║
╚══════════════════════════════════════════════════════════════════╝

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📘 SECTION 1 — PROBLEM UNDERSTANDING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Given the head of a SORTED linked list, delete all duplicates
  such that each element appears only once. Return the head of
  the cleaned sorted linked list.

  Input : head = sorted linked list (may have duplicates)
  Output: head of list with duplicates removed

  Example 1 — basic:
    Input : 1 → 1 → 2
    Output: 1 → 2
    Why?  : Second 1 is duplicate, remove it

  Example 2 — slightly tricky (multiple duplicate groups):
    Input : 1 → 1 → 2 → 3 → 3
    Output: 1 → 2 → 3
    Why?  : Both groups of duplicates removed

  Constraints:
    - 0 <= number of nodes <= 300
    - -100 <= Node.val <= 100
    - List is sorted in ascending order

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🧠 SECTION 2 — KANGLISH THINKING — ಹೇಗೆ ಯೋಚಿಸಬೇಕು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  Problem odi aada mele namma brain enu think maadabeeku:

  ಹಂತ 1 — Problem ಅರ್ಥ ಮಾಡಿಕೊಳ್ಳಿ
  ┌─────────────────────────────────────────────────────────┐
  │  Input ಏನು ಕೊಡ್ತಾರೆ?  →  sorted linked list           │
  │  Output ಏನು ಬೇಕು?     →  duplicates remove ಮಾಡಿದ list │
  │  Constraints ಏನಿದೆ?   →  already SORTED!              │
  │                           first occurrence keep ಮಾಡು  │
  └─────────────────────────────────────────────────────────┘

  ಹಂತ 2 — ನನಗೆ ಗೊತ್ತಿರೋ simple way ಏನು?
  →  ಪ್ರತಿ node ಗೆ, ಅದರ next ಅದೇ value ಇದ್ಯಾ ಅಂತ check ಮಾಡು
     Same iddre next ಅನ್ನು skip ಮಾಡು
  →  List sorted ಆಗಿರೋದ್ರಿಂದ duplicates always adjacent!
  →  Single pass ಲ್ಲಿ O(n) ಲ್ಲಿ solve ಆಗತ್ತೆ!

  ಹಂತ 3 — Better way ಹೇಗೆ ಯೋಚಿಸುವುದು?
  →  curr pointer ಒಂದೇ ಸಾಕು!
  →  curr.val == curr.next.val iddre:
     curr.next = curr.next.next  (skip duplicate!)
  →  Else: curr = curr.next (move forward)

  ಹಂತ 4 — Technique ಯಾಕೆ ಇಲ್ಲಿ ಕೆಲಸ ಮಾಡುತ್ತೆ?
  →  Sorted list → duplicates always consecutive
  →  No need for HashSet — just compare with next node!
  →  In-place: just redirect next pointers, O(1) space

  💡 Interview ನಲ್ಲಿ ಹೇಗೆ ಮಾತಾಡಬೇಕು:
  →  "List is sorted so duplicates are always adjacent"
  →  "If curr.val == curr.next.val → skip next node"
  →  "Otherwise advance curr — single pass O(n) O(1)"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🏷️ SECTION 3 — TECHNIQUE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Primary   : Single Pointer Traversal (exploit sorted property)
  Secondary : —

  WHY single pointer?
  → Sorted → duplicates always adjacent → just check curr vs curr.next
  → No need for previous pointer — redirect curr.next in-place
  → O(1) space, O(n) time — cleanest possible solution

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 💡 SECTION 4 — INTUITION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Because the list is SORTED, any duplicate values will be
  right next to each other. So we never need to look far ahead —
  just compare curr with curr.next.

  If they're equal → skip curr.next by setting curr.next = curr.next.next
  If they're different → safe to advance curr forward

  Key: do NOT advance curr when skipping a duplicate —
  the new curr.next might ALSO be a duplicate of curr!

  The journey from brute to optimal:
    Brute thought   →  HashSet to track seen values, rebuild list
    Problem with it →  O(n) extra space — not needed!
    Better question →  "Are duplicates always adjacent?"
    Insight         →  YES! List is sorted → exploit adjacency
    Optimal         →  Single pointer, O(n) time, O(1) space

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🐢 SECTION 5 — APPROACH 1 — BRUTE FORCE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    Use HashSet to track seen values.
    Use dummy node + prev pointer to skip duplicates.

  Time  : O(n)   →  Why: single pass
  Space : O(n)   →  Why: HashSet stores all unique values

  ಇದು ಯಾಕೆ ಸಾಕಾಗಲ್ಲ?
    → O(n) space waste! Sorted iddre HashSet beekilla!
    → List sorted → adjacent compare alone sufficient!

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🚀 SECTION 6 — APPROACH 2 — OPTIMAL
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    Single pointer curr. Compare curr with curr.next.
    If same → skip curr.next. Else → advance curr.

  Key steps:
    1. curr = head
    2. While curr and curr.next:
       a. if curr.val == curr.next.val:
             curr.next = curr.next.next  ← skip duplicate!
          else:
             curr = curr.next            ← advance
    3. return head

  ಕನ್ನಡದಲ್ಲಿ ಒಂದು ಸಲ ಹೇಳಿ:
    → "curr = head ಇಂದ start maadu.
       curr.val == curr.next.val iddre → curr.next skip maadu
       (curr.next = curr.next.next).
       Different iddre → curr = curr.next advance maadu.
       Sorted iddre duplicates always adjacent — O(n) O(1)!"

  Time  : O(n)   →  Why: each node visited at most once
  Space : O(1)   →  Why: only curr pointer

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🔍 SECTION 7 — DRY RUN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Input: 1 → 1 → 2 → 3 → 3

  curr=1(first)
  curr.val=1, curr.next.val=1 → SAME → curr.next=2
  List: 1 → 2 → 3 → 3

  curr=1(still)
  curr.val=1, curr.next.val=2 → DIFF → curr=2
  List: 1 → 2 → 3 → 3

  curr=2
  curr.val=2, curr.next.val=3 → DIFF → curr=3(first)
  List: 1 → 2 → 3 → 3

  curr=3(first)
  curr.val=3, curr.next.val=3 → SAME → curr.next=None
  List: 1 → 2 → 3

  curr=3
  curr.next=None → exit loop

  Output: 1 → 2 → 3 ✓

  ಇನ್ನೊಂದು — all same:
  Input: 1 → 1 → 1
  curr=1: same → skip → 1→1
  curr=1: same → skip → 1→None
  curr=1: curr.next=None → exit
  Output: 1 ✓

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 ⚠️ SECTION 8 — EDGE CASES — ಇವನ್ನ ಮರೆಯಬೇಡ!
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  ✓ Empty list?           →  return None
  ✓ Single node?          →  no duplicates possible, return head
  ✓ All same values?      →  1→1→1 → 1 (keep first)
  ✓ No duplicates?        →  1→2→3 → 1→2→3 unchanged
  ✓ Three same in a row?  →  1→1→1→2 → 1→2 (skip all duplicates)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📊 SECTION 9 — COMPLEXITY SUMMARY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                  Time    Space
  Brute (HashSet) O(n)    O(n)
  Optimal         O(n)    O(1)   ← use this ✅

  Time yaake O(n)?  → Each node visited at most once
  Space yaake O(1)? → Only curr pointer — no extra space!

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🎯 SECTION 10 — PATTERN LEARNED — ಇದರಿಂದ ಕಲಿತದ್ದು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Pattern Name: Exploit Sorted Property — Adjacent Comparison

  Key insight for ALL sorted list problems:
  → Sorted = duplicates/patterns always adjacent
  → No need for HashSet or extra storage
  → Just compare with immediate neighbor!

  Idee pattern beere problemsalli kaanisatte:
  → Remove Duplicates from Sorted Array #26 (same idea, array!)
  → Remove Duplicates from Sorted List II #82 (remove ALL occurrences)
  → Merge Two Sorted Lists #21 (sorted merge)

  #83 vs #82 key difference:
  → #83: keep one copy of each duplicate group (easier)
  → #82: remove ALL nodes with duplicate values (harder, needs dummy)

  Next time intaha problem bandre naanu modalu idannu think maadtene:
  → "Sorted list duplicates remove beeka?
     → curr.val == curr.next.val iddre skip!
     curr.next = curr.next.next. Advance only when different.
     Sorted = adjacent duplicates = O(1) space!"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🗣️ SECTION 11 — INTERVIEWALLI HEGE EXPLAIN MAADABEEKU
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  1. Understand:
     "Remove duplicate values from sorted linked list,
      keeping one occurrence of each value."

  2. Brute force:
     "HashSet to track seen values — O(n) space. Not needed!"

  3. Optimize:
     "Key insight: list is sorted, so duplicates are always adjacent.
      Just compare curr with curr.next. Same → skip next node by
      setting curr.next = curr.next.next. Different → advance curr.
      Single pass O(n), O(1) space."

  4. Code:
     "curr = head. While curr and curr.next: if same → skip next,
      else advance. Return head."

  5. Complexity:
     "Time O(n). Space O(1)."

  Mukhya: summane kuutu code bareyabeda!
          "Sorted → adjacent duplicates" — key insight mention maadu!
          Don't advance when skipping — new next might also be dup!
"""


# ─── Node Definition ──────────────────────────────────────────────
class ListNode:
    def __init__(self, val=0, next=None):
        self.val  = val
        self.next = next


# ─── Helpers ──────────────────────────────────────────────────────
def build(vals):
    dummy = ListNode(0)
    curr  = dummy
    for v in vals:
        curr.next = ListNode(v)
        curr = curr.next
    return dummy.next

def to_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


# ═══════════════════════════════════════════════════════════════════
# BRUTE FORCE — O(n) Time | O(n) Space
# ═══════════════════════════════════════════════════════════════════
def delete_duplicates_brute(head):
    """Idu modala aaloochane — HashSet to track seen values"""
    seen  = set()
    dummy = ListNode(0)
    dummy.next = head
    prev  = dummy
    curr  = head

    while curr:
        if curr.val in seen:
            prev.next = curr.next   # skip duplicate
        else:
            seen.add(curr.val)
            prev = curr             # advance prev only for unique
        curr = curr.next

    return dummy.next


# ═══════════════════════════════════════════════════════════════════
# OPTIMAL — O(n) Time | O(1) Space
# ═══════════════════════════════════════════════════════════════════
def delete_duplicates(head):
    """
    Idu final answer — exploit sorted property!
    Duplicates always adjacent → just compare with next node
    Skip if same, advance if different
    """
    curr = head

    while curr and curr.next:
        if curr.val == curr.next.val:
            curr.next = curr.next.next  # skip duplicate node
            # DO NOT advance curr — new next might also be duplicate!
        else:
            curr = curr.next            # safe to advance

    return head


# ═══════════════════════════════════════════════════════════════════
# TEST CASES
# ═══════════════════════════════════════════════════════════════════
if __name__ == "__main__":
    # Test 1 — Basic single duplicate
    assert to_list(delete_duplicates(build([1, 1, 2]))) == [1, 2]

    # Test 2 — Multiple duplicate groups
    assert to_list(delete_duplicates(build([1, 1, 2, 3, 3]))) == [1, 2, 3]

    # Test 3 — All same
    assert to_list(delete_duplicates(build([1, 1, 1]))) == [1]

    # Test 4 — No duplicates
    assert to_list(delete_duplicates(build([1, 2, 3]))) == [1, 2, 3]

    # Test 5 — Single node
    assert to_list(delete_duplicates(build([1]))) == [1]

    # Test 6 — Empty list
    assert to_list(delete_duplicates(None)) == []

    # Test 7 — Three in a row
    assert to_list(delete_duplicates(build([1, 1, 1, 2, 3]))) == [1, 2, 3]

    # Test 8 — Brute force check
    assert to_list(delete_duplicates_brute(build([1, 1, 2, 3, 3]))) == [1, 2, 3]

    print("All tests passed!")
