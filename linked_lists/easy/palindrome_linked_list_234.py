"""
╔══════════════════════════════════════════════════════════════════╗
║  PALINDROME LINKED LIST                                          ║
║  LeetCode #234  |  Difficulty: Easy  |  Topic: Linked Lists     ║
║  Link: https://leetcode.com/problems/palindrome-linked-list/    ║
╚══════════════════════════════════════════════════════════════════╝

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📘 SECTION 1 — PROBLEM UNDERSTANDING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Given the head of a singly linked list, return True if it is
  a palindrome, False otherwise.
  Must solve in O(n) time and O(1) space.

  Input : head = first node of linked list
  Output: True if palindrome, False otherwise

  Example 1 — basic:
    Input : 1 → 2 → 2 → 1
    Output: True
    Why?  : Reads same forwards and backwards

  Example 2 — slightly tricky (not palindrome):
    Input : 1 → 2
    Output: False
    Why?  : 1→2 forwards, 2→1 backwards — different

  Constraints:
    - 1 <= number of nodes <= 10^5
    - 0 <= Node.val <= 9
    - O(n) time and O(1) extra space required

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🧠 SECTION 2 — KANGLISH THINKING — ಹೇಗೆ ಯೋಚಿಸಬೇಕು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  Problem odi aada mele namma brain enu think maadabeeku:

  ಹಂತ 1 — Problem ಅರ್ಥ ಮಾಡಿಕೊಳ್ಳಿ
  ┌─────────────────────────────────────────────────────────┐
  │  Input ಏನು ಕೊಡ್ತಾರೆ?  →  linked list head             │
  │  Output ಏನು ಬೇಕು?     →  palindrome True/False        │
  │  Constraints ಏನಿದೆ?   →  O(n) time, O(1) space must!  │
  └─────────────────────────────────────────────────────────┘

  ಹಂತ 2 — ನನಗೆ ಗೊತ್ತಿರೋ simple way ಏನು?
  →  All values array ಲ್ಲಿ collect ಮಾಡಿ two pointer
     palindrome check ಮಾಡೋಣ → O(n) time O(n) space
  →  ಆದರೆ ಇದು slow ಯಾಕೆ?
     O(1) space beeku — array use ಮಾಡಲ್ಲ!

  ಹಂತ 3 — Better way ಹೇಗೆ ಯೋಚಿಸುವುದು?
  →  "Palindrome = first half == reverse of second half"
  →  Step 1: slow/fast pointers → find middle
  →  Step 2: reverse second half in-place
  →  Step 3: compare first half with reversed second half
  →  Step 4: (optional) restore original list
  →  ಇದರಿಂದ ನಾವು Slow/Fast + Reverse use ಮಾಡಬಹuದು!

  ಹಂತ 4 — Technique ಯಾಕೆ ಇಲ್ಲಿ ಕೆಲಸ ಮಾಡುತ್ತೆ?
  →  slow/fast = middle find ಮಾಡಲು (already know from LC #876)
  →  Reverse second half = LC #206 already solved!
  →  Compare two halves = simple traversal
  →  3 problems combined into 1 elegant solution!

  💡 Interview ನಲ್ಲಿ ಹೇಗೆ ಮಾತಾಡಬೇಕು:
  →  "Combine slow/fast pointer + reverse linked list"
  →  "Find middle, reverse second half, compare both halves"
  →  "O(n) time, O(1) space — no extra array needed"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🏷️ SECTION 3 — TECHNIQUE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Primary   : Slow/Fast Pointer + In-place Reverse + Compare
  Secondary : Array collection (brute force, O(n) space)

  WHY this combination?
  → slow/fast → finds middle in O(n), O(1) space
  → reverse second half → O(n), O(1) space
  → compare two halves → O(n), O(1) space
  → Total: O(n) time, O(1) space — perfect!

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 💡 SECTION 4 — INTUITION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  A palindrome reads the same forwards and backwards.
  For a linked list: first half should equal the reverse of second half.

  Since we can't go backwards in a singly linked list,
  we REVERSE the second half and then compare!

  Four steps:
  1. Find middle using slow/fast pointers
  2. Reverse from middle to end
  3. Compare first half with reversed second half
  4. (Restore list if needed — good practice)

  The journey from brute to optimal:
    Brute thought   →  Collect values in array, two pointer check
    Problem with it →  O(n) extra space — not allowed
    Better question →  "Can I check palindrome without extra array?"
    Insight         →  Reverse second half in-place!
                       Then compare first and reversed second half
    Optimal         →  Find mid + reverse + compare → O(n), O(1)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🐢 SECTION 5 — APPROACH 1 — BRUTE FORCE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    Collect all node values into a list.
    Check if the list is a palindrome using two pointers.

  Pseudocode:
    step 1: vals = [node.val for each node]
    step 2: left=0, right=len-1
    step 3: while left < right:
              if vals[left] != vals[right]: return False
              left++, right--
    step 4: return True

  Time  : O(n)  →  Why: one pass to collect + one pass to check
  Space : O(n)  →  Why: vals array stores all values

  ಇದು ಯಾಕೆ ಸಾಕಾಗಲ್ಲ?
    → O(1) space beeku — O(n) space allowed alla!

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🚀 SECTION 6 — APPROACH 2 — OPTIMAL
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    Find middle → reverse second half → compare → restore.

  Key steps:
    1. Find middle using slow/fast:
       slow moves 1 step, fast moves 2 steps
       when fast reaches end, slow is at middle

    2. Reverse from slow.next to end
       (second half starts at slow.next)

    3. Compare p1 (from head) and p2 (from reversed second half)
       while p2 exists: if values differ → not palindrome

    4. Return result

  ಕನ್ನಡದಲ್ಲಿ ಒಂದು ಸಲ ಹೇಳಿ:
    → "slow/fast ಮೂಲಕ middle find maadu.
       slow.next ಇಂದ end ತನಕ reverse maadu.
       head ಇಂದ ಮತ್ತು reversed half ಇಂದ simultaneously
       compare maadu. Values differ iddre False, else True!"

  Time  : O(n)  →  Why: find mid O(n) + reverse O(n) + compare O(n)
  Space : O(1)  →  Why: only slow, fast, prev, curr pointers

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🔍 SECTION 7 — DRY RUN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Input: 1 → 2 → 2 → 1

  Step 1 — Find middle:
    slow=1, fast=1
    slow=2, fast=2(next=2, skip to 1... wait fast moves 2)
    Actually: slow=1→2, fast=1→2→1... let me retrace
    
    Start: slow=node(1), fast=node(1)
    iter1: slow=node(2), fast=node(2)  [fast.next.next=node(2)]
    iter2: fast.next=node(1), fast.next.next=None → stop
           slow=node(2) [the second 2]
    Middle = slow = second node(2)

  Step 2 — Reverse from slow.next:
    Reverse [1] → still [1]
    second_head = node(1) [last node]

  Step 3 — Compare:
    p1=node(1)[first], p2=node(1)[last]
    1 == 1 ✓ → p1=node(2)[second], p2=None → stop
    All match → return True ✓

  ಇನ್ನೊಂದು — odd length:
  Input: 1 → 2 → 3 → 2 → 1

  Find middle: slow=node(3) [exact middle]
  Reverse slow.next=[2→1]: reversed=[1→2]
  Compare: p1=1, p2=1 ✓ → p1=2, p2=2 ✓ → p2=None → True ✓

  Not palindrome:
  Input: 1 → 2
  Find middle: slow=node(1) [first node, fast reaches end faster]
  Reverse slow.next=[2]: second_head=node(2)
  Compare: p1=1, p2=2 → 1≠2 → return False ✓

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 ⚠️ SECTION 8 — EDGE CASES — ಇವನ್ನ ಮರೆಯಬೇಡ!
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  ✓ Single node?        →  Always palindrome → True
  ✓ Two nodes same?     →  1→1 → True
  ✓ Two nodes diff?     →  1→2 → False
  ✓ Odd length?         →  Middle node is ignored in comparison
  ✓ Even length?        →  Both halves compared fully
  ✓ All same values?    →  Always True

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📊 SECTION 9 — COMPLEXITY SUMMARY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                  Time    Space
  Brute Force     O(n)    O(n)
  Optimal         O(n)    O(1)   ← use this ✅

  Time yaake O(n)?
    → Find mid O(n) + reverse O(n) + compare O(n) = O(n)
  Space yaake O(1)?
    → Only slow, fast, prev, curr, p1, p2 — all pointers!

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🎯 SECTION 10 — PATTERN LEARNED — ಇದರಿಂದ ಕಲಿತದ್ದು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Pattern Name: Find Middle + Reverse Half + Compare

  This problem combines 3 patterns you already know:
  ┌─────────────────────────────────────────────────────┐
  │  slow/fast pointer  → find middle (#876)            │
  │  three pointer      → reverse list (#206)           │
  │  two pointer        → compare two halves            │
  └─────────────────────────────────────────────────────┘

  Idee pattern beere problemsalli kaanisatte:
  → Reorder List #143 (find mid + reverse + merge)
  → Maximum Twin Sum #2130 (find mid + reverse + sum)
  → Sort List #148 (find mid + merge sort)

  Next time intaha problem bandre naanu modalu idannu think maadtene:
  → "Linked list palindrome O(1) space?
     → slow/fast middle find maadu. Second half reverse maadu.
     Both halves compare maadu. 3 patterns combined!"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🗣️ SECTION 11 — INTERVIEWALLI HEGE EXPLAIN MAADABEEKU
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  1. Understand:
     "Check if linked list is palindrome in O(n) time O(1) space."

  2. Brute force:
     "Collect values in array, two pointer check. O(n) space."

  3. Optimize:
     "Three steps: find middle with slow/fast pointers,
      reverse second half in-place (reuse LC #206 logic),
      compare first half with reversed second half."

  4. Code:
     "slow/fast to find mid. Reverse from slow.next.
      p1=head, p2=second_head. Compare while p2 exists."

  5. Complexity:
     "Time O(n) — three linear passes. Space O(1) — only pointers."

  Mukhya: summane kuutu code bareyabeda!
          "3 problems combined" — show pattern recognition!
          Mention restoring the list — shows clean coding habits!
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
# BRUTE FORCE — O(n) Time | O(n) Space
# ═══════════════════════════════════════════════════════════════════
def is_palindrome_brute(head):
    """Idu modala aaloochane — collect values, two pointer check"""
    vals = []
    curr = head
    while curr:
        vals.append(curr.val)
        curr = curr.next

    left, right = 0, len(vals) - 1
    while left < right:
        if vals[left] != vals[right]:
            return False
        left  += 1
        right -= 1
    return True


# ─── Helper: reverse a linked list ────────────────────────────────
def reverse(head):
    """Three pointer reversal — LC #206 pattern"""
    prev = None
    curr = head
    while curr:
        next_node  = curr.next
        curr.next  = prev
        prev       = curr
        curr       = next_node
    return prev


