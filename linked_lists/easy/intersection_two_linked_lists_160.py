"""
╔══════════════════════════════════════════════════════════════════╗
║  INTERSECTION OF TWO LINKED LISTS                                ║
║  LeetCode #160  |  Difficulty: Easy  |  Topic: Linked Lists     ║
║  Link: https://leetcode.com/problems/intersection-of-two-linked-lists/                                                    ║
╚══════════════════════════════════════════════════════════════════╝

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📘 SECTION 1 — PROBLEM UNDERSTANDING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Given the heads of two singly linked lists headA and headB,
  return the node at which the two lists INTERSECT.
  If they do not intersect, return null.
  The intersection is by NODE REFERENCE, not by value.
  After intersection, both lists share the exact same nodes.

  Input : headA, headB = heads of two linked lists
  Output: intersecting node (by reference), or None

  Example 1 — basic:
    List A: a1 → a2 → c1 → c2 → c3
    List B:       b1 → c1 → c2 → c3
    Output: c1
    Why?  : Both lists merge at node c1 (same node object)

  Example 2 — no intersection:
    List A: 2 → 6 → 4
    List B: 1 → 5
    Output: None

  Constraints:
    - Lists may or may not intersect
    - No cycles in either list
    - Must be O(n) time, O(1) space

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🧠 SECTION 2 — KANGLISH THINKING — ಹೇಗೆ ಯೋಚಿಸಬೇಕು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  Problem odi aada mele namma brain enu think maadabeeku:

  ಹಂತ 1 — Problem ಅರ್ಥ ಮಾಡಿಕೊಳ್ಳಿ
  ┌─────────────────────────────────────────────────────────┐
  │  Input ಏನು ಕೊಡ್ತಾರೆ?  →  2 linked list heads          │
  │  Output ಏನು ಬೇಕು?     →  intersection node reference  │
  │  Constraints ಏನಿದೆ?   →  O(n) time, O(1) space        │
  │                           node reference check          │
  │                           (not value comparison!)       │
  └─────────────────────────────────────────────────────────┘

  ಹಂತ 2 — ನನಗೆ ಗೊತ್ತಿರೋ simple way ಏನು?
  →  List A ರ ಎಲ್ಲ nodes HashSet ಲ್ಲಿ store ಮಾಡಿ
     List B traverse ಮಾಡಿ first common node find ಮಾಡೋಣ
  →  ಆದರೆ ಇದು slow ಯಾಕೆ?
     O(n) space HashSet — O(1) space beeku!

  ಹಂತ 3 — Better way ಹೇಗೆ ಯೋಚಿಸುವುದು?
  →  "Two lists lengths different ಆದ್ರೆ...
     longer list ಲ್ಲಿ longer part skip ಮಾಡಿ same length
     ಇಂದ compare ಮಾಡೋಣ!"
  →  Approach 2 (elegant): Two pointers!
     pA = headA, pB = headB
     When pA reaches end → redirect to headB
     When pB reaches end → redirect to headA
     They meet at intersection or both reach None!
  →  WHY? Both traverse same total distance:
     lenA + lenB = lenB + lenA → meet at intersection!

  ಹಂತ 4 — Technique ಯಾಕೆ ಇಲ್ಲಿ ಕೆಲಸ ಮಾಡುತ್ತೆ?
  →  pA traverses: A's unique part + intersection + B's unique part
  →  pB traverses: B's unique part + intersection + A's unique part
  →  Both travel same total distance → meet at intersection!
  →  If no intersection → both reach None simultaneously!

  💡 Interview ನಲ್ಲಿ ಹೇಗೆ ಮಾತಾಡಬೇಕು:
  →  "Two pointers — when one reaches end, redirect to other head"
  →  "Both travel lenA + lenB total — meet at intersection"
  →  "No intersection → both become None at same time"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🏷️ SECTION 3 — TECHNIQUE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Primary   : Two Pointer — Cross Traverse Trick
  Secondary : Length Difference (align then compare)

  WHY Cross Traverse?
  → pA: A unique + shared + B unique = lenA + lenB - shared + shared
  → pB: B unique + shared + A unique = same total!
  → Both reach intersection at same step → meet there!
  → If no intersection → both become None together → exit!
  → O(1) space, O(m+n) time — most elegant solution!

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 💡 SECTION 4 — INTUITION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Think of two people walking two paths that merge:
  Person A walks path A then path B.
  Person B walks path B then path A.
  They walk the same total distance → meet at the junction!

  pA: [A unique] → [shared] → [B unique] → REDIRECT → [B unique] ...
  pB: [B unique] → [shared] → [A unique] → REDIRECT → [A unique] ...

  Wait, let me be precise:
  pA travels: a_unique + intersection + b_unique (total = m+n-shared)
  pB travels: b_unique + intersection + a_unique (total = n+m-shared)
  Same total distance → when pA and pB reach intersection,
  they've both traveled a_unique + b_unique steps → they're equal!

  The journey from brute to optimal:
    Brute thought   →  HashSet for all of A, scan B → O(n) space
    Problem with it →  O(1) space required
    Better thought  →  Align lengths, then scan together → O(1) space
    Best insight    →  Cross traverse — same total distance trick!
    Optimal         →  Two pointer cross traverse O(m+n), O(1)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🐢 SECTION 5 — APPROACH 1 — BRUTE FORCE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    Store all nodes of list A in a HashSet.
    Traverse list B — first node found in HashSet = intersection.

  Time  : O(m + n)  →  Why: one pass each list
  Space : O(m)      →  Why: HashSet stores list A nodes

  ಇದು ಯಾಕೆ ಸಾಕಾಗಲ್ಲ?
    → O(m) space — O(1) beeku!

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🚶 SECTION 6 — APPROACH 2 — BETTER (Length Align)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    Find lengths of both lists. Advance the longer one by the
    difference. Then traverse both together until they meet.

  Time  : O(m + n)  →  two passes + one aligned pass
  Space : O(1)      →  only pointers

  ಇನ್ನೂ elegant solution iddaa?
    → YES! Cross traverse trick!

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🚀 SECTION 7 — APPROACH 3 — OPTIMAL (Cross Traverse)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    Two pointers pA and pB start at headA and headB.
    When pA reaches end → redirect to headB.
    When pB reaches end → redirect to headA.
    They meet at intersection or both become None.

  Key steps:
    1. pA = headA, pB = headB
    2. While pA != pB:
       a. pA = pA.next if pA else headB
       b. pB = pB.next if pB else headA
    3. return pA (either intersection node or None)

  ಕನ್ನಡದಲ್ಲಿ ಒಂದು ಸಲ ಹೇಳಿ:
    → "pA = headA, pB = headB ಇಂದ start maadu.
       pA != pB iddre: pA next ಗೆ, end iddre headB ಗೆ jump.
       pB next ಗೆ, end iddre headA ಗೆ jump.
       Meet aadaaga = intersection! Both None = no intersection.
       Same total distance travel maadtaare!"

  Time  : O(m + n)  →  Why: each pointer traverses at most m+n nodes
  Space : O(1)      →  Why: only two pointers

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🔍 SECTION 8 — DRY RUN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  List A: a1(2) → a2(3) → c1(8) → c2(4)
  List B:         b1(5) → c1(8) → c2(4)
  lenA=4, lenB=3, intersection=c1

  pA=a1, pB=b1 → not equal → advance
  pA=a2, pB=c1 → not equal → advance
  pA=c1, pB=c2 → not equal → advance
  pA=c2, pB=None → pB redirect to headA=a1
  pA=None → pA redirect to headB=b1, pB=a1
  pA=b1, pB=a2 → not equal → advance
  pA=c1, pB=c1 → EQUAL → return c1 ✓

  No intersection:
  List A: 2→6→4 (len=3)
  List B: 1→5   (len=2)

  Both will reach None and redirect to other head.
  After traversing 3+2=5 steps each → both become None → exit!
  return pA = None ✓

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 ⚠️ SECTION 9 — EDGE CASES — ಇವನ್ನ ಮರೆಯಬೇಡ!
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  ✓ No intersection?         →  Both become None → return None
  ✓ Same list?               →  headA == headB → return immediately
  ✓ Intersection at head?    →  headA == headB
  ✓ One list empty?          →  No intersection possible → None
  ✓ Same length lists?       →  Cross traverse still works!

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📊 SECTION 10 — COMPLEXITY SUMMARY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                   Time       Space
  Brute (HashSet)  O(m+n)     O(m)
  Length Align     O(m+n)     O(1)
  Cross Traverse   O(m+n)     O(1)   ← use this ✅

  Time yaake O(m+n)? → Each pointer travels at most m+n nodes
  Space yaake O(1)?  → Only pA and pB pointers

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🎯 SECTION 11 — PATTERN LEARNED — ಇದರಿಂದ ಕಲಿತದ್ದು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Pattern Name: Two Pointer Cross Traverse

  The magic formula:
    pA traverses: A + B = m + n total
    pB traverses: B + A = n + m total
    Same distance → meet at intersection!

  Idee pattern beere problemsalli kaanisatte:
  → Linked List Cycle II #142 (Floyd's — similar two pointer)
  → Find Duplicate Number #287 (Floyd's cycle detection)
  → Any "two sequence alignment" problem

  Next time intaha problem bandre naanu modalu idannu think maadtene:
  → "Two lists intersection beeka, O(1) space?
     → Cross traverse! pA end iddre headB gu jump.
     pB end iddre headA gu jump. Same total distance
     → meet at intersection or both None!"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🗣️ SECTION 12 — INTERVIEWALLI HEGE EXPLAIN MAADABEEKU
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  1. Understand:
     "Find the node where two linked lists intersect.
      Intersection is by reference, not value."

  2. Brute force:
     "HashSet of all A nodes, scan B for first match. O(m) space."

  3. Optimize:
     "Cross traverse trick: pA starts at headA, pB at headB.
      When pA reaches end → jump to headB.
      When pB reaches end → jump to headA.
      Both travel m+n nodes total → meet at intersection.
      If no intersection → both become None simultaneously."

  4. Code:
     "while pA != pB: pA = pA.next if pA else headB,
      pB = pB.next if pB else headA. Return pA."

  5. Complexity:
     "Time O(m+n). Space O(1)."

  Mukhya: summane kuutu code bareyabeda!
          Math intuition explain maadu: same total distance!
          No intersection case: both None simultaneously!
"""


