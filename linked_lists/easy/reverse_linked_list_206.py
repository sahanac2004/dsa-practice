"""
╔══════════════════════════════════════════════════════════════════╗
║  REVERSE LINKED LIST                                             ║
║  LeetCode #206  |  Difficulty: Easy  |  Topic: Linked Lists     ║
║  Link: https://leetcode.com/problems/reverse-linked-list/       ║
╚══════════════════════════════════════════════════════════════════╝

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📘 SECTION 1 — PROBLEM UNDERSTANDING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Given the head of a singly linked list, reverse the list and
  return the new head.

  Input : head = first node of linked list
  Output: head of reversed linked list

  Example 1 — basic:
    Input : 1 → 2 → 3 → 4 → 5 → None
    Output: 5 → 4 → 3 → 2 → 1 → None
    Why?  : Every node's next pointer is flipped

  Example 2 — slightly tricky (single node):
    Input : 1 → None
    Output: 1 → None
    Why?  : Single node reversed is itself

  Constraints:
    - 0 <= number of nodes <= 5000
    - -5000 <= Node.val <= 5000
    - Must solve both iteratively AND recursively

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🧠 SECTION 2 — KANGLISH THINKING — ಹೇಗೆ ಯೋಚಿಸಬೇಕು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  Problem odi aada mele namma brain enu think maadabeeku:

  ಹಂತ 1 — Problem ಅರ್ಥ ಮಾಡಿಕೊಳ್ಳಿ
  ┌─────────────────────────────────────────────────────────┐
  │  Input ಏನು ಕೊಡ್ತಾರೆ?  →  linked list head node        │
  │  Output ಏನು ಬೇಕು?     →  reversed list head node      │
  │  Constraints ಏನಿದೆ?   →  in-place reverse beeku,      │
  │                           O(1) extra space              │
  └─────────────────────────────────────────────────────────┘

  ಹಂತ 2 — ನನಗೆ ಗೊತ್ತಿರೋ simple way ಏನು?
  →  All values collect ಮಾಡಿ array ಗೆ, reverse ಮಾಡಿ
     linked list ಮತ್ತೆ build ಮಾಡೋಣ → O(n) time O(n) space
  →  ಆದರೆ ಇದು slow ಯಾಕೆ?
     O(1) space ಲ್ಲಿ in-place ಮಾಡಬಹuದು!

  ಹಂತ 3 — Better way ಹೇಗೆ ಯೋಚಿಸುವುದು?
  →  "ಪ್ರತಿ node ರ next pointer ಅನ್ನು flip ಮಾಡಬಹudaa?"
  →  YES! 3 pointers: prev, curr, next_node
     curr.next = prev (flip!)
     prev = curr (advance prev)
     curr = next_node (advance curr)
  →  ಇದರಿಂದ ನಾವು Three Pointer Iterative use ಮಾಡಬಹuದು!

  ಹಂತ 4 — Technique ಯಾಕೆ ಇಲ್ಲಿ ಕೆಲಸ ಮಾಡುತ್ತೆ?
  →  ಪ್ರತಿ step ಲ್ಲಿ curr.next ಅನ್ನು prev ಗೆ point ಮಾಡ್ತೇವೆ
  →  ಮೊದಲು next_node save ಮಾಡಬೇಕು — otherwise pointer lost!
  →  curr = None ಆದ್ರೆ prev = new head!

  💡 Interview ನಲ್ಲಿ ಹೇಗೆ ಮಾತಾಡಬೇಕು:
  →  "Need 3 pointers: prev (starts None), curr (starts head), next"
  →  "At each step: save next, flip curr.next to prev, advance both"
  →  "When curr is None, prev is the new head"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🏷️ SECTION 3 — TECHNIQUE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Primary   : Three Pointer Iterative (prev, curr, next)
  Secondary : Recursion (elegant but O(n) stack space)

  WHY Three Pointers?
  → Must flip each node's next pointer
  → Need to save next before flipping (otherwise chain breaks!)
  → O(1) space — no extra data structure needed

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 💡 SECTION 4 — INTUITION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Think of it as "redirecting traffic":
  Originally: 1 → 2 → 3 → 4 → 5
  We want:    1 ← 2 ← 3 ← 4 ← 5

  At each node, we flip its arrow direction.
  But before flipping, we must save where it was pointing
  (otherwise we lose the rest of the list!)

  Three pointer dance:
    prev = None    (nothing behind first node yet)
    curr = head    (start at head)

  Each iteration:
    next_node = curr.next   ← SAVE next before flipping
    curr.next = prev        ← FLIP the arrow!
    prev = curr             ← advance prev
    curr = next_node        ← advance curr

  The journey from brute to optimal:
    Brute thought   →  Store all values, reverse, rebuild → O(n) space
    Problem with it →  Wastes O(n) extra space
    Better question →  "Can I flip pointers in-place?"
    Insight         →  YES! 3 pointers — save next, flip, advance
    Optimal         →  O(n) time, O(1) space iterative

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🐢 SECTION 5 — APPROACH 1 — BRUTE FORCE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    Collect all values into a list. Reverse the list.
    Overwrite node values in original list.

  Pseudocode:
    step 1: vals = []
    step 2: traverse list, collect all values
    step 3: reverse vals
    step 4: traverse list again, assign vals[i] to each node

  Time  : O(n)   →  Why: two passes through list
  Space : O(n)   →  Why: extra list to store values

  ಇದು ಯಾಕೆ ಸಾಕಾಗಲ್ಲ?
    → O(n) space wasteful — in-place O(1) space possible!
    → Also doesn't actually reverse pointers (just values)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🚀 SECTION 6 — APPROACH 2 — OPTIMAL ITERATIVE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    Three pointers. Flip each node's next pointer one by one.

  Key steps:
    1. prev=None, curr=head
    2. While curr is not None:
       a. next_node = curr.next    ← save next
       b. curr.next = prev         ← flip arrow!
       c. prev = curr              ← move prev forward
       d. curr = next_node         ← move curr forward
    3. return prev                 ← prev is new head

  ಕನ್ನಡದಲ್ಲಿ ಒಂದು ಸಲ ಹೇಳಿ:
    → "prev=None, curr=head ಇಂದ start maadu.
       ಪ್ರತಿ step ಲ್ಲಿ: next save maadu, curr.next ಅನ್ನು prev ಗೆ
       flip maadu, prev ಮತ್ತು curr ಎರಡನ್ನೂ forward move maadu.
       curr=None ಆದ್ರೆ prev = new head!"

  Time  : O(n)   →  Why: single pass through list
  Space : O(1)   →  Why: only 3 pointers

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🚀 SECTION 7 — APPROACH 3 — RECURSIVE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    Recurse to end of list. On the way back, flip pointers.

  Key insight:
    reverse(head) → go to end → on return, flip head.next.next = head
    head.next = None (clean up)

  ಕನ್ನಡದಲ್ಲಿ ಒಂದು ಸಲ ಹೇಳಿ:
    → "End ತನಕ recurse maadu. Return ಮಾಡುವಾಗ:
       head.next.next = head (flip!)
       head.next = None (old pointer remove maadu)
       new_head ಅನ್ನು recursion ಮೂಲಕ return maadu!"

  Time  : O(n)   →  Why: visit each node once
  Space : O(n)   →  Why: recursion call stack depth n

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🔍 SECTION 8 — DRY RUN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Input: 1 → 2 → 3 → None
  prev=None, curr=1

  Step 1: next=2, 1.next=None, prev=1, curr=2
    List so far: None ← 1    2 → 3 → None

  Step 2: next=3, 2.next=1, prev=2, curr=3
    List so far: None ← 1 ← 2    3 → None

  Step 3: next=None, 3.next=2, prev=3, curr=None
    List so far: None ← 1 ← 2 ← 3

  curr=None → exit loop → return prev=3

  Output: 3 → 2 → 1 → None ✓

  ಇನ್ನೊಂದು — empty list:
  Input: None
  prev=None, curr=None → loop never runs → return None ✓

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 ⚠️ SECTION 9 — EDGE CASES — ಇವನ್ನ ಮರೆಯಬೇಡ!
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  ✓ Empty list (None)?        →  return None
  ✓ Single node?              →  return same node
  ✓ Two nodes?                →  1→2 becomes 2→1
  ✓ Already reversed?         →  works fine, just reverses again

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📊 SECTION 10 — COMPLEXITY SUMMARY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                  Time    Space
  Brute Force     O(n)    O(n)
  Iterative       O(n)    O(1)   ← use this ✅
  Recursive       O(n)    O(n)   (call stack)

  Time yaake O(n)?  → Each node visited exactly once
  Space yaake O(1)? → Only prev, curr, next_node — 3 pointers!

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🎯 SECTION 11 — PATTERN LEARNED — ಇದರಿಂದ ಕಲಿತದ್ದು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Pattern Name: Three Pointer Linked List Reversal

  Three pointer dance — memorize this:
  ┌────────────────────────────────────────────┐
  │  next_node = curr.next   ← SAVE first!    │
  │  curr.next = prev        ← FLIP arrow     │
  │  prev = curr             ← advance prev   │
  │  curr = next_node        ← advance curr   │
  └────────────────────────────────────────────┘

  Ee pattern yaavaaga use maadabeeku?
  → Any linked list reversal (full or partial)
  → Palindrome linked list (reverse second half)
  → Reorder List (reverse second half)
  → Reverse in k-group (same reversal, repeated)

  Idee pattern beere problemsalli kaanisatte:
  → Reverse Linked List II #92 (partial reverse)
  → Palindrome Linked List #234 (reverse second half)
  → Reorder List #143 (find mid + reverse + merge)
  → Reverse Nodes in K-Group #25 (hard — k at a time)

  Next time intaha problem bandre naanu modalu idannu think maadtene:
  → "Linked list reverse beeka?
     → prev=None, curr=head. 4-line dance:
     next save, curr.next=prev flip, prev=curr, curr=next.
     curr=None iddre prev = new head!"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🗣️ SECTION 12 — INTERVIEWALLI HEGE EXPLAIN MAADABEEKU
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  1. Understand:
     "Reverse a singly linked list in-place."

  2. Brute force:
     "Collect values, reverse array, put back. O(n) space."

  3. Optimize:
     "Use three pointers — prev, curr, next. At each node:
      save next, flip curr.next to prev, advance both.
      O(1) space — no extra data structure."

  4. Code:
     "prev=None, curr=head. While curr: next_node=curr.next,
      curr.next=prev, prev=curr, curr=next_node. Return prev."

  5. Complexity:
     "Time O(n) — single pass. Space O(1) — 3 pointers only."

  Mukhya: summane kuutu code bareyabeda!
          "Save next BEFORE flipping" — common mistake if forgotten!
          Recursive solution also show — interviewer might ask both!
"""


