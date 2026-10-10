"""
╔══════════════════════════════════════════════════════════════════╗
║  REMOVE LINKED LIST ELEMENTS                                     ║
║  LeetCode #203  |  Difficulty: Easy  |  Topic: Linked Lists     ║
║  Link: https://leetcode.com/problems/remove-linked-list-elements/║
╚══════════════════════════════════════════════════════════════════╝

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📘 SECTION 1 — PROBLEM UNDERSTANDING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Given the head of a linked list and an integer `val`, remove
  ALL nodes whose value equals `val`, and return the new head.

  Input : head = first node of linked list, val = target value
  Output: head of the list with all matching nodes removed

  Example 1 — basic:
    Input : 1 → 2 → 6 → 3 → 4 → 5 → 6 → None, val = 6
    Output: 1 → 2 → 3 → 4 → 5 → None
    Why?  : both nodes with value 6 (middle and end) are removed

  Example 2 — slightly tricky (matches at the head):
    Input : 7 → 7 → 7 → 7 → None, val = 7
    Output: None
    Why?  : every node matches, including the original head —
            the new head must itself be updated correctly

  Example 3 — empty list:
    Input : None, val = 1
    Output: None
    Why?  : nothing to remove from an empty list

  Constraints:
    - 0 <= number of nodes <= 10^4
    - 1 <= Node.val <= 50
    - 0 <= val <= 50

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🧠 SECTION 2 — KANGLISH THINKING — ಹೇಗೆ ಯೋಚಿಸಬೇಕು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  Problem odi aada mele namma brain enu think maadabeeku:

  ಹಂತ 1 — Problem ಅರ್ಥ ಮಾಡಿಕೊಳ್ಳಿ
  ┌─────────────────────────────────────────────────────────┐
  │  Input ಏನು ಕೊಡ್ತಾರೆ?  →  linked list head, target val    │
  │  Output ಏನು ಬೇಕು?     →  val ಇರೋ ಎಲ್ಲಾ nodes remove ಮಾಡಿ│
  │                           ಉಳಿದ list ರ head return ಮಾಡಿ   │
  │  Constraints ಏನಿದೆ?   →  HEAD ಕೂಡ match ಆಗಬಹುದು — new   │
  │                           head ಬದಲಾಗಬಹುದು!               │
  └─────────────────────────────────────────────────────────┘

  ಹಂತ 2 — ಯಾಕೆ ಇದು tricky? "HEAD matches ಆದ್ರೆ?" ಅಂತ ಯೋಚಿಸಿ
  →  ಸಾಮಾನ್ಯ node ಅನ್ನ delete ಮಾಡೋಕೆ, ಅದರ PREVIOUS node ಗೆ
     access ಬೇಕು (prev.next = curr.next)
  →  ಆದ್ರೆ HEAD ಗೆ PREVIOUS node ಇಲ್ಲ! ಪ್ರತ್ಯೇಕ ಆಗಿ handle
     ಮಾಡಬೇಕಾ, ಅಥವಾ ಒಂದೇ ಕೋಡ್ ಲಾಜಿಕ್ ಸಾಕಾ?

  ಹಂತ 3 — "DUMMY NODE" trick ಏನಿದೆ?
  →  "head ಗೆ ಒಂದು FAKE previous node ಸೃಷ್ಟಿಸಿ ಮುಂದೆ ಇಟ್ಟುಕೊಂಡ್ರೆ?"
  →  dummy.next = head ಅಂತ ಇಟ್ಟುಕೊಂಡ್ರೆ, ಈಗ EVERY node (head
     ಸೇರಿ) ಗೂ ಒಂದು "previous" ಇರುತ್ತೆ — special-case ಬೇಡ!
  →  ಕೊನೆಗೆ dummy.next ಅನ್ನೇ final answer ಆಗಿ return ಮಾಡಿ (ಇದೇ
     actual new head, ಹೆಡ್ ಬದಲಾಗಿದ್ರೂ ಸರಿಯಾಗಿ ಗೊತ್ತಾಗುತ್ತೆ)

  ಹಂತ 4 — Technique ಯಾಕೆ ಇಲ್ಲಿ ಕೆಲಸ ಮಾಡುತ್ತೆ?
  →  curr ಅನ್ನ dummy ಇಂದ ಶುರು ಮಾಡಿ, curr.next ಅನ್ನ ಪ್ರತಿ ಸಲ
     check ಮಾಡಿ: match ಆದ್ರೆ curr.next = curr.next.next (skip
     ಮಾಡಿ), ಇಲ್ಲಾಂದ್ರೆ curr = curr.next (ಮುಂದಕ್ಕೆ ಹೋಗು)
  →  ಈ ಒಂದೇ loop, HEAD ಮತ್ತು middle nodes ಎಲ್ಲಾ ಒಂದೇ ಹಾಗೆ
     handle ಮಾಡುತ್ತೆ — no special casing needed!

  💡 Interview ನಲ್ಲಿ ಹೇಗೆ ಮಾತಾಡಬೇಕು:
  →  "Use a dummy node pointing to head — this avoids special-
      casing when the head itself needs to be removed"
  →  "Walk with curr starting at dummy; if curr.next matches,
      skip it (curr.next = curr.next.next); otherwise advance curr"
  →  "Return dummy.next as the new head"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🏷️ SECTION 3 — TECHNIQUE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Primary   : Dummy Node — iterative, O(1) space
  Secondary : Recursion — elegant but O(n) call stack

  WHY Dummy Node?
  → It eliminates the special case of "the node to remove IS the
    head" by giving even the head a predecessor. One uniform
    loop then handles every node, head included, with no branch
    for "is this the first node?"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 💡 SECTION 4 — INTUITION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  The key insight: removing a node always requires rewiring its
  PREDECESSOR's `next` pointer — but the head has no predecessor
  in the original list. Inventing a fake one (the dummy node)
  makes every node, including the head, removable with the exact
  same logic. At the end, dummy.next naturally reflects whatever
  survived — even if that's a completely different node than the
  original head, or even None.

  The journey from brute to optimal:
    Brute thought   →  Recursively process each node: "if my
                       value matches, I disappear and my next's
                       result becomes my replacement; otherwise
                       I keep my (recursively-fixed) next"
    Problem with it →  O(n) call stack depth — fine for most
                       inputs, but not O(1) space
    Better question →  "Can I avoid recursion and a head special
                       case at the same time?"
    Insight         →  A dummy predecessor node makes head
                       removal just as uniform as any other
                       removal, iteratively
    Optimal         →  Single iterative pass, O(1) extra space

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🐢 SECTION 5 — APPROACH 1 — RECURSIVE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    Recurse to the end of the list first. On the way back, each
    node decides: if its own value matches `val`, it's dropped
    (return whatever its next resolved to); otherwise it keeps
    itself, with `next` already pointing to the cleaned-up rest.

  Pseudocode:
    step 1: if head is None: return None
    step 2: head.next = remove_elements(head.next, val)
    step 3: return head.next if head.val == val else head

  Time  : O(n)  →  Why: visits every node exactly once
  Space : O(n)  →  Why: recursion call stack depth equals list
                        length

  ಇದು ಯಾಕೆ ಸಾಕಾಗಲ್ಲ?
    → Correct and clean, but O(n) stack space — for n up to
      10^4 this works, but the iterative dummy-node approach
      gets the same result with O(1) extra space.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🚀 SECTION 6 — OPTIMAL (Dummy Node, Iterative)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    Create a dummy node pointing at `head`. Walk `curr` starting
    at the dummy. At each step, if `curr.next` matches `val`,
    skip it by rewiring `curr.next = curr.next.next` (don't
    advance curr — the new curr.next might ALSO match). Otherwise
    advance curr normally. Return `dummy.next`.

  Key steps:
    1. dummy = ListNode(0, head); curr = dummy
    2. while curr.next:
    3.   if curr.next.val == val: curr.next = curr.next.next
    4.   else: curr = curr.next
    5. return dummy.next

  ಕನ್ನಡದಲ್ಲಿ ಒಂದು ಸಲ ಹೇಳಿ:
    → "dummy node ಅನ್ನ head ಗೆ point ಮಾಡಿ, curr=dummy ಇಂದ ಶುರು
       ಮಾಡು. curr.next match ಆದ್ರೆ skip ಮಾಡು (curr ಅಲ್ಲಿಯೇ
       ಇರಲಿ, ಮುಂದಿನ node ಕೂಡ match ಆಗಬಹುದು!). match ಆಗದಿದ್ರೆ
       curr ಅನ್ನ ಮುಂದಕ್ಕೆ ಸರಿಸು. ಕೊನೆಗೆ dummy.next return ಮಾಡು!"

  Time  : O(n)  →  Why: single pass through the list
  Space : O(1)  →  Why: only dummy and curr pointers, no
                        recursion or extra storage

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🔍 SECTION 7 — DRY RUN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Input: 1 → 2 → 6 → 3 → 4 → 5 → 6 → None, val = 6

  dummy → 1 → 2 → 6 → 3 → 4 → 5 → 6 → None
  curr = dummy

  curr.next=1, no match → curr=1
  curr.next=2, no match → curr=2
  curr.next=6, MATCH → curr.next = 3 (skip the 6)
    list now: ...2 → 3 → 4 → 5 → 6 → None
  curr.next=3, no match → curr=3
  curr.next=4, no match → curr=4
  curr.next=5, no match → curr=5
  curr.next=6, MATCH → curr.next = None (skip the 6)
    list now: ...5 → None

  Return dummy.next = 1 → 2 → 3 → 4 → 5 → None

  Output: 1 → 2 → 3 → 4 → 5 → None ✓

  ಇನ್ನೊಂದು example — head itself matches, repeatedly:
  Input: 7 → 7 → 7 → 7 → None, val = 7

  dummy → 7 → 7 → 7 → 7 → None, curr = dummy
  curr.next=7, MATCH → curr.next=7 (skip) — repeat 4 times,
  curr stays at dummy throughout since every node matches
  Final: dummy.next = None

  Output: None ✓

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 ⚠️ SECTION 8 — EDGE CASES — ಇವನ್ನ ಮರೆಯಬೇಡ!
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  ✓ Empty list?                    →  None — loop never runs
  ✓ All nodes match (head too)?    →  None — dummy.next ends up
                                       None naturally
  ✓ No nodes match?                →  list unchanged, head
                                       returned as-is (via dummy)
  ✓ Only the head matches?         →  rest of list becomes the
                                       new head, handled with no
                                       special case
  ✓ Consecutive matching nodes?    →  curr doesn't advance while
                                       skipping, so runs of
                                       matches are all removed

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📊 SECTION 9 — COMPLEXITY SUMMARY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                  Time    Space
  Recursive       O(n)    O(n)   (call stack)
  Dummy Node      O(n)    O(1)   ← use this ✅

  Time yaake O(n)?  → Single pass, every node visited once
  Space yaake O(1)? → Only dummy + curr pointers — no recursion,
                       no extra list

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🎯 SECTION 10 — PATTERN LEARNED — ಇದರಿಂದ ಕಲಿತದ್ದು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Pattern Name: Dummy Node — uniform head handling

  Ee pattern yaavaaga use maadabeeku?
  → Any linked-list problem where the HEAD itself might need to
     be removed, replaced, or skipped — dummy node removes the
     need for a separate "is this the head?" branch
  → Merge Two Sorted Lists, Remove Nth Node From End, Add Two
     Numbers — all lean on this exact same dummy-node trick

  Idee pattern beere problemsalli kaanisatte:
  → Remove Nth Node From End #19 (already done — same dummy
     node trick, different removal condition)
  → Merge Two Sorted Lists #21 (already done — dummy node to
     avoid special-casing which list starts first)
  → Sort List #148 (next in curriculum — merge sort on a linked
     list, dummy node reused again during merging)

  Next time intaha problem bandre naanu modalu idannu think maadtene:
  → "Linked list alli HEAD itself remove/replace aagabahudu
     antadre → dummy node use madu! Special-case illade, ONE
     uniform loop ella nodes handle maaduttade."

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🗣️ SECTION 11 — INTERVIEWALLI HEGE EXPLAIN MAADABEEKU
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  1. Understand:
     "Remove every node whose value equals val, including
      possibly the head itself, and return the new head."

  2. Brute force (recursive):
     "Recurse to the end; on the way back, each node either
      drops itself (returns its next) or keeps itself with a
      cleaned-up next. O(n) time, O(n) stack space."

  3. Optimize:
     "Use a dummy node pointing at head so the head has a
      predecessor too. Walk curr from dummy; skip curr.next
      whenever it matches (without advancing curr), else advance
      curr. Return dummy.next."

  4. Code:
     "dummy = ListNode(0, head); curr = dummy. While curr.next:
      skip or advance based on curr.next.val == val."

  5. Complexity:
     "Time O(n) — single pass. Space O(1) — two pointers only."

  Mukhya: whenever the HEAD might need removing, reach for a
          dummy node first — it turns a special case into the
          same uniform loop as everything else!
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
# RECURSIVE — O(n) Time | O(n) Space (call stack)
# ═══════════════════════════════════════════════════════════════════
def remove_elements_recursive(head, val):
    """
    Idu modala aaloochane — end tanaka recurse madi, return
    maadtha prati node tanna value match aadre bidu, illa andre
    tanna cleaned-up next itkondu self return madu
    """
    if not head:
        return None

    head.next = remove_elements_recursive(head.next, val)

    return head.next if head.val == val else head


# ═══════════════════════════════════════════════════════════════════
# OPTIMAL — O(n) Time | O(1) Space (dummy node, iterative)
# ═══════════════════════════════════════════════════════════════════
def remove_elements(head, val):
    """
    Idu final answer — dummy node head ge point madi, curr.next
    match aadre skip madu (curr advance madabeda), illa andre
    curr advance madu
    """
    dummy = ListNode(0, head)
    curr = dummy

    while curr.next:
        if curr.next.val == val:
            curr.next = curr.next.next
        else:
            curr = curr.next

    return dummy.next


# ═══════════════════════════════════════════════════════════════════
# TEST CASES
# ═══════════════════════════════════════════════════════════════════
if __name__ == "__main__":
    # Test 1 — Basic
    assert to_list(remove_elements(build([1, 2, 6, 3, 4, 5, 6]), 6)) == [1, 2, 3, 4, 5]

    # Test 2 — Every node matches (including head)
    assert to_list(remove_elements(build([7, 7, 7, 7]), 7)) == []

    # Test 3 — Empty list
    assert to_list(remove_elements(None, 1)) == []

    # Test 4 — No matches
    assert to_list(remove_elements(build([1, 2, 3]), 5)) == [1, 2, 3]

    # Test 5 — Only head matches
    assert to_list(remove_elements(build([1, 2, 3]), 1)) == [2, 3]

    # Cross-check: recursive version must agree on all of the above
    assert to_list(remove_elements_recursive(build([1, 2, 6, 3, 4, 5, 6]), 6)) == [1, 2, 3, 4, 5]
    assert to_list(remove_elements_recursive(build([7, 7, 7, 7]), 7)) == []
    assert to_list(remove_elements_recursive(None, 1)) == []
    assert to_list(remove_elements_recursive(build([1, 2, 3]), 5)) == [1, 2, 3]
    assert to_list(remove_elements_recursive(build([1, 2, 3]), 1)) == [2, 3]

    print("All tests passed!")