# ─── Node Definition ──────────────────────────────────────────────
class ListNode:
    def __init__(self, val=0, next=None):
        self.val  = val
        self.next = next


# ═══════════════════════════════════════════════════════════════════
# BRUTE FORCE — O(m+n) Time | O(m) Space
# ═══════════════════════════════════════════════════════════════════
def get_intersection_brute(headA, headB):
    """Idu modala aaloochane — HashSet of A nodes"""
    seen = set()
    curr = headA
    while curr:
        seen.add(id(curr))    # store memory address (node identity)
        curr = curr.next

    curr = headB
    while curr:
        if id(curr) in seen:
            return curr       # first node of B found in A
        curr = curr.next

    return None


# ═══════════════════════════════════════════════════════════════════
# BETTER — O(m+n) Time | O(1) Space (Length Align)
# ═══════════════════════════════════════════════════════════════════
def get_intersection_length(headA, headB):
    """Length difference approach — align then scan together"""
    def length(head):
        n, curr = 0, head
        while curr:
            n += 1
            curr = curr.next
        return n

    lenA, lenB = length(headA), length(headB)
    pA, pB = headA, headB

    # advance longer list pointer
    while lenA > lenB:
        pA = pA.next
        lenA -= 1
    while lenB > lenA:
        pB = pB.next
        lenB -= 1

    # now scan together
    while pA != pB:
        pA = pA.next
        pB = pB.next

    return pA    # None if no intersection


