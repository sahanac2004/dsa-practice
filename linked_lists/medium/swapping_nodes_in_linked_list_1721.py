"""
╔══════════════════════════════════════════════════════════════════╗
║  SWAPPING NODES IN A LINKED LIST                                  ║
║  LeetCode #1721  |  Difficulty: Medium  |  Topic: Linked Lists ║
║  Link: https://leetcode.com/problems/                           ║
║        swapping-nodes-in-a-linked-list/                          ║
╚══════════════════════════════════════════════════════════════════╝

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📘 SECTION 1 — PROBLEM UNDERSTANDING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Given the head of a singly linked list and an integer k,
  swap the VALUES of the k-th node from the beginning and the
  k-th node from the end (1-indexed), then return the head.

  Input : head = singly linked list, k = 1-indexed position
  Output: head of the list with those two nodes' VALUES swapped
          (only values swap — the nodes themselves stay in place)

  Example 1 — basic:
    Input : head = [1,2,3,4,5], k = 2
    Output: [1,4,3,2,5]
    Why?  : 2nd node from start = 2, 2nd node from end = 4 —
            swap their values

  Example 2 — k picks the same node (middle, odd length):
    Input : head = [7,9,6,6,7,8,3,0,9,5], k = 5
    Output: [7,9,6,6,8,7,3,0,9,5]
    Why?  : 5th from start = 7, 5th from end (6th position from
            start, since length=10) = 8 — swap their values

  Constraints:
    - 1 <= number of nodes <= 10^5
    - 1 <= Node.val <= 100
    - 1 <= k <= number of nodes

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🧠 SECTION 2 — KANGLISH THINKING — ಹೇಗೆ ಯೋಚಿಸಬೇಕು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  Problem odi aada mele namma brain enu think maadabeeku:

  ಹಂತ 1 — Problem ಅರ್ಥ ಮಾಡಿಕೊಳ್ಳಿ
  ┌─────────────────────────────────────────────────────────┐
  │  Input ಏನು ಕೊಡ್ತಾರೆ?  →  linked list ಮತ್ತು k (position)   │
  │  Output ಏನು ಬೇಕು?     →  k-th node from START ಮತ್ತು k-th  │
  │                           node from END ನ VALUES swap      │
  │  Constraints ಏನಿದೆ?   →  ನೋಡ್ಸ್ ಅಲ್ಲ, ಕೇವಲ VALUES swap     │
  └─────────────────────────────────────────────────────────┘

  ಹಂತ 2 — ಯಾಕೆ ಇದು tricky? "'from end' ಅಂದ್ರೆ ಎಲ್ಲಿ ಅಂತ length
           ಗೊತ್ತಿಲ್ಲದೇ ಹೇಗೆ ಗೊತ್ತಾಗುತ್ತೆ?" ಅಂತ ಯೋಚಿಸಿ
  →  "k-th from end" ಅಂದ್ರೆ ಮೊದಲು length ಗೊತ್ತಾಗ್ಬೇಕು, ಇಲ್ಲಾ
     ಬೇರೆ ಟ್ರಿಕ್ ಬೇಕು — linked list ಲ್ಲಿ "back ಇಂದ ಎಣಿಸೋದು"
     ನೇರವಾಗಿ ಆಗಲ್ಲ (array ಆಗಿದ್ರೆ length-k index ಗೆ ಹೋಗ್ಬಹುದಿತ್ತು)

  ಹಂತ 3 — ಮೊದಲ simple idea (brute force) ಏನು?
  →  "ಮೊದಲು list ಪೂರ್ತಿ walk ಮಾಡಿ length ಕಂಡುಹಿಡಿ, ಆಮೇಲೆ k-th
      from start ಗೆ, ಮತ್ತೆ (length - k + 1)-th from start (ಅಂದ್ರೆ
      k-th from end) ಗೆ ಪ್ರತ್ಯೇಕವಾಗಿ walk ಮಾಡಿದ್ರೆ?"
  →  ಕೆಲಸ ಆಗುತ್ತೆ, ಆದ್ರೆ list ಅನ್ನ ಬಹುಶಃ ಮೂರು ಸಲ traverse
     ಮಾಡ್ಬೇಕು (length ಗೆ, ಒಂದೊಂದು node ಗೆ)

  ಹಂತ 4 — Optimal idea (two pointer, one pass) ಹೇಗೆ ಬರುತ್ತೆ?
  →  "k-th from START ಗೆ ಮೊದಲೇ ಹುಡುಕ್ಬಿಡೋಣ (k steps ಮುಂದೆ ಹೋಗಿ).
      ಆಮೇಲೆ ಇನ್ನೊಂದು pointer ಅನ್ನ head ಇಂದ ಆ node ಜೊತೆ ಒಟ್ಟಿಗೆ
      ಮುಂದೆ ಸಾಗಿಸಿದ್ರೆ, ಮೊದಲ pointer list ಕೊನೆ ತಲುಪೋ ಹೊತ್ತಿಗೆ
      ಎರಡನೇ pointer EXACTLY k-th from end ಗೆ ತಲುಪಿರುತ್ತೆ!"
     (ಇದೇ 'Remove Nth Node from End' #19 ಲ್ಲಿ ಬಳಸಿದ ಗ್ಯಾಪ್
     ಟ್ರಿಕ್!)

  ಹಂತ 5 — Technique ಯಾಕೆ ಇಲ್ಲಿ ಕೆಲಸ ಮಾಡುತ್ತೆ?
  →  ಎರಡು pointer ಗಳ ಮಧ್ಯೆ ಇರೋ FIXED GAP (k nodes) ಇಟ್ಟುಕೊಂಡು
     ಇಬ್ಬರನ್ನೂ ಒಟ್ಟಿಗೆ ಮುಂದೆ ಸಾಗಿಸಿದ್ರೆ, ಮುಂದಿನ pointer list
     ಕೊನೆ ತಲುಪಿದಾಗ, ಹಿಂದಿನ pointer ಅ GAP ಅಷ್ಟೇ ಹಿಂದೆ ಇರುತ್ತೆ
     — ಅಂದ್ರೆ EXACTLY "from end" ಅ ಜಾಗ! ಇದಕ್ಕೆ length ಗೊತ್ತಿರೋ
     ಅಗತ್ಯ ಇಲ್ಲ, ಒಂದೇ pass ಸಾಕು

  💡 Interview ನಲ್ಲಿ ಹೇಗೆ ಮಾತಾಡಬೇಕು:
  →  "First approach: find length first, then walk to both
      positions separately — up to three traversals."
  →  "Optimal: find the k-th node from start by walking k steps.
      Then walk a SECOND pointer from head, in lockstep with a
      pointer that started at the k-th node, until that leading
      pointer hits the end — the second pointer is now exactly
      the k-th from the end. Swap values. One single pass plus
      the initial k steps."

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🏷️ SECTION 3 — TECHNIQUE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Primary   : Fixed-Gap Two Pointers, Single Pass (O(n) time, O(1) space)
  Secondary : Two-Pass (Count Length, Then Walk to Both Positions)

  WHY Fixed-Gap Two Pointers over Two-Pass?
  → The two-pass approach needs the exact length before it can
    compute "k-th from the end" as an index from the start —
    that's effectively two or more traversals. The fixed-gap
    technique (the same one used in Remove Nth Node From End
    #19) finds BOTH target nodes in a single combined pass: find
    the k-th-from-start node directly by counting, then march a
    second pointer from head in lockstep with a pointer
    continuing from there — when the leading one falls off the
    end, the trailing one is exactly k-th from the end.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 💡 SECTION 4 — INTUITION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  The key insight: finding the k-th node from the START is
  trivial — just walk k-1 steps. Finding the k-th node from the
  END is the hard part without knowing the length. But if you
  keep a pointer EXACTLY k nodes ahead of another, and slide
  both forward together until the leading one reaches the last
  node, the trailing one must be sitting exactly k nodes before
  the end — because the gap between them (k) stays constant the
  whole time. So: find first_node (k-th from start) during the
  initial walk, then start second_node at head and advance BOTH
  first_node and second_node together until first_node has no
  more next — second_node lands exactly where we need it.

  The journey from brute to optimal:
    Brute thought   →  Count the length, compute the from-end
                       node's index from the start, walk to both
                       the k-th node and that computed node
                       separately
    Problem with it →  Essentially multiple traversals of the list
    Better question →  "Can a FIXED GAP between two pointers find
                       the 'k-th from end' node without ever
                       knowing the length?"
    Insight         →  Yes — same mechanism as Remove Nth Node
                       From End #19: a constant gap between two
                       pointers automatically marks the from-end
                       position when the leading pointer exhausts
                       the list
    Optimal         →  One O(n) pass: walk k-1 steps to find
                       first_node, then advance a second pointer
                       from head alongside first_node (continuing
                       to walk it to the end) — swap their values

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🐢 SECTION 5 — APPROACH 1 — BRUTE FORCE (Count Length, Walk Twice)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    First pass: count the total length n. Compute the from-end
    node's position as (n - k + 1) counted from the start.
    Second pass: walk to the k-th node from start and swap its
    value with the node at position (n - k + 1), found via a
    separate walk from head.

  Pseudocode:
    step 1: length = 0; curr = head
    step 2: while curr: length += 1; curr = curr.next
    step 3: curr = head
    step 4: for _ in range(k - 1): curr = curr.next
    step 5: first_node = curr
    step 6: curr = head
    step 7: for _ in range(length - k): curr = curr.next
    step 8: second_node = curr
    step 9: first_node.val, second_node.val = second_node.val, first_node.val
    step 10: return head

  Time  : O(n)  →  Why: counting length plus two separate walks,
                        all still linear, combined O(n)
  Space : O(1)  →  Why: only a length counter and a pointer

  ಇದು ಯಾಕೆ ಸಾಕಾಗಲ್ಲ?
    → Correct and O(n) time overall, but conceptually walks the
      list up to THREE times (count, walk to first, walk to
      second) — the fixed-gap approach does it with ONE combined
      traversal.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🚀 SECTION 6 — OPTIMAL (Fixed-Gap Two Pointers, Single Pass)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    Walk a pointer `first_node` k-1 steps from head — this IS
    the k-th node from the start. Now start `second_node` at
    head, and ALSO keep advancing a copy of first_node (call it
    `runner`, continuing from where first_node stopped) to the
    end of the list, advancing second_node in lockstep. When
    runner falls off the end, second_node is exactly the k-th
    node from the end. Swap first_node.val and second_node.val.

  Key steps:
    1. first_node = head
       for _ in range(k - 1): first_node = first_node.next
    2. second_node = head
       runner = first_node
       while runner.next:
           runner = runner.next
           second_node = second_node.next
    3. first_node.val, second_node.val = second_node.val, first_node.val
    4. return head

  ಕನ್ನಡದಲ್ಲಿ ಒಂದು ಸಲ ಹೇಳಿ:
    → "ಮೊದಲು k-1 steps ಮುಂದೆ ಹೋಗಿ first_node (k-th from start)
       ಹುಡುಕು. ಆಮೇಲೆ second_node ಅನ್ನ head ಲ್ಲಿ ಇಟ್ಟು, ಒಂದು
       runner pointer ಅನ್ನ first_node ಇಂದ ಮುಂದೆ ಸಾಗಿಸುತ್ತಾ,
       second_node ಅನ್ನೂ ಒಟ್ಟಿಗೆ ಮುಂದೆ ಸಾಗಿಸು. runner list
       ಕೊನೆ ತಲುಪಿದಾಗ second_node EXACTLY k-th from end ಆಗಿರುತ್ತೆ
       — ಈಗ ಇವೆರಡರ values swap ಮಾಡು!"

  Time  : O(n)  →  Why: a single combined linear pass — k-1
                        steps plus one walk to the end
  Space : O(1)  →  Why: only a few pointer variables, no length
                        counter or extra storage

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🔍 SECTION 7 — DRY RUN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Input: head = [1,2,3,4,5], k = 2

  Step 1 — find first_node (k-th from start, k=2):
    first_node = head (val=1)
    loop runs (k-1)=1 time: first_node = first_node.next
    first_node = node valued 2

  Step 2 — find second_node (k-th from end) using runner:
    second_node = head (val=1)
    runner = first_node (val=2)

    runner.next exists (val=3):
      runner = 3, second_node = 2
    runner.next exists (val=4):
      runner = 4, second_node = 3
    runner.next exists (val=5):
      runner = 5, second_node = 4
    runner.next is None → loop exits

    second_node = node valued 4

  Step 3 — swap values:
    first_node.val (2) <-> second_node.val (4)
    first_node becomes 4, second_node becomes 2

  Chain: 1 -> 4 -> 3 -> 2 -> 5

  Output: [1,4,3,2,5] ✓ matches expected

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 ⚠️ SECTION 8 — EDGE CASES — ಇವನ್ನ ಮರೆಯಬೇಡ!
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  ✓ Single node, k=1?             →  first_node and second_node
                                      both end up being that same
                                      node — swapping it with
                                      itself is a harmless no-op
  ✓ k = 1 (first node from start
    and last node from end)?      →  handled naturally — no
                                      special casing needed
  ✓ k = length (last from start,
    first from end)?              →  also handled naturally —
                                      the gap logic works
                                      symmetrically
  ✓ k picks the exact middle
    (odd-length list)?            →  first_node and second_node
                                      coincide at the same node —
                                      swap is a no-op, correct
  ✓ Two-node list, k=1?           →  first_node = node 1,
                                      second_node ends up at
                                      node 2 — straightforward
                                      swap

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📊 SECTION 9 — COMPLEXITY SUMMARY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                                Time    Space
  Brute (count + walk twice)     O(n)    O(1)
  Fixed-gap two pointers          O(n)    O(1)   ← use this ✅
                                                  (one combined pass)

  Time yaake O(n)?  → k-1 steps to find first_node, plus a
                       single walk to the end for the gap — both
                       bounded by list length
  Space yaake O(1)? → Just a handful of pointer variables,
                       regardless of list size

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🎯 SECTION 10 — PATTERN LEARNED — ಇದರಿಂದ ಕಲಿತದ್ದು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Pattern Name: Fixed-Gap Two Pointers (From-the-End Finder)

  Ee pattern yaavaaga use maadabeeku?
  → ANY "k-th node/element from the end" problem on a linked
     list — maintain a constant gap of k nodes between two
     pointers; when the leading one exhausts the list, the
     trailing one is exactly at the from-end target
  → Works for finding, removing, or (as here) just reading a
     from-end position, all without ever needing the list's
     total length

  Idee pattern beere problemsalli kaanisatte:
  → Remove Nth Node From End #19 — the EXACT same fixed-gap
     mechanism, but deletes the from-end node instead of just
     reading/swapping its value
  → Any "distance from the end" variant of a linked-list problem

  Next time intaha problem bandre naanu modalu idannu think maadtene:
  → "k-th node FROM THE END beku antadre, length count madodu
     bedi — k nodes gap ittukondu eradu pointer ondhe pass alli
     odhsi, modalu pointer list mugiside, eradne pointer
     EXACTLY from-end position lli iruttade!"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🗣️ SECTION 11 — INTERVIEWALLI HEGE EXPLAIN MAADABEEKU
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  1. Understand:
     "Swap the VALUES (not the nodes) of the k-th node from the
      start and the k-th node from the end, 1-indexed."

  2. Brute force:
     "Count the length, compute the from-end position as an
      index from start, then walk to both positions separately.
      O(n) time overall but multiple traversals."

  3. Optimize:
     "Walk k-1 steps to find the k-th node from start
      (first_node). Then walk a second pointer from head, in
      lockstep with a runner continuing from first_node, until
      the runner reaches the end — the second pointer is now
      exactly k-th from the end."

  4. Code:
     "first_node = head, advance k-1 times. second_node = head,
      runner = first_node. While runner.next: advance both
      runner and second_node. Swap first_node.val and
      second_node.val."

  5. Complexity:
     "Time O(n) — one combined pass, k-1 steps plus a walk to
      the end. Space O(1) — just a few pointers."

  Mukhya: whenever a problem mentions 'from the end' on a linked
          list, think fixed-gap two pointers FIRST — it avoids
          ever needing to know the list's length, in a single
          pass!
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
# BRUTE FORCE — O(n) Time | O(1) Space (count length, walk twice)
# ═══════════════════════════════════════════════════════════════════
def swap_nodes_brute(head, k):
    """
    Idu modala aaloochane — modalu length count madu, aamele
    k-th from start mathu k-th from end ge bere bere walk madu
    """
    length = 0
    curr = head
    while curr:
        length += 1
        curr = curr.next

    curr = head
    for _ in range(k - 1):
        curr = curr.next
    first_node = curr

    curr = head
    for _ in range(length - k):
        curr = curr.next
    second_node = curr

    first_node.val, second_node.val = second_node.val, first_node.val

    return head


# ═══════════════════════════════════════════════════════════════════
# OPTIMAL — O(n) Time | O(1) Space (fixed-gap two pointers)
# ═══════════════════════════════════════════════════════════════════
def swap_nodes(head, k):
    """
    Idu final answer — k-1 steps hogi first_node hudu, aamele
    runner ondu second_node ondu lockstep alli odhsi second_node
    na k-th from end ge hudu, values swap madu
    """
    first_node = head
    for _ in range(k - 1):
        first_node = first_node.next

    second_node = head
    runner = first_node
    while runner.next:
        runner = runner.next
        second_node = second_node.next

    first_node.val, second_node.val = second_node.val, first_node.val

    return head


# ═══════════════════════════════════════════════════════════════════
# TEST CASES
# ═══════════════════════════════════════════════════════════════════
if __name__ == "__main__":
    # Test 1 — Basic (LeetCode example 1)
    head = build([1, 2, 3, 4, 5])
    assert to_list(swap_nodes(head, 2)) == [1, 4, 3, 2, 5]

    # Test 2 — LeetCode example 2 (longer list)
    head = build([7, 9, 6, 6, 7, 8, 3, 0, 9, 5])
    assert to_list(swap_nodes(head, 5)) == [7, 9, 6, 6, 8, 7, 3, 0, 9, 5]

    # Test 3 — Single node, k=1 (swap with itself, no-op)
    head = build([1])
    assert to_list(swap_nodes(head, 1)) == [1]

    # Test 4 — k=1 (first and last)
    head = build([1, 2, 3, 4, 5])
    assert to_list(swap_nodes(head, 1)) == [5, 2, 3, 4, 1]

    # Test 5 — k = length (same as k=1 case, symmetric)
    head = build([1, 2, 3, 4, 5])
    assert to_list(swap_nodes(head, 5)) == [5, 2, 3, 4, 1]

    # Test 6 — k picks the exact middle (odd length, no-op)
    head = build([1, 2, 3, 4, 5])
    assert to_list(swap_nodes(head, 3)) == [1, 2, 3, 4, 5]

    # Test 7 — Two nodes, k=1
    head = build([1, 2])
    assert to_list(swap_nodes(head, 1)) == [2, 1]

    # Cross-check: brute force must agree on all of the above
    head = build([1, 2, 3, 4, 5])
    assert to_list(swap_nodes_brute(head, 2)) == [1, 4, 3, 2, 5]

    head = build([7, 9, 6, 6, 7, 8, 3, 0, 9, 5])
    assert to_list(swap_nodes_brute(head, 5)) == [7, 9, 6, 6, 8, 7, 3, 0, 9, 5]

    head = build([1])
    assert to_list(swap_nodes_brute(head, 1)) == [1]

    head = build([1, 2, 3, 4, 5])
    assert to_list(swap_nodes_brute(head, 1)) == [5, 2, 3, 4, 1]

    head = build([1, 2, 3, 4, 5])
    assert to_list(swap_nodes_brute(head, 5)) == [5, 2, 3, 4, 1]

    head = build([1, 2, 3, 4, 5])
    assert to_list(swap_nodes_brute(head, 3)) == [1, 2, 3, 4, 5]

    head = build([1, 2])
    assert to_list(swap_nodes_brute(head, 1)) == [2, 1]

    print("All tests passed!")
