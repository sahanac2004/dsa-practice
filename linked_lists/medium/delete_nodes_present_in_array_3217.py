"""
╔══════════════════════════════════════════════════════════════════╗
║  DELETE NODES FROM LINKED LIST PRESENT IN ARRAY                  ║
║  LeetCode #3217  |  Difficulty: Medium  |  Topic: Linked Lists ║
║  Link: https://leetcode.com/problems/                           ║
║        delete-nodes-from-linked-list-present-in-array/          ║
╚══════════════════════════════════════════════════════════════════╝

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📘 SECTION 1 — PROBLEM UNDERSTANDING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Given an integer array `nums` and the head of a linked list,
  remove every node from the linked list whose value is present
  in `nums`. Return the head of the modified linked list.

  Input : nums = array of integers, head = singly linked list
  Output: head of the list with all nodes whose value appears
          in nums removed

  Example 1 — basic:
    Input : nums = [1,2,3], head = [1,2,3,4,5]
    Output: [4,5]
    Why?  : nodes valued 1, 2, 3 all appear in nums, so they're
            removed; 4 and 5 don't appear, so they stay

  Example 2 — no overlap:
    Input : nums = [1], head = [1,2,1,2,1,2]
    Output: [2,2,2]
    Why?  : every node valued 1 is removed (it's in nums); nodes
            valued 2 stay since 2 is not in nums

  Example 3 — nothing removed:
    Input : nums = [5], head = [1,2,3,4]
    Output: [1,2,3,4]
    Why?  : none of the list's values (1,2,3,4) appear in nums

  Constraints:
    - 1 <= nums.length <= 10^5
    - 1 <= nums[i] <= 10^5
    - 1 <= number of list nodes <= 10^5
    - 1 <= Node.val <= 10^5
    - The input is generated such that the result is never empty

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🧠 SECTION 2 — KANGLISH THINKING — ಹೇಗೆ ಯೋಚಿಸಬೇಕು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  Problem odi aada mele namma brain enu think maadabeeku:

  ಹಂತ 1 — Problem ಅರ್ಥ ಮಾಡಿಕೊಳ್ಳಿ
  ┌─────────────────────────────────────────────────────────┐
  │  Input ಏನು ಕೊಡ್ತಾರೆ?  →  array (nums) ಮತ್ತು linked list  │
  │  Output ಏನು ಬೇಕು?     →  nums ಒಳಗೆ value ಇರೋ nodes       │
  │                           ಅನ್ನ delete ಮಾಡಿದ list          │
  │  Constraints ಏನಿದೆ?   →  nums, list ಎರಡೂ 10^5 ಅಷ್ಟು      │
  │                           ದೊಡ್ಡ ಆಗಬಹುದು                   │
  └─────────────────────────────────────────────────────────┘

  ಹಂತ 2 — ಯಾಕೆ ಇದು tricky? "value nums ಒಳಗೆ ಇದ್ಯಾ ಅಂತ ಪ್ರತಿ
           node ಗೂ FAST ಆಗಿ check ಮಾಡೋದು ಹೇಗೆ?" ಅಂತ ಯೋಚಿಸಿ
  →  nums ಅನ್ನ ಪ್ರತಿ node ಗೂ linear search ಮಾಡಿದ್ರೆ O(n * m)
     ಆಗುತ್ತೆ (n = list length, m = nums length) — ಇದು ಸ್ಲೋ
     ಆಗಬಹುದು nums, list ಎರಡೂ ದೊಡ್ಡ ಇದ್ರೆ

  ಹಂತ 3 — ಮೊದಲ simple idea (brute force) ಏನು?
  →  "ಪ್ರತಿ node ಗೂ, nums ಒಳಗೆ `in` ಬಳಸಿ linear search ಮಾಡಿ check
      ಮಾಡಿದ್ರೆ?"
  →  ಕೆಲಸ ಆಗುತ್ತೆ, ಆದ್ರೆ O(n * m) time — nums ದೊಡ್ಡ ಇದ್ರೆ ತುಂಬಾ ಸ್ಲೋ

  ಹಂತ 4 — Optimal idea ಹೇಗೆ ಬರುತ್ತೆ?
  →  "nums ಅನ್ನ SET ಗೆ ಹಾಕಿ ಇಟ್ಟುಕೊಂಡ್ರೆ?" ಅಂತ ಯೋಚಿಸಿ — set
     membership check O(1) ಆಗುತ್ತೆ! ಆಮೇಲೆ dummy node ಬಳಸಿ, ಒಂದೇ
     pass ಲ್ಲಿ ಪ್ರತಿ node ಅನ್ನ check ಮಾಡಿ, set ಒಳಗೆ ಇದ್ರೆ skip
     ಮಾಡಿ (delete), ಇಲ್ದಿದ್ರೆ ಇಟ್ಟುಕೋ

  ಹಂತ 5 — Technique ಯಾಕೆ ಇಲ್ಲಿ ಕೆಲಸ ಮಾಡುತ್ತೆ?
  →  "HashSet ಒಳಗೆ ಇದ್ಯಾ" ಅನ್ನೋ check O(1) ಆಗೋದ್ರಿಂದ, ಪ್ರತಿ
     node ಗೂ ಒಂದೇ constant-time lookup ಸಾಕು — ಪೂರ್ತಿ nums ಅನ್ನ
     ಮತ್ತೆ ಮತ್ತೆ scan ಮಾಡೋ ಅಗತ್ಯ ಇಲ್ಲ. dummy node ಬಳಸಿದ್ರೆ
     "delete ಮಾಡ್ಬೇಕಾ, ಇಡ್ಬೇಕಾ" ಅನ್ನೋ logic ಅನ್ನ ಕ್ಲೀನ್ ಆಗಿ
     handle ಮಾಡ್ಬಹುದು (head ಅನ್ನೇ delete ಮಾಡ್ಬೇಕಾದ ಪರಿಸ್ಥಿತಿ
     ಸೇರಿ)

  💡 Interview ನಲ್ಲಿ ಹೇಗೆ ಮಾತಾಡಬೇಕು:
  →  "First approach: for each node, linearly search nums —
      O(n*m) time, too slow for large inputs"
  →  "Optimal: put nums into a HashSet for O(1) lookups, then
      walk the list once with a dummy node, skipping any node
      whose value is in the set — O(n+m) time, O(m) space"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🏷️ SECTION 3 — TECHNIQUE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Primary   : HashSet Lookup + Dummy-Node Single Pass (O(n+m) time)
  Secondary : Linear Search in nums for Each Node (O(n*m) time)

  WHY HashSet over Linear Search?
  → Checking "is this value in nums" via linear search costs
    O(m) EVERY time, for each of the n list nodes — O(n*m)
    total, which is painfully slow when both nums and the list
    can be up to 10^5 elements. Converting nums to a HashSet
    once (O(m)) turns every subsequent membership check into
    O(1), making the whole deletion pass O(n) after that O(m)
    setup — O(n+m) overall.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 💡 SECTION 4 — INTUITION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  The key insight: this problem is really two separate sub-
  problems bolted together — "how do I check membership fast?"
  and "how do I delete nodes from a linked list cleanly?" For
  the first, a HashSet turns a slow repeated scan into instant
  lookups. For the second, the classic trick is a DUMMY node
  before head, so that deleting the very first node (if it
  happens to be in nums) doesn't need special-casing — you just
  walk a `prev` pointer and splice out any node whose value is
  flagged, exactly the same way regardless of position.

  The journey from brute to optimal:
    Brute thought   →  For each list node, scan nums linearly to
                       check membership
    Problem with it →  O(n*m) time — scanning nums repeatedly for
                       every single node is wasteful
    Better question →  "Can membership checks be made O(1)
                       instead of O(m) each?"
    Insight         →  A HashSet built once from nums answers
                       "is this value present" in O(1)
    Optimal         →  Build the set in O(m), then one O(n) pass
                       with a dummy node to splice out flagged
                       nodes — O(n+m) total, O(m) extra space

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🐢 SECTION 5 — APPROACH 1 — BRUTE FORCE (Linear Search Per Node)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    Walk the list with a dummy node and a `prev` pointer. For
    each node, check whether its value exists ANYWHERE in nums
    using a plain linear scan (Python's `in` on a list). If
    found, splice the node out; otherwise, advance prev.

  Pseudocode:
    step 1: dummy = ListNode(0, head); prev = dummy
    step 2: while prev.next:
    step 3:   if prev.next.val in nums (linear scan):
    step 4:       prev.next = prev.next.next
    step 5:   else:
    step 6:       prev = prev.next
    step 7: return dummy.next

  Time  : O(n * m)  →  Why: each of the n nodes triggers an
                            O(m) linear scan through nums
  Space : O(1)       →  Why: only a dummy node and prev pointer,
                            no auxiliary set/map

  ಇದು ಯಾಕೆ ಸಾಕಾಗಲ್ಲ?
    → With both n and m up to 10^5, O(n*m) could mean up to 10^10
      operations — far too slow. The HashSet approach reduces
      each lookup to O(1).

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🚀 SECTION 6 — OPTIMAL (HashSet Lookup + Dummy-Node Single Pass)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    Convert nums into a HashSet once, so membership checks are
    O(1). Then walk the list using a dummy node and a `prev`
    pointer: for each node, if its value is in the set, splice
    it out (prev.next = prev.next.next); otherwise, advance prev
    to that node.

  Key steps:
    1. to_delete = set(nums)
    2. dummy = ListNode(0, head)
       prev = dummy
    3. while prev.next:
           if prev.next.val in to_delete:
               prev.next = prev.next.next
           else:
               prev = prev.next
    4. return dummy.next

  ಕನ್ನಡದಲ್ಲಿ ಒಂದು ಸಲ ಹೇಳಿ:
    → "nums ಅನ್ನ ಒಂದು SET ಗೆ convert ಮಾಡು (O(1) lookup ಗೆ).
       dummy node, prev pointer ಇಟ್ಟುಕೊಂಡು list ಅನ್ನ walk ಮಾಡು
       — ಪ್ರತಿ node ಅದರ value set ಒಳಗೆ ಇದ್ರೆ splice ಔಟ್ ಮಾಡು,
       ಇಲ್ದಿದ್ರೆ prev ಅನ್ನ ಮುಂದೆ ಸಾಗಿಸು!"

  Time  : O(n + m)  →  Why: O(m) to build the set once, O(n) to
                            walk the list with O(1) lookups each
  Space : O(m)       →  Why: the set holds up to m distinct
                            values from nums

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🔍 SECTION 7 — DRY RUN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Input: nums = [1,2,3], head = [1,2,3,4,5]

  Step 1 — build set:
    to_delete = {1, 2, 3}

  Step 2 — walk with dummy + prev:
    dummy -> 1 -> 2 -> 3 -> 4 -> 5
    prev = dummy

    prev.next = 1, 1 in to_delete → splice: prev.next = 2
      (prev stays at dummy)
    prev.next = 2, 2 in to_delete → splice: prev.next = 3
      (prev stays at dummy)
    prev.next = 3, 3 in to_delete → splice: prev.next = 4
      (prev stays at dummy)
    prev.next = 4, 4 NOT in to_delete → advance: prev = 4
    prev.next = 5, 5 NOT in to_delete → advance: prev = 5
    prev.next = None → loop exits

  Output: dummy.next = 4 -> 5 → [4,5] ✓ matches expected

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 ⚠️ SECTION 8 — EDGE CASES — ಇವನ್ನ ಮರೆಯಬೇಡ!
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  ✓ Head itself must be deleted?  →  dummy node handles this
                                      cleanly — no special-casing
                                      needed, prev starts BEFORE
                                      head
  ✓ Every node gets deleted?      →  problem guarantees the
                                      result is never empty, but
                                      the dummy-node logic would
                                      correctly return None if it
                                      somehow could
  ✓ No node matches nums at all?  →  prev just advances through
                                      the whole list, nothing
                                      spliced, list unchanged
  ✓ Consecutive nodes to delete?  →  handled naturally — prev
                                      doesn't move while
                                      splicing, so a run of
                                      matches all get removed
  ✓ nums contains duplicates or
    values not in the list?       →  irrelevant — set membership
                                      only cares whether a value
                                      exists, not how many times
  ✓ Single-node list, that node
    must be deleted?              →  dummy.next ends up None,
                                      correctly returns None (if
                                      the problem allowed it)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📊 SECTION 9 — COMPLEXITY SUMMARY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                              Time      Space
  Brute (linear search)        O(n*m)    O(1)
  HashSet + dummy pass          O(n+m)    O(m)   ← use this ✅

  Time yaake O(n+m)? → O(m) once to build the set, then O(n) to
                        walk the list with O(1) lookups each
  Space yaake O(m)?  → The set stores up to m distinct values
                        from nums

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🎯 SECTION 10 — PATTERN LEARNED — ಇದರಿಂದ ಕಲಿತದ್ದು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Pattern Name: HashSet Lookup Table + Dummy-Node Deletion

  Ee pattern yaavaaga use maadabeeku?
  → Any "remove elements matching SOME external collection"
     problem — convert that collection to a set FIRST so each
     membership check is O(1), instead of re-scanning it
  → Any linked-list deletion problem where the node to remove
     could be the head itself — a dummy node (placed one
     position BEFORE head) eliminates special-casing

  Idee pattern beere problemsalli kaanisatte:
  → Remove Linked List Elements #203 (same dummy-node deletion
     pattern, but condition is "equals a single value" instead
     of "is in a set")
  → Two Sum / Contains Duplicate style problems — same core idea
     of trading an O(m) repeated scan for an O(1) hashset lookup

  Next time intaha problem bandre naanu modalu idannu think maadtene:
  → "External collection (array) ondu value member aagide anta
     repeatedly check madabekagidre → adhanna SET ge convert
     madu modalu, O(1) lookup sigutte. List nodes delete
     madabekagidre, head ne delete aagbahuda anta yochisi —
     dummy node haaki splice madu, special case bedave illa!"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🗣️ SECTION 11 — INTERVIEWALLI HEGE EXPLAIN MAADABEEKU
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  1. Understand:
     "Remove every linked-list node whose value appears in a
      given array nums, and return the resulting list."

  2. Brute force:
     "For each node, linearly scan nums to check membership.
      O(n*m) time — too slow when both can be up to 10^5."

  3. Optimize:
     "Convert nums into a HashSet once, so membership checks
      become O(1). Then walk the list with a dummy node and a
      prev pointer, splicing out any node whose value is flagged."

  4. Code:
     "to_delete = set(nums). dummy = ListNode(0, head), prev =
      dummy. While prev.next: if prev.next.val in to_delete,
      splice it out; else advance prev. Return dummy.next."

  5. Complexity:
     "Time O(n+m) — O(m) to build the set, O(n) to walk the list
      with O(1) lookups. Space O(m) for the set."

  Mukhya: whenever you need to repeatedly check 'is this value
          present in some collection,' convert that collection to
          a HashSet FIRST — it turns O(m) repeated scans into
          O(1) lookups, and always pair list node deletion with a
          dummy node so deleting the head needs no special case!
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
# BRUTE FORCE — O(n * m) Time | O(1) Space (linear search per node)
# ═══════════════════════════════════════════════════════════════════
def delete_nodes_brute(nums, head):
    """
    Idu modala aaloochane — prathi node ge nums olage linear
    scan madi check madi, sikidre splice madu
    """
    dummy = ListNode(0, head)
    prev = dummy

    while prev.next:
        if prev.next.val in nums:
            prev.next = prev.next.next
        else:
            prev = prev.next

    return dummy.next


# ═══════════════════════════════════════════════════════════════════
# OPTIMAL — O(n + m) Time | O(m) Space (hashset + dummy-node pass)
# ═══════════════════════════════════════════════════════════════════
def delete_nodes(nums, head):
    """
    Idu final answer — nums anna set ge convert madi, dummy
    node ittukondu ondhe pass alli sariyada nodes splice madu
    """
    to_delete = set(nums)

    dummy = ListNode(0, head)
    prev = dummy

    while prev.next:
        if prev.next.val in to_delete:
            prev.next = prev.next.next
        else:
            prev = prev.next

    return dummy.next


# ═══════════════════════════════════════════════════════════════════
# TEST CASES
# ═══════════════════════════════════════════════════════════════════
if __name__ == "__main__":
    # Test 1 — Basic (LeetCode example 1)
    head = build([1, 2, 3, 4, 5])
    assert to_list(delete_nodes([1, 2, 3], head)) == [4, 5]

    # Test 2 — LeetCode example 2 (all occurrences of a value removed)
    head = build([1, 2, 1, 2, 1, 2])
    assert to_list(delete_nodes([1], head)) == [2, 2, 2]

    # Test 3 — LeetCode example 3 (nothing removed)
    head = build([1, 2, 3, 4])
    assert to_list(delete_nodes([5], head)) == [1, 2, 3, 4]

    # Test 4 — Head itself must be deleted
    head = build([1, 2, 3])
    assert to_list(delete_nodes([1], head)) == [2, 3]

    # Test 5 — Single node, not deleted
    head = build([5])
    assert to_list(delete_nodes([1], head)) == [5]

    # Test 6 — Consecutive nodes to delete
    head = build([1, 1, 1, 2, 3])
    assert to_list(delete_nodes([1], head)) == [2, 3]

    # Test 7 — nums has duplicates and extras not in list
    head = build([1, 2, 3])
    assert to_list(delete_nodes([2, 2, 99, 100], head)) == [1, 3]

    # Cross-check: brute force must agree on all of the above
    head = build([1, 2, 3, 4, 5])
    assert to_list(delete_nodes_brute([1, 2, 3], head)) == [4, 5]

    head = build([1, 2, 1, 2, 1, 2])
    assert to_list(delete_nodes_brute([1], head)) == [2, 2, 2]

    head = build([1, 2, 3, 4])
    assert to_list(delete_nodes_brute([5], head)) == [1, 2, 3, 4]

    head = build([1, 2, 3])
    assert to_list(delete_nodes_brute([1], head)) == [2, 3]

    head = build([5])
    assert to_list(delete_nodes_brute([1], head)) == [5]

    head = build([1, 1, 1, 2, 3])
    assert to_list(delete_nodes_brute([1], head)) == [2, 3]

    head = build([1, 2, 3])
    assert to_list(delete_nodes_brute([2, 2, 99, 100], head)) == [1, 3]

    print("All tests passed!")
