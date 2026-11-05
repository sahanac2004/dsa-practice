"""
╔══════════════════════════════════════════════════════════════════╗
║  ADD 1 TO A NUMBER REPRESENTED AS A LINKED LIST                   ║
║  GFG  |  Difficulty: Medium  |  Topic: Linked Lists             ║
║  Link: https://www.geeksforgeeks.org/problems/                  ║
║        add-1-to-a-number-represented-as-linked-list/1           ║
╚══════════════════════════════════════════════════════════════════╝

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📘 SECTION 1 — PROBLEM UNDERSTANDING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  A non-negative number is represented as a singly linked list,
  where the HEAD holds the MOST significant digit and the TAIL
  holds the LEAST significant digit (i.e. the list reads left
  to right exactly like the number is written). Add 1 to this
  number and return the head of the resulting linked list.

  Input : head = linked list, each node a single digit (0-9),
          head = most significant digit
  Output: head of the linked list representing (number + 1)

  Example 1 — basic, no carry propagation:
    Input : head = [1,2,3]  (represents 123)
    Output: [1,2,4]  (124)

  Example 2 — carry propagates through the whole number:
    Input : head = [9,9,9]  (represents 999)
    Output: [1,0,0,0]  (1000 — note the list GROWS by one digit)

  Example 3 — single digit:
    Input : head = [9]
    Output: [1,0]

  Constraints:
    - 1 <= number of nodes <= 10^5
    - 0 <= Node.val <= 9
    - The number has no leading zeros (except the number 0
      itself, as a single node)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🧠 SECTION 2 — KANGLISH THINKING — ಹೇಗೆ ಯೋಚಿಸಬೇಕು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  Problem odi aada mele namma brain enu think maadabeeku:

  ಹಂತ 1 — Problem ಅರ್ಥ ಮಾಡಿಕೊಳ್ಳಿ
  ┌─────────────────────────────────────────────────────────┐
  │  Input ಏನು ಕೊಡ್ತಾರೆ?  →  number ಅನ್ನ digit-by-digit list  │
  │                           (head = most significant digit) │
  │  Output ಏನು ಬೇಕು?     →  (number + 1) ಅನ್ನ ಅದೇ format ಲ್ಲಿ│
  │  Constraints ಏನಿದೆ?   →  carry "999 + 1 = 1000" ತರ ಪೂರ್ತಿ │
  │                           ಪ್ರಸಾರ ಆಗ್ಬಹುದು, list ಬೆಳೀಬಹುದು │
  └─────────────────────────────────────────────────────────┘

  ಹಂತ 2 — ಯಾಕೆ ಇದು tricky? "+1 ಅನ್ನ LAST digit ಗೆ ಮಾತ್ರ ಮಾಡ್ಬೇಕು,
           ಆದ್ರೆ ಪ್ರಾಬ್ಲಮ್ ಕೊಟ್ಟಿರೋ list head = MOST significant
           digit!" ಅಂತ ಯೋಚಿಸಿ
  →  ಸಾಧಾರಣ addition ಅಂದ್ರೆ LEAST significant digit (ಅಂದ್ರೆ
     LIST ಅ ಕೊನೆ) ಇಂದ ಪ್ರಾರಂಭ ಆಗ್ಬೇಕು — ಆದ್ರೆ singly linked
     list ಲ್ಲಿ ಹಿಂದಿಂದ ಮುಂದೆ ನೇರವಾಗಿ ಹೋಗೋಕೆ ಆಗಲ್ಲ

  ಹಂತ 3 — ಮೊದಲ simple idea (brute force) ಏನು?
  →  "list ಅನ್ನ REVERSE ಮಾಡಿ (ಈಗ head = least significant digit),
      +1 ಮತ್ತು carry ಅನ್ನ ಸುಲಭ ಆಗಿ ಮುಂದಿಂದ ಹಿಂದಕ್ಕೆ propagate
      ಮಾಡಿ, ಕೊನೆಗೆ ಮತ್ತೆ REVERSE ಮಾಡಿ ಮೂಲ order ಗೆ ಮರಳಿಸಿದ್ರೆ?"
  →  ಕೆಲಸ ಆಗುತ್ತೆ! O(n) time, O(1) extra space — ಆದ್ರೆ list ಅನ್ನ
     ಎರಡು ಸಲ reverse ಮಾಡ್ಬೇಕು (ಹಿಂದೆ, ಮುಂದೆ)

  ಹಂತ 4 — Optimal idea (recursion, ಒಂದೇ pass) ಹೇಗೆ ಬರುತ್ತೆ?
  →  "recursion ಬಳಸಿದ್ರೆ, ಕೊನೆ node ಗೆ ಮೊದಲು ಹೋಗಿ, ಅಲ್ಲಿಂದ
      ಹಿಂದೆ ಬರ್ತಾ +1 ಮತ್ತು carry propagate ಮಾಡಿದ್ರೆ?" ಅಂತ
      ಯೋಚಿಸಿ — call stack ಅನ್ನೇ "implicit reversal" ಆಗಿ
      ಬಳಸ್ಬಹುದು! recursion ಕೊನೆ node ತಲುಪಿದ ಮೇಲೆ +1 ಮಾಡಿ carry
      ಅನ್ನ return ಮಾಡುತ್ತೆ, ಪ್ರತಿ level ಆ carry ಅನ್ನ ಅದರ digit
      ಗೆ add ಮಾಡಿ ಮುಂದಿನ carry ಅನ್ನ return ಮಾಡುತ್ತೆ

  ಹಂತ 5 — Technique ಯಾಕೆ ಇಲ್ಲಿ ಕೆಲಸ ಮಾಡುತ್ತೆ?
  →  Recursion call stack unwind ಆಗೋವಾಗ, ಅದು ಸ್ವಾಭಾವಿಕವಾಗೇ
     list ಅನ್ನ "ಕೊನೆ ಇಂದ ಮೊದಲಿಗೆ" visit ಮಾಡುತ್ತೆ — ಇದೇ ಬೇಕಾಗಿರೋ
     "least significant digit ಇಂದ most significant ಗೆ" ಕ್ರಮ!
     list ಅನ್ನ ಫಿಸಿಕಲ್ ಆಗಿ reverse ಮಾಡೋ ಅಗತ್ಯ ಇಲ್ಲ

  💡 Interview ನಲ್ಲಿ ಹೇಗೆ ಮಾತಾಡಬೇಕು:
  →  "First approach: reverse the list, add 1 with carry
      propagation left-to-right (now least-significant-first),
      reverse back. O(n) time, O(1) space, but two reversals."
  →  "Optimal: recurse to the end of the list, then add 1 and
      propagate the carry back up through the return values —
      the call stack naturally processes digits least-
      significant-first without ever physically reversing the
      list."

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🏷️ SECTION 3 — TECHNIQUE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Primary   : Recursive Carry Propagation (implicit reversal via
              call stack)
  Secondary : Reverse → Add With Carry → Reverse Back

  WHY Recursion over Double-Reversal?
  → The double-reversal approach is correct and O(1) extra
    space, but physically mutates the list TWICE just to access
    it in the right order. Recursion achieves the same "process
    least-significant-first" order for free — the call stack
    IS the reversal, since it naturally unwinds from the last
    node backward to the first — without ever touching a single
    `next` pointer for reversal purposes.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 💡 SECTION 4 — INTUITION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  The key insight: adding 1 to a number is fundamentally a
  right-to-left (least-significant-first) operation, but the
  list is given left-to-right (most-significant-first). Instead
  of physically reversing the list to fix the direction,
  recursion can visit the nodes in reverse order "for free":
  recurse all the way to the last node first, THEN do work as
  each recursive call returns. Each call adds the incoming carry
  to its own digit, updates that digit, and returns the new
  carry (0 or 1) to its caller — exactly mimicking right-to-left
  addition, driven by the stack unwinding instead of reversed
  pointers.

  The journey from brute to optimal:
    Brute thought   →  Reverse the list so it reads least-
                       significant-first, add 1 with ordinary
                       carry propagation, reverse back to restore
                       the original digit order
    Problem with it →  Two full list reversals — more pointer
                       manipulation than strictly necessary
    Better question →  "Can I process digits right-to-left
                       WITHOUT physically reversing the list?"
    Insight         →  Recursion's call stack naturally unwinds
                       last-to-first — use that instead of
                       reversing
    Optimal         →  One recursive traversal: recurse to the
                       end, add 1 there, propagate carry back up
                       through return values; if a carry survives
                       past the head, prepend a new node

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🐢 SECTION 5 — APPROACH 1 — BRUTE FORCE (Reverse, Add, Reverse Back)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    Reverse the list in place (now head = least significant
    digit). Walk it once, adding 1 (as a starting carry) to each
    digit, propagating any resulting carry to the next node. If
    a carry remains after the last node, append a new node
    valued 1. Reverse the list back to restore the original
    (most-significant-first) order.

  Pseudocode:
    step 1: head = reverse(head)
    step 2: carry = 1; curr = head; prev = None
    step 3: while curr:
    step 4:   total = curr.val + carry
    step 5:   curr.val = total % 10
    step 6:   carry = total // 10
    step 7:   prev = curr; curr = curr.next
    step 8: if carry: prev.next = ListNode(carry)
    step 9: return reverse(head)

  Time  : O(n)  →  Why: two reversals plus one addition pass,
                        all linear
  Space : O(1)  →  Why: only in-place pointer rewiring for both
                        reversals and the addition pass

  ಇದು ಯಾಕೆ ಸಾಕಾಗಲ್ಲ?
    → Correct and O(n) time with O(1) space, but it's doing
      TWICE the pointer-rewiring work of the recursive approach
      — the recursive version achieves the same result in a
      single traversal (implicitly, via the call stack).

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🚀 SECTION 6 — OPTIMAL (Recursive Carry Propagation)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    Recurse to the end of the list first. At the last node, add
    1 directly (base case). As each recursive call returns, it
    receives the carry from the node after it, adds that carry
    to its own digit, updates the digit in place, and returns
    whatever NEW carry resulted. If the carry survives all the
    way back past the head (e.g. 999 -> 1000), prepend a brand
    new node valued 1.

  Key steps:
    1. def add_one_helper(node):
           if node.next is None:
               node.val += 1
           else:
               carry = add_one_helper(node.next)
               node.val += carry
           if node.val == 10:
               node.val = 0
               return 1
           return 0
    2. carry = add_one_helper(head)
    3. if carry:
           new_head = ListNode(1, head)
           return new_head
       return head

  ಕನ್ನಡದಲ್ಲಿ ಒಂದು ಸಲ ಹೇಳಿ:
    → "recursion ಬಳಸಿ list ಕೊನೆ node ತನಕ ಹೋಗು. ಕೊನೆ node ಗೆ
       ನೇರವಾಗಿ +1 ಮಾಡು. ಹಿಂದೆ ಬರ್ತಾ, ಪ್ರತಿ node ಗೆ ಮುಂದಿನ node
       ಇಂದ ಬಂದ carry ಅನ್ನ add ಮಾಡಿ, digit ಅನ್ನ update ಮಾಡಿ,
       10 ಆಗಿದ್ರೆ 0 ಗೆ reset ಮಾಡಿ carry=1 return ಮಾಡು. ಕೊನೆಗೆ
       head ಗೂ carry ಉಳಿದ್ರೆ, ಹೊಸ node (val=1) ಅನ್ನ ಮುಂದೆ
       ಸೇರಿಸು!"

  Time  : O(n)  →  Why: a single recursive traversal — each
                        node is visited exactly once going down
                        and once coming back up
  Space : O(n)  →  Why: the recursion call stack holds one frame
                        per node (this trades O(1) pointer-space
                        for O(n) call-stack space)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🔍 SECTION 7 — DRY RUN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Input: head = [9,9,9] (represents 999)

  Recursive descent (going down):
    add_one_helper(node=9) -> calls add_one_helper(node=9)
      -> calls add_one_helper(node=9) [last node, base case]

  Base case (last node, val=9):
    node.next is None -> node.val += 1 -> node.val = 10
    node.val == 10 -> reset to 0, return carry = 1

  Unwind level 2 (middle node, val=9):
    carry received = 1
    node.val += 1 -> node.val = 10
    node.val == 10 -> reset to 0, return carry = 1

  Unwind level 1 (head node, val=9):
    carry received = 1
    node.val += 1 -> node.val = 10
    node.val == 10 -> reset to 0, return carry = 1

  Back at top level:
    carry = 1 (survived past head)
    new_head = ListNode(1, head)

  List is now: 1 -> 0 -> 0 -> 0

  Output: [1,0,0,0] ✓ matches expected (999 + 1 = 1000)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 ⚠️ SECTION 8 — EDGE CASES — ಇವನ್ನ ಮರೆಯಬೇಡ!
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  ✓ Single node, value 9?         →  base case fires
                                      immediately: 9+1=10, reset
                                      to 0, carry=1 survives to
                                      top -> prepend new node 1
                                      -> [1,0]
  ✓ No carry propagation needed
    (e.g. [1,2,3] -> [1,2,4])?    →  only the base case node
                                      changes; every other level
                                      receives carry=0 and does
                                      nothing extra
  ✓ All-9s number (max carry
    propagation, e.g. [9,9,9])?   →  carry propagates through
                                      EVERY level, survives past
                                      head, list GROWS by one node
  ✓ Number is just 0?             →  single node val=0 -> 0+1=1,
                                      no carry, result is [1]
  ✓ Very long list (10^5 nodes,
    max constraint)?              →  recursion depth would equal
                                      list length — acceptable
                                      here, but worth knowing the
                                      brute-force (reverse-based)
                                      alternative avoids deep
                                      recursion if that's a
                                      concern in a stricter runtime

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📊 SECTION 9 — COMPLEXITY SUMMARY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                                Time    Space
  Brute (reverse-add-reverse)    O(n)    O(1)
  Recursive carry propagation     O(n)    O(n)   ← use this ✅
                                                  (simplest to
                                                   reason about)

  Time yaake O(n)?  → Each node is visited once going down the
                       recursion and once coming back up
  Space yaake O(n)? → The call stack holds one frame per node —
                       this is the tradeoff for avoiding physical
                       list reversal

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🎯 SECTION 10 — PATTERN LEARNED — ಇದರಿಂದ ಕಲಿತದ್ದು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Pattern Name: Recursion as Implicit Reversal (Carry Propagation)

  Ee pattern yaavaaga use maadabeeku?
  → Any problem where a singly linked list needs to be processed
     in REVERSE order (right-to-left, least-significant-first,
     tail-to-head) but physically reversing it feels wasteful —
     recursion's call-stack unwind naturally provides that
     reversed visiting order
  → Classic use case: digit-by-digit arithmetic (add 1, add two
     numbers stored in reverse-unfriendly order) where carries
     must flow from the last digit backward

  Idee pattern beere problemsalli kaanisatte:
  → Add Two Numbers #2 (contrast — there the list is ALREADY
     least-significant-first, so no reversal/recursion trick is
     needed; carries flow naturally forward)
  → Reverse Linked List #206 (the explicit-reversal alternative
     to this problem's implicit, recursion-based one)

  Next time intaha problem bandre naanu modalu idannu think maadtene:
  → "List na REVERSE order alli process madabekagidre (carry,
     right-to-left arithmetic, etc.) — physically reverse maado
     bedi, recursion use madu! call stack unwind aagovaaga
     automatic aagi last-to-first order sigutte, carry return
     value alli propagate madabahudu."

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🗣️ SECTION 11 — INTERVIEWALLI HEGE EXPLAIN MAADABEEKU
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  1. Understand:
     "The list reads most-significant-digit-first. Add 1 to the
      represented number and return the updated list, growing it
      by one node if the carry survives past the head (e.g.
      999 -> 1000)."

  2. Brute force:
     "Reverse the list so addition can proceed naturally
      left-to-right (now least-significant-first), add 1 with
      carry propagation, reverse back. O(n) time, O(1) space,
      but two full reversals."

  3. Optimize:
     "Use recursion to reach the last node first, add 1 there,
      then let the carry propagate back up through each
      function's return value as the stack unwinds — no
      physical reversal needed."

  4. Code:
     "Recursive helper: base case at node.next is None, add 1
      directly. Otherwise, recurse first, add the returned carry
      to this node's value. If value hits 10, reset to 0 and
      return carry 1; else return 0. At the top level, if a
      carry remains, prepend a new node valued 1."

  5. Complexity:
     "Time O(n) — one down-and-up recursive pass. Space O(n) for
      the call stack (versus O(1) for the reverse-based
      alternative)."

  Mukhya: whenever a singly linked list needs right-to-left
          processing but was given left-to-right, recursion's
          call stack can act as a FREE implicit reversal — no
          need to touch a single `next` pointer for that purpose!
"""


