"""
╔══════════════════════════════════════════════════════════════════╗
║  MIDDLE OF THE LINKED LIST                                       ║
║  LeetCode #876  |  Difficulty: Easy  |  Topic: Linked Lists    ║
║  Link: https://leetcode.com/problems/                           ║
║        middle-of-the-linked-list/                                ║
╚══════════════════════════════════════════════════════════════════╝

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📘 SECTION 1 — PROBLEM UNDERSTANDING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Given the head of a singly linked list, return the MIDDLE
  node of the linked list. If there are two middle nodes (the
  list has an even number of nodes), return the SECOND middle
  node.

  Input : head = singly linked list
  Output: the middle node (not just its value — the node itself,
          so everything from there onward is also returned)

  Example 1 — odd length:
    Input : head = [1,2,3,4,5]
    Output: [3,4,5]  (node valued 3 is the exact middle)

  Example 2 — even length:
    Input : head = [1,2,3,4,5,6]
    Output: [4,5,6]  (two middles would be 3 and 4 — return the
            SECOND one, 4)

  Constraints:
    - 1 <= number of nodes <= 100
    - 1 <= Node.val <= 100

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🧠 SECTION 2 — KANGLISH THINKING — ಹೇಗೆ ಯೋಚಿಸಬೇಕು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  Problem odi aada mele namma brain enu think maadabeeku:

  ಹಂತ 1 — Problem ಅರ್ಥ ಮಾಡಿಕೊಳ್ಳಿ
  ┌─────────────────────────────────────────────────────────┐
  │  Input ಏನು ಕೊಡ್ತಾರೆ?  →  singly linked list              │
  │  Output ಏನು ಬೇಕು?     →  middle node (even length ಇದ್ರೆ   │
  │                           SECOND middle)                   │
  │  Constraints ಏನಿದೆ?   →  list length ಮೊದಲೇ ಗೊತ್ತಿಲ್ಲ        │
  └─────────────────────────────────────────────────────────┘

  ಹಂತ 2 — ಯಾಕೆ ಇದು tricky? "middle ಅಂದ್ರೆ ಎಲ್ಲಿ ಅಂತ length
           ಗೊತ್ತಿಲ್ಲದೇ ಹೇಗೆ ಗೊತ್ತಾಗುತ್ತೆ?" ಅಂತ ಯೋಚಿಸಿ
  →  Array ಆಗಿದ್ರೆ length/2 index ಗೆ ನೇರವಾಗಿ ಹೋಗಬಹುದಿತ್ತು —
     linked list ಲ್ಲಿ ಹಾಗೆ ಮಾಡೋಕೆ ಆಗಲ್ಲ, ಮೊದಲು length ಗೊತ್ತಾಗಬೇಕು
     ಅಥವಾ ಬೇರೆ ಟ್ರಿಕ್ ಬೇಕು

  ಹಂತ 3 — ಮೊದಲ simple idea (brute force) ಏನು?
  →  "ಮೊದಲು list ಪೂರ್ತಿ walk ಮಾಡಿ length ಕಂಡುಹಿಡಿ, ಆಮೇಲೆ
      length//2 ಸಲ ಮತ್ತೆ walk ಮಾಡಿ ಆ node ಗೆ ಹೋಗಿದ್ರೆ?"
  →  ಕೆಲಸ ಆಗುತ್ತೆ, ಆದ್ರೆ list ಅನ್ನ ಎರಡು ಸಲ traverse ಮಾಡ್ಬೇಕು

  ಹಂತ 4 — Optimal idea (slow/fast) ಹೇಗೆ ಬರುತ್ತೆ?
  →  "ಒಂದೇ pass ಲ್ಲಿ middle ಕಂಡುಹಿಡಿಯೋಕೆ ಆಗ್ತದಾ?" ಅಂತ ಯೋಚಿಸಿ:
     slow pointer 1 step, fast pointer 2 step ಮುಂದೆ ಸಾಗಿಸಿದ್ರೆ,
     fast list ಕೊನೆ ತಲುಪೋ ಹೊತ್ತಿಗೆ slow EXACTLY middle ಗೆ
     ತಲುಪಿರುತ್ತೆ! (fast ಡಬಲ್ ಸ್ಪೀಡ್ ಲ್ಲಿ ಇರೋದ್ರಿಂದ)

  ಹಂತ 5 — Technique ಯಾಕೆ ಇಲ್ಲಿ ಕೆಲಸ ಮಾಡುತ್ತೆ?
  →  fast ಯಾವಾಗ ಕೊನೆ ತಲುಪುತ್ತೋ (None ಅಥವಾ fast.next None), ಆ
     ಹೊತ್ತಿಗೆ slow ಅರ್ಧ distance ಮಾತ್ರ ಕ್ರಮಿಸಿರುತ್ತೆ — ಅಂದ್ರೆ
     EXACTLY middle ಲ್ಲಿ ಇರುತ್ತೆ! even length ಆದ್ರೆ fast.next
     None ಆಗೋ ಹೊತ್ತಿಗೆ slow ಸ್ವಾಭಾವಿಕವಾಗೇ SECOND middle ಲ್ಲಿ
     ಇರುತ್ತೆ

  💡 Interview ನಲ್ಲಿ ಹೇಗೆ ಮಾತಾಡಬೇಕು:
  →  "First approach: two passes — count the length, then walk
      length // 2 steps to the middle. O(n) time, O(1) space,
      but two traversals."
  →  "Optimal: slow/fast pointers in a single pass. slow moves
      1 step, fast moves 2 steps. When fast reaches the end,
      slow is exactly at the middle — and naturally lands on the
      SECOND middle for even-length lists."

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🏷️ SECTION 3 — TECHNIQUE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Primary   : Slow/Fast Pointers, Single Pass (O(n) time, O(1) space)
  Secondary : Two-Pass (Count Length, Then Walk to Middle)

  WHY Slow/Fast over Two-Pass?
  → The two-pass approach is correct and still O(n) overall, but
    it does two separate traversals: one to measure length, one
    to walk to the middle. The slow/fast pointer trick achieves
    the identical result in exactly ONE traversal — slow trails
    at half the speed of fast, so when fast exhausts the list,
    slow has covered precisely half the distance.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 💡 SECTION 4 — INTUITION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  The key insight: if one pointer always moves exactly twice as
  fast as another, then whenever the fast one finishes the full
  distance, the slow one has covered exactly half of it — by
  definition, that's the middle. No need to know the length in
  advance; the relative speeds encode "half" automatically. For
  an even-length list, this naturally lands on the SECOND middle
  because fast exhausts the list (via fast.next being None) one
  step "ahead" of where a floor-division midpoint would land.

  The journey from brute to optimal:
    Brute thought   →  Count the list length in one pass, then
                       walk floor(length/2) steps in a second
                       pass to reach the middle
    Problem with it →  Two full traversals of the list
    Better question →  "Can a single pass find the midpoint
                       without knowing the length upfront?"
    Insight         →  A pointer moving twice as fast finishes
                       exactly when the slow one is at the
                       halfway point
    Optimal         →  One O(n) pass with slow (1 step) and fast
                       (2 steps) pointers, O(1) extra space

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🐢 SECTION 5 — APPROACH 1 — BRUTE FORCE (Two-Pass: Count + Walk)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    First pass: walk the entire list to count its length. Second
    pass: walk exactly length // 2 steps from head to land on
    the middle node (which, for even lengths, is naturally the
    SECOND middle due to integer division).

  Pseudocode:
    step 1: length = 0; curr = head
    step 2: while curr: length += 1; curr = curr.next
    step 3: curr = head
    step 4: for _ in range(length // 2): curr = curr.next
    step 5: return curr

  Time  : O(n)  →  Why: one pass to count, one pass to walk —
                        both linear, combined still O(n)
  Space : O(1)  →  Why: only a length counter and a pointer

  ಇದು ಯಾಕೆ ಸಾಕಾಗಲ್ಲ?
    → Correct and O(n) time overall, but requires traversing the
      list TWICE — the slow/fast approach gets the same answer
      in a single traversal.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🚀 SECTION 6 — OPTIMAL (Slow/Fast Pointers, Single Pass)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    Start both slow and fast at head. Advance slow by one step
    and fast by two steps, together, as long as fast and
    fast.next both exist. When the loop ends (fast can't move
    two more steps), slow is sitting exactly at the middle node.

  Key steps:
    1. slow = fast = head
    2. while fast and fast.next:
    3.     slow = slow.next
    4.     fast = fast.next.next
    5. return slow

  ಕನ್ನಡದಲ್ಲಿ ಒಂದು ಸಲ ಹೇಳಿ:
    → "slow pointer ಅನ್ನ 1 step, fast pointer ಅನ್ನ 2 step ಅಂತ
       ಒಟ್ಟಿಗೆ ಮುಂದೆ ಸಾಗಿಸು. fast ಇನ್ನೂ ಮುಂದೆ ಹೋಗೋಕಾಗ್ದಿದ್ರೆ
       (ಅಥವಾ fast.next ಇಲ್ದಿದ್ರೆ) ಅಲ್ಲೇ ನಿಲ್ಲಿಸು — ಆ ಹೊತ್ತಿಗೆ
       slow ಇರೋ ಜಾಗವೇ middle!"

  Time  : O(n)  →  Why: a single linear pass — fast makes at
                        most n/2 iterations
  Space : O(1)  →  Why: only two pointer variables, no counting
                        or extra storage

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🔍 SECTION 7 — DRY RUN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Input: head = [1,2,3,4,5,6] (even length, 6 nodes)

  Start: slow = 1, fast = 1

  Iteration 1:
    fast and fast.next exist (1 and 2)
    slow = 2, fast = 3

  Iteration 2:
    fast and fast.next exist (3 and 4)
    slow = 3, fast = 5

  Iteration 3:
    fast and fast.next exist (5 and 6)
    slow = 4, fast = None (6.next is None)

  Check loop condition: fast is None → loop exits

  Output: slow = node valued 4 → [4,5,6] ✓ matches expected
          (the SECOND middle for an even-length list)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 ⚠️ SECTION 8 — EDGE CASES — ಇವನ್ನ ಮರೆಯಬೇಡ!
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  ✓ Single node?                  →  slow never moves — returns
                                      that single node itself
  ✓ Two nodes?                    →  fast moves once and
                                      exhausts the list — slow
                                      lands on the SECOND node
  ✓ Odd length (e.g. 5 nodes)?    →  slow lands on the exact
                                      middle, no ambiguity
  ✓ Even length (e.g. 6 nodes)?   →  slow lands on the SECOND
                                      of the two middle nodes
  ✓ Very long list (100 nodes,
    max constraint)?              →  handled identically — O(n)
                                      single pass regardless of
                                      size

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📊 SECTION 9 — COMPLEXITY SUMMARY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                              Time    Space
  Brute (count then walk)      O(n)    O(1)   (two traversals)
  Slow/Fast single pass         O(n)    O(1)   ← use this ✅
                                                (one traversal)

  Time yaake O(n)?  → Fast makes at most n/2 iterations, each
                       O(1) work
  Space yaake O(1)? → Only two pointer variables, regardless of
                       list size

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🎯 SECTION 10 — PATTERN LEARNED — ಇದರಿಂದ ಕಲಿತದ್ದು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Pattern Name: Slow/Fast Pointers for Midpoint-Finding

  Ee pattern yaavaaga use maadabeeku?
  → Any linked-list problem needing the middle (or a fractional
     position) WITHOUT a separate length-counting pass — a
     pointer moving at k times the speed of another finds the
     1/k position when it exhausts the list
  → Foundation technique reused inside bigger problems: Sort
     List #148 (split in half), Reorder List #143 (find middle
     before reversing second half), Palindrome Linked List #234

  Idee pattern beere problemsalli kaanisatte:
  → Sort List #148 — uses this exact slow/fast midpoint-finding
     as its FIRST step before recursively sorting each half
  → Reorder List #143 — same midpoint trick before reversing the
     second half and merging alternately
  → Linked List Cycle #141 / #142 — same slow(1)/fast(2) pointer
     mechanics, but used for loop DETECTION instead of midpoint

  Next time intaha problem bandre naanu modalu idannu think maadtene:
  → "List na middle beku antadre, length count madi eradu pass
     maadodu bedi — slow (1 step) fast (2 step) pointer ondhe
     pass alli odhsi, fast list mugiside slow exactly middle
     lli iruttade!"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🗣️ SECTION 11 — INTERVIEWALLI HEGE EXPLAIN MAADABEEKU
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  1. Understand:
     "Return the middle node of a singly linked list — for even
      length, return the SECOND of the two middle nodes."

  2. Brute force:
     "Count the length in one pass, then walk length // 2 steps
      from head in a second pass. O(n) time, O(1) space, but two
      traversals."

  3. Optimize:
     "Use slow/fast pointers in a single pass. slow moves 1
      step, fast moves 2. When fast can't advance two more steps,
      slow is exactly at the middle."

  4. Code:
     "slow = fast = head. While fast and fast.next exist: advance
      slow by 1, fast by 2. Return slow once the loop exits."

  5. Complexity:
     "Time O(n) — a single pass, fast makes at most n/2
      iterations. Space O(1) — just two pointers."

  Mukhya: whenever you need a FRACTION of a list's length (half,
          a third, etc.) without knowing the length upfront, a
          pointer moving at a proportional speed finds it in one
          pass — no separate counting pass needed!
"""


