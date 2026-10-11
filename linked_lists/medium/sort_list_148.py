"""
╔══════════════════════════════════════════════════════════════════╗
║  SORT LIST                                                       ║
║  LeetCode #148  |  Difficulty: Medium  |  Topic: Linked Lists   ║
║  Link: https://leetcode.com/problems/sort-list/                 ║
╚══════════════════════════════════════════════════════════════════╝

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📘 SECTION 1 — PROBLEM UNDERSTANDING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Given the head of a singly linked list, sort it in ASCENDING
  order and return the sorted list's head.

  Follow-up asked by LeetCode: can you do it in O(n log n) time
  AND O(1) extra space? (The classic recursive merge sort below
  gets O(n log n) time but O(log n) space from recursion; a
  bottom-up iterative merge sort achieves true O(1) extra space.)

  Input : head = first node of linked list
  Output: head of the sorted linked list

  Example 1 — basic:
    Input : 4 → 2 → 1 → 3 → None
    Output: 1 → 2 → 3 → 4 → None
    Why?  : standard ascending sort

  Example 2 — slightly tricky (negatives, duplicates handled
  implicitly):
    Input : -1 → 5 → 3 → 4 → 0 → None
    Output: -1 → 0 → 3 → 4 → 5 → None
    Why?  : negative numbers sort correctly like any other value

  Example 3 — trivial cases:
    Input : None  or  5 → None
    Output: same as input — 0 or 1 node is already "sorted"

  Constraints:
    - 0 <= number of nodes <= 5 * 10^4
    - -10^5 <= Node.val <= 10^5

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🧠 SECTION 2 — KANGLISH THINKING — ಹೇಗೆ ಯೋಚಿಸಬೇಕು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  Problem odi aada mele namma brain enu think maadabeeku:

  ಹಂತ 1 — Problem ಅರ್ಥ ಮಾಡಿಕೊಳ್ಳಿ
  ┌─────────────────────────────────────────────────────────┐
  │  Input ಏನು ಕೊಡ್ತಾರೆ?  →  linked list head                │
  │  Output ಏನು ಬೇಕು?     →  ascending order ನಲ್ಲಿ sorted    │
  │                           list ರ head                     │
  │  Constraints ಏನಿದೆ?   →  O(n log n) time ಬೇಕು (follow-up:│
  │                           O(1) space ಕೂಡ ಸಾಧ್ಯ)           │
  └─────────────────────────────────────────────────────────┘

  ಹಂತ 2 — Array ಆಗಿದ್ರೆ ಗೊತ್ತಿರೋ sort algorithms ಏನಿವೆ?
  →  Quick sort, Merge sort — ಎಲ್ಲಾ O(n log n)
  →  ಆದ್ರೆ linked list ಗೆ RANDOM ACCESS ಇಲ್ಲ (nums[i] ತರ ಇಲ್ಲ)
     — quick sort ರ partition step linked list ಗೆ ಸ್ವಲ್ಪ awkward
  →  MERGE SORT ಆದ್ರೆ ಬೇರೆ! ಅದಕ್ಕೆ ಬೇಕಾಗಿರೋದು ಬರೀ: (1) list ಅನ್ನ
     ಅರ್ಧ ಮಾಡೋದು, (2) ಎರಡು SORTED lists ಅನ್ನ merge ಮಾಡೋದು —
     ಇವೆರಡೂ linked list ಮೇಲೆ ಸಲೀಸಾಗಿ ಆಗುತ್ತೆ!

  ಹಂತ 3 — ಇದನ್ನ previous problems ಜೊತೆ connect ಮಾಡಿ ನೋಡಿ!
  →  "list ಅನ್ನ ಅರ್ಧ ಮಾಡೋದು" → Reorder List #143 ರಲ್ಲಿ ಬಳಸಿದ
     slow/fast middle-finding technique ನೇ!
  →  "ಎರಡು SORTED lists ಅನ್ನ merge ಮಾಡೋದು" → Merge Two Sorted
     Lists #21 ರಲ್ಲಿ ಬಳಸಿದ dummy-node merge technique ನೇ!
  →  So Sort List = ಎರಡು ಈಗಾಗಲೇ ಗೊತ್ತಿರೋ building blocks ಅನ್ನ
     RECURSIVELY ಜೋಡಿಸಿದ್ರೆ ಸಾಕು!

  ಹಂತ 4 — Merge Sort recursion ಹೇಗೆ apply ಆಗುತ್ತೆ?
  →  Base case: 0 ಅಥವಾ 1 node ಇದ್ರೆ, ಅದೇ ಈಗಾಗಲೇ "sorted"
  →  ಇಲ್ಲಾಂದ್ರೆ: middle find ಮಾಡಿ list ಅನ್ನ ಎರಡು ಭಾಗ ಮಾಡಿ,
     ಎರಡೂ ಭಾಗಗಳ ಮೇಲೆ RECURSIVELY sort_list() call ಮಾಡಿ,
     ಆಮೇಲೆ ಎರಡೂ sorted ಭಾಗಗಳ ಅನ್ನ merge ಮಾಡಿ

  ಹಂತ 5 — Technique ಯಾಕೆ ಇಲ್ಲಿ ಕೆಲಸ ಮಾಡುತ್ತೆ?
  →  Merge sort ರ divide step (split in half) ಮತ್ತು combine
     step (merge two sorted) ಎರಡೂ linked list ಮೇಲೆ O(n) time,
     O(1) extra space (per level) ನಲ್ಲಿ ಆಗುತ್ತೆ — array ಗೆ
     ಬೇಕಾಗೋ extra copying ಕೂಡ ಬೇಡ!
  →  O(log n) levels of recursion × O(n) work per level = O(n log n)

  💡 Interview ನಲ್ಲಿ ಹೇಗೆ ಮಾತಾಡಬೇಕು:
  →  "Merge sort is the natural fit for linked lists — unlike
      quicksort, it doesn't need random access"
  →  "Find the middle with slow/fast pointers, split, recursively
      sort both halves, then merge the two sorted halves — reusing
      the exact merge logic from Merge Two Sorted Lists"
  →  "Base case: 0 or 1 node is already sorted"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🏷️ SECTION 3 — TECHNIQUE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Primary   : Merge Sort (split via slow/fast + merge two sorted lists)
  Secondary : Extract values, sort array, write back (brute force)

  WHY Merge Sort over Quick Sort here?
  → Quick sort's partition step relies on cheap random access
    and in-place swaps — awkward on a singly linked list. Merge
    sort only needs sequential splitting and sequential merging,
    both of which are natural, O(n)-per-level operations on a
    linked list.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 💡 SECTION 4 — INTUITION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  The key insight: sorting a linked list is really just two
  problems you've already solved, applied recursively. "Split
  in half" is the exact slow/fast middle-finding from Reorder
  List. "Combine two sorted sequences into one" is the exact
  dummy-node merge from Merge Two Sorted Lists. Merge sort is
  simply: split until pieces are trivially sorted (size 0 or 1),
  then merge pairs back together on the way up.

  The journey from brute to optimal:
    Brute thought   →  Walk the list once collecting values into
                       an array, sort the array, walk the list
                       again overwriting values in sorted order
    Problem with it →  O(n) extra space for the array — doesn't
                       exploit the fact that merge sort works
                       natively on linked structures
    Better question →  "Can I sort using only list operations —
                       splitting and merging — without an array?"
    Insight         →  Merge sort's two building blocks (split,
                       merge) are both things I've already built
                       for other linked-list problems
    Optimal         →  Recursive merge sort: O(n log n) time,
                       O(log n) space (recursion depth)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🐢 SECTION 5 — APPROACH 1 — BRUTE FORCE (extract, sort array, write back)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    Walk the list once to collect all values into a Python list.
    Sort that list. Walk the linked list again, overwriting each
    node's value with the next sorted value.

  Pseudocode:
    step 1: vals = [collect every node's value]
    step 2: vals.sort()
    step 3: curr = head
    step 4: for v in vals: curr.val = v; curr = curr.next
    step 5: return head

  Time  : O(n log n)  →  Why: Python's sort() dominates; the two
                              list traversals are O(n)
  Space : O(n)          →  Why: the `vals` array holds every node's
                              value

  ಇದು ಯಾಕೆ ಸಾಕಾಗಲ್ಲ?
    → Meets the time requirement, but uses O(n) extra space —
      doesn't exploit merge sort's natural fit for linked
      structures, which gets the same time bound with less
      (or, with the iterative bottom-up variant, zero) extra space.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🚀 SECTION 6 — OPTIMAL (Merge Sort: split + recursive sort + merge)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    If the list has 0 or 1 node, it's already sorted — return it.
    Otherwise, find the middle with slow/fast pointers, split the
    list into two halves, recursively sort EACH half, then merge
    the two now-sorted halves using the standard dummy-node merge.

  Key steps:
    1. if not head or not head.next: return head
    2. slow, fast = head, head.next
       while fast and fast.next: slow=slow.next; fast=fast.next.next
    3. mid = slow.next; slow.next = None
    4. left = sort_list(head); right = sort_list(mid)
    5. return merge(left, right)    # dummy-node merge, as in #21

  ಕನ್ನಡದಲ್ಲಿ ಒಂದು ಸಲ ಹೇಳಿ:
    → "0 ಅಥವಾ 1 node ಇದ್ರೆ ಈಗಾಗಲೇ sorted — return ಮಾಡು.
       ಇಲ್ಲಾಂದ್ರೆ slow/fast ಬಳಸಿ middle find ಮಾಡಿ list ಅನ್ನ
       ಎರಡು ಭಾಗ ಮಾಡು. ಎರಡೂ ಭಾಗಗಳ ಮೇಲೆ ಅದೇ sort_list()
       recursively call ಮಾಡು. ಕೊನೆಗೆ ಎರಡೂ sorted ಭಾಗಗಳ ಅನ್ನ
       merge ಮಾಡು — #21 ರಲ್ಲಿ ಬಳಸಿದ ಅದೇ dummy-node merge!"

  Time  : O(n log n)  →  Why: O(log n) levels of splitting, O(n)
                              total work (split + merge) per level
  Space : O(log n)     →  Why: recursion call stack depth equals
                              the number of split levels

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🔍 SECTION 7 — DRY RUN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Input: 4 → 2 → 1 → 3 → None

  sort_list(4,2,1,3):
    split at middle → left=(4,2), right=(1,3)
    sort_list(4,2):
      split → left=(4), right=(2)
      sort_list(4) → [4] (base case)
      sort_list(2) → [2] (base case)
      merge([4],[2]) → [2,4]
    sort_list(1,3):
      split → left=(1), right=(3)
      merge([1],[3]) → [1,3]
    merge([2,4],[1,3]):
      compare 2 vs 1 → take 1 → [1]
      compare 2 vs 3 → take 2 → [1,2]
      compare 4 vs 3 → take 3 → [1,2,3]
      only 4 left    → take 4 → [1,2,3,4]

  Output: 1 → 2 → 3 → 4 → None ✓

  ಇನ್ನೊಂದು example — with a negative number:
  Input: -1 → 5 → 3 → 4 → 0 → None

  Recursively splits and merges exactly as above, comparisons
  work identically for negative values.

  Output: -1 → 0 → 3 → 4 → 5 → None ✓

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 ⚠️ SECTION 8 — EDGE CASES — ಇವನ್ನ ಮರೆಯಬೇಡ!
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  ✓ Empty list (None)?             →  None — base case returns
                                       immediately
  ✓ Single node?                   →  unchanged — base case
                                       returns it as-is
  ✓ Already sorted?                →  works fine, just confirms
                                       the order via merges
  ✓ All duplicate values?          →  sorts fine (stable-ish;
                                       merge uses <=, preserving
                                       relative order of equal
                                       values from the left half)
  ✓ Negative and positive mixed?   →  comparisons (<=) handle
                                       sign correctly, no special
                                       casing needed

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📊 SECTION 9 — COMPLEXITY SUMMARY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                              Time        Space
  Brute (array sort)          O(n log n)  O(n)
  Merge Sort (recursive)      O(n log n)  O(log n)   ← use this ✅

  * A bottom-up ITERATIVE merge sort achieves true O(1) extra
    space (no recursion stack) — a further optimization beyond
    what's implemented here, for the follow-up constraint.

  Time yaake O(n log n)?  → O(log n) split levels, each doing
                             O(n) total split + merge work
  Space yaake O(log n)?   → Recursion depth equals the number
                             of halving steps

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🎯 SECTION 10 — PATTERN LEARNED — ಇದರಿಂದ ಕಲಿತದ್ದು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Pattern Name: Merge Sort on Linked Lists (split + recursive sort + merge)

  Ee pattern yaavaaga use maadabeeku?
  → Sorting a linked list (no random access, so quicksort-style
     partitioning is awkward) — merge sort is the natural choice
  → ANY problem needing "divide a linked list in half" + "merge
     two sorted linked lists" as sub-steps — recognize these as
     reusable building blocks from Reorder List and Merge Two
     Sorted Lists respectively

  Idee pattern beere problemsalli kaanisatte:
  → Merge Two Sorted Lists #21 (the merge building block, reused
     directly here)
  → Reorder List #143 (the middle-finding/splitting building
     block, reused directly here)
  → Merge K Sorted Lists #23 (next level up — merge sort's
     "combine" step generalized to K lists instead of 2)

  Next time intaha problem bandre naanu modalu idannu think maadtene:
  → "Linked list sort madabekagidre → merge sort try maadu!
     Split (slow/fast middle) + merge (dummy node) — eradu
     building blocks already gottu ide, recursively jodisidre
     saaku!"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🗣️ SECTION 11 — INTERVIEWALLI HEGE EXPLAIN MAADABEEKU
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  1. Understand:
     "Sort a singly linked list in ascending order, ideally in
      O(n log n) time."

  2. Brute force:
     "Extract all values into an array, sort the array, write
      the sorted values back into the existing nodes. O(n log n)
      time, O(n) space."

  3. Optimize:
     "Merge sort fits linked lists naturally — no random access
      needed. Find the middle (slow/fast pointers), split,
      recursively sort each half, then merge the two sorted
      halves using a dummy node — same merge as Merge Two Sorted
      Lists."

  4. Code:
     "Base case: 0/1 node. Otherwise split via slow/fast, recurse
      on both halves, merge with a dummy-node walk comparing
      heads and advancing the smaller one."

  5. Complexity:
     "Time O(n log n) — log n split levels, O(n) work each.
      Space O(log n) — recursion stack depth."

  Mukhya: Sort List = Merge Two Sorted Lists + Reorder List's
          middle-finding, applied recursively — spot the reusable
          building blocks before writing anything new!
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
# BRUTE FORCE — O(n log n) Time | O(n) Space (extract, sort, write back)
# ═══════════════════════════════════════════════════════════════════
def sort_list_brute(head):
    """
    Idu modala aaloochane — ella values array ge collect madi,
    sort madi, aamele list ge mathe write madu
    """
    vals = to_list(head)
    vals.sort()

    curr = head
    for v in vals:
        curr.val = v
        curr = curr.next

    return head


# ═══════════════════════════════════════════════════════════════════
# OPTIMAL — O(n log n) Time | O(log n) Space (merge sort)
# ═══════════════════════════════════════════════════════════════════
def _merge(l1, l2):
    """Standard dummy-node merge of two sorted lists (same as Merge Two Sorted Lists)."""
    dummy = ListNode(0)
    curr = dummy

    while l1 and l2:
        if l1.val <= l2.val:
            curr.next = l1
            l1 = l1.next
        else:
            curr.next = l2
            l2 = l2.next
        curr = curr.next

    curr.next = l1 if l1 else l2
    return dummy.next


def sort_list(head):
    """
    Idu final answer — merge sort: slow/fast middle find madi
    split madu, eradu halves recursively sort madi, merge madu
    """
    if not head or not head.next:
        return head

    # find the middle (slow/fast pointers)
    slow, fast = head, head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # split into two halves
    mid = slow.next
    slow.next = None

    # recursively sort each half, then merge
    left = sort_list(head)
    right = sort_list(mid)
    return _merge(left, right)


# ═══════════════════════════════════════════════════════════════════
# TEST CASES
# ═══════════════════════════════════════════════════════════════════
if __name__ == "__main__":
    # Test 1 — Basic
    assert to_list(sort_list(build([4, 2, 1, 3]))) == [1, 2, 3, 4]

    # Test 2 — Negatives and positives mixed
    assert to_list(sort_list(build([-1, 5, 3, 4, 0]))) == [-1, 0, 3, 4, 5]

    # Test 3 — Already sorted
    assert to_list(sort_list(build([1, 2, 3]))) == [1, 2, 3]

    # Test 4 — Single node
    assert to_list(sort_list(build([5]))) == [5]

    # Test 5 — Empty list
    assert to_list(sort_list(None)) == []

    # Cross-check: brute force must agree on all of the above
    assert to_list(sort_list_brute(build([4, 2, 1, 3]))) == [1, 2, 3, 4]
    assert to_list(sort_list_brute(build([-1, 5, 3, 4, 0]))) == [-1, 0, 3, 4, 5]
    assert to_list(sort_list_brute(build([1, 2, 3]))) == [1, 2, 3]
    assert to_list(sort_list_brute(build([5]))) == [5]
    assert to_list(sort_list_brute(None)) == []

    print("All tests passed!")
