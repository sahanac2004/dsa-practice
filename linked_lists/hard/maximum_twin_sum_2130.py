"""
╔══════════════════════════════════════════════════════════════════╗
║  MAXIMUM TWIN SUM OF A LINKED LIST                                ║
║  LeetCode #2130  |  Difficulty: Medium  |  Topic: Linked Lists ║
║  (Grouped here with Hard per the curriculum checklist)          ║
║  Link: https://leetcode.com/problems/                           ║
║        maximum-twin-sum-of-a-linked-list/                        ║
╚══════════════════════════════════════════════════════════════════╝

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📘 SECTION 1 — PROBLEM UNDERSTANDING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  You are given the head of a linked list with an EVEN number
  of nodes. For each node at index i (0-indexed), its "twin" is
  the node at index (n - 1 - i), where n is the total node
  count — i.e. the node at the mirrored position from the other
  end. The "twin sum" of a node is its value plus its twin's
  value. Return the MAXIMUM twin sum across the whole list.

  Input : head = singly linked list with an EVEN number of nodes
  Output: the maximum twin sum (an integer)

  Example 1 — basic:
    Input : head = [5,4,2,1]
    Output: 6
    Why?  : node 0 (val=5) twin is node 3 (val=1) -> sum = 6
            node 1 (val=4) twin is node 2 (val=2) -> sum = 6
            max twin sum = 6

  Example 2 — larger list:
    Input : head = [4,2,2,3]
    Output: 7
    Why?  : node 0 (val=4) & node 3 (val=3) -> sum = 7
            node 1 (val=2) & node 2 (val=2) -> sum = 4
            max twin sum = 7

  Example 3 — all same twin sums:
    Input : head = [1,100000]
    Output: 100001

  Constraints:
    - number of nodes is EVEN, between 2 and 10^5
    - 1 <= Node.val <= 10^5

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🧠 SECTION 2 — KANGLISH THINKING — ಹೇಗೆ ಯೋಚಿಸಬೇಕು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  Problem odi aada mele namma brain enu think maadabeeku:

  ಹಂತ 1 — Problem ಅರ್ಥ ಮಾಡಿಕೊಳ್ಳಿ
  ┌─────────────────────────────────────────────────────────┐
  │  Input ಏನು ಕೊಡ್ತಾರೆ?  →  EVEN length linked list          │
  │  Output ಏನು ಬೇಕು?     →  twin pairs (i, n-1-i) ಗಳ ಒಳಗೆ    │
  │                           MAXIMUM sum                       │
  │  Constraints ಏನಿದೆ?   →  length always EVEN (no middle    │
  │                           odd-one-out node to worry about) │
  └─────────────────────────────────────────────────────────┘

  ಹಂತ 2 — ಯಾಕೆ ಇದು tricky? "twin ಅಂದ್ರೆ 'from the end' ಇಂದ
           ಪೇರ್ ಮಾಡಬೇಕು, ಆದ್ರೆ singly linked list ಲ್ಲಿ ಹಿಂದಿಂದ
           ಮುಂದೆ ನೇರವಾಗಿ ಹೋಗೋಕೆ ಆಗಲ್ಲ!" ಅಂತ ಯೋಚಿಸಿ
  →  "front ಇಂದ i-th node" ಸುಲಭ, ಆದ್ರೆ "(n-1-i)-th node"
     (ಅಂದ್ರೆ back ಇಂದ i-th) ಅನ್ನ ನೇರವಾಗಿ ಹೋಗೋಕೆ ಆಗಲ್ಲ — ಬೇಕಾಗಿರೋದು
     front ಮತ್ತು back ಅನ್ನ ಒಟ್ಟಿಗೇ walk ಮಾಡೋ ಟ್ರಿಕ್

  ಹಂತ 3 — ಮೊದಲ simple idea (brute force) ಏನು?
  →  "ಎಲ್ಲಾ values ಅನ್ನ array ಗೆ ಹಾಕಿ, i ಮತ್ತು (n-1-i) index
      ಗಳ ಸಮ್ ಅನ್ನ ಚೆಕ್ ಮಾಡಿ max ಹುಡುಕ್ಕಿದ್ರೆ?"
  →  ಕೆಲಸ ಆಗುತ್ತೆ, ಆದ್ರೆ O(n) extra space ಬೇಕಾಗುತ್ತೆ array ಗೆ

  ಹಂತ 4 — Optimal idea (ಒಂದೇ pass, O(1) space) ಹೇಗೆ ಬರುತ್ತೆ?
  →  "list ಅ ಮೊದಲ ಅರ್ಧ ಅನ್ನ REVERSE ಮಾಡಿದ್ರೆ (slow/fast ಬಳಸಿ
      middle ಹುಡುಕಿ), ಈಗ second half ಅನ್ನ FORWARD ಓಡಿದಾಗ, first
      half ಅನ್ನ REVERSED order ಲ್ಲಿ ಓಡಿದಾಗ — ಎರಡೂ ಒಟ್ಟಿಗೆ ಪ್ರತಿ
      step ಗೂ 'twin pair' ಆಗ್ತಾರೆ!" ಅಂತ ಯೋಚಿಸಿ
  →  reversed_first_half[0] + second_half[0] = node 0 + node
     (n-1) ಅ twin sum! reversed_first_half[1] + second_half[1]
     = node 1 + node (n-2) ಅ twin sum! ಇದೇ ಕ್ರಮ ಮುಂದುವರಿಯುತ್ತೆ

  ಹಂತ 5 — Technique ಯಾಕೆ ಇಲ್ಲಿ ಕೆಲಸ ಮಾಡುತ್ತೆ?
  →  "Reverse ಮಾಡಿದ ಮೇಲೆ, first half ಅ ಕ್ರಮ ಹಿಂದಿಂದ ಮುಂದೆ
     (ಅಂದ್ರೆ ಮೂಲ list ಅ KONE node ಗಳಿಂದ MODALU node ಗಳಿಗೆ) ಆಗುತ್ತೆ
     — ಇದೇ ಬೇಕಾಗಿರೋ 'back-to-front' ಕ್ರಮ! ಈಗ second half ಅನ್ನ
     front-to-back ಓಡಿದಾಗ, ಎರಡೂ ಒಟ್ಟಿಗೆ ಹೋದ್ರೆ ಅದೇ twin pairs!

  💡 Interview ನಲ್ಲಿ ಹೇಗೆ ಮಾತಾಡಬೇಕು:
  →  "First approach: dump values into an array, pair index i
      with index n-1-i, take the max — O(n) time, O(n) space"
  →  "Optimal: find the middle with slow/fast pointers, reverse
      the first half in place. Now walk the reversed first half
      and the second half TOGETHER, step by step — each pair of
      current nodes is exactly a twin pair. Track the max sum.
      O(n) time, O(1) extra space."

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🏷️ SECTION 3 — TECHNIQUE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Primary   : Find Middle + Reverse First Half + Parallel Walk
              (O(n) time, O(1) space)
  Secondary : Extract to Array + Pair Indices i and n-1-i

  WHY Reverse-First-Half over Array Extraction?
  → Extracting to an array works but needs O(n) extra space to
    index both ends. Reversing the first half physically
    reorders those nodes so that walking it front-to-back now
    visits them in EXACTLY the same order as walking the
    original list back-to-front — meaning two simple pointers
    (one on the reversed first half, one on the second half),
    advancing together, land on twin pairs automatically, no
    index arithmetic needed.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 💡 SECTION 4 — INTUITION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  The key insight: a "twin" pairs the FRONT half with the BACK
  half in MIRRORED order (node 0 with node n-1, node 1 with node
  n-2, etc.). If the first half is physically reversed, walking
  it from its (new) head now visits nodes in the order n/2-1,
  n/2-2, ..., 1, 0 — wait, more precisely: reversing [0..n/2-1]
  makes its new head be the OLD node at index n/2-1 and its new
  tail be the OLD node at index 0. Walking the reversed first
  half from head pairs naturally with walking the second half
  from ITS head — reversed_first[0] (= original last-of-first-
  half) pairs with second_half[0] (= original first-of-second-
  half)... actually what matters practically is: reversing the
  FIRST half and then walking it in STEP with the second half
  produces exactly the twin sums, because reversal flips the
  traversal direction to match the "from the end" requirement.

  The journey from brute to optimal:
    Brute thought   →  Extract values to an array, pair up
                       index i with index (n-1-i) for each i,
                       take the maximum sum
    Problem with it →  O(n) extra space for the array
    Better question →  "Can the list itself be rearranged so a
                       simple parallel walk produces twin pairs
                       directly?"
    Insight         →  Reversing the first half re-threads it so
                       that, walked alongside the second half, a
                       single step on each side produces exactly
                       one twin pair
    Optimal         →  Find the middle (slow/fast), reverse the
                       first half in place, walk both halves
                       together summing and tracking the max —
                       O(n) time, O(1) extra space

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🐢 SECTION 5 — APPROACH 1 — BRUTE FORCE (Array Index Pairing)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    Walk the list once, collecting all values into an array.
    For each i from 0 to n//2 - 1, compute values[i] +
    values[n-1-i], and track the maximum such sum.

  Pseudocode:
    step 1: values = [all node values, in order]
    step 2: n = len(values)
    step 3: max_sum = 0
    step 4: for i in range(n // 2):
    step 5:     max_sum = max(max_sum, values[i] + values[n-1-i])
    step 6: return max_sum

  Time  : O(n)  →  Why: one linear scan to collect values, one
                        linear scan to compute all twin sums
  Space : O(n)  →  Why: stores all node values in an array

  ಇದು ಯಾಕೆ ಸಾಕಾಗಲ್ಲ?
    → Correct and O(n) time, but uses O(n) extra space — the
      reverse-first-half approach reuses the existing nodes
      directly and needs no array.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🚀 SECTION 6 — OPTIMAL (Find Middle + Reverse First Half + Parallel Walk)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    Find the middle of the list using slow/fast pointers (since
    length is guaranteed even, slow ends up exactly at the start
    of the second half). Reverse the FIRST half in place (using
    the standard 3-pointer technique, walking from head up to
    but not including slow). Now walk two pointers — one
    starting at the reversed first half's new head, one at
    `slow` (start of the second half) — together, step by step,
    summing node values and tracking the maximum.

  Key steps:
    1. slow = fast = head
       while fast and fast.next:
           slow = slow.next
           fast = fast.next.next
       (slow now points to the start of the second half)
    2. prev = None
       curr = head
       while curr is not slow:
           next_node = curr.next
           curr.next = prev
           prev = curr
           curr = next_node
       (prev is now the head of the reversed first half)
    3. max_sum = 0
       first, second = prev, slow
       while first and second:
           max_sum = max(max_sum, first.val + second.val)
           first = first.next
           second = second.next
    4. return max_sum

  ಕನ್ನಡದಲ್ಲಿ ಒಂದು ಸಲ ಹೇಳಿ:
    → "ಮೊದಲು slow/fast ಬಳಸಿ second half ಅ start ಹುಡುಕು. ಆಮೇಲೆ
       first half ಅನ್ನ (head ಇಂದ slow ತನಕ) 3-pointer reversal
       ಬಳಸಿ reverse ಮಾಡು. ಈಗ reversed first half ಮತ್ತು second
       half ಅನ್ನ ಒಟ್ಟಿಗೆ step-by-step walk ಮಾಡಿ, ಪ್ರತಿ step ಗೂ
       values ಅ sum ಅನ್ನ max ಜೊತೆ compare ಮಾಡು!"

  Time  : O(n)  →  Why: finding the middle, reversing the first
                        half, and the parallel walk are all
                        separate linear passes, combined still O(n)
  Space : O(1)  →  Why: only a handful of pointer variables and
                        a running max — no array

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🔍 SECTION 7 — DRY RUN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Input: head = [5,4,2,1]

  Step 1 — find middle:
    slow=5, fast=5
    iter 1: slow=4, fast=2
    iter 2: slow=2, fast=None (2.next=1, then 1.next=None... )
      Actually: fast=5 -> fast.next.next: 5.next=4, 4.next=2,
      so fast becomes 2 after iter1; iter2: fast=2.next.next,
      2.next=1, 1.next=None -> fast=None
    loop exits (fast is None)
    slow = node valued 2 (start of second half)

  Step 2 — reverse first half (head=5 up to but not including
  slow=2):
    prev=None, curr=5
    iter: next_node=4, 5.next=None, prev=5, curr=4
    iter: next_node=2 (=slow, stop condition met after this),
          4.next=5, prev=4, curr=2 -> curr is slow, loop exits
    prev = node valued 4 (new head of reversed first half: 4->5)

  Step 3 — parallel walk:
    first = node(4) [chain: 4 -> 5], second = node(2) [chain: 2 -> 1]
    step 1: first.val(4) + second.val(2) = 6; max_sum = 6
            first = node(5), second = node(1)
    step 2: first.val(5) + second.val(1) = 6; max_sum = 6
            first = None, second = None
    loop exits

  Output: 6 ✓ matches expected

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 ⚠️ SECTION 8 — EDGE CASES — ಇವನ್ನ ಮರೆಯಬೇಡ!
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  ✓ Minimum length (2 nodes)?     →  the only twin pair is
                                      (node 0, node 1) — handled
                                      as a single iteration of
                                      the parallel walk
  ✓ All twin sums equal?          →  max_sum correctly stays at
                                      that common value throughout
  ✓ Maximum twin sum at the very
    first pair vs. the very last
    pair?                         →  the parallel walk checks
                                      every pair unconditionally,
                                      so position doesn't matter
  ✓ Largest allowed values
    (10^5 + 10^5)?                →  plain integer addition in
                                      Python handles this with no
                                      overflow concerns
  ✓ Length is always even
    (guaranteed by constraints)?  →  slow/fast middle-finding
                                      relies on this — no odd-
                                      length special case needed

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📊 SECTION 9 — COMPLEXITY SUMMARY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                                   Time    Space
  Brute (array index pairing)      O(n)    O(n)
  Reverse-half + parallel walk      O(n)    O(1)   ← use this ✅

  Time yaake O(n)?  → Three separate linear passes (find middle,
                       reverse first half, parallel walk), each
                       bounded by n, combined still O(n)
  Space yaake O(1)? → Only pointer variables and a running max —
                       the original nodes are reused directly

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🎯 SECTION 10 — PATTERN LEARNED — ಇದರಿಂದ ಕಲಿತದ್ದು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Pattern Name: Reverse Half + Parallel Walk (Mirror Pairing)

  Ee pattern yaavaaga use maadabeeku?
  → Any problem needing to pair FRONT elements with BACK
     elements of a linked list (palindrome checks, mirror
     comparisons, twin sums) — instead of indexing from the
     end (impossible directly on a singly linked list),
     reverse HALF the list so a simple parallel walk produces
     mirrored pairs automatically
  → A close cousin of the "find middle + reverse second half"
     trick from Reorder List #143 and Palindrome Linked List
     #234 — here only ONE half needs reversing since both
     halves are walked independently rather than merged back

  Idee pattern beere problemsalli kaanisatte:
  → Palindrome Linked List #234 (same find-middle + reverse-half
     foundation, used to COMPARE instead of SUM mirrored pairs)
  → Reorder List #143 (reverses the SECOND half instead, then
     merges rather than just comparing/summing)

  Next time intaha problem bandre naanu modalu idannu think maadtene:
  → "Linked list ina FRONT mathu BACK elements anna pair
     madabekagidre (mirror comparison, twin sum, palindrome
     check) → index from the end madoke singly linked list
     alli aagalla, bere ondhu half reverse madi parallel walk
     madu — mirrored pairs automatic aagi sigutte, O(1) space!"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🗣️ SECTION 11 — INTERVIEWALLI HEGE EXPLAIN MAADABEEKU
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  1. Understand:
     "For a linked list of even length n, each node at index i
      pairs with the node at index n-1-i (a 'twin'). Return the
      maximum sum of any twin pair."

  2. Brute force:
     "Extract values to an array, pair index i with n-1-i for
      each i < n/2, take the max. O(n) time, O(n) space."

  3. Optimize:
     "Find the middle with slow/fast pointers (length is even,
      so slow lands exactly at the second half's start). Reverse
      the first half in place. Walk the reversed first half and
      the second half together, step by step — each step is a
      twin pair. Track the max sum."

  4. Code:
     "slow/fast to find middle. Standard 3-pointer reversal on
      [head, slow). Two pointers (reversed-first-head, slow)
      advance together; max_sum = max(max_sum, first.val +
      second.val) each step."

  5. Complexity:
     "Time O(n) — three linear passes. Space O(1) — pointer
      rewiring only, no extra storage."

  Mukhya: whenever front and back elements of a SINGLY linked
          list need to be paired up, reversing one half turns an
          impossible 'index from the end' into a simple parallel
          walk — no array, no extra space!
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
# BRUTE FORCE — O(n) Time | O(n) Space (array index pairing)
# ═══════════════════════════════════════════════════════════════════
def pair_sum_brute(head):
    """
    Idu modala aaloochane — values array ge haaki, index i
    mathu n-1-i pair madi max sum hudu
    """
    values = to_list(head)
    n = len(values)
    max_sum = 0

    for i in range(n // 2):
        max_sum = max(max_sum, values[i] + values[n - 1 - i])

    return max_sum


# ═══════════════════════════════════════════════════════════════════
# OPTIMAL — O(n) Time | O(1) Space (reverse first half + parallel walk)
# ═══════════════════════════════════════════════════════════════════
def pair_sum(head):
    """
    Idu final answer — middle hudu, first half reverse madi,
    eradu halves parallel walk madi twin sums track madu
    """
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    prev = None
    curr = head
    while curr is not slow:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node

    max_sum = 0
    first, second = prev, slow
    while first and second:
        max_sum = max(max_sum, first.val + second.val)
        first = first.next
        second = second.next

    return max_sum


# ═══════════════════════════════════════════════════════════════════
# TEST CASES
# ═══════════════════════════════════════════════════════════════════
if __name__ == "__main__":
    # Test 1 — Basic (LeetCode example 1)
    head = build([5, 4, 2, 1])
    assert pair_sum(head) == 6

    # Test 2 — LeetCode example 2
    head = build([4, 2, 2, 3])
    assert pair_sum(head) == 7

    # Test 3 — LeetCode example 3 (minimum length)
    head = build([1, 100000])
    assert pair_sum(head) == 100001

    # Test 4 — All twin sums equal
    head = build([3, 3, 3, 3])
    assert pair_sum(head) == 6

    # Test 5 — Larger list, max at a middle pair
    head = build([1, 2, 10, 10, 2, 1])
    assert pair_sum(head) == 20

    # Test 6 — Two nodes, distinct values
    head = build([7, 1])
    assert pair_sum(head) == 8

    # Cross-check: brute force must agree on all of the above
    head = build([5, 4, 2, 1])
    assert pair_sum_brute(head) == 6

    head = build([4, 2, 2, 3])
    assert pair_sum_brute(head) == 7

    head = build([1, 100000])
    assert pair_sum_brute(head) == 100001

    head = build([3, 3, 3, 3])
    assert pair_sum_brute(head) == 6

    head = build([1, 2, 10, 10, 2, 1])
    assert pair_sum_brute(head) == 20

    head = build([7, 1])
    assert pair_sum_brute(head) == 8

    print("All tests passed!")