# ─── Linked List Node Definition ──────────────────────────────────
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# ─── Helper: build a linked list from a Python list of digits ────
def build(digits):
    head = None
    tail = None
    for d in digits:
        node = ListNode(d)
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


# ─── Helper: reverse a linked list in place (used by brute force) ─
def _reverse(head):
    prev = None
    curr = head
    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    return prev


# ═══════════════════════════════════════════════════════════════════
# BRUTE FORCE — O(n) Time | O(1) Space (reverse, add, reverse back)
# ═══════════════════════════════════════════════════════════════════
def add_one_brute(head):
    """
    Idu modala aaloochane — list reverse madi (least significant
    first aagi), +1 add madi carry propagate madi, mathe reverse
    madi mulaka order ge hyandiru
    """
    head = _reverse(head)

    carry = 1
    curr = head
    prev = None
    while curr:
        total = curr.val + carry
        curr.val = total % 10
        carry = total // 10
        prev = curr
        curr = curr.next

    if carry:
        prev.next = ListNode(carry)

    return _reverse(head)


# ═══════════════════════════════════════════════════════════════════
# OPTIMAL — O(n) Time | O(n) Space (recursive carry propagation)
# ═══════════════════════════════════════════════════════════════════
def _add_one_helper(node):
    if node.next is None:
        node.val += 1
    else:
        carry = _add_one_helper(node.next)
        node.val += carry

    if node.val == 10:
        node.val = 0
        return 1
    return 0