# ─── Node Definition ──────────────────────────────────────────────
class ListNode:
    def __init__(self, val=0, next=None):
        self.val  = val
        self.next = next


# ─── Helper: build list from array ────────────────────────────────
def build(vals):
    dummy = ListNode(0)
    curr  = dummy
    for v in vals:
        curr.next = ListNode(v)
        curr = curr.next
    return dummy.next


# ─── Helper: list to array ────────────────────────────────────────
def to_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


# ═══════════════════════════════════════════════════════════════════
# BRUTE FORCE — O(n) Time | O(n) Space
# ═══════════════════════════════════════════════════════════════════
def reverse_list_brute(head):
    """Idu modala aaloochane — collect values, reverse, assign"""
    vals = []
    curr = head
    while curr:
        vals.append(curr.val)
        curr = curr.next

    vals.reverse()
    curr = head
    for v in vals:
        curr.val = v
        curr = curr.next

    return head


# ═══════════════════════════════════════════════════════════════════
# OPTIMAL ITERATIVE — O(n) Time | O(1) Space
# ═══════════════════════════════════════════════════════════════════
def reverse_list(head):
    """
    Idu final answer — three pointer dance
    prev=None, curr=head
    Each step: save next, flip, advance both
    """
    prev = None
    curr = head

    while curr:
        next_node  = curr.next   # 1. SAVE next before flipping!
        curr.next  = prev        # 2. FLIP arrow to prev
        prev       = curr        # 3. advance prev
        curr       = next_node   # 4. advance curr

    return prev                  # prev is the new head


