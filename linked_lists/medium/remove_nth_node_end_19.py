"""
╔══════════════════════════════════════════════════════════════════╗
║  REMOVE NTH NODE FROM END OF LIST                                ║
║  LeetCode #19  |  Difficulty: Medium  |  Topic: Linked Lists    ║
║  Link: https://leetcode.com/problems/remove-nth-node-from-end-of-list/
║  NeetCode: https://neetcode.io/problems/remove-node-from-end-of-linked-list
╚══════════════════════════════════════════════════════════════════╝

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📘 SECTION 1 — PROBLEM UNDERSTANDING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Given the head of a linked list, remove the nth node from the
  END of the list and return its head.

  Input : head = linked list, n = position from end (1-indexed)
  Output: head of list after removing that node

  Example 1 — basic:
    Input : 1→2→3→4→5, n=2
    Output: 1→2→3→5
    Why?  : 2nd from end is node 4 → remove it

  Example 2 — remove head:
    Input : 1→2, n=2
    Output: 2
    Why?  : 2nd from end = node 1 (the head) → remove head

  Constraints:
    - 1 <= number of nodes <= 30
    - 0 <= Node.val <= 100
    - 1 <= n <= number of nodes (n is always valid)
    - Follow-up: do it in ONE PASS!

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🧠 SECTION 2 — KANGLISH THINKING — ಹೇಗೆ ಯೋಚಿಸಬೇಕು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  Problem odi aada mele namma brain enu think maadabeeku:

  ಹಂತ 1 — Problem ಅರ್ಥ ಮಾಡಿಕೊಳ್ಳಿ
  ┌─────────────────────────────────────────────────────────┐
  │  Input ಏನು ಕೊಡ್ತಾರೆ?  →  linked list + n              │
  │  Output ಏನು ಬೇಕು?     →  nth from end remove ಮಾಡಿದ   │
  │                           list                          │
  │  Constraints ಏನಿದೆ?   →  ONE pass preferred!          │
  │                           n is always valid             │
  └─────────────────────────────────────────────────────────┘

  ಹಂತ 2 — ನನಗೆ ಗೊತ್ತಿರೋ simple way ಏನು?
  →  Pass 1: length find ಮಾಡು
     Pass 2: (length - n)th node ಗೆ ಹೋಗಿ next skip ಮಾಡು
  →  ಆದರೆ Two pass! Follow-up: ONE pass ಲ್ಲಿ ಮಾಡು

  ಹಂತ 3 — One pass ಹೇಗೆ?
  →  "Two pointers! fast ಮತ್ತು slow!"
  →  fast ಅನ್ನು n steps ahead ಕಳ್ಳೋಣ.
     Then fast ಮತ್ತು slow together move ಮಾಡೋಣ.
     fast = None ಆದಾಗ, slow = node BEFORE the target!
  →  ಯಾಕೆ? fast n steps ahead iddre,
     fast=None ಆದಾಗ slow = (length-n)th node
     = previous of nth-from-end!

  ಹಂತ 4 — Dummy node ಯಾಕೆ ಬೇಕು?
  →  Head ತಾನೇ remove ಆಗಬೇಕಾದ್ರೆ?
     (n = list length)
  →  Dummy node ಮುಂದೆ ಇಟ್ಟರೆ slow always has a
     previous node to modify!
  →  dummy → head → ... → target → ...
     slow starts at dummy, not head!

  💡 Interview ನಲ್ಲಿ ಹೇಗೆ ಮಾತಾಡಬೇಕು:
  →  "Two pointers with n-gap. Dummy node handles head removal."
  →  "fast n+1 steps ahead so slow stops at node BEFORE target"
  →  "When fast=None, slow.next = slow.next.next"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🏷️ SECTION 3 — TECHNIQUE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Primary   : Two Pointer — Fixed Gap (n apart)
  Secondary : Dummy Node (handle head removal cleanly)

  WHY Fixed Gap?
  → fast is n steps ahead of slow
  → When fast reaches end (None), slow is exactly
    at the node BEFORE the one we want to delete
  → One pass, O(1) space

  WHY Dummy Node?
  → If head itself needs removal (n = list length),
    slow needs a node before head to point from
  → dummy → [head] → ... : slow=dummy, fast advances n+1
    so slow.next is always the target to remove

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 💡 SECTION 4 — INTUITION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Imagine two runners on a track, n meters apart.
  When the front runner reaches the finish line,
  the back runner is exactly n meters from the end!

  We want slow to stop at the node BEFORE the target.
  So we need fast to be (n+1) steps ahead of slow.
  When fast = None, slow.next = target → skip it!

  Why n+1 and not n?
  → If fast is n ahead: when fast=last_node, slow=target
    (can't delete — no previous pointer!)
  → If fast is n+1 ahead: when fast=None, slow=prev of target ✓

  The journey from brute to optimal:
    Brute thought   →  Two pass: find length, then go to (len-n)th
    Problem with it →  Two traversals
    Follow-up       →  Can you do it in one pass?
    Insight         →  Fixed-gap two pointers! fast n+1 ahead
                       When fast=None, slow is prev of target
    Optimal         →  One pass, O(1) space

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🐢 SECTION 5 — APPROACH 1 — BRUTE FORCE (Two Pass)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    Pass 1: count length of list.
    Pass 2: go to (length - n - 1)th node, skip its next.
    Use dummy node to handle head removal.

  Time  : O(n)   →  two passes but both O(n)
  Space : O(1)   →  only pointers

  ಇದು ಯಾಕೆ ಸಾಕಾಗಲ್ಲ?
    → Valid, but two passes. Follow-up asks for one pass.
    → Interview ಲ್ಲಿ one pass solution impress more maadutthe!

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🚀 SECTION 6 — APPROACH 2 — OPTIMAL (One Pass, Two Pointers)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    dummy node before head. fast and slow both start at dummy.
    Move fast (n+1) steps ahead.
    Move both until fast = None.
    Now slow.next is the target — skip it!

  Key steps:
    1. dummy = ListNode(0, head); fast = slow = dummy
    2. Move fast (n+1) steps forward
    3. While fast: fast = fast.next, slow = slow.next
    4. slow.next = slow.next.next   ← remove target!
    5. return dummy.next

  ಕನ್ನಡದಲ್ಲಿ ಒಂದು ಸಲ ಹೇಳಿ:
    → "dummy ಮುಂದೆ ಇಡು. fast ಮತ್ತು slow dummy ಇಂದ start.
       fast ಅನ್ನು n+1 steps forward ತಳ್ಳು.
       fast=None ತನಕ both advance maadu.
       slow.next = slow.next.next — target skip!
       dummy.next return maadu!"

  Time  : O(L)   →  L = list length, one pass
  Space : O(1)   →  only dummy, fast, slow

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🔍 SECTION 7 — DRY RUN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Input: 1→2→3→4→5, n=2
  dummy→1→2→3→4→5

  fast = slow = dummy(0)

  Move fast (n+1)=3 steps:
    step1: fast=1
    step2: fast=2
    step3: fast=3

  Now fast=3, slow=dummy(0)
  Move both until fast=None:
    fast=3→4, slow=dummy→1 : fast=4, slow=1
    fast=4→5, slow=1→2     : fast=5, slow=2
    fast=5→None, slow=2→3  : fast=None, slow=3

  fast=None → stop!
  slow=3, slow.next=4 (the target!)
  slow.next = slow.next.next = 5
  List: 1→2→3→5 ✓

  ಇನ್ನೊಂದು — remove head (n=list length):
  Input: 1→2, n=2
  dummy→1→2

  Move fast (n+1)=3 steps:
    step1: fast=1
    step2: fast=2
    step3: fast=None ← already None after 3 steps!

  fast=None → while loop never executes! slow=dummy
  slow.next = slow.next.next = 2
  List: 2 ✓  (head removed)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 ⚠️ SECTION 8 — EDGE CASES — ಇವನ್ನ ಮರೆಯಬೇಡ!
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  ✓ Remove head?      →  n = list length → dummy handles it!
  ✓ Remove tail?      →  n = 1 → slow stops at second-to-last
  ✓ Single node?      →  [1], n=1 → remove only node → []
  ✓ Two nodes?        →  [1,2], n=2 → remove head → [2]
  ✓ n always valid?   →  Yes per constraints (no bounds check needed)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📊 SECTION 9 — COMPLEXITY SUMMARY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                  Time    Space
  Brute (2 pass)  O(L)    O(1)
  Optimal (1pass) O(L)    O(1)   ← use this ✅

  Same complexity but one pass is cleaner and interview-preferred.
  Time yaake O(L)?  → Traverse list at most once
  Space yaake O(1)? → Only dummy, fast, slow pointers

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🎯 SECTION 10 — PATTERN LEARNED — ಇದರಿಂದ ಕಲಿತದ್ದು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Pattern Name: Fixed-Gap Two Pointers on Linked List

  The gap trick:
  ┌──────────────────────────────────────────────────────┐
  │  Want slow at PREV of nth-from-end?                  │
  │  → Move fast (n+1) ahead of slow                     │
  │  → When fast=None: slow = prev of target ✓           │
  │                                                      │
  │  Want slow AT nth-from-end?                          │
  │  → Move fast n ahead of slow                         │
  │  → When fast=last node: slow = target                │
  └──────────────────────────────────────────────────────┘

  Dummy node rule:
  → Anytime head itself might be deleted → use dummy!
  → slow starts at dummy, not head

  Idee pattern beere problemsalli kaanisatte:
  → Middle of Linked List #876 (already solved! fast=2x speed)
  → Linked List Cycle #141 (fast=2x speed)
  → Linked List Cycle II #142 (upcoming!)
  → Reorder List #143 (upcoming — also uses mid-finding!)

  Next time intaha problem bandre naanu modalu idannu think maadtene:
  → "nth from end remove maadabekittu?
     → Dummy + two pointers! fast n+1 ahead of slow.
     fast=None iddre slow=prev of target.
     slow.next = slow.next.next!"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🗣️ SECTION 11 — INTERVIEWALLI HEGE EXPLAIN MAADABEEKU
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  1. Understand:
     "Remove nth node from end. Return head of modified list."

  2. Brute force:
     "Two pass: find length, then skip (length-n)th node. O(L) O(1)."

  3. Optimize:
     "One pass with fixed-gap two pointers.
      Dummy node before head handles head-removal edge case.
      Move fast (n+1) steps ahead of slow.
      Then advance both until fast=None.
      Now slow.next is the target — slow.next = slow.next.next."

  4. Why n+1 and not n?
     "n steps ahead → slow lands ON target, no prev pointer.
      n+1 steps ahead → slow lands on PREV of target. ✓"

  5. Complexity:
     "Time O(L). Space O(1). Single pass."

  Mukhya: summane kuutu code bareyabeda!
          n+1 vs n — explain clearly WHY n+1!
          Dummy node — WHY it's needed for head removal!
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
# BRUTE FORCE — O(L) Time | O(1) Space (Two Pass)
# ═══════════════════════════════════════════════════════════════════
def remove_nth_from_end_brute(head, n):
    """Idu modala aaloochane — find length, then skip target"""
    dummy = ListNode(0, head)

    # Pass 1: find length
    length = 0
    curr   = head
    while curr:
        length += 1
        curr    = curr.next

    # Pass 2: go to (length - n - 1)th node (0-indexed)
    curr  = dummy
    steps = length - n      # how many steps from dummy to prev
    for _ in range(steps):
        curr = curr.next

    curr.next = curr.next.next  # skip target
    return dummy.next


# ═══════════════════════════════════════════════════════════════════
# OPTIMAL — O(L) Time | O(1) Space (One Pass, Two Pointers)
# ═══════════════════════════════════════════════════════════════════
def remove_nth_from_end(head, n):
    """
    Idu final answer — dummy + fixed-gap two pointers
    fast starts (n+1) ahead of slow
    When fast=None: slow = prev of target → skip it!
    """
    dummy = ListNode(0, head)
    fast  = dummy
    slow  = dummy

    # Move fast (n+1) steps ahead
    for _ in range(n + 1):
        fast = fast.next

    # Advance both until fast = None
    while fast:
        fast = fast.next
        slow = slow.next

    # slow.next is the target — remove it
    slow.next = slow.next.next

    return dummy.next


# ═══════════════════════════════════════════════════════════════════
# TEST CASES
# ═══════════════════════════════════════════════════════════════════
if __name__ == "__main__":
    # Test 1 — Basic: remove 2nd from end
    assert to_list(remove_nth_from_end(
        build([1,2,3,4,5]), 2)) == [1,2,3,5]

    # Test 2 — Remove head (n = length)
    assert to_list(remove_nth_from_end(
        build([1,2]), 2)) == [2]

    # Test 3 — Remove tail (n = 1)
    assert to_list(remove_nth_from_end(
        build([1,2,3,4,5]), 1)) == [1,2,3,4]

    # Test 4 — Single node
    assert to_list(remove_nth_from_end(
        build([1]), 1)) == []

    # Test 5 — Two nodes, remove head
    assert to_list(remove_nth_from_end(
        build([1,2]), 2)) == [2]

    # Test 6 — Two nodes, remove tail
    assert to_list(remove_nth_from_end(
        build([1,2]), 1)) == [1]

    # Test 7 — Brute force matches optimal
    assert to_list(remove_nth_from_end_brute(
        build([1,2,3,4,5]), 2)) == [1,2,3,5]
    assert to_list(remove_nth_from_end_brute(
        build([1,2]), 2)) == [2]

    print("All tests passed!")
