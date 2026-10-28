"""
╔══════════════════════════════════════════════════════════════════╗
║  PARTITION LIST                                                  ║
║  LeetCode #86  |  Difficulty: Medium  |  Topic: Linked Lists    ║
║  Link: https://leetcode.com/problems/partition-list/            ║
╚══════════════════════════════════════════════════════════════════╝

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📘 SECTION 1 — PROBLEM UNDERSTANDING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Given the head of a linked list and a value x, partition it
  such that all nodes LESS than x come before all nodes GREATER
  THAN OR EQUAL to x. The relative order of the nodes within
  each of the two partitions must be preserved (this is NOT a
  sort — it's a stable partition).

  Input : head = linked list, x = partition value
  Output: head of the partitioned list

  Example 1 — basic:
    Input : head = [1,4,3,2,5,2], x = 3
    Output: [1,2,2,4,3,5]
    Why?  : nodes < 3 in original order: 1,2,2
            nodes >= 3 in original order: 4,3,5
            concatenated: 1,2,2,4,3,5

  Example 2 — all equal partition value:
    Input : head = [2,1], x = 2
    Output: [1,2]
    Why?  : 1 < 2 goes first; 2 >= 2 goes second

  Constraints:
    - 0 <= number of nodes <= 200
    - -100 <= Node.val <= 100
    - -200 <= x <= 200

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🧠 SECTION 2 — KANGLISH THINKING — ಹೇಗೆ ಯೋಚಿಸಬೇಕು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  Problem odi aada mele namma brain enu think maadabeeku:

  ಹಂತ 1 — Problem ಅರ್ಥ ಮಾಡಿಕೊಳ್ಳಿ
  ┌─────────────────────────────────────────────────────────┐
  │  Input ಏನು ಕೊಡ್ತಾರೆ?  →  linked list ಮತ್ತು x (partition  │
  │                           value)                           │
  │  Output ಏನು ಬೇಕು?     →  x ಗಿಂತ ಕಡಿಮೆ ಇರೋ nodes ಮೊದಲು,     │
  │                           x ಗಿಂತ ಹೆಚ್ಚು/ಸಮ ಇರೋ nodes ಆಮೇಲೆ │
  │  Constraints ಏನಿದೆ?   →  ಒಳಗಿನ RELATIVE ORDER maintain     │
  │                           ಆಗ್ಬೇಕು (stable partition!)       │
  └─────────────────────────────────────────────────────────┘

  ಹಂತ 2 — ಯಾಕೆ ಇದು tricky? "order maintain ಮಾಡೋದು ಹೇಗೆ?" ಅಂತ
           ಯೋಚಿಸಿ
  →  ಇದು sort ಅಲ್ಲ! ಪ್ರತಿ group ಒಳಗೆ nodes ಮೂಲ order ನಲ್ಲೇ
     ಇರ್ಬೇಕು. ಒಂದೇ list ಅನ್ನ in-place rearrange ಮಾಡೋಕೆ ಹೋದ್ರೆ
     "ಈಗ ಎಲ್ಲಿ insert ಮಾಡ್ಬೇಕು" ಅನ್ನೋ ಗೊಂದಲ ಬರುತ್ತೆ

  ಹಂತ 3 — ಮೊದಲ simple idea (brute force) ಏನು?
  →  "ಎಲ್ಲಾ values ಅನ್ನ array ಗೆ ಹಾಕಿ, stable partition ಮಾಡಿ,
      ಮತ್ತೆ list ಕಟ್ಟಿದ್ರೆ?"
  →  ಕೆಲಸ ಆಗುತ್ತೆ, ಆದ್ರೆ O(n) extra space ಬೇಕಾಗುತ್ತೆ array ಗೆ

  ಹಂತ 4 — Optimal idea ಹೇಗೆ ಬರುತ್ತೆ?
  →  "ಎರಡು ಪ್ರತ್ಯೇಕ list ಕಟ್ಟಿದ್ರೆ?" ಅಂತ ಯೋಚಿಸಿ: ಒಂದು list
     'less than x' nodes ಗೆ, ಒಂದು list '>= x' nodes ಗೆ — ಒಂದೇ
     pass ನಲ್ಲಿ ಪ್ರತಿ node ಅನ್ನ ಸರಿಯಾದ list ಗೆ ಜೋಡಿಸಿ, ಕೊನೆಗೆ
     ಎರಡು list ಗಳನ್ನ ಜೋಡಿಸಿ!
  →  ಇದಕ್ಕೆ ಎಕ್ಸ್ಟ್ರಾ array ಬೇಡ — ಇರೋ nodes ಅನ್ನೇ ಮರುಬಳಕೆ
     ಮಾಡ್ತಿದ್ದೀವಿ, ಕೇವಲ pointers ಮಾತ್ರ ಬದಲಾಯಿಸ್ತಿದ್ದೀವಿ

  ಹಂತ 5 — Technique ಯಾಕೆ ಇಲ್ಲಿ ಕೆಲಸ ಮಾಡುತ್ತೆ?
  →  ಎರಡು dummy head ಬಳಸಿ (less ಗೆ ಒಂದು, greater_equal ಗೆ
     ಒಂದು) ಪ್ರತಿ node ಅನ್ನ ಅದರ ಸರಿಯಾದ chain ಗೆ append ಮಾಡಿದ್ರೆ,
     ಪ್ರತಿ chain ಒಳಗೆ ಮೂಲ relative order ಸ್ವಾಭಾವಿಕವಾಗೇ
     ಉಳಿಯುತ್ತೆ (ಒಂದೇ pass ಲ್ಲಿ encounter ಆಗೋ order ಅಲ್ಲೇ append
     ಆಗೋದ್ರಿಂದ)

  💡 Interview ನಲ್ಲಿ ಹೇಗೆ ಮಾತಾಡಬೇಕು:
  →  "First approach: dump values into an array, stable-
      partition it, rebuild the list — O(n) time, O(n) space"
  →  "Optimal: build two separate chains (less-than and
      greater-or-equal) in a single pass using dummy heads,
      then splice them together — O(n) time, O(1) extra space"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🏷️ SECTION 3 — TECHNIQUE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Primary   : Two Dummy-Head Chains + Splice (O(n) time, O(1) space)
  Secondary : Extract to Array + Stable Partition + Rebuild (O(n) space)

  WHY Two Chains over Array Extraction?
  → Extracting to an array and rebuilding works, but allocates
    O(n) extra space just to hold values temporarily. Building
    two chains directly out of the EXISTING nodes (just rewiring
    `next` pointers into two separate lists, then joining them)
    gets the same stable-partition result with no extra storage
    beyond a couple of pointers.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 💡 SECTION 4 — INTUITION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  The key insight: a "stable partition" just means "walk through
  once, and sort each element into one of two buckets, preserving
  the order you saw them in." A linked list makes building a
  "bucket" trivial — it's just a chain you append to. So instead
  of one list being rearranged in place (confusing, since you'd
  need to track insertion points), build TWO independent chains
  as you walk the original list once, then glue the second
  chain onto the tail of the first.

  The journey from brute to optimal:
    Brute thought   →  Collect all values into an array, run a
                       stable partition (values < x, then >= x,
                       both preserving original order), rebuild
                       the list from that array
    Problem with it →  O(n) extra space for the array
    Better question →  "Can I build the two groups directly as
                       linked chains, using the existing nodes?"
    Insight         →  Two dummy heads, one pass, append each
                       node to the right chain, then join them
    Optimal         →  One O(n) pass + O(1) splice, O(1) extra
                       space (reusing existing nodes)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🐢 SECTION 5 — APPROACH 1 — BRUTE FORCE (Array + Stable Partition)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    Walk the list once, collecting all values into an array.
    Build a new array by first taking all values < x (in their
    original relative order), then all values >= x (in their
    original relative order). Rebuild a fresh linked list from
    that array.

  Pseudocode:
    step 1: values = [all node values, in order]
    step 2: less = [v for v in values if v < x]
    step 3: greater_equal = [v for v in values if v >= x]
    step 4: result_values = less + greater_equal
    step 5: build and return a new linked list from result_values

  Time  : O(n)  →  Why: a constant number of linear scans over
                        the values
  Space : O(n)  →  Why: stores all values in intermediate lists/
                        arrays before rebuilding

  ಇದು ಯಾಕೆ ಸಾಕಾಗಲ್ಲ?
    → Correct and O(n) time, but uses O(n) extra space — the
      two-chain approach reuses the original nodes directly and
      needs no extra storage for values.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🚀 SECTION 6 — OPTIMAL (Two Dummy-Head Chains + Splice)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    Create two dummy nodes: one to anchor the "less than x"
    chain, one to anchor the "greater than or equal to x" chain.
    Walk the original list once; append each node to the tail of
    whichever chain it belongs to. Finally, link the tail of the
    "less" chain to the head of the "greater_equal" chain, and
    terminate the combined list with None.

  Key steps:
    1. less_dummy = ListNode(); less_tail = less_dummy
       ge_dummy = ListNode(); ge_tail = ge_dummy
    2. curr = head
       while curr:
           if curr.val < x:
               less_tail.next = curr; less_tail = curr
           else:
               ge_tail.next = curr; ge_tail = curr
           curr = curr.next
    3. ge_tail.next = None          (terminate the ge chain)
       less_tail.next = ge_dummy.next  (splice ge chain after less)
       return less_dummy.next

  ಕನ್ನಡದಲ್ಲಿ ಒಂದು ಸಲ ಹೇಳಿ:
    → "ಎರಡು dummy node ಇಟ್ಟುಕೊಂಡು, ಒಂದೇ pass ನಲ್ಲಿ ಪ್ರತಿ node
       ಅನ್ನ ಅದರ value x ಗಿಂತ ಕಡಿಮೆನಾ ಅಲ್ಲ ಹೆಚ್ಚು/ಸಮನಾ ಅಂತ check
       ಮಾಡಿ, ಸರಿಯಾದ chain ಗೆ append ಮಾಡಿ. ಕೊನೆಗೆ ಎರಡು chain
       ಗಳನ್ನ ಜೋಡಿಸಿ, greater_equal chain ಅನ್ನ None ಇಂದ
       terminate ಮಾಡು!"

  Time  : O(n)  →  Why: a single linear pass over the original
                        list, plus O(1) splice at the end
  Space : O(1)  →  Why: only dummy/tail pointers used — all
                        nodes are the ORIGINAL nodes, just
                        rewired

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🔍 SECTION 7 — DRY RUN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Input: head = [1,4,3,2,5,2], x = 3

  Walk through each node:
    1 < 3  → append to less chain:        less: 1
    4 >= 3 → append to ge chain:           ge: 4
    3 >= 3 → append to ge chain:           ge: 4,3
    2 < 3  → append to less chain:        less: 1,2
    5 >= 3 → append to ge chain:           ge: 4,3,5
    2 < 3  → append to less chain:        less: 1,2,2

  After the pass:
    less chain: 1 -> 2 -> 2
    ge chain:   4 -> 3 -> 5

  Splice: less_tail(2).next = ge_dummy.next (head of ge chain, 4)
    Combined: 1 -> 2 -> 2 -> 4 -> 3 -> 5 -> None

  Output: [1,2,2,4,3,5] ✓ matches expected

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 ⚠️ SECTION 8 — EDGE CASES — ಇವನ್ನ ಮರೆಯಬೇಡ!
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  ✓ Empty list (None)?            →  both chains empty, returns
                                      None
  ✓ Single node?                  →  goes entirely into one
                                      chain, returned as-is
  ✓ All nodes < x?                →  ge chain is empty, result
                                      is just the original order
  ✓ All nodes >= x?                →  less chain is empty, result
                                      is just the original order
  ✓ x smaller than every value?   →  everything lands in the ge
                                      chain — no values are < x
  ✓ Duplicate values straddling x
    (e.g. multiple equal to x)?   →  all go into the ge chain,
                                      in their original relative
                                      order (>= includes equal)
  ✓ Forgetting to terminate the
    ge chain's tail with None?    →  would leave a dangling
                                      reference to a node later
                                      in the original list —
                                      MUST set ge_tail.next = None

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📊 SECTION 9 — COMPLEXITY SUMMARY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                              Time    Space
  Brute (array rebuild)       O(n)    O(n)
  Two chains + splice          O(n)    O(1)   ← use this ✅

  Time yaake O(n)?  → One linear pass to distribute nodes into
                       two chains, O(1) work per node
  Space yaake O(1)? → Reuses the existing nodes — only a
                       constant number of pointer variables used

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🎯 SECTION 10 — PATTERN LEARNED — ಇದರಿಂದ ಕಲಿತದ್ದು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Pattern Name: Two Dummy-Head Chains (Bucket-by-Condition)

  Ee pattern yaavaaga use maadabeeku?
  → Any linked-list problem asking to SEPARATE nodes into two
     (or more) groups by a condition while preserving each
     group's original relative order — build one dummy-anchored
     chain per group in a single pass, then splice the chains
     together at the end
  → Variants: separate odd/even indexed nodes, separate
     positive/negative values, segregate 0s/1s/2s (Dutch
     National Flag on a list) — same dummy-head-per-bucket idea

  Idee pattern beere problemsalli kaanisatte:
  → Odd Even Linked List #328 (two chains: odd-position nodes,
     even-position nodes, spliced at the end)
  → Sort List #148 (contrast — that MERGES two sorted chains;
     this problem SPLITS one chain into two unsorted-but-
     order-preserved chains)

  Next time intaha problem bandre naanu modalu idannu think maadtene:
  → "List na condition prakara group madabekagidre, in-place
     rearrange maadokinta, bere-bere dummy-head chain kattu,
     ondu pass alli sariyada chain ge append madu, kodage
     splice madu — O(1) space alli stable partition sigutte!"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🗣️ SECTION 11 — INTERVIEWALLI HEGE EXPLAIN MAADABEEKU
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  1. Understand:
     "Partition a linked list around value x — all nodes < x
      come first, all nodes >= x come after, each group keeping
      its original relative order (a stable partition)."

  2. Brute force:
     "Extract all values to an array, stable-partition the
      array, rebuild the list. O(n) time, O(n) space."

  3. Optimize:
     "Build two chains directly from the existing nodes using
      dummy heads — one for values < x, one for values >= x —
      in a single pass. Splice the second chain onto the end of
      the first."

  4. Code:
     "Two dummy nodes and their tails. Walk once, append each
      node to the right tail based on the condition. At the end,
      null-terminate the ge chain, then link less_tail.next to
      the head of the ge chain."

  5. Complexity:
     "Time O(n) — a single pass. Space O(1) — no extra storage,
      just rewiring existing nodes."

  Mukhya: a 'stable partition into two groups while preserving
          order' problem on a linked list almost always wants
          two dummy-head chains built in one pass, not an
          in-place rearrangement!
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
# BRUTE FORCE — O(n) Time | O(n) Space (array stable partition)
# ═══════════════════════════════════════════════════════════════════
def partition_brute(head, x):
    """
    Idu modala aaloochane — values array ge haaki, stable
    partition madi, aamele hosa list build madu
    """
    values = to_list(head)
    less = [v for v in values if v < x]
    greater_equal = [v for v in values if v >= x]
    return build(less + greater_equal)


# ═══════════════════════════════════════════════════════════════════
# OPTIMAL — O(n) Time | O(1) Space (two dummy-head chains)
# ═══════════════════════════════════════════════════════════════════
def partition(head, x):
    """
    Idu final answer — eradu dummy-head chain (less, ge) kattu,
    ondu pass alli sariyada chain ge append madu, kodage splice madu
    """
    less_dummy = ListNode()
    less_tail = less_dummy
    ge_dummy = ListNode()
    ge_tail = ge_dummy

    curr = head
    while curr:
        if curr.val < x:
            less_tail.next = curr
            less_tail = curr
        else:
            ge_tail.next = curr
            ge_tail = curr
        curr = curr.next

    ge_tail.next = None
    less_tail.next = ge_dummy.next

    return less_dummy.next


# ═══════════════════════════════════════════════════════════════════
# TEST CASES
# ═══════════════════════════════════════════════════════════════════
if __name__ == "__main__":
    # Test 1 — Basic (LeetCode example 1)
    head = build([1, 4, 3, 2, 5, 2])
    assert to_list(partition(head, 3)) == [1, 2, 2, 4, 3, 5]

    # Test 2 — LeetCode example 2
    head = build([2, 1])
    assert to_list(partition(head, 2)) == [1, 2]

    # Test 3 — Empty list
    assert partition(None, 5) is None

    # Test 4 — Single node, less than x
    head = build([1])
    assert to_list(partition(head, 5)) == [1]

    # Test 5 — Single node, >= x
    head = build([5])
    assert to_list(partition(head, 5)) == [5]

    # Test 6 — All values < x (already fully "less" partition)
    head = build([1, 2, 3])
    assert to_list(partition(head, 10)) == [1, 2, 3]

    # Test 7 — All values >= x (already fully "ge" partition)
    head = build([10, 20, 30])
    assert to_list(partition(head, 5)) == [10, 20, 30]

    # Test 8 — Duplicates straddling x
    head = build([3, 3, 3, 1, 1])
    assert to_list(partition(head, 3)) == [1, 1, 3, 3, 3]

    # Cross-check: brute force must agree on all of the above
    head = build([1, 4, 3, 2, 5, 2])
    assert to_list(partition_brute(head, 3)) == [1, 2, 2, 4, 3, 5]

    head = build([2, 1])
    assert to_list(partition_brute(head, 2)) == [1, 2]

    assert partition_brute(None, 5) is None

    head = build([1])
    assert to_list(partition_brute(head, 5)) == [1]

    head = build([5])
    assert to_list(partition_brute(head, 5)) == [5]

    head = build([1, 2, 3])
    assert to_list(partition_brute(head, 10)) == [1, 2, 3]

    head = build([10, 20, 30])
    assert to_list(partition_brute(head, 5)) == [10, 20, 30]

    head = build([3, 3, 3, 1, 1])
    assert to_list(partition_brute(head, 3)) == [1, 1, 3, 3, 3]

    print("All tests passed!")