# ═══════════════════════════════════════════════════════════════════
# RECURSIVE — O(n) Time | O(n) Space (call stack)
# ═══════════════════════════════════════════════════════════════════
def reverse_list_recursive(head):
    """
    Recursive: go to end, flip pointers on the way back
    head.next.next = head (flip!)
    head.next = None    (remove old pointer)
    """
    # base case: empty or single node
    if not head or not head.next:
        return head

    # recurse to end — new_head is the last node
    new_head = reverse_list_recursive(head.next)

    # on the way back: flip the pointer
    head.next.next = head   # next node now points BACK to head
    head.next      = None   # remove head's old forward pointer

    return new_head         # keep passing back the new head


# ═══════════════════════════════════════════════════════════════════
# TEST CASES
# ═══════════════════════════════════════════════════════════════════
if __name__ == "__main__":
    # Test 1 — Basic
    assert to_list(reverse_list(build([1,2,3,4,5]))) == [5,4,3,2,1]

    # Test 2 — Two nodes
    assert to_list(reverse_list(build([1,2]))) == [2,1]

    # Test 3 — Single node
    assert to_list(reverse_list(build([1]))) == [1]

    # Test 4 — Empty list
    assert to_list(reverse_list(None)) == []

    # Test 5 — Recursive version
    assert to_list(reverse_list_recursive(build([1,2,3,4,5]))) == [5,4,3,2,1]
    assert to_list(reverse_list_recursive(build([1]))) == [1]
    assert to_list(reverse_list_recursive(None)) == []

    print("All tests passed!")
