"""
╔══════════════════════════════════════════════════════════════════╗
║  ODD EVEN LINKED LIST                                            ║
║  LeetCode #328  |  Difficulty: Medium  |  Topic: Linked Lists  ║
║  Link: https://leetcode.com/problems/odd-even-linked-list/      ║
╚══════════════════════════════════════════════════════════════════╝

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📘 SECTION 1 — PROBLEM UNDERSTANDING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Given the head of a singly linked list, group all the nodes
  with ODD indices together followed by the nodes with EVEN
  indices, and return the reordered list.

  The first node is considered ODD-indexed, the second node is
  EVEN-indexed, and so on (1-indexed, NOT 0-indexed). The
  relative order inside the odd group and inside the even group
  must be preserved — this is NOT a sort, just a regrouping.

  Input : head = singly linked list
  Output: head of the list with odd-indexed nodes first,
          followed by even-indexed nodes, both in original order

  Example 1 — basic:
    Input : head = [1,2,3,4,5]
    Output: [1,3,5,2,4]
    Why?  : odd-indexed nodes (1st,3rd,5th) = 1,3,5
            even-indexed nodes (2nd,4th) = 2,4
            concatenated: 1,3,5,2,4

  Example 2 — even count:
    Input : head = [2,1,3,5,6,4,7]
    Output: [2,3,6,7,1,5,4]
    Why?  : odd-indexed (1st,3rd,5th,7th) = 2,3,6,7
            even-indexed (2nd,4th,6th) = 1,5,4
            concatenated: 2,3,6,7,1,5,4

  Constraints:
    - 0 <= number of nodes <= 10^4
    - -10^6 <= Node.val <= 10^6
    - MUST solve in O(1) extra space, O(n) time

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🧠 SECTION 2 — KANGLISH THINKING — ಹೇಗೆ ಯೋಚಿಸಬೇಕು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  Problem odi aada mele namma brain enu think maadabeeku:

  ಹಂತ 1 — Problem ಅರ್ಥ ಮಾಡಿಕೊಳ್ಳಿ
  ┌─────────────────────────────────────────────────────────┐
  │  Input ಏನು ಕೊಡ್ತಾರೆ?  →  singly linked list              │
  │  Output ಏನು ಬೇಕು?     →  odd-indexed nodes (1,3,5...)     │
  │                           ಮೊದಲು, even-indexed (2,4,6...) │
  │                           ಆಮೇಲೆ — ಒಳಗಿನ order maintain     │
  │  Constraints ಏನಿದೆ?   →  O(1) space, O(n) time            │
  └─────────────────────────────────────────────────────────┘

  ಹಂತ 2 — ಯಾಕೆ ಇದು tricky? "position prakara group ಮಾಡೋದು
           ಹೇಗೆ, extra space ಇಲ್ಲದೇ?" ಅಂತ ಯೋಚಿಸಿ
  →  position (index) ಅನ್ನ ಟ್ರ್ಯಾಕ್ ಮಾಡ್ಬೇಕು, ಆದ್ರೆ node ಅನ್ನ
     MOVE ಮಾಡೋಕೆ array ಬೇಡ — ಇರೋ nodes ಅನ್ನೇ pointer rewiring
     ಮಾಡಿ ಬೇರ್ಪಡಿಸಿದ್ರೆ ಸಾಕು

  ಹಂತ 3 — ಮೊದಲ simple idea (brute force) ಏನು?
  →  "ಎಲ್ಲಾ values ಅನ್ನ array ಗೆ ಹಾಕಿ, odd index values + even
      index values ಅಂತ ಬೇರ್ಪಡಿಸಿ, ಮತ್ತೆ list ಕಟ್ಟಿದ್ರೆ?"
  →  ಕೆಲಸ ಆಗುತ್ತೆ, ಆದ್ರೆ O(n) extra space ಬೇಕಾಗುತ್ತೆ array ಗೆ

  ಹಂತ 4 — Optimal idea ಹೇಗೆ ಬರುತ್ತೆ?
  →  "ಎರಡು ಪ್ರತ್ಯೇಕ pointer (odd, even) ಇಟ್ಟುಕೊಂಡು, ಪ್ರತಿ node
      ಅನ್ನ ONE node ahead ಗೆ ಜೋಡಿಸಿದ್ರೆ?" ಅಂತ ಯೋಚಿಸಿ: odd.next =
      odd.next.next (ಮುಂದಿನ odd node ಗೆ skip), ಅದೇ ರೀತಿ even
      ಗೂ! ಕೊನೆಗೆ odd chain ಕೊನೆಗೆ even chain ಅನ್ನ ಜೋಡಿಸಿ
  →  ಇದಕ್ಕೆ ಎಕ್ಸ್ಟ್ರಾ array ಬೇಡ — ಇರೋ nodes ಅನ್ನೇ ಮರುಬಳಕೆ
     ಮಾಡ್ತಿದ್ದೀವಿ, ಕೇವಲ `next` pointers ಮಾತ್ರ ಬದಲಾಯಿಸ್ತಿದ್ದೀವಿ

  ಹಂತ 5 — Technique ಯಾಕೆ ಇಲ್ಲಿ ಕೆಲಸ ಮಾಡುತ್ತೆ?
  →  "ಪ್ರತಿ node ಗೆ ಅದರ ಮುಂದಿನ SAME-PARITY node ಗೆ ಜಂಪ್ ಮಾಡಿಸೋದು"
     ಅಂದ್ರೆ, odd nodes ಗಳ ಒಳಗಿನ relative order, ಮತ್ತು even
     nodes ಗಳ ಒಳಗಿನ relative order ಸ್ವಾಭಾವಿಕವಾಗೇ ಉಳಿಯುತ್ತೆ
     (ಪ್ರತಿ chain ಒಳಗೆ ಮೂಲ sequence ಅಲ್ಲೇ ಇರೋದ್ರಿಂದ)

  💡 Interview ನಲ್ಲಿ ಹೇಗೆ ಮಾತಾಡಬೇಕು:
  →  "First approach: dump values into an array, separate by
      index parity, rebuild — O(n) time, O(n) space"
  →  "Optimal: two pointers, odd and even, each skipping ahead
      to the next node of the same parity. Splice the even
      chain onto the end of the odd chain. O(n) time, O(1) space"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🏷️ SECTION 3 — TECHNIQUE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Primary   : Two Interleaved Pointers (Skip-One) + Splice (O(1) space)
  Secondary : Extract to Array + Regroup by Parity + Rebuild (O(n) space)

  WHY Two Interleaved Pointers over Array Extraction?
  → Extracting to an array works but needs O(n) extra space to
    hold values temporarily. Since the list is already perfectly
    interleaved (odd, even, odd, even, ...), each pointer can
    simply "skip over" the opposite-parity node to reach its own
    next same-parity node — no extra storage needed, just
    rewiring `next` pointers in place.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 💡 SECTION 4 — INTUITION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  The key insight: the list already alternates odd, even, odd,
  even, ... by construction (position 1, 2, 3, 4, ...). That
  means "the next odd node" is always exactly TWO steps ahead of
  the current odd node (skipping over one even node), and
  likewise "the next even node" is two steps ahead of the
  current even node. So maintain two pointers — one walking the
  odd positions, one walking the even positions — each jumping
  two nodes at a time. Once both chains are built (still
  threaded through the ORIGINAL nodes), splice the even chain
  onto the tail of the odd chain.

  The journey from brute to optimal:
    Brute thought   →  Collect all values into an array, split
                       by position parity (odd-indexed first,
                       then even-indexed), rebuild the list
    Problem with it →  O(n) extra space for the array
    Better question →  "Can I rewire IN PLACE, since odd/even
                       positions already alternate perfectly?"
    Insight         →  Each odd node's "next odd node" is just
                       two hops away; same for even — no need to
                       extract anything
    Optimal         →  One O(n) pass with two pointers skipping
                       ahead by two, then a single splice,
                       O(1) extra space

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🐢 SECTION 5 — APPROACH 1 — BRUTE FORCE (Array + Regroup by Parity)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    Walk the list once, collecting all values into an array.
    Build a new array by first taking values at odd positions
    (1st, 3rd, 5th, ...), then values at even positions (2nd,
    4th, ...). Rebuild a fresh linked list from that array.

  Pseudocode:
    step 1: values = [all node values, in order]
    step 2: odd_vals = values[0::2]   (1-indexed odd positions)
    step 3: even_vals = values[1::2]  (1-indexed even positions)
    step 4: result_values = odd_vals + even_vals
    step 5: build and return a new linked list from result_values

  Time  : O(n)  →  Why: a constant number of linear scans over
                        the values
  Space : O(n)  →  Why: stores all values in intermediate lists
                        before rebuilding

  ಇದು ಯಾಕೆ ಸಾಕಾಗಲ್ಲ?
    → Correct and O(n) time, but uses O(n) extra space — the
      two-pointer approach reuses the original nodes directly
      and needs no extra storage for values.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🚀 SECTION 6 — OPTIMAL (Two Interleaved Pointers + Splice)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    Keep an `odd` pointer starting at head and an `even` pointer
    starting at head.next. Remember even_head (head.next) to
    splice onto the end later. Repeatedly: link odd to the node
    two steps ahead (skipping the even node), advance odd there;
    link even to the node two steps ahead (skipping the odd
    node), advance even there. Stop when even or even.next runs
    out. Finally, attach odd.next = even_head.

  Key steps:
    1. if not head or not head.next: return head
    2. odd = head
       even = head.next
       even_head = even
    3. while even and even.next:
           odd.next = even.next
           odd = odd.next
           even.next = odd.next
           even = even.next
    4. odd.next = even_head
       return head

  ಕನ್ನಡದಲ್ಲಿ ಒಂದು ಸಲ ಹೇಳಿ:
    → "odd pointer head ಲ್ಲಿ, even pointer head.next ಲ್ಲಿ
       ಇಟ್ಟುಕೊಂಡು, even_head ಅನ್ನ ನೆನಪಿಟ್ಟುಕೋ. ಪ್ರತಿ ಸಲ odd
       ಅನ್ನ ಅದರ ಮುಂದಿನ odd node ಗೆ (even ಅನ್ನ ಸ್ಕಿಪ್ ಮಾಡಿ)
       ಜೋಡಿಸಿ ಮುಂದೆ ಸಾಗಿಸು, ಅದೇ ರೀತಿ even ಅನ್ನೂ ಮುಂದಿನ even
       node ಗೆ ಜೋಡಿಸಿ ಮುಂದೆ ಸಾಗಿಸು. ಕೊನೆಗೆ odd chain ಕೊನೆಗೆ
       even_head ಅನ್ನ ಜೋಡಿಸು!"

  Time  : O(n)  →  Why: a single linear pass — each node is
                        visited exactly once across both pointers
  Space : O(1)  →  Why: only a handful of pointer variables, no
                        extra storage

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🔍 SECTION 7 — DRY RUN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Input: head = [1,2,3,4,5]

  Start:
    odd = 1, even = 2, even_head = 2

  Iteration 1 (even=2, even.next=3, both exist):
    odd.next = even.next → 1.next = 3
    odd = odd.next → odd = 3
    even.next = odd.next → 2.next = 4
    even = even.next → even = 4

  Iteration 2 (even=4, even.next=5, both exist):
    odd.next = even.next → 3.next = 5
    odd = odd.next → odd = 5
    even.next = odd.next → 4.next = None (5.next is None)
    even = even.next → even = None

  Loop check: even is None → loop exits

  Final splice:
    odd.next = even_head → 5.next = 2

  Chain: 1 -> 3 -> 5 -> 2 -> 4 -> None

  Output: [1,3,5,2,4] ✓ matches expected

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 ⚠️ SECTION 8 — EDGE CASES — ಇವನ್ನ ಮರೆಯಬೇಡ!
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  ✓ Empty list (None)?            →  return None immediately
  ✓ Single node?                  →  no head.next, return head
                                      as-is (nothing to regroup)
  ✓ Two nodes?                    →  odd=1st, even=2nd; loop
                                      body never runs (even.next
                                      is None), splice odd.next
                                      = even_head keeps order
  ✓ Odd total count (e.g. 5)?     →  last node is odd-indexed;
                                      even chain ends one node
                                      shorter, handled naturally
  ✓ Even total count (e.g. 7
    nodes → wait, use e.g. 6)?    →  last node is even-indexed;
                                      odd.next = None happens
                                      naturally via even.next
  ✓ Forgetting to save even_head
    BEFORE rewiring?              →  would lose the starting
                                      point of the even chain —
                                      MUST capture it before the
                                      loop begins

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📊 SECTION 9 — COMPLEXITY SUMMARY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                              Time    Space
  Brute (array regroup)        O(n)    O(n)
  Two pointers + splice          O(n)    O(1)   ← use this ✅

  Time yaake O(n)?  → One linear pass — the combined work of
                       both pointers visits each node exactly
                       once
  Space yaake O(1)? → Reuses the existing nodes — only a
                       constant number of pointer variables used

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🎯 SECTION 10 — PATTERN LEARNED — ಇದರಿಂದ ಕಲಿತದ್ದು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Pattern Name: Skip-One Interleaved Pointers (Bucket-by-Position)

  Ee pattern yaavaaga use maadabeeku?
  → Any linked-list problem asking to SEPARATE nodes by their
     POSITION (not value) while preserving each group's
     relative order — when the groups already alternate
     perfectly, each pointer can "skip ahead by two" directly,
     no dummy-head-per-condition check needed
  → Contrast with Partition List #86 (separates by VALUE
     condition, needs a per-node check) — here the grouping
     rule (odd/even position) is already baked into the
     alternating structure

  Idee pattern beere problemsalli kaanisatte:
  → Partition List #86 (two dummy-head chains — contrast:
     that's a value-based condition check per node, this is a
     position-based "always skip one" pattern)
  → Reverse Nodes in k-Group style problems — any time a list's
     STRUCTURE already alternates or repeats, pointers can jump
     fixed distances instead of doing conditional dummy-chain
     building

  Next time intaha problem bandre naanu modalu idannu think maadtene:
  → "Position (index) prakara group madabekagidre, mathu list
     already alternate aagide antadre → eradu pointer (odd,
     even) ittukondu, prathi sala TWO hops jump madi sariyada
     chain kattu, kodage splice madu — O(1) space alli
     regroup sigutte!"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🗣️ SECTION 11 — INTERVIEWALLI HEGE EXPLAIN MAADABEEKU
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  1. Understand:
     "Group odd-indexed nodes (1-indexed) before even-indexed
      nodes, preserving relative order within each group."

  2. Brute force:
     "Extract all values to an array, split by index parity,
      rebuild. O(n) time, O(n) space."

  3. Optimize:
     "Two pointers, odd and even, each starting one node apart.
      Each pointer skips two nodes ahead to reach its next
      same-parity node. Remember even's starting node, then
      splice it onto the end of the odd chain."

  4. Code:
     "odd = head, even = head.next, even_head = even. While even
      and even.next: relink odd.next to even.next and advance
      odd; relink even.next to odd.next and advance even. Finally
      odd.next = even_head."

  5. Complexity:
     "Time O(n) — one combined pass. Space O(1) — no extra
      storage, just rewiring existing nodes."

  Mukhya: when a list's groups already alternate in a fixed
          pattern (odd/even position, every k-th node, etc.),
          pointers can jump fixed distances directly — no
          conditional per-node dummy-chain logic needed!
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
# BRUTE FORCE — O(n) Time | O(n) Space (array regroup by parity)
# ═══════════════════════════════════════════════════════════════════
def odd_even_list_brute(head):
    """
    Idu modala aaloochane — values array ge haaki, odd/even
    index prakara bere maadi, aamele hosa list build madu
    """
    values = to_list(head)
    odd_vals = values[0::2]
    even_vals = values[1::2]
    return build(odd_vals + even_vals)


# ═══════════════════════════════════════════════════════════════════
# OPTIMAL — O(n) Time | O(1) Space (two interleaved pointers)
# ═══════════════════════════════════════════════════════════════════
def odd_even_list(head):
    """
    Idu final answer — odd, even pointer ittukondu TWO hops
    jump madi sariyada chain kattu, kodage splice madu
    """
    if not head or not head.next:
        return head

    odd = head
    even = head.next
    even_head = even

    while even and even.next:
        odd.next = even.next
        odd = odd.next
        even.next = odd.next
        even = even.next

    odd.next = even_head

    return head


# ═══════════════════════════════════════════════════════════════════
# TEST CASES
# ═══════════════════════════════════════════════════════════════════
if __name__ == "__main__":
    # Test 1 — Basic (LeetCode example 1)
    head = build([1, 2, 3, 4, 5])
    assert to_list(odd_even_list(head)) == [1, 3, 5, 2, 4]

    # Test 2 — LeetCode example 2
    head = build([2, 1, 3, 5, 6, 4, 7])
    assert to_list(odd_even_list(head)) == [2, 3, 6, 7, 1, 5, 4]

    # Test 3 — Empty list
    assert odd_even_list(None) is None

    # Test 4 — Single node
    head = build([1])
    assert to_list(odd_even_list(head)) == [1]

    # Test 5 — Two nodes
    head = build([1, 2])
    assert to_list(odd_even_list(head)) == [1, 2]

    # Test 6 — Even total count
    head = build([1, 2, 3, 4, 5, 6])
    assert to_list(odd_even_list(head)) == [1, 3, 5, 2, 4, 6]

    # Test 7 — Odd total count
    head = build([1, 2, 3, 4, 5, 6, 7])
    assert to_list(odd_even_list(head)) == [1, 3, 5, 7, 2, 4, 6]

    # Cross-check: brute force must agree on all of the above
    head = build([1, 2, 3, 4, 5])
    assert to_list(odd_even_list_brute(head)) == [1, 3, 5, 2, 4]

    head = build([2, 1, 3, 5, 6, 4, 7])
    assert to_list(odd_even_list_brute(head)) == [2, 3, 6, 7, 1, 5, 4]

    assert odd_even_list_brute(None) is None

    head = build([1])
    assert to_list(odd_even_list_brute(head)) == [1]

    head = build([1, 2])
    assert to_list(odd_even_list_brute(head)) == [1, 2]

    head = build([1, 2, 3, 4, 5, 6])
    assert to_list(odd_even_list_brute(head)) == [1, 3, 5, 2, 4, 6]

    head = build([1, 2, 3, 4, 5, 6, 7])
    assert to_list(odd_even_list_brute(head)) == [1, 3, 5, 7, 2, 4, 6]

    print("All tests passed!")
