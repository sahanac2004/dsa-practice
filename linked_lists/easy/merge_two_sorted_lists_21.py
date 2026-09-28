"""
╔══════════════════════════════════════════════════════════════════╗
║  MERGE TWO SORTED LISTS                                          ║
║  LeetCode #21  |  Difficulty: Easy  |  Topic: Linked Lists      ║
║  Link: https://leetcode.com/problems/merge-two-sorted-lists/    ║
╚══════════════════════════════════════════════════════════════════╝

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📘 SECTION 1 — PROBLEM UNDERSTANDING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Given the heads of two sorted linked lists list1 and list2,
  merge them into one sorted linked list and return its head.
  The merged list should be made by splicing together the nodes
  of the two lists (not creating new nodes).

  Input : list1, list2 = heads of two sorted linked lists
  Output: head of merged sorted linked list

  Example 1 — basic:
    Input : list1 = 1→2→4, list2 = 1→3→4
    Output: 1→1→2→3→4→4
    Why?  : Compare heads each time, pick smaller

  Example 2 — slightly tricky (one empty):
    Input : list1 = [], list2 = [0]
    Output: [0]
    Why?  : Empty list + any list = that list

  Constraints:
    - 0 <= number of nodes in each list <= 50
    - -100 <= Node.val <= 100
    - Both lists are sorted in non-decreasing order

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🧠 SECTION 2 — KANGLISH THINKING — ಹೇಗೆ ಯೋಚಿಸಬೇಕು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  Problem odi aada mele namma brain enu think maadabeeku:

  ಹಂತ 1 — Problem ಅರ್ಥ ಮಾಡಿಕೊಳ್ಳಿ
  ┌─────────────────────────────────────────────────────────┐
  │  Input ಏನು ಕೊಡ್ತಾರೆ?  →  2 sorted linked lists        │
  │  Output ಏನು ಬೇಕು?     →  1 merged sorted list         │
  │  Constraints ಏನಿದೆ?   →  existing nodes reuse maadu   │
  │                           new nodes create ಮಾಡಬೇಡ     │
  └─────────────────────────────────────────────────────────┘

  ಹಂತ 2 — ನನಗೆ ಗೊತ್ತಿರೋ simple way ಏನು?
  →  Both lists values collect ಮಾಡಿ sort ಮಾಡಿ
     new list build ಮಾಡೋಣ → O(n log n) + O(n) space
  →  ಆದರೆ ಇದು slow ಯಾಕೆ?
     Already sorted iddare! O(n) possible using two pointers

  ಹಂತ 3 — Better way ಹೇಗೆ ಯೋಚಿಸುವುದು?
  →  "Merge Sort ರ merge step ಅಲ್ಲವಾ ಇದು?"
  →  YES! Two pointers, compare heads, pick smaller
  →  Dummy node trick — result list ಅನ್ನು build ಮಾಡಲು
     dummy head ಇಟ್ಟರೆ edge cases handle easy ಆಗತ್ತೆ!
  →  ಇದರಿಂದ ನಾವು Dummy Node + Two Pointer use ಮಾಡಬಹuದು!

  ಹಂತ 4 — Technique ಯಾಕೆ ಇಲ್ಲಿ ಕೆಲಸ ಮಾಡುತ್ತೆ?
  →  Dummy node = fake head, avoids null checks at start
  →  curr pointer builds the merged list
  →  l1 and l2 advance as we pick nodes
  →  Remaining nodes just attach at end!

  💡 Interview ನಲ್ಲಿ ಹೇಗೆ ಮಾತಾಡಬೇಕು:
  →  "This is the merge step of merge sort on linked lists"
  →  "Dummy node trick avoids special casing the head"
  →  "Compare heads, attach smaller, advance that pointer"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🏷️ SECTION 3 — TECHNIQUE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Primary   : Dummy Node + Two Pointer Merge
  Secondary : Recursion (elegant but O(n) stack space)

  WHY Dummy Node?
  → Without dummy: need to special case selecting the first node
  → With dummy: curr starts at dummy, just keep appending
  → Return dummy.next as the real head
  → Classic linked list trick used in many problems!

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 💡 SECTION 4 — INTUITION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Think of two sorted card piles. You compare the top cards,
  pick the smaller one and put it in your hand. Repeat until
  one pile is empty, then add remaining cards from other pile.

  The dummy node is like a placeholder in your hand —
  you build the merged list from dummy.next.

  The journey from brute to optimal:
    Brute thought   →  Collect all + sort + rebuild → O(n log n)
    Problem with it →  Lists already sorted — don't need to sort!
    Better question →  "Can I merge in O(n) using sorted property?"
    Insight         →  YES! Two pointer merge — same as merge sort
                       Dummy node makes head handling clean
    Optimal         →  O(m+n) time, O(1) space iterative

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🐢 SECTION 5 — APPROACH 1 — BRUTE FORCE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    Collect all values from both lists into an array.
    Sort the array. Build a new linked list from sorted values.

  Pseudocode:
    step 1: vals = all values from list1 + list2
    step 2: sort vals
    step 3: build new linked list from vals

  Time  : O((m+n) log(m+n))  →  Why: sorting
  Space : O(m+n)             →  Why: vals array + new nodes

  ಇದು ಯಾಕೆ ಸಾಕಾಗಲ್ಲ?
    → Lists already sorted — sort step is waste!
    → Creates new nodes — problem says reuse existing!

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🚀 SECTION 6 — APPROACH 2 — OPTIMAL ITERATIVE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    Use a dummy node to simplify head handling.
    Use curr pointer to build merged list.
    Compare l1 and l2 heads, attach smaller, advance that pointer.

  Key steps:
    1. dummy = ListNode(0), curr = dummy
    2. While l1 and l2 both exist:
       a. if l1.val <= l2.val → curr.next=l1, l1=l1.next
       b. else → curr.next=l2, l2=l2.next
       c. curr = curr.next
    3. curr.next = l1 if l1 else l2  (attach remaining)
    4. return dummy.next

  ಕನ್ನಡದಲ್ಲಿ ಒಂದು ಸಲ ಹೇಳಿ:
    → "dummy node create maadu. curr = dummy.
       l1 ಮತ್ತು l2 compare maadu — smaller ಅನ್ನು curr.next ಗೆ attach.
       ಆ pointer advance maadu. curr ಕೂಡ advance.
       Loop end ಆದ್ರೆ remaining nodes attach maadu.
       dummy.next return maadu — that's our merged head!"

  Time  : O(m + n)  →  Why: each node visited exactly once
  Space : O(1)      →  Why: only dummy, curr pointers

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🚀 SECTION 7 — APPROACH 3 — RECURSIVE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    Compare heads. Smaller head's next = merge(smaller.next, other).

  ಕನ್ನಡದಲ್ಲಿ ಒಂದು ಸಲ ಹೇಳಿ:
    → "l1.val < l2.val iddre: l1.next = merge(l1.next, l2)
       return l1. Else: l2.next = merge(l1, l2.next) return l2.
       Elegant! But O(m+n) call stack."

  Time  : O(m + n)  →  Why: each node visited once
  Space : O(m + n)  →  Why: recursion call stack

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🔍 SECTION 8 — DRY RUN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Input: l1=1→2→4, l2=1→3→4
  dummy→None, curr=dummy

  Step 1: l1.val=1, l2.val=1 → equal, pick l1
    curr.next=1(l1), l1=2, curr=1
    dummy→1

  Step 2: l1.val=2, l2.val=1 → l2 smaller
    curr.next=1(l2), l2=3, curr=1
    dummy→1→1

  Step 3: l1.val=2, l2.val=3 → l1 smaller
    curr.next=2, l1=4, curr=2
    dummy→1→1→2

  Step 4: l1.val=4, l2.val=3 → l2 smaller
    curr.next=3, l2=4, curr=3
    dummy→1→1→2→3

  Step 5: l1.val=4, l2.val=4 → equal, pick l1
    curr.next=4(l1), l1=None, curr=4
    dummy→1→1→2→3→4

  l1=None → exit loop
  curr.next = l2 = 4(l2)
  dummy→1→1→2→3→4→4 ✓

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 ⚠️ SECTION 9 — EDGE CASES — ಇವನ್ನ ಮರೆಯಬೇಡ!
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  ✓ Both empty?          →  return None (dummy.next = None)
  ✓ One empty?           →  curr.next = other list directly
  ✓ Equal values?        →  pick either (we pick l1) — stable
  ✓ Different lengths?   →  remaining nodes attached at end

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📊 SECTION 10 — COMPLEXITY SUMMARY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                  Time          Space
  Brute Force     O((m+n)logn)  O(m+n)
  Iterative       O(m+n)        O(1)    ← use this ✅
  Recursive       O(m+n)        O(m+n)  (call stack)

  Time yaake O(m+n)? → Each node from both lists visited once
  Space yaake O(1)?  → Only dummy and curr pointers

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🎯 SECTION 11 — PATTERN LEARNED — ಇದರಿಂದ ಕಲಿತದ್ದು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Pattern Name: Dummy Node + Two Pointer Merge

  Dummy Node trick — when to use:
  → Building a new linked list from scratch
  → Avoids special casing the very first node
  → Return dummy.next as the actual head
  → Used in: merge lists, remove nodes, partition lists

  Idee pattern beere problemsalli kaanisatte:
  → Merge K Sorted Lists #23 (extend this to k lists!)
  → Sort List #148 (merge sort uses this merge step)
  → Reorder List #143 (merge modified halves)
  → Add Two Numbers #2 (build result with dummy node)

  Next time intaha problem bandre naanu modalu idannu think maadtene:
  → "Two sorted lists merge beeka?
     → Dummy node! curr=dummy. Compare heads, pick smaller,
     advance that pointer + curr. Remaining attach at end.
     dummy.next = merged head!"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🗣️ SECTION 12 — INTERVIEWALLI HEGE EXPLAIN MAADABEEKU
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  1. Understand:
     "Merge two sorted linked lists into one sorted list
      by reusing existing nodes."

  2. Brute force:
     "Collect all values, sort, rebuild. O((m+n) log n) — ignores
      the fact that lists are already sorted!"

  3. Optimize:
     "This is the merge step of merge sort. Use dummy node to
      simplify head handling. Compare l1 and l2 heads each step,
      attach smaller to curr, advance that pointer and curr."

  4. Code:
     "dummy=ListNode(0), curr=dummy. While both exist: compare,
      attach smaller, advance. After loop: attach remaining.
      Return dummy.next."

  5. Complexity:
     "Time O(m+n) — each node once. Space O(1) — 2 pointers."

  Mukhya: summane kuutu code bareyabeda!
          Dummy node trick — explain WHY it simplifies things!
          Recursive version also beautiful — show both!
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
# BRUTE FORCE — O((m+n) log(m+n)) Time | O(m+n) Space
# ═══════════════════════════════════════════════════════════════════
def merge_two_lists_brute(list1, list2):
    """Idu modala aaloochane — collect, sort, rebuild"""
    vals = []
    curr = list1
    while curr:
        vals.append(curr.val)
        curr = curr.next
    curr = list2
    while curr:
        vals.append(curr.val)
        curr = curr.next

    vals.sort()
    dummy = ListNode(0)
    curr = dummy
    for v in vals:
        curr.next = ListNode(v)
        curr = curr.next
    return dummy.next


# ═══════════════════════════════════════════════════════════════════
# OPTIMAL ITERATIVE — O(m+n) Time | O(1) Space
# ═══════════════════════════════════════════════════════════════════
def merge_two_lists(list1, list2):
    """
    Idu final answer — dummy node + two pointer merge
    Merge step of merge sort on linked lists!
    """
    dummy = ListNode(0)   # dummy head — avoids null checks
    curr  = dummy

    while list1 and list2:
        if list1.val <= list2.val:
            curr.next = list1     # attach smaller node
            list1     = list1.next
        else:
            curr.next = list2
            list2     = list2.next
        curr = curr.next          # advance curr

    # attach remaining nodes (at most one list has nodes left)
    curr.next = list1 if list1 else list2

    return dummy.next             # dummy.next = real head


# ═══════════════════════════════════════════════════════════════════
# RECURSIVE — O(m+n) Time | O(m+n) Space
# ═══════════════════════════════════════════════════════════════════
def merge_two_lists_recursive(list1, list2):
    """
    Recursive: smaller head's next = merge(smaller.next, other)
    Elegant but O(m+n) call stack
    """
    if not list1:
        return list2
    if not list2:
        return list1

    if list1.val <= list2.val:
        list1.next = merge_two_lists_recursive(list1.next, list2)
        return list1
    else:
        list2.next = merge_two_lists_recursive(list1, list2.next)
        return list2


# ═══════════════════════════════════════════════════════════════════
# TEST CASES
# ═══════════════════════════════════════════════════════════════════
if __name__ == "__main__":
    # Test 1 — Basic
    assert to_list(merge_two_lists(
        build([1,2,4]), build([1,3,4]))) == [1,1,2,3,4,4]

    # Test 2 — Both empty
    assert to_list(merge_two_lists(None, None)) == []

    # Test 3 — One empty
    assert to_list(merge_two_lists(None, build([0]))) == [0]

    # Test 4 — Different lengths
    assert to_list(merge_two_lists(
        build([1,3,5,7]), build([2,4]))) == [1,2,3,4,5,7]

    # Test 5 — Recursive version
    assert to_list(merge_two_lists_recursive(
        build([1,2,4]), build([1,3,4]))) == [1,1,2,3,4,4]

    # Test 6 — All same values
    assert to_list(merge_two_lists(
        build([1,1,1]), build([1,1]))) == [1,1,1,1,1]

    print("All tests passed!")