# ─── Linked List Node Definition ──────────────────────────────────
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# ─── Helper: build a linked list from a Python list ───────────────
def build(values):
    head = None
    tail = None
    for v in values:
        node = ListNode(v)
        if not head:
            head = node
            tail = node
        else:
            tail.next = node
            tail = node
    return head


# ─── Helper: convert a linked list back to a Python list ──────────
def to_list(head):
    result = []
    curr = head
    while curr:
        result.append(curr.val)
        curr = curr.next
    return result


# ═══════════════════════════════════════════════════════════════════
# BRUTE FORCE — O(n) Time | O(1) Space (two passes: count + walk)
# ═══════════════════════════════════════════════════════════════════
def middle_node_brute(head):
    """
    Idu modala aaloochane — modalu length count madu, aamele
    length // 2 sala walk madi middle ge hogu
    """
    length = 0
    curr = head
    while curr:
        length += 1
        curr = curr.next

    curr = head
    for _ in range(length // 2):
        curr = curr.next

    return curr


# ═══════════════════════════════════════════════════════════════════
# OPTIMAL — O(n) Time | O(1) Space (slow/fast, single pass)
# ═══════════════════════════════════════════════════════════════════
def middle_node(head):
    """
    Idu final answer — slow (1 step) fast (2 step) pointer
    ondhe pass alli odhsi, fast mugiside slow middle lli iruttade
    """
    slow = fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow


# ═══════════════════════════════════════════════════════════════════
# TEST CASES
# ═══════════════════════════════════════════════════════════════════
if __name__ == "__main__":
    # Test 1 — Basic odd length (LeetCode example 1)
    head = build([1, 2, 3, 4, 5])
    assert to_list(middle_node(head)) == [3, 4, 5]

    # Test 2 — Even length, return SECOND middle (LeetCode example 2)
    head = build([1, 2, 3, 4, 5, 6])
    assert to_list(middle_node(head)) == [4, 5, 6]

    # Test 3 — Single node
    head = build([1])
    assert to_list(middle_node(head)) == [1]

    # Test 4 — Two nodes
    head = build([1, 2])
    assert to_list(middle_node(head)) == [2]

    # Test 5 — Three nodes (odd)
    head = build([1, 2, 3])
    assert to_list(middle_node(head)) == [2, 3]

    # Test 6 — Larger even length
    head = build([1, 2, 3, 4, 5, 6, 7, 8])
    assert to_list(middle_node(head)) == [5, 6, 7, 8]

    # Cross-check: brute force must agree on all of the above
    head = build([1, 2, 3, 4, 5])
    assert to_list(middle_node_brute(head)) == [3, 4, 5]

    head = build([1, 2, 3, 4, 5, 6])
    assert to_list(middle_node_brute(head)) == [4, 5, 6]

    head = build([1])
    assert to_list(middle_node_brute(head)) == [1]

    head = build([1, 2])
    assert to_list(middle_node_brute(head)) == [2]

    head = build([1, 2, 3])
    assert to_list(middle_node_brute(head)) == [2, 3]

    head = build([1, 2, 3, 4, 5, 6, 7, 8])
    assert to_list(middle_node_brute(head)) == [5, 6, 7, 8]

    print("All tests passed!")
