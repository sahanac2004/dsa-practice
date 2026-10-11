"""
╔══════════════════════════════════════════════════════════════════╗
║  MERGE K SORTED LISTS                                            ║
║  LeetCode #23  |  Difficulty: Hard  |  Topic: Linked Lists      ║
║  Link: https://leetcode.com/problems/merge-k-sorted-lists/      ║
╚══════════════════════════════════════════════════════════════════╝

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📘 SECTION 1 — PROBLEM UNDERSTANDING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  You are given an array of `k` linked-lists, each already
  sorted in ascending order. Merge ALL of them into a single
  sorted linked list and return its head.

  Input : lists = array of k sorted linked-list heads
  Output: head of one fully merged, sorted linked list

  Example 1 — basic:
    Input : lists = [[1,4,5], [1,3,4], [2,6]]
    Output: 1 → 1 → 2 → 3 → 4 → 4 → 5 → 6 → None
    Why?  : merging all three sorted lists produces one fully
            sorted sequence containing every node

  Example 2 — slightly tricky (empty lists mixed in):
    Input : lists = [[], [1]]
    Output: 1 → None
    Why?  : empty lists contribute nothing; only the non-empty
            ones matter

  Example 3 — no lists at all:
    Input : lists = []
    Output: None
    Why?  : nothing to merge

  Constraints:
    - 0 <= k <= 10^4
    - 0 <= total nodes across all lists <= 10^4
    - -10^4 <= Node.val <= 10^4
    - each individual list is sorted in ascending order

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🧠 SECTION 2 — KANGLISH THINKING — ಹೇಗೆ ಯೋಚಿಸಬೇಕು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  Problem odi aada mele namma brain enu think maadabeeku:

  ಹಂತ 1 — Problem ಅರ್ಥ ಮಾಡಿಕೊಳ್ಳಿ
  ┌─────────────────────────────────────────────────────────┐
  │  Input ಏನು ಕೊಡ್ತಾರೆ?  →  k ಸಂಖ್ಯೆಯ SORTED linked lists   │
  │  Output ಏನು ಬೇಕು?     →  ಎಲ್ಲಾ k lists ಅನ್ನ ಒಂದೇ SORTED │
  │                           list ಆಗಿ merge ಮಾಡಿ return ಮಾಡಿ│
  │  Constraints ಏನಿದೆ?   →  ಪ್ರತಿ list ಈಗಾಗಲೇ sorted ಇದೆ    │
  └─────────────────────────────────────────────────────────┘

  ಹಂತ 2 — ಇದನ್ನ #148 (Sort List) ಜೊತೆ EXACT ಆಗಿ CONNECT ಮಾಡಿ
           ನೋಡಿ!
  →  #148 ರಲ್ಲಿ: "ಎರಡು SORTED halves ಅನ್ನ merge ಮಾಡೋದು" ಅನ್ನೋ
     building block ಬಳಸಿ, merge sort apply ಮಾಡಿದ್ವಿ
  →  ಇಲ್ಲಿ: ಅದೇ "merge two sorted lists" building block ಅನ್ನ,
     k lists ಗೆ GENERALIZE ಮಾಡಬೇಕು — PAIRS ಆಗಿ merge ಮಾಡ್ತಾ
     ಹೋದ್ರೆ, ಕೊನೆಗೆ ಒಂದೇ list ಉಳಿಯುತ್ತೆ!

  ಹಂತ 3 — ಮೊದಲ simple idea ಏನು?
  →  ಎಲ್ಲಾ k lists ರ ಎಲ್ಲಾ values ಅನ್ನ ಒಂದು array ಗೆ collect
     ಮಾಡಿ, sort ಮಾಡಿ, ಹೊಸ linked list ಆಗಿ build ಮಾಡಿ

  ಹಂತ 4 — Divide & Conquer (pairwise merge) ಹೇಗೆ?
  →  "k lists ಅನ್ನ ಒಂದೊಂದೇ merge ಮಾಡೋ ಬದಲು, PAIRS ಆಗಿ merge
      ಮಾಡಿದ್ರೆ?" ಅಂತ ಯೋಚಿಸಿ
  →  Round 1: list[0]+list[1], list[2]+list[3], ... → k/2 lists
  →  Round 2: ಆ k/2 lists ಅನ್ನ ಮತ್ತೆ pairs ಆಗಿ merge → k/4 lists
  →  ಹೀಗೆ log(k) rounds ಆಗೋವರೆಗೆ ಮುಂದುವರಿಸಿದ್ರೆ, ಕೊನೆಗೆ ಒಂದೇ
     list ಉಳಿಯುತ್ತೆ — ಅದೇ ಫೈನಲ್ ಆನ್ಸರ್!

  ಹಂತ 5 — Technique ಯಾಕೆ ಇಲ್ಲಿ ಕೆಲಸ ಮಾಡುತ್ತೆ?
  →  "ಒಂದೊಂದೇ list ಅನ್ನ running result ಗೆ merge ಮಾಡ್ತಾ ಹೋದ್ರೆ"
     (naive sequential merge), running result ಗಾತ್ರ ಬೆಳಿತಾ
     ಹೋಗುತ್ತೆ — ಪ್ರತಿ merge ಗೂ ಆ ಬೆಳೆದ result ಅನ್ನ ಮತ್ತೆ scan
     ಮಾಡಬೇಕು → O(N*k) time!
  →  PAIRWISE (tournament-style) merge ಆದ್ರೆ, ಪ್ರತಿ round ನಲ್ಲೂ
     ಪ್ರತಿ node ಒಮ್ಮೆ ಮಾತ್ರ touch ಆಗುತ್ತೆ (O(N) per round),
     ಮತ್ತು log(k) rounds ಮಾತ್ರ ಬೇಕು → O(N log k) time — ಬಹಳ
     ವೇಗ!

  💡 Interview ನಲ್ಲಿ ಹೇಗೆ ಮಾತಾಡಬೇಕು:
  →  "I'll reuse the exact merge-two-sorted-lists helper from
      Sort List / Merge Two Sorted Lists"
  →  "Instead of merging lists one-by-one into a growing result
      (which re-scans the growing result every time), I merge
      them in PAIRS, tournament-style — this halves the list
      count each round"
  →  "log(k) rounds, each doing O(N) total work, gives O(N log k)
      instead of the naive O(N*k)"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🏷️ SECTION 3 — TECHNIQUE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Primary   : Divide & Conquer — pairwise merge, tournament-style
  Secondary : Collect all values, sort, rebuild (brute force)

  WHY Pairwise (Divide & Conquer) Merge?
  → Merging lists one-at-a-time into a growing result repeatedly
    re-processes the ALREADY-merged portion, giving O(N*k) total
    work. Pairing lists up and merging simultaneously means each
    node is only ever touched once per round, and there are only
    log(k) rounds — exactly the same halving idea as merge sort's
    recursion tree, just applied to a list of lists instead of
    one list.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 💡 SECTION 4 — INTUITION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  The key insight: this is Sort List's merge step, generalized.
  In Sort List, we recursively split ONE list down to single
  nodes, then merged pairs back up. Here, we're handed k
  ALREADY-sorted lists directly — so we skip the splitting phase
  entirely and jump straight to the "merge pairs, then merge
  pairs of those, etc." phase. It's the same tournament-bracket
  shape: round 1 produces k/2 lists, round 2 produces k/4, and so
  on until one list remains after log2(k) rounds.

  The journey from brute to optimal:
    Brute thought   →  Collect every value from every list into
                       one array, sort it, rebuild as a list
    Problem with it →  O(N log N) time, O(N) space — doesn't
                       exploit that each input list is ALREADY
                       sorted
    Better question →  "Can I merge the already-sorted lists
                       directly, without re-sorting everything?"
    Insight         →  Merge pairs of lists simultaneously each
                       round (tournament-style) instead of
                       sequentially into one growing result
    Optimal         →  O(N log k) time: log k rounds, O(N) work
                       per round

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🐢 SECTION 5 — APPROACH 1 — BRUTE FORCE (collect, sort, rebuild)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    Walk every list, collecting every node's value into one
    array. Sort that array. Build a brand-new linked list from
    the sorted values.

  Pseudocode:
    step 1: vals = []
    step 2: for each list in lists: walk it, append all values
    step 3: vals.sort()
    step 4: return build(vals)   # new linked list from sorted values

  Time  : O(N log N)  →  Why: N = total nodes across all lists;
                              sorting dominates
  Space : O(N)         →  Why: the `vals` array holds every value

  ಇದು ಯಾಕೆ ಸಾಕಾಗಲ್ಲ?
    → Correct, but throws away the fact that each input list is
      ALREADY sorted — full re-sorting is wasted work compared
      to directly merging pre-sorted sequences.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🚀 SECTION 6 — OPTIMAL (Divide & Conquer, Pairwise Merge)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    While more than one list remains: pair up adjacent lists and
    merge each pair with the standard two-sorted-lists merge
    (reused from #148/#21). This produces half as many lists.
    Repeat until only one list is left.

  Key steps:
    1. if not lists: return None
    2. while len(lists) > 1:
    3.   merged = []
    4.   for i in range(0, len(lists), 2):
    5.     l1 = lists[i]
    6.     l2 = lists[i+1] if i+1 < len(lists) else None
    7.     merged.append(_merge(l1, l2))
    8.   lists = merged
    9. return lists[0]

  ಕನ್ನಡದಲ್ಲಿ ಒಂದು ಸಲ ಹೇಳಿ:
    → "lists ಗಳಲ್ಲಿ ಒಂದಕ್ಕಿಂತ ಜಾಸ್ತಿ ಇರೋವರೆಗೆ: adjacent lists
       ಅನ್ನ PAIRS ಆಗಿ ತಗೊಂಡು, ಪ್ರತಿ pair ಅನ್ನ standard
       merge-two-sorted-lists ಬಳಸಿ ಜೋಡಿಸು. ಇದ್ರಿಂದ lists ಅರ್ಧ
       ಆಗುತ್ತೆ. ಇದೇ ಮುಂದುವರಿಸಿ, ಒಂದೇ list ಉಳಿಯೋವರೆಗೆ!"

  Time  : O(N log k)  →  Why: log k rounds (each round halves
                              the list count), each round merges
                              all N nodes exactly once across its
                              pairs
  Space : O(k)         →  Why: the `merged` list holds up to k/2
                              new list head pointers per round
                              (small, bounded by k — not N)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🔍 SECTION 7 — DRY RUN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Input: lists = [[1,4,5], [1,3,4], [2,6]]

  Round 1 (pair up: (list0,list1), (list2,None)):
    merge([1,4,5], [1,3,4]) → [1,1,3,4,4,5]
    merge([2,6], None)      → [2,6]
    lists = [[1,1,3,4,4,5], [2,6]]

  Round 2 (pair up: (list0,list1)):
    merge([1,1,3,4,4,5], [2,6]) → [1,1,2,3,4,4,5,6]
    lists = [[1,1,2,3,4,4,5,6]]

  Only one list left → return it

  Output: 1 → 1 → 2 → 3 → 4 → 4 → 5 → 6 → None ✓

  ಇನ್ನೊಂದು example — empty list mixed in:
  Input: lists = [[], [1]]

  Round 1: merge(None, [1]) → [1]
  lists = [[1]] → only one left → return it

  Output: 1 → None ✓

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 ⚠️ SECTION 8 — EDGE CASES — ಇವನ್ನ ಮರೆಯಬೇಡ!
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  ✓ No lists at all (k=0)?         →  None — guard before the loop
  ✓ Single list only (k=1)?        →  that list unchanged —
                                       while loop never runs
  ✓ Some lists empty?              →  _merge handles None
                                       gracefully (acts as an
                                       empty sorted list)
  ✓ All lists empty?               →  None — every merge produces
                                       None, final result is None
  ✓ Odd number of lists in a
    round?                         →  the unpaired last list just
                                       passes through unchanged
                                       (merged with None)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📊 SECTION 9 — COMPLEXITY SUMMARY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                              Time        Space
  Brute (collect+sort)        O(N log N)  O(N)
  Divide & Conquer (pairwise) O(N log k)  O(k)   ← use this ✅

  N = total nodes across all lists, k = number of lists

  Time yaake O(N log k)?  → log k rounds; each round's merges
                             collectively touch all N nodes once
  Space yaake O(k)?        → Only the list of merged-list-head
                             pointers per round, bounded by k

  📌 NOTE: an alternative O(N log k) approach uses a MIN-HEAP of
  size k (push each list's current head, pop the smallest,
  push its successor) — same time bound, O(k) space for the
  heap. The pairwise divide-and-conquer shown here is preferred
  when you want to directly reuse the merge-two-sorted-lists
  building block without a heap import.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🎯 SECTION 10 — PATTERN LEARNED — ಇದರಿಂದ ಕಲಿತದ್ದು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Pattern Name: Tournament-Style Pairwise Merge (Divide & Conquer)

  Ee pattern yaavaaga use maadabeeku?
  → "Merge K already-sorted sequences into one" — whenever you
     have MULTIPLE pre-sorted structures (not just one list to
     split), skip the splitting phase and jump straight to
     pairwise merging in rounds
  → Any "combine N sorted things efficiently" problem where
     sequential one-by-one merging would be too slow (O(N*k)
     instead of O(N log k))

  Idee pattern beere problemsalli kaanisatte:
  → Sort List #148 (previous problem — same merge building
     block, but used after a SPLIT phase instead of starting
     with pre-sorted pieces)
  → Merge Two Sorted Lists #21 (the core 2-list merge helper,
     reused directly here)
  → Reverse Nodes in k-Group #25 (different technique, but same
     "k groups" framing — processing a list in chunks of k)

  Next time intaha problem bandre naanu modalu idannu think maadtene:
  → "K already-sorted sequences merge madabekagidre → pairwise
     tournament-style merge try maadu! Sequential one-by-one
     merge O(N*k) — pairs round-by-round O(N log k) ge
     ilisabahudu!"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🗣️ SECTION 11 — INTERVIEWALLI HEGE EXPLAIN MAADABEEKU
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  1. Understand:
     "Merge k already-sorted linked lists into one fully sorted
      linked list."

  2. Brute force:
     "Collect every value into an array, sort it, rebuild as a
      list. O(N log N) time, O(N) space — ignores that inputs
      are already sorted."

  3. Optimize:
     "Reuse the merge-two-sorted-lists helper, but apply it
      PAIRWISE across all k lists simultaneously each round,
      halving the list count. log k rounds, O(N) work per round
      → O(N log k) total. (A min-heap of size k is an equally
      valid O(N log k) alternative.)"

  4. Code:
     "While more than one list remains: pair up adjacent lists,
      merge each pair, collect results into a new list-of-lists.
      Repeat until one list remains."

  5. Complexity:
     "Time O(N log k) — log k halving rounds, O(N) total merge
      work per round. Space O(k) for the per-round list of
      merged heads."

  Mukhya: K pre-sorted sequences merge madabekagidre, sequential
          one-by-one merge bittu — tournament-style PAIRS round-
          by-round merge madu, O(N*k) inda O(N log k) ge
          ilisabahudu!
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
# BRUTE FORCE — O(N log N) Time | O(N) Space (collect, sort, rebuild)
# ═══════════════════════════════════════════════════════════════════
def merge_k_lists_brute(lists):
    """
    Idu modala aaloochane — ella lists ra ella values array ge
    collect madi, sort madi, hosa linked list build madu
    """
    vals = []
    for head in lists:
        curr = head
        while curr:
            vals.append(curr.val)
            curr = curr.next

    vals.sort()
    return build(vals)


# ═══════════════════════════════════════════════════════════════════
# OPTIMAL — O(N log k) Time | O(k) Space (divide & conquer, pairwise)
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


def merge_k_lists(lists):
    """
    Idu final answer — lists ondakkinta jaasti idde tanaka,
    adjacent lists pairs aagi merge madtha hogu (tournament style)
    """
    if not lists:
        return None

    lists = list(lists)

    while len(lists) > 1:
        merged = []
        for i in range(0, len(lists), 2):
            l1 = lists[i]
            l2 = lists[i + 1] if i + 1 < len(lists) else None
            merged.append(_merge(l1, l2))
        lists = merged

    return lists[0]


# ═══════════════════════════════════════════════════════════════════
# TEST CASES
# ═══════════════════════════════════════════════════════════════════
if __name__ == "__main__":
    # Test 1 — Basic
    assert to_list(merge_k_lists([build([1, 4, 5]), build([1, 3, 4]), build([2, 6])])) == \
        [1, 1, 2, 3, 4, 4, 5, 6]

    # Test 2 — Empty list mixed in
    assert to_list(merge_k_lists([build([]), build([1])])) == [1]

    # Test 3 — No lists at all
    assert to_list(merge_k_lists([])) == []

    # Test 4 — All lists empty
    assert to_list(merge_k_lists([build([]), build([])])) == []

    # Test 5 — Single list
    assert to_list(merge_k_lists([build([1, 2, 3])])) == [1, 2, 3]

    # Cross-check: brute force must agree on all of the above
    assert to_list(merge_k_lists_brute([build([1, 4, 5]), build([1, 3, 4]), build([2, 6])])) == \
        [1, 1, 2, 3, 4, 4, 5, 6]
    assert to_list(merge_k_lists_brute([build([]), build([1])])) == [1]
    assert to_list(merge_k_lists_brute([])) == []
    assert to_list(merge_k_lists_brute([build([]), build([])])) == []
    assert to_list(merge_k_lists_brute([build([1, 2, 3])])) == [1, 2, 3]

    print("All tests passed!")