# ═══════════════════════════════════════════════════════════════════
# OPTIMAL — O(m+n) Time | O(1) Space (Cross Traverse)
# ═══════════════════════════════════════════════════════════════════
def get_intersection_node(headA, headB):
    """
    Idu final answer — cross traverse trick!
    pA and pB travel same total distance (m+n)
    → meet at intersection or both become None
    """
    pA = headA
    pB = headB

    while pA != pB:
        pA = pA.next if pA else headB   # end of A → jump to headB
        pB = pB.next if pB else headA   # end of B → jump to headA

    return pA   # intersection node or None


# ═══════════════════════════════════════════════════════════════════
# TEST CASES
# ═══════════════════════════════════════════════════════════════════
if __name__ == "__main__":
    # Build intersecting lists manually
    # shared: c1 → c2 → c3
    c1 = ListNode(8)
    c2 = ListNode(4)
    c1.next = c2

    # List A: 4 → 1 → c1 → c2
    a1 = ListNode(4)
    a2 = ListNode(1)
    a1.next = a2
    a2.next = c1

    # List B: 5 → 6 → 1 → c1 → c2
    b1 = ListNode(5)
    b2 = ListNode(6)
    b3 = ListNode(1)
    b1.next = b2
    b2.next = b3
    b3.next = c1

    # Test 1 — Intersection at c1
    result = get_intersection_node(a1, b1)
    assert result is c1, f"Expected c1, got {result}"

    # Test 2 — Cross traverse same as length align
    result2 = get_intersection_length(a1, b1)
    assert result2 is c1

    # Test 3 — No intersection
    x1 = ListNode(2)
    x2 = ListNode(6)
    x3 = ListNode(4)
    x1.next = x2
    x2.next = x3

    y1 = ListNode(1)
    y2 = ListNode(5)
    y1.next = y2

    assert get_intersection_node(x1, y1) is None

    # Test 4 — Same list (intersection at head)
    z1 = ListNode(1)
    assert get_intersection_node(z1, z1) is z1

    # Test 5 — One empty list
    assert get_intersection_node(None, y1) is None
    assert get_intersection_node(x1, None) is None

    print("All tests passed!")
