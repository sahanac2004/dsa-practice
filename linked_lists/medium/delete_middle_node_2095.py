"""
╔══════════════════════════════════════════════════════════════════╗
║  DELETE THE MIDDLE NODE OF A LINKED LIST                         ║
║  LeetCode #2095  |  Difficulty: Medium  |  Topic: Linked Lists  ║
║  Link: https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/
╚══════════════════════════════════════════════════════════════════╝

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📘 SECTION 1 — PROBLEM UNDERSTANDING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Given the head of a linked list, delete the MIDDLE node and
  return the head of the modified list.

  Middle = node at index ⌊n/2⌋  (0-indexed, n = total nodes)

  Input : head = linked list
  Output: head after deleting middle node

  Example 1 — odd length:
    Input : 1→3→4→7→1→2→6  (n=7, middle index=3)
    Output: 1→3→4→1→2→6
    Why?  : ⌊7/2⌋ = 3 → 0-indexed node 3 = value 7 → remove it

  Example 2 — even length:
    Input : 1→2→3→4  (n=4, middle index=2)
    Output: 1→2→4
    Why?  : ⌊4/2⌋ = 2 → 0-indexed node 2 = value 3 → remove it

  Example 3 — two nodes:
    Input : 1→2  (n=2, middle index=1)
    Output: 1
    Why?  : ⌊2/2⌋ = 1 → node 1 = value 2 → remove it

  Constraints:
    - 1 <= nodes <= 10^5
    - 1 <= Node.val <= 10^5
    - Single node: return None (only node IS the middle)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🧠 SECTION 2 — KANGLISH THINKING — ಹೇಗೆ ಯೋಚಿಸಬೇಕು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  Problem odi aada mele namma brain enu think maadabeeku:

  ಹಂತ 1 — Problem ಅರ್ಥ ಮಾಡಿಕೊಳ್ಳಿ
  ┌─────────────────────────────────────────────────────────┐
  │  Input ಏನು ಕೊಡ್ತಾರೆ?  →  linked list                  │
  │  Output ಏನು ಬೇಕು?     →  middle node remove ಮಾಡಿದ    │
  │                           list                          │
  │  Middle ಯಾವದು?        →  index ⌊n/2⌋ (0-indexed)     │
  │  Constraints ಏನಿದೆ?   →  single node → return None   │
  └─────────────────────────────────────────────────────────┘

  ಹಂತ 2 — ನನಗೆ ಗೊತ್ತಿರೋ simple way ಏನು?
  →  Length find ಮಾಡಿ ⌊n/2⌋ th node ಗೆ ಹೋಗಿ skip ಮಾಡು
  →  Two pass!

  ಹಂತ 3 — One pass ಹೇಗೆ?
  →  #876 Middle of Linked List ನಲ್ಲಿ fast/slow trick ಕಲಿತೆ!
  →  fast = 2x speed slow = 1x speed
     fast = None ಆದಾಗ slow = middle!
  →  ಆದರೆ ಇಲ್ಲಿ slow ಅನ್ನು middle PREVIOUS ಗೆ ತರಬೇಕು
     (delete ಮಾಡಬೇಕಾದ್ರೆ prev pointer ಬೇಕು!)
  →  Dummy node! slow = dummy ಇಂದ start.
     fast = head ಇಂದ start (one step behind normal).
     fast = None ಆದಾಗ slow = prev of middle!

  ಹಂತ 4 — fast ಎಷ್ಟು speed?
  →  Standard: fast = fast.next.next, slow = slow.next
  →  ಆದರೆ ⌊n/2⌋ middle definition ಗೆ ಸರಿಯಾಗಿ tune ಮಾಡಬೇಕು
  →  fast 2 steps, slow 1 step → when fast=None or fast.next=None,
     slow is AT middle.
  →  We need slow ONE BEFORE middle → start slow at dummy!

  💡 Interview ನಲ್ಲಿ ಹೇಗೆ ಮಾತಾಡಬೇಕು:
  →  "Fast/slow pointers. Slow starts at dummy (one behind head)."
  →  "Fast moves 2x, slow moves 1x. When fast exhausted → slow=prev of middle."
  →  "slow.next = slow.next.next removes the middle node."

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🏷️ SECTION 3 — TECHNIQUE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Primary   : Fast/Slow Pointers (Tortoise and Hare — modified)
  Secondary : Dummy Node (slow starts one behind)

  WHY Fast/Slow?
  → Find middle in one pass without knowing length
  → fast 2x, slow 1x → fast exhausted ↔ slow at middle
  → Start slow at dummy → slow arrives at PREV of middle

  Difference from #876 (Middle of Linked List):
  → #876: slow starts at head → lands ON middle (to return it)
  → #2095: slow starts at dummy → lands BEFORE middle (to delete it)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 💡 SECTION 4 — INTUITION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Same tortoise-and-hare as #876 but with a twist:
  We need the node BEFORE the middle, not the middle itself.

  Solution: start slow one position earlier (at dummy).
  Fast still starts at head, moves 2 steps per round.
  Slow starts at dummy, moves 1 step per round.
  When fast is exhausted, slow = prev of middle → delete!

  Why does this give ⌊n/2⌋?
  → For n=7: middle index = 3 (0-indexed)
    fast covers 7 nodes at 2/step → 3-4 steps
    slow covers same steps from dummy → index 3 from head ✓
  → For n=4: middle index = 2
    fast covers 4 nodes → 2 steps
    slow covers 2 steps from dummy → index 2 from head ✓

  The journey from brute to optimal:
    Brute thought   →  Two pass: find length n, go to ⌊n/2⌋-1
    Problem with it →  Two traversals
    Better question →  "Can I use fast/slow like #876?"
    Insight         →  YES! Start slow at dummy instead of head
                       → lands at prev of middle → delete!
    Optimal         →  O(n) time, O(1) space, one pass

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🐢 SECTION 5 — APPROACH 1 — BRUTE FORCE (Two Pass)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    Pass 1: count length n.
    Pass 2: go to node at index ⌊n/2⌋ - 1 (prev of middle).
    Skip middle: prev.next = prev.next.next

  Time  : O(n)   →  two passes
  Space : O(1)   →  only pointers

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🚀 SECTION 6 — APPROACH 2 — OPTIMAL (One Pass, Fast/Slow)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    dummy before head. slow = dummy, fast = head.
    Advance: fast moves 2 steps, slow moves 1 step.
    When fast exhausted → slow = prev of middle.
    Delete: slow.next = slow.next.next

  Key steps:
    1. dummy = ListNode(0, head)
    2. slow = dummy, fast = head
    3. While fast and fast.next:
       fast = fast.next.next
       slow = slow.next
    4. slow.next = slow.next.next
    5. return dummy.next

  ಕನ್ನಡದಲ್ಲಿ ಒಂದು ಸಲ ಹೇಳಿ:
    → "dummy ಮುಂದೆ ಇಡು. slow=dummy, fast=head.
       fast and fast.next iddre: fast 2 steps, slow 1 step.
       Loop end iddre slow = prev of middle.
       slow.next = slow.next.next → middle delete!
       dummy.next return!"

  Time  : O(n)   →  single pass
  Space : O(1)   →  only dummy, slow, fast

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🔍 SECTION 7 — DRY RUN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Input: 1→3→4→7→1→2→6  (n=7, middle=index 3=value 7)
  dummy→1→3→4→7→1→2→6

  slow=dummy, fast=1(idx0)

  Round 1: fast=4(idx2), slow=1(idx0)
  Round 2: fast=1(idx4), slow=3(idx1)
  Round 3: fast=6(idx6), slow=4(idx2)
  Round 4: fast.next=None → exit!

  slow=4(idx2) → slow.next=7(idx3) → TARGET!
  slow.next = 1(idx4)
  Result: 1→3→4→1→2→6 ✓

  ಇನ್ನೊಂದು — even length:
  Input: 1→2→3→4  (n=4, middle=index 2=value 3)
  dummy→1→2→3→4

  slow=dummy, fast=1(idx0)

  Round 1: fast=3(idx2), slow=1(idx0)
  Round 2: fast.next=None → exit!

  slow=1(idx0) → slow.next=2(idx1)... wait!
  Hmm, slow=1 means slow.next=2 not 3. Let me recheck.

  Actually: slow=dummy at start.
  Round 1: fast=1→3(idx2), slow=dummy→1(idx0)
  Round 2: fast=3→None (fast.next=4, fast=4, fast.next=None)
           Actually fast=4(idx3), fast.next=None → exit
           slow=1→2(idx1)

  slow=2(idx1) → slow.next=3(idx2) → TARGET (⌊4/2⌋=2) ✓
  slow.next = 4(idx3)
  Result: 1→2→4 ✓

  Single node:
  dummy→1, slow=dummy, fast=1
  fast.next=None → loop never runs
  slow=dummy → slow.next=1 → slow.next=None
  Result: None ✓

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 ⚠️ SECTION 8 — EDGE CASES — ಇವನ್ನ ಮರೆಯಬೇಡ!
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  ✓ Single node?    →  middle = only node → return None
  ✓ Two nodes?      →  middle = index 1 (second) → remove tail
  ✓ Three nodes?    →  middle = index 1 (second) → remove middle
  ✓ Even length?    →  ⌊n/2⌋ picks the second of the two middles
  ✓ Odd length?     →  ⌊n/2⌋ picks the exact middle

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📊 SECTION 9 — COMPLEXITY SUMMARY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                  Time    Space
  Brute (2 pass)  O(n)    O(1)
  Optimal (1pass) O(n)    O(1)   ← use this ✅

  Both same complexity, but single pass is cleaner code.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🎯 SECTION 10 — PATTERN LEARNED — ಇದರಿಂದ ಕಲಿತದ್ದು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Pattern Name: Fast/Slow — Start slow at dummy to get PREV of middle

  The three flavours of fast/slow:
  ┌─────────────────────────────────────────────────────────┐
  │  #876 Find middle      → slow=head, fast=head           │
  │                           → slow lands ON middle        │
  │  #2095 Delete middle   → slow=dummy, fast=head          │
  │                           → slow lands BEFORE middle    │
  │  #19 Remove nth from   → fixed gap (n+1 apart)          │
  │       end              → slow lands BEFORE nth-from-end │
  └─────────────────────────────────────────────────────────┘

  Idee pattern beere problemsalli kaanisatte:
  → Palindrome Linked List #234 (find middle, then reverse)
  → Reorder List #143 (find middle, split, merge) ← NEXT!
  → Linked List Cycle #141 (fast/slow detect cycle)

  Next time intaha problem bandre naanu modalu idannu think maadtene:
  → "Middle delete maadabekittu?
     → slow=dummy, fast=head. fast 2x, slow 1x.
     fast exhausted iddre slow = prev of middle.
     slow.next = slow.next.next!"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🗣️ SECTION 11 — INTERVIEWALLI HEGE EXPLAIN MAADABEEKU
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  1. Understand:
     "Delete node at index ⌊n/2⌋ (0-indexed). Return head."

  2. Brute force:
     "Two pass: find length, go to ⌊n/2⌋-1 th node, skip next."

  3. Optimize:
     "Fast/slow pointers in one pass.
      Key trick: start slow at dummy (one before head).
      Fast starts at head, moves 2 steps; slow moves 1 step.
      When fast exhausted, slow = prev of middle.
      slow.next = slow.next.next removes middle node."

  4. Why dummy for slow?
     "Starting slow at head would land it ON middle with no
      previous pointer to delete from. Dummy shifts it back one."

  5. Complexity:
     "Time O(n). Space O(1). Single pass."
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
# BRUTE FORCE — O(n) Time | O(1) Space (Two Pass)
# ═══════════════════════════════════════════════════════════════════
def delete_middle_brute(head):
    """Two pass: find length, go to prev of middle, skip it"""
    if not head or not head.next:
        return None

    # Pass 1: find length
    n, curr = 0, head
    while curr:
        n   += 1
        curr = curr.next

    # Pass 2: go to node at index (n//2 - 1)
    mid  = n // 2
    curr = head
    for _ in range(mid - 1):
        curr = curr.next

    curr.next = curr.next.next
    return head


# ═══════════════════════════════════════════════════════════════════
# OPTIMAL — O(n) Time | O(1) Space (One Pass, Fast/Slow)
# ═══════════════════════════════════════════════════════════════════
def delete_middle(head):
    """
    Idu final answer — fast/slow with slow starting at dummy
    slow=dummy so when fast exhausted → slow = PREV of middle
    slow.next = slow.next.next removes the middle node
    """
    # Single node: middle IS the only node → return None
    if not head or not head.next:
        return None

    dummy = ListNode(0, head)
    slow  = dummy      # starts ONE before head
    fast  = head       # starts at head

    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next

    # slow is now prev of middle
    slow.next = slow.next.next

    return dummy.next


# ═══════════════════════════════════════════════════════════════════
# TEST CASES
# ═══════════════════════════════════════════════════════════════════
if __name__ == "__main__":
    # Test 1 — Odd length: middle index=3, value=7
    assert to_list(delete_middle(
        build([1,3,4,7,1,2,6]))) == [1,3,4,1,2,6]

    # Test 2 — Even length: middle index=2, value=3
    assert to_list(delete_middle(
        build([1,2,3,4]))) == [1,2,4]

    # Test 3 — Two nodes: middle index=1
    assert to_list(delete_middle(
        build([1,2]))) == [1]

    # Test 4 — Single node: return None
    assert to_list(delete_middle(
        build([1]))) == []

    # Test 5 — Three nodes: middle index=1
    assert to_list(delete_middle(
        build([1,2,3]))) == [1,3]

    # Test 6 — Five nodes: middle index=2
    assert to_list(delete_middle(
        build([1,2,3,4,5]))) == [1,2,4,5]

    # Test 7 — Six nodes: middle index=3
    assert to_list(delete_middle(
        build([1,2,3,4,5,6]))) == [1,2,3,5,6]

    # Test 8 — Brute force matches optimal
    assert to_list(delete_middle_brute(
        build([1,3,4,7,1,2,6]))) == [1,3,4,1,2,6]
    assert to_list(delete_middle_brute(
        build([1,2,3,4]))) == [1,2,4]

    print("All tests passed!")