def add_one(head):
    """
    Idu final answer — recursion bhalasi last node tanaka hogi,
    carry propagate madtha hindhe bandu, head ge carry ulidre
    hosa node prepend madu
    """
    carry = _add_one_helper(head)

    if carry:
        return ListNode(1, head)

    return head


# ═══════════════════════════════════════════════════════════════════
# TEST CASES
# ═══════════════════════════════════════════════════════════════════
if __name__ == "__main__":
    # Test 1 — Basic, no carry propagation
    head = build([1, 2, 3])
    assert to_list(add_one(head)) == [1, 2, 4]

    # Test 2 — Carry propagates through the whole number, list grows
    head = build([9, 9, 9])
    assert to_list(add_one(head)) == [1, 0, 0, 0]

    # Test 3 — Single digit, carry propagates and grows
    head = build([9])
    assert to_list(add_one(head)) == [1, 0]

    # Test 4 — Number is zero
    head = build([0])
    assert to_list(add_one(head)) == [1]

    # Test 5 — Partial carry propagation
    head = build([1, 9, 9])
    assert to_list(add_one(head)) == [2, 0, 0]

    # Test 6 — Single digit, no carry
    head = build([5])
    assert to_list(add_one(head)) == [6]

    # Test 7 — Larger number, carry stops partway
    head = build([4, 3, 2, 1])
    assert to_list(add_one(head)) == [4, 3, 2, 2]

    # Cross-check: brute force must agree on all of the above
    head = build([1, 2, 3])
    assert to_list(add_one_brute(head)) == [1, 2, 4]

    head = build([9, 9, 9])
    assert to_list(add_one_brute(head)) == [1, 0, 0, 0]

    head = build([9])
    assert to_list(add_one_brute(head)) == [1, 0]

    head = build([0])
    assert to_list(add_one_brute(head)) == [1]

    head = build([1, 9, 9])
    assert to_list(add_one_brute(head)) == [2, 0, 0]

    head = build([5])
    assert to_list(add_one_brute(head)) == [6]

    head = build([4, 3, 2, 1])
    assert to_list(add_one_brute(head)) == [4, 3, 2, 2]

    print("All tests passed!")
