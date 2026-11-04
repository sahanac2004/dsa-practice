"""
╔══════════════════════════════════════════════════════════════════╗
║  REVERSE LINKED LIST II                                           ║
║  LeetCode #92  |  Difficulty: Medium  |  Topic: Linked Lists   ║
║  Link: https://leetcode.com/problems/reverse-linked-list-ii/   ║
╚══════════════════════════════════════════════════════════════════╝

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📘 SECTION 1 — PROBLEM UNDERSTANDING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Given the head of a singly linked list and two integers left
  and right (1-indexed, left <= right), reverse the nodes of
  the list from position left to position right, and return
  the reversed list. Everything before `left` and after `right`
  must stay exactly in place — only the SUBLIST in between gets
  reversed.

  Input : head = singly linked list, left = start position,
          right = end position (both 1-indexed)
  Output: head of the list with positions [left, right] reversed

  Example 1 — basic:
    Input : head = [1,2,3,4,5], left = 2, right = 4
    Output: [1,4,3,2,5]
    Why?  : positions 2 through 4 (values 2,3,4) get reversed
            to 4,3,2 — positions 1 and 5 (values 1,5) stay put

  Example 2 — reverse the whole list:
    Input : head = [5], left = 1, right = 1
    Output: [5]
    Why?  : reversing a single node is a no-op

  Constraints:
    - 1 <= number of nodes <= 500
    - -500 <= Node.val <= 500
    - 1 <= left <= right <= number of nodes
    - Follow-up: solve in ONE PASS

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🧠 SECTION 2 — KANGLISH THINKING — ಹೇಗೆ ಯೋಚಿಸಬೇಕು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  Problem odi aada mele namma brain enu think maadabeeku:

  ಹಂತ 1 — Problem ಅರ್ಥ ಮಾಡಿಕೊಳ್ಳಿ
  ┌─────────────────────────────────────────────────────────┐
  │  Input ಏನು ಕೊಡ್ತಾರೆ?  →  linked list, left, right        │
  │                           positions                        │
  │  Output ಏನು ಬೇಕು?     →  [left, right] ನಡುವಿನ ಭಾಗ ಮಾತ್ರ   │
  │                           reverse ಆದ list                 │
  │  Constraints ಏನಿದೆ?   →  left ಗೆ ಮೊದಲಿನ, right ಗೆ ಆಮೇಲಿನ  │
  │                           ಭಾಗ as-is ಇರ್ಬೇಕು, ONE pass ಆಗ್ಬೇಕು │
  └─────────────────────────────────────────────────────────┘

  ಹಂತ 2 — ಯಾಕೆ ಇದು tricky? "reverse ಮಾಡೋ ಭಾಗ ಅನ್ನ ಮೊದಲಿನ ಭಾಗ
           ಗೆ ಮತ್ತೆ ಹೇಗೆ ಜೋಡಿಸೋದು?" ಅಂತ ಯೋಚಿಸಿ
  →  ಪೂರ್ತಿ list reverse ಮಾಡೋ ಟ್ರಿಕ್ ಗೊತ್ತು (3-pointer), ಆದ್ರೆ
     ಇಲ್ಲಿ ಕೇವಲ MIDDLE ಭಾಗ ಅನ್ನ ಮಾತ್ರ reverse ಮಾಡ್ಬೇಕು — reverse
     ಆದ ಮೇಲೆ ಅದರ "ಮುಂದಿನ" ಮತ್ತು "ಹಿಂದಿನ" connections ಅನ್ನ
     ಸರಿಯಾಗಿ ಮರು-ಜೋಡಿಸ್ಬೇಕು

  ಹಂತ 3 — ಮೊದಲ simple idea (brute force) ಏನು?
  →  "ಎಲ್ಲಾ values ಅನ್ನ array ಗೆ ಹಾಕಿ, [left-1, right-1] slice
      ಅನ್ನ reverse ಮಾಡಿ, ಮತ್ತೆ list ಕಟ್ಟಿದ್ರೆ?"
  →  ಕೆಲಸ ಆಗುತ್ತೆ, ಆದ್ರೆ O(n) extra space ಬೇಕಾಗುತ್ತೆ array ಗೆ

  ಹಂತ 4 — Optimal idea (ONE pass, in-place) ಹೇಗೆ ಬರುತ್ತೆ?
  →  "left position ತನಕ ನಡೆದು ಹೋಗಿ, ಅಲ್ಲಿಂದ 3-pointer reversal
      technique ಬಳಸಿ (right - left + 1) nodes ಅಷ್ಟೇ reverse
      ಮಾಡಿದ್ರೆ?" ಅಂತ ಯೋಚಿಸಿ: left ಗೆ ಮೊದಲಿನ node (`before`) ಅನ್ನ
      ನೆನಪಿಟ್ಟುಕೊಂಡು, reverse ಮುಗಿದ ಮೇಲೆ before.next ಮತ್ತು
      reversed ಭಾಗ ಅ ಕೊನೆ ಅನ್ನ ಸರಿಯಾಗಿ ಜೋಡಿಸಿ

  ಹಂತ 5 — Technique ಯಾಕೆ ಇಲ್ಲಿ ಕೆಲಸ ಮಾಡುತ್ತೆ?
  →  dummy node ಬಳಸಿದ್ರೆ "left=1 ಆಗಿದ್ರೆ before ಇಲ್ಲ" ಅನ್ನೋ
     special case ಬೇಡ — dummy ಯಾವಾಗಲೂ before ಆಗಿ ಕೆಲಸ ಮಾಡುತ್ತೆ.
     reverse ಮಾಡೋ sublist ಅ FIRST node (reversal ಗೆ ಮೊದಲು) ಅದೇ
     reversal ಆದ ಮೇಲೆ ಅ LAST node ಆಗುತ್ತೆ — ಅದನ್ನ `before.next`
     ಗೆ ಜೋಡಿಸಿ, ಮತ್ತು reversal ಗೆ ಮೊದಲಿನ pointer ಅ current position
     ಅನ್ನ "after" ಗೆ ಜೋಡಿಸಿ ಪೂರ್ತಿ ಮಾಡ್ಬಹುದು

  💡 Interview ನಲ್ಲಿ ಹೇಗೆ ಮಾತಾಡಬೇಕು:
  →  "First approach: extract values to an array, reverse the
      slice [left-1, right-1], rebuild — O(n) time, O(n) space"
  →  "Optimal: walk to position left-1 using a dummy node, then
      do an in-place 3-pointer reversal for exactly
      (right-left+1) nodes, then reconnect the reversed segment
      to the untouched before/after parts — O(n) time, O(1)
      space, single pass"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🏷️ SECTION 3 — TECHNIQUE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Primary   : In-Place Sublist Reversal with Dummy Node (O(1) space)
  Secondary : Extract to Array + Reverse Slice + Rebuild (O(n) space)

  WHY In-Place Sublist Reversal over Array Extraction?
  → Extracting to an array works but needs O(n) extra space to
    hold values temporarily. The sublist to reverse is already
    sitting right there in the list — the same 3-pointer
    reversal trick used for reversing a WHOLE list works
    identically on just a SEGMENT of it, as long as you
    remember the node right before the segment (to reconnect
    afterward) and correctly identify the segment's original
    first node (which becomes its new tail after reversal).

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 💡 SECTION 4 — INTUITION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  The key insight: reversing a SEGMENT of a list is exactly like
  reversing the WHOLE list, except you stop early and reconnect
  the ends. Use a dummy node before head so position `left`
  being the very first node needs no special casing. Walk a
  pointer to the node just before position `left` — call it
  `before`. The node at position `left` itself will END UP being
  the TAIL of the reversed segment (since reversal flips the
  order), so remember it too — call it `first_in_segment`. Do a
  standard 3-pointer in-place reversal for exactly
  (right - left + 1) nodes. Afterward, reconnect:
  before.next = the new head of the reversed segment (which was
  the OLD tail, i.e. the node that used to be at position right),
  and first_in_segment.next = whatever comes after the segment.

  The journey from brute to optimal:
    Brute thought   →  Extract all values to an array, reverse
                       just the slice [left-1:right], rebuild the
                       list from that array
    Problem with it →  O(n) extra space for the array
    Better question →  "Can the existing nodes be re-linked
                       in place, the same way a full reversal
                       works, just bounded to a segment?"
    Insight         →  The exact same 3-pointer reversal dance
                       works on a sub-range; just remember the
                       boundary nodes (before and
                       first_in_segment) to reconnect afterward
    Optimal         →  One O(n) pass: walk to `before`, reverse
                       (right-left+1) nodes in place, reconnect
                       both ends — O(1) extra space

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🐢 SECTION 5 — APPROACH 1 — BRUTE FORCE (Array Slice Reverse + Rebuild)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    Walk the list once, collecting all values into an array.
    Reverse the slice of that array from index (left-1) to
    (right-1) (0-indexed). Rebuild a fresh linked list from the
    modified array.

  Pseudocode:
    step 1: values = [all node values, in order]
    step 2: values[left-1:right] = reversed(values[left-1:right])
    step 3: build and return a new linked list from values

  Time  : O(n)  →  Why: a constant number of linear scans over
                        the values
  Space : O(n)  →  Why: stores all values in an intermediate
                        array before rebuilding

  ಇದು ಯಾಕೆ ಸಾಕಾಗಲ್ಲ?
    → Correct and O(n) time, but uses O(n) extra space — the
      in-place reversal approach reuses the original nodes
      directly and needs no extra storage for values.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🚀 SECTION 6 — OPTIMAL (In-Place Sublist Reversal with Dummy Node)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    Use a dummy node before head. Walk `before` to the node just
    before position `left` ((left-1) steps from dummy).
    `first_in_segment` = before.next (this will become the
    segment's tail after reversal). Do a standard 3-pointer
    in-place reversal for exactly (right - left + 1) nodes,
    starting from first_in_segment. After reversal, reconnect:
    before.next points to the new head of the reversed segment
    (prev after the loop), and first_in_segment.next points to
    whatever node comes after the segment (curr after the loop).

  Key steps:
    1. dummy = ListNode(0, head)
       before = dummy
       for _ in range(left - 1): before = before.next
    2. first_in_segment = before.next
       prev = None
       curr = first_in_segment
       for _ in range(right - left + 1):
           next_node = curr.next
           curr.next = prev
           prev = curr
           curr = next_node
    3. before.next = prev
       first_in_segment.next = curr
       return dummy.next

  ಕನ್ನಡದಲ್ಲಿ ಒಂದು ಸಲ ಹೇಳಿ:
    → "dummy node ಇಟ್ಟುಕೊಂಡು, left-1 steps ಮುಂದೆ ಹೋಗಿ before
       ಹುಡುಕು. before.next ಅನ್ನ first_in_segment ಅಂತ ನೆನಪಿಟ್ಟುಕೋ
       (ಇದೇ ಮುಂದೆ reversed segment ಅ TAIL ಆಗುತ್ತೆ). ಆಮೇಲೆ
       standard 3-pointer reversal, (right-left+1) nodes ಗೆ
       ಮಾತ್ರ ಮಾಡು. ಕೊನೆಗೆ before.next ಅನ್ನ ಹೊಸ head ಗೆ (prev),
       first_in_segment.next ಅನ್ನ ಮುಂದಿನ ಭಾಗ ಗೆ (curr) ಜೋಡಿಸು!"

  Time  : O(n)  →  Why: a single linear pass — walk to before,
                        then reverse the bounded segment
  Space : O(1)  →  Why: only a dummy node and a handful of
                        pointer variables, no extra storage

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🔍 SECTION 7 — DRY RUN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Input: head = [1,2,3,4,5], left = 2, right = 4

  Step 1 — find before:
    dummy -> 1 -> 2 -> 3 -> 4 -> 5
    before = dummy
    loop runs (left-1)=1 time: before = before.next (= node 1)
    before = node valued 1

  Step 2 — reversal setup + loop:
    first_in_segment = before.next = node valued 2
    prev = None, curr = node valued 2 (count = right-left+1 = 3)

    Iteration 1: next_node=3, 2.next=None, prev=2, curr=3
    Iteration 2: next_node=4, 3.next=2, prev=3, curr=4
    Iteration 3: next_node=5, 4.next=3, prev=4, curr=5

    After loop: prev = node valued 4 (new head of segment)
                curr = node valued 5 (first node AFTER segment)

  Step 3 — reconnect:
    before.next = prev → 1.next = 4
    first_in_segment.next = curr → 2.next = 5

  Chain: 1 -> 4 -> 3 -> 2 -> 5 -> None

  Output: [1,4,3,2,5] ✓ matches expected

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 ⚠️ SECTION 8 — EDGE CASES — ಇವನ್ನ ಮರೆಯಬೇಡ!
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  ✓ left == right (single node)? →  the reversal loop runs
                                      exactly once — reversing a
                                      single node is a no-op,
                                      result unchanged
  ✓ left == 1 (reverse from the
    very start)?                 →  dummy node makes `before`
                                      naturally be dummy itself
                                      — no special case needed
  ✓ right == length (reverse to
    the very end)?                →  curr naturally becomes
                                      None after the loop,
                                      first_in_segment.next = None
                                      correctly terminates the list
  ✓ left == 1 AND right == length
    (reverse the whole list)?     →  handled identically — dummy
                                      absorbs both edge conditions
                                      at once
  ✓ Single-node list, left=right=1?→  same no-op single-node
                                      reversal case, trivially
                                      correct

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📊 SECTION 9 — COMPLEXITY SUMMARY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                              Time    Space
  Brute (array slice reverse)  O(n)    O(n)
  In-place dummy-node reversal  O(n)    O(1)   ← use this ✅

  Time yaake O(n)?  → One pass: (left-1) steps to find before,
                       plus (right-left+1) steps to reverse —
                       together bounded by n
  Space yaake O(1)? → Reuses the existing nodes — only a dummy
                       node and a few pointer variables used

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🎯 SECTION 10 — PATTERN LEARNED — ಇದರಿಂದ ಕಲಿತದ್ದು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Pattern Name: Bounded In-Place Reversal with Dummy Anchoring

  Ee pattern yaavaaga use maadabeeku?
  → Any "reverse only a PORTION of a linked list" problem —
     reuse the same 3-pointer in-place reversal from reversing
     a whole list, but bound the loop to a count, and remember
     the two boundary nodes (before-the-segment and the
     segment's ORIGINAL first node, which becomes its tail) to
     reconnect afterward
  → A dummy node BEFORE head always eliminates the "what if the
     segment starts at the very head" special case

  Idee pattern beere problemsalli kaanisatte:
  → Reverse Linked List #206 (the base 3-pointer reversal
     technique, applied to the WHOLE list instead of a segment)
  → Reverse Nodes in k-Group #25 (repeatedly applies this exact
     bounded-reversal idea to consecutive groups of size k)

  Next time intaha problem bandre naanu modalu idannu think maadtene:
  → "List na ondu PORTION (range) reverse madabekagidre, pooorthi
     list reverse maado 3-pointer trick anne use madu, adhre
     count ge bound madi nillisu. before mathu segment ina
     ORIGINAL first node (adhu TAIL aagutte) nenapittukondu,
     reversal aada mele reconnect madu — dummy node haaki left=1
     special case thappisu!"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🗣️ SECTION 11 — INTERVIEWALLI HEGE EXPLAIN MAADABEEKU
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  1. Understand:
     "Reverse only the nodes from position left to right
      (1-indexed) in a linked list — everything else stays put."

  2. Brute force:
     "Extract all values to an array, reverse the slice
      [left-1:right], rebuild the list. O(n) time, O(n) space."

  3. Optimize:
     "Use a dummy node, walk to the node before position left
      (`before`). Remember the segment's original first node
      (it becomes the tail after reversal). Do a bounded
      3-pointer reversal for exactly (right-left+1) nodes.
      Reconnect before.next to the new segment head, and the
      original first node's next to whatever comes after."

  4. Code:
     "dummy = ListNode(0, head). Walk before left-1 steps.
      first_in_segment = before.next. Standard reversal loop for
      (right-left+1) iterations. before.next = prev;
      first_in_segment.next = curr. Return dummy.next."

  5. Complexity:
     "Time O(n) — one combined pass. Space O(1) — dummy node
      plus a few pointers, no extra storage."

  Mukhya: reversing a SEGMENT is just a bounded version of
          reversing the WHOLE list — the exact same 3-pointer
          dance, plus remembering the two boundary nodes to
          reconnect afterward, with a dummy node to dodge the
          'segment starts at head' special case!
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
# BRUTE FORCE — O(n) Time | O(n) Space (array slice reverse + rebuild)
# ═══════════════════════════════════════════════════════════════════
def reverse_between_brute(head, left, right):
    """
    Idu modala aaloochane — values array ge haaki, [left-1,right)
    slice reverse madi, hosa list build madu
    """
    values = to_list(head)
    values[left - 1:right] = reversed(values[left - 1:right])
    return build(values)


# ═══════════════════════════════════════════════════════════════════
# OPTIMAL — O(n) Time | O(1) Space (in-place dummy-node reversal)
# ═══════════════════════════════════════════════════════════════════
def reverse_between(head, left, right):
    """
    Idu final answer — dummy node ittukondu before hudu, bounded
    3-pointer reversal madi, kodage reconnect madu
    """
    dummy = ListNode(0, head)
    before = dummy
    for _ in range(left - 1):
        before = before.next

    first_in_segment = before.next
    prev = None
    curr = first_in_segment
    for _ in range(right - left + 1):
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node

    before.next = prev
    first_in_segment.next = curr

    return dummy.next


# ═══════════════════════════════════════════════════════════════════
# TEST CASES
# ═══════════════════════════════════════════════════════════════════
if __name__ == "__main__":
    # Test 1 — Basic (LeetCode example 1)
    head = build([1, 2, 3, 4, 5])
    assert to_list(reverse_between(head, 2, 4)) == [1, 4, 3, 2, 5]

    # Test 2 — Single node (LeetCode example 2)
    head = build([5])
    assert to_list(reverse_between(head, 1, 1)) == [5]

    # Test 3 — Reverse from the very start
    head = build([1, 2, 3, 4, 5])
    assert to_list(reverse_between(head, 1, 3)) == [3, 2, 1, 4, 5]

    # Test 4 — Reverse to the very end
    head = build([1, 2, 3, 4, 5])
    assert to_list(reverse_between(head, 3, 5)) == [1, 2, 5, 4, 3]

    # Test 5 — Reverse the whole list
    head = build([1, 2, 3, 4, 5])
    assert to_list(reverse_between(head, 1, 5)) == [5, 4, 3, 2, 1]

    # Test 6 — left == right in the middle (no-op)
    head = build([1, 2, 3, 4, 5])
    assert to_list(reverse_between(head, 3, 3)) == [1, 2, 3, 4, 5]

    # Test 7 — Two nodes, reverse both
    head = build([1, 2])
    assert to_list(reverse_between(head, 1, 2)) == [2, 1]

    # Cross-check: brute force must agree on all of the above
    head = build([1, 2, 3, 4, 5])
    assert to_list(reverse_between_brute(head, 2, 4)) == [1, 4, 3, 2, 5]

    head = build([5])
    assert to_list(reverse_between_brute(head, 1, 1)) == [5]

    head = build([1, 2, 3, 4, 5])
    assert to_list(reverse_between_brute(head, 1, 3)) == [3, 2, 1, 4, 5]

    head = build([1, 2, 3, 4, 5])
    assert to_list(reverse_between_brute(head, 3, 5)) == [1, 2, 5, 4, 3]

    head = build([1, 2, 3, 4, 5])
    assert to_list(reverse_between_brute(head, 1, 5)) == [5, 4, 3, 2, 1]

    head = build([1, 2, 3, 4, 5])
    assert to_list(reverse_between_brute(head, 3, 3)) == [1, 2, 3, 4, 5]

    head = build([1, 2])
    assert to_list(reverse_between_brute(head, 1, 2)) == [2, 1]

    print("All tests passed!")