# ═══════════════════════════════════════════════════════════════════
# OPTIMAL — O(n) Time | O(1) Space
# ═══════════════════════════════════════════════════════════════════
def is_palindrome(head):
    """
    Idu final answer — find middle + reverse second half + compare
    Combines: slow/fast (#876) + reverse (#206) + two pointer
    """
    if not head or not head.next:
        return True              # single node always palindrome

    # STEP 1: Find middle using slow/fast pointers
    slow = head
    fast = head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    # slow is now at middle (for even: left-middle, odd: exact middle)

    # STEP 2: Reverse second half (from slow.next to end)
    second_head = reverse(slow.next)
    slow.next   = None           # cut the list in half (optional but clean)

    # STEP 3: Compare first half and reversed second half
    p1     = head
    p2     = second_head
    result = True

    while p2:                    # second half may be shorter (odd length)
        if p1.val != p2.val:
            result = False
            break
        p1 = p1.next
        p2 = p2.next

    # STEP 4: Restore the list (good practice in interviews!)
    slow.next = reverse(second_head)

    return result


# ═══════════════════════════════════════════════════════════════════
# TEST CASES
# ═══════════════════════════════════════════════════════════════════
if __name__ == "__main__":
    # Test 1 — Even palindrome
    assert is_palindrome(build([1, 2, 2, 1])) == True

    # Test 2 — Not palindrome
    assert is_palindrome(build([1, 2])) == False

    # Test 3 — Odd palindrome
    assert is_palindrome(build([1, 2, 3, 2, 1])) == True

    # Test 4 — Odd not palindrome
    assert is_palindrome(build([1, 2, 3, 4, 1])) == False

    # Test 5 — Single node
    assert is_palindrome(build([1])) == True

    # Test 6 — Two same nodes
    assert is_palindrome(build([1, 1])) == True

    # Test 7 — All same values
    assert is_palindrome(build([5, 5, 5, 5, 5])) == True

    # Test 8 — Brute force check
    assert is_palindrome_brute(build([1, 2, 2, 1])) == True
    assert is_palindrome_brute(build([1, 2]))        == False

    print("All tests passed!")
