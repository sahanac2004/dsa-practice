"""
╔══════════════════════════════════════════════════════════════════╗
║  REORDER LIST                                                    ║
║  LeetCode #143  |  Difficulty: Medium  |  Topic: Linked Lists    ║
║  Link: https://leetcode.com/problems/reorder-list/               ║
╚══════════════════════════════════════════════════════════════════╝

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📘 SECTION 1 — PROBLEM UNDERSTANDING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  You are given the head of a singly linked list, containing
  nodes L0 → L1 → L2 → ... → Ln-1 → Ln.

  Reorder it IN PLACE to be:
    L0 → Ln → L1 → Ln-1 → L2 → Ln-2 → ...

  You may NOT modify node values — only rearrange the nodes
  themselves (rewire the `next` pointers).

  Input : head = first node of linked list
  Output: None (reorder in place; LeetCode checks the mutated list)

  Example 1 — basic (even length):
    Input : 1 → 2 → 3 → 4 → None
    Output: 1 → 4 → 2 → 3 → None
    Why?  : first node, then last, then second, then
            second-to-last — alternating from both ends inward

  Example 2 — slightly tricky (odd length):
    Input : 1 → 2 → 3 → 4 → 5 → None
    Output: 1 → 5 → 2 → 4 → 3 → None
    Why?  : same alternating pattern; the middle node (3) ends
            up last since there's no further pair to interleave

  Constraints:
    - 1 <= number of nodes <= 5 * 10^4
    - 1 <= Node.val <= 1000

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🧠 SECTION 2 — KANGLISH THINKING — ಹೇಗೆ ಯೋಚಿಸಬೇಕು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  Problem odi aada mele namma brain enu think maadabeeku:

  ಹಂತ 1 — Problem ಅರ್ಥ ಮಾಡಿಕೊಳ್ಳಿ
  ┌─────────────────────────────────────────────────────────┐
  │  Input ಏನು ಕೊಡ್ತಾರೆ?  →  linked list head node          │
  │  Output ಏನು ಬೇಕು?     →  in-place reorder: first, last,  │
  │                           second, second-last, ...        │
  │  Constraints ಏನಿದೆ?   →  values ಬದಲಾಯಿಸಬಾರದು, ಬರೀ       │
  │                           pointers rewire ಮಾಡಬೇಕು         │
  └─────────────────────────────────────────────────────────┘

  ಹಂತ 2 — ಇದನ್ನ previous problems (#206 Reverse LL, #234
           Palindrome LL) ಜೊತೆ connect ಮಾಡಿ ನೋಡಿ!
  →  #234 ರಲ್ಲಿ "second half reverse ಮಾಡಿ, ಎಡ-ಬಲ ಗಳನ್ನ
     compare ಮಾಡಿದ್ವಿ" — ಇಲ್ಲಿ ಕೂಡ "second half reverse" ಬೇಕು,
     ಆದ್ರೆ compare ಬದಲು MERGE ಮಾಡಬೇಕು!
  →  So idea: middle find ಮಾಡಿ, second half reverse ಮಾಡಿ,
     ಆಮೇಲೆ ಎರಡೂ halves ಅನ್ನ ALTERNATELY ಜೋಡಿಸಿ

  ಹಂತ 3 — ಮೊದಲ simple idea ಏನು?
  →  ಎಲ್ಲಾ nodes ಅನ್ನ ಒಂದು list (array) ಗೆ collect ಮಾಡಿ
  →  ಎಡ pointer i=0, ಬಲ pointer j=n-1 ಇಟ್ಟುಕೊಂಡು, ಪ್ರತಿ ಸಲ
     nodes[i].next = nodes[j], ನಂತರ i++, ಆಮೇಲೆ nodes[j].next =
     nodes[i] (next left), j-- — ಹೀಗೆ alternate ಆಗಿ ಜೋಡಿಸಿ

  ಹಂತ 4 — Optimal (O(1) extra space) ಹೇಗೆ?
  →  Step 1: slow/fast pointers ಬಳಸಿ MIDDLE find ಮಾಡಿ (#876
     ರಲ್ಲಿ ಬಳಸಿದ ಅದೇ technique!)
  →  Step 2: list ಅನ್ನ ಎರಡು ಭಾಗ ಮಾಡಿ, second half ಅನ್ನ
     REVERSE ಮಾಡಿ (#206 ರ three-pointer reversal!)
  →  Step 3: ಎರಡೂ halves ಅನ್ನ ALTERNATE ಆಗಿ merge ಮಾಡಿ
     (first1→first2→second1→second2→...)

  ಹಂತ 5 — Technique ಯಾಕೆ ಇಲ್ಲಿ ಕೆಲಸ ಮಾಡುತ್ತೆ?
  →  Second half ಅನ್ನ reverse ಮಾಡಿದ ಮೇಲೆ, ಅದರ ಮೊದಲ node ಕೊನೆಯ
     original node ಆಗಿರುತ್ತೆ (Ln) — ಇದೇ ನಮಗೆ ಬೇಕಾಗಿರೋ "Ln,
     Ln-1, ..." ಕ್ರಮ!
  →  ಎರಡೂ halves ಅನ್ನ ಒಂದೊಂದೇ node ಆಗಿ alternate ಮಾಡಿ ಜೋಡಿಸಿದ್ರೆ,
     ಬೇಕಾದ L0,Ln,L1,Ln-1,... pattern ತಾನಾಗೇ ಸಿಗುತ್ತೆ!

  💡 Interview ನಲ್ಲಿ ಹೇಗೆ ಮಾತಾಡಬೇಕು:
  →  "Find the middle with slow/fast pointers"
  →  "Split into two halves, reverse the second half"
  →  "Merge the two halves node-by-node, alternating between them"
  →  "This reuses the exact reversal technique from Reverse
      Linked List, and the middle-finding from Middle of the
      Linked List"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🏷️ SECTION 3 — TECHNIQUE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Primary   : Find Middle (slow/fast) + Reverse Second Half + Merge
  Secondary : Collect nodes into an array, two-pointer rewiring

  WHY find-middle + reverse + merge?
  → It reuses two already-mastered linked-list techniques
    (slow/fast middle-finding, three-pointer reversal) and
    combines them with a simple alternating merge — no extra
    array needed, true O(1) extra space.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 💡 SECTION 4 — INTUITION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  The key insight: the target order L0, Ln, L1, Ln-1, L2, ... is
  exactly what you get by zig-zagging between the FRONT half
  (in its original order) and the BACK half (in REVERSED order).
  Reversing the second half turns "walk backward from the end"
  into "walk forward from a new head" — then merging the two
  halves one node at a time, alternating sides, produces the
  exact target sequence.

  The journey from brute to optimal:
    Brute thought   →  Collect every node into an array, then
                       use two pointers (front/back) over the
                       array to rewire next pointers in the
                       target order
    Problem with it →  O(n) extra space for the array of node
                       references
    Better question →  "Can I avoid the array by physically
                       splitting and reversing half the list?"
    Insight         →  Reversing the second half turns it into a
                       forward-walkable sequence ending where we
                       need it to start
    Optimal         →  Find middle (O(n)) + reverse half (O(n))
                       + merge (O(n)) = O(n) time, O(1) extra space

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🐢 SECTION 5 — APPROACH 1 — BRUTE FORCE (collect into array)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    Walk the list once, storing every node reference in an
    array. Then use two pointers — one starting at the front,
    one at the back — to rewire `next` pointers in the target
    alternating order.

  Pseudocode:
    step 1: nodes = [all node references in order]
    step 2: i, j = 0, len(nodes) - 1
    step 3: while i < j:
    step 4:   nodes[i].next = nodes[j]
    step 5:   i += 1
    step 6:   if i == j: break
    step 7:   nodes[j].next = nodes[i]
    step 8:   j -= 1
    step 9: nodes[i].next = None

  Time  : O(n)  →  Why: one pass to collect, one pass to rewire
  Space : O(n)  →  Why: array holding every node reference

  ಇದು ಯಾಕೆ ಸಾಕಾಗಲ್ಲ?
    → Correct and O(n) time, but allocates an O(n) array just to
      get positional access — the optimal approach gets the same
      positional access via physically reversing half the list,
      with zero extra array.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🚀 SECTION 6 — APPROACH 2 — OPTIMAL (Middle + Reverse + Merge)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    1. Find the middle using slow/fast pointers.
    2. Split the list into two halves at the middle; reverse
       the second half using the standard three-pointer reversal.
    3. Merge the two halves by alternating nodes: take one from
       the first half, then one from the second, repeat.

  Key steps:
    1. slow, fast = head, head
       while fast and fast.next: slow = slow.next; fast = fast.next.next
    2. second = slow.next; slow.next = None   # split
    3. reverse `second` in place (3-pointer dance)
    4. first, second = head, reversed_second
       while second:
         tmp1, tmp2 = first.next, second.next
         first.next = second
         second.next = tmp1
         first, second = tmp1, tmp2

  ಕನ್ನಡದಲ್ಲಿ ಒಂದು ಸಲ ಹೇಳಿ:
    → "slow/fast ಬಳಸಿ middle find ಮಾಡಿ, list ಅನ್ನ ಎರಡು ಭಾಗ
       ಮಾಡಿ. second half ಅನ್ನ reverse ಮಾಡಿ. ಆಮೇಲೆ ಎರಡೂ halves
       ಇಂದ ಒಂದೊಂದೇ node ತಗೊಂಡು alternate ಆಗಿ ಜೋಡಿಸಿ — first ರ
       next = second ರ node, second ರ next = first ರ ಮುಂದಿನ
       node — ಹೀಗೆ ಮುಂದುವರಿಸಿ!"

  Time  : O(n)  →  Why: finding middle, reversing half, and
                        merging are each a single O(n) pass
  Space : O(1)  →  Why: only a handful of pointers — no array,
                        no recursion

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🔍 SECTION 7 — DRY RUN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Input: 1 → 2 → 3 → 4 → None

  Step 1 — find middle (slow/fast):
    slow ends at node 2 (for even length, slow lands on the
    first node of the second half's predecessor)

  Step 2 — split:
    first half:  1 → 2 → None
    second half: 3 → 4 → None

  Step 3 — reverse second half:
    second half becomes: 4 → 3 → None

  Step 4 — merge alternately:
    first=1, second=4 → 1.next=4, 4.next=2 (saved first.next)
    first=2, second=3 → 2.next=3, 3.next=None (saved second.next)
    first=None → loop ends

  Result: 1 → 4 → 2 → 3 → None

  Output: 1 → 4 → 2 → 3 → None ✓

  ಇನ್ನೊಂದು example — odd length:
  Input: 1 → 2 → 3 → 4 → 5 → None

  Middle lands on node 3. Split:
    first half:  1 → 2 → 3 → None
    second half: 4 → 5 → None
  Reverse second half: 5 → 4 → None
  Merge: 1→5, 5→2, 2→4, 4→3, 3→None

  Output: 1 → 5 → 2 → 4 → 3 → None ✓

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 ⚠️ SECTION 8 — EDGE CASES — ಇವನ್ನ ಮರೆಯಬೇಡ!
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  ✓ Single node [1]?               →  [1] — nothing to reorder
  ✓ Two nodes [1,2]?               →  [1,2] — already "reordered"
                                       (L0, L1 with no distinct Ln)
  ✓ Odd length [1,2,3,4,5]?        →  middle node ends up last,
                                       as shown above
  ✓ Even length [1,2,3,4]?         →  clean alternation, no
                                       leftover middle node
  ✓ Longer list, many alternations? →  pattern continues correctly
                                        until one half runs out

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📊 SECTION 9 — COMPLEXITY SUMMARY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                              Time    Space
  Brute (array of nodes)     O(n)    O(n)
  Optimal (mid+reverse+merge) O(n)    O(1)   ← use this ✅

  Time yaake O(n)?  → Three linear passes (find middle, reverse
                       half, merge) — still O(n) overall
  Space yaake O(1)? → Only pointer variables — no array, no
                       recursion stack

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🎯 SECTION 10 — PATTERN LEARNED — ಇದರಿಂದ ಕಲಿತದ್ದು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Pattern Name: Find-Middle + Reverse-Half + Merge (Linked List Combo)

  Ee pattern yaavaaga use maadabeeku?
  → Any problem needing to "work from both ends toward the
     middle" on a SINGLY linked list, where array/two-pointer
     tricks don't directly apply (no backward traversal) —
     reverse the back half to make it forward-walkable instead
  → Combines three building-block techniques you've already
     mastered: slow/fast middle-finding, three-pointer reversal,
     and simple node-by-node merging

  Idee pattern beere problemsalli kaanisatte:
  → Reverse Linked List #206 (the reversal half of this combo)
  → Palindrome Linked List #234 (same mid+reverse idea, used for
     comparison instead of merging)
  → Sort List #148 (next in curriculum — merge sort on a linked
     list, reuses the "merge two halves" idea in a different way)

  Next time intaha problem bandre naanu modalu idannu think maadtene:
  → "Singly linked list alli 'both ends toward middle' kelidre →
     slow/fast middle find madi, second half reverse madi,
     forward-walkable aagutte — aamele simple merge!"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🗣️ SECTION 11 — INTERVIEWALLI HEGE EXPLAIN MAADABEEKU
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  1. Understand:
     "Rearrange a singly linked list in place into the pattern
      first, last, second, second-last, ... without changing
      node values."

  2. Brute force:
     "Collect all nodes into an array, then rewire next pointers
      using two pointers from both ends of the array. O(n) time,
      O(n) space."

  3. Optimize:
     "Find the middle with slow/fast pointers, split the list
      there, reverse the second half, then merge the two halves
      one node at a time, alternating sides. O(1) extra space."

  4. Code:
     "Standard slow/fast middle-find. Split. Reuse the 3-pointer
      reversal on the second half. Merge loop: save both next
      pointers before rewiring, alternate first/second."

  5. Complexity:
     "Time O(n) — three linear passes. Space O(1) — pointers
      only, no array or recursion."

  Mukhya: this problem is a direct COMBO of two techniques you
          already know (middle-finding + reversal) plus a simple
          merge — recognize the building blocks before reaching
          for an array!
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
# BRUTE FORCE — O(n) Time | O(n) Space (collect into array)
# ═══════════════════════════════════════════════════════════════════
def reorder_list_brute(head):
    """
    Idu modala aaloochane — ella nodes ondu array ge collect
    madi, two pointers (front/back) bhalasi next rewire madu
    """
    if not head:
        return

    nodes = []
    curr = head
    while curr:
        nodes.append(curr)
        curr = curr.next

    i, j = 0, len(nodes) - 1
    while i < j:
        nodes[i].next = nodes[j]
        i += 1
        if i == j:
            break
        nodes[j].next = nodes[i]
        j -= 1

    nodes[i].next = None


# ═══════════════════════════════════════════════════════════════════
# OPTIMAL — O(n) Time | O(1) Space (find middle + reverse + merge)
# ═══════════════════════════════════════════════════════════════════
def reorder_list(head):
    """
    Idu final answer — slow/fast middle find madi, second half
    reverse madi, eradu halves alternate aagi merge madu
    """
    if not head or not head.next:
        return

    # Step 1: find the middle (slow/fast pointers)
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # Step 2: split into two halves
    second = slow.next
    slow.next = None
    first = head

    # Step 3: reverse the second half (three-pointer reversal)
    prev = None
    curr = second
    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    second = prev

    # Step 4: merge the two halves, alternating nodes
    while second:
        tmp1 = first.next
        tmp2 = second.next
        first.next = second
        second.next = tmp1
        first = tmp1
        second = tmp2


# ═══════════════════════════════════════════════════════════════════
# TEST CASES
# ═══════════════════════════════════════════════════════════════════
if __name__ == "__main__":
    # Test 1 — Even length
    head = build([1, 2, 3, 4])
    reorder_list(head)
    assert to_list(head) == [1, 4, 2, 3]

    # Test 2 — Odd length
    head = build([1, 2, 3, 4, 5])
    reorder_list(head)
    assert to_list(head) == [1, 5, 2, 4, 3]

    # Test 3 — Single node
    head = build([1])
    reorder_list(head)
    assert to_list(head) == [1]

    # Test 4 — Two nodes
    head = build([1, 2])
    reorder_list(head)
    assert to_list(head) == [1, 2]

    # Test 5 — Longer list
    head = build([1, 2, 3, 4, 5, 6])
    reorder_list(head)
    assert to_list(head) == [1, 6, 2, 5, 3, 4]

    # Cross-check: brute force must agree on all of the above
    head = build([1, 2, 3, 4])
    reorder_list_brute(head)
    assert to_list(head) == [1, 4, 2, 3]

    head = build([1, 2, 3, 4, 5])
    reorder_list_brute(head)
    assert to_list(head) == [1, 5, 2, 4, 3]

    head = build([1])
    reorder_list_brute(head)
    assert to_list(head) == [1]

    head = build([1, 2])
    reorder_list_brute(head)
    assert to_list(head) == [1, 2]

    head = build([1, 2, 3, 4, 5, 6])
    reorder_list_brute(head)
    assert to_list(head) == [1, 6, 2, 5, 3, 4]

    print("All tests passed!")
