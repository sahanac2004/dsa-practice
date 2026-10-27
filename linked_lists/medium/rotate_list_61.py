"""
╔══════════════════════════════════════════════════════════════════╗
║  ROTATE LIST                                                     ║
║  LeetCode #61  |  Difficulty: Medium  |  Topic: Linked Lists    ║
║  Link: https://leetcode.com/problems/rotate-list/               ║
╚══════════════════════════════════════════════════════════════════╝

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📘 SECTION 1 — PROBLEM UNDERSTANDING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Given the head of a linked list, rotate the list to the RIGHT
  by k places. Rotating right by k means: take the last k nodes
  and move them, as a block (keeping their relative order), to
  the front of the list.

  Input : head = linked list, k = number of right-rotations
  Output: head of the rotated list

  Example 1 — basic:
    Input : head = [1,2,3,4,5], k = 2
    Output: [4,5,1,2,3]
    Why?  : last 2 nodes (4,5) move to the front, rest follow

  Example 2 — k larger than list length:
    Input : head = [0,1,2], k = 4
    Output: [2,0,1]
    Why?  : rotating by len(list) brings the list back to
            itself, so effectively only k % len rotations matter
            (4 % 3 = 1 → rotate by 1)

  Constraints:
    - 0 <= number of nodes <= 500
    - -100 <= Node.val <= 100
    - 0 <= k <= 2 * 10^9

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🧠 SECTION 2 — KANGLISH THINKING — ಹೇಗೆ ಯೋಚಿಸಬೇಕು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  Problem odi aada mele namma brain enu think maadabeeku:

  ಹಂತ 1 — Problem ಅರ್ಥ ಮಾಡಿಕೊಳ್ಳಿ
  ┌─────────────────────────────────────────────────────────┐
  │  Input ಏನು ಕೊಡ್ತಾರೆ?  →  linked list ಮತ್ತು k (rotate     │
  │                           ಎಷ್ಟು right ಗೆ ಮಾಡ್ಬೇಕು)         │
  │  Output ಏನು ಬೇಕು?     →  last k nodes ಅನ್ನ front ಗೆ       │
  │                           ತಗೊಂಡು ಹೋಗಿ ಜೋಡಿಸಿದ list        │
  │  Constraints ಏನಿದೆ?   →  k ತುಂಬಾ ದೊಡ್ಡದಾಗಿರಬಹುದು (list   │
  │                           length ಗಿಂತ ಜಾಸ್ತಿ ಸಹ ಆಗಬಹುದು)   │
  └─────────────────────────────────────────────────────────┘

  ಹಂತ 2 — ಯಾಕೆ ಇದು tricky? "k ತುಂಬಾ ದೊಡ್ಡ ಇದ್ರೆ?" ಅಂತ ಯೋಚಿಸಿ
  →  k = 2 * 10^9 ಇರಬಹುದು, ಆದ್ರೆ list length ಕೇವಲ 500! k ಸಲ
     ಅಕ್ಷರಶಃ rotate ಮಾಡಿದ್ರೆ ಟೈಮ್ limit exceed ಆಗುತ್ತೆ
  →  Key observation: list ಅನ್ನ ಅದರ own length ಇಂದ rotate
     ಮಾಡಿದ್ರೆ, ಅದು ಮೊದಲಿನ ಹಾಗೇ ಆಗುತ್ತೆ (full circle!) — so
     ಬೇಕಾಗಿರೋದು k % length ಮಾತ್ರ, ಪೂರ್ತಿ k ಅಲ್ಲ

  ಹಂತ 3 — ಮೊದಲ simple idea (brute force) ಏನು?
  →  "k ಸಲ, ಪ್ರತಿ ಸಲ last node ಅನ್ನ cut ಮಾಡಿ front ಗೆ ಹಾಕಿದ್ರೆ?"
  →  ಆದ್ರೆ ಪ್ರತಿ rotation ಗೂ list ಕೊನೆ ತನಕ ಹೋಗಿ last node ಹುಡುಕ್ಬೇಕು
     → O(k * n) time — k ದೊಡ್ಡ ಇದ್ರೆ ತುಂಬಾ ಸ್ಲೋ

  ಹಂತ 4 — Optimal idea ಹೇಗೆ ಬರುತ್ತೆ?
  →  "list ಅನ್ನ ಒಂದು CIRCLE ಮಾಡಿದ್ರೆ?" ಅಂತ ಯೋಚಿಸಿ: last node
     ಅನ್ನ head ಗೆ ಜೋಡಿಸಿ circular ಮಾಡಿ, ಆಮೇಲೆ ಸರಿಯಾದ ಜಾಗದಲ್ಲಿ
     break ಮಾಡಿದ್ರೆ rotation ಸಿಗುತ್ತೆ!
  →  ಎಲ್ಲಿ break ಮಾಡ್ಬೇಕು? → new tail ಅಂದ್ರೆ (length - k % length)
     ನೇ node (0-indexed ಆದ್ರೆ length - k%length - 1), new head
     ಅಂದ್ರೆ ಅದರ ಮುಂದಿನ node

  ಹಂತ 5 — Technique ಯಾಕೆ ಇಲ್ಲಿ ಕೆಲಸ ಮಾಡುತ್ತೆ?
  →  Circular ಮಾಡಿದ ಮೇಲೆ, "ಎಲ್ಲಿ cut ಮಾಡಿದ್ರೂ" ಒಂದು valid
     rotation ಸಿಗುತ್ತೆ — so ಸರಿಯಾದ ಜಾಗ ಕಂಡುಹಿಡಿದು ಒಂದೇ cut
     ಮಾಡಿದ್ರೆ ಸಾಕು, k ಸಲ repeat ಮಾಡೋ ಅಗತ್ಯ ಇಲ್ಲ

  💡 Interview ನಲ್ಲಿ ಹೇಗೆ ಮಾತಾಡಬೇಕು:
  →  "First approach: literally rotate k times, O(k*n) — too
      slow since k can be huge"
  →  "Optimal: compute k % length to cap rotations, make the
      list circular, then find the new tail and break the
      circle there — O(n) time, O(1) space"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🏷️ SECTION 3 — TECHNIQUE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Primary   : Make Circular + Break at New Tail (O(n) time, O(1) space)
  Secondary : Repeated single-rotation simulation (O(k*n) brute force)

  WHY Circular-and-break over repeated rotation?
  → Repeating "move last node to front" k times re-walks the
    list each time, and k can be astronomically larger than the
    list itself. Reducing k to k % length first, then doing ONE
    pass to link tail→head (circular) and ONE pass to find and
    cut at the new tail, turns a potentially O(k*n) disaster
    into a guaranteed O(n).

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 💡 SECTION 4 — INTUITION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  The key insight: rotating a list of length n by n brings it
  right back to itself — rotation is periodic with period n. So
  the only rotations that actually matter are k % n of them.
  Once k is reduced to something at most n-1, picture joining
  the tail to the head to form a ring. Walking "k % n" steps
  isn't even needed per-element — instead walk to position
  (n - k % n - 1) from the head, that becomes the NEW tail, and
  the node right after it becomes the NEW head. Cut the ring
  there and you're done in one pass.

  The journey from brute to optimal:
    Brute thought   →  Repeat "cut last node, place at front" k
                       times
    Problem with it →  Each repetition re-scans to find the last
                       node — O(k*n), and k can be up to 2*10^9
    Better question →  "Does rotating by the FULL length change
                       anything?" → No, it's a no-op. So only
                       k % length matters.
    Insight         →  Link tail to head (circular), then find
                       the new tail/head boundary and cut once
    Optimal         →  Two O(n) passes (find length + link tail
                       to head, then find new tail and cut),
                       O(1) extra space

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🐢 SECTION 5 — APPROACH 1 — BRUTE FORCE (Repeated Rotation)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    Reduce k to k % length first (otherwise this would be
    hopeless for huge k). Then repeat, k times: walk to the last
    node and its previous node, detach the last node, and place
    it at the front.

  Pseudocode:
    step 1: if not head or not head.next: return head
    step 2: length = count nodes
    step 3: k = k % length; if k == 0: return head
    step 4: repeat k times:
    step 5:   walk to second-to-last node (prev) and last node (last)
    step 6:   prev.next = None
    step 7:   last.next = head
    step 8:   head = last
    step 9: return head

  Time  : O(k * n)  →  Why: each of the k repetitions re-walks
                        the whole list to find the last node
  Space : O(1)      →  Why: only pointer rewiring, no extra storage

  ಇದು ಯಾಕೆ ಸಾಕಾಗಲ್ಲ?
    → Even after capping k with k % length, k can still be up
      to length-1 (e.g. ~499), so this is O(n^2) in the worst
      case — the circular trick does the same job in O(n).

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🚀 SECTION 6 — OPTIMAL (Make Circular, Break at New Tail)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    1. Walk to the last node, counting length, and link the
       last node's next to head — now the list is a ring.
    2. Reduce k to k % length (no-op rotation if 0).
    3. Walk (length - k - 1) steps from head to reach the new
       tail. The node right after it is the new head.
    4. Cut the ring there: new_tail.next = None.

  Key steps:
    1. length = 1; tail = head
       while tail.next: tail = tail.next; length += 1
       tail.next = head  (make circular)
    2. k = k % length
       steps_to_new_tail = length - k
    3. new_tail = head
       for _ in range(steps_to_new_tail - 1): new_tail = new_tail.next
       new_head = new_tail.next
       new_tail.next = None
       return new_head

  ಕನ್ನಡದಲ್ಲಿ ಒಂದು ಸಲ ಹೇಳಿ:
    → "ಮೊದಲು list ಕೊನೆ ತನಕ ಹೋಗಿ length ಕಂಡುಹಿಡಿ, last node ಅನ್ನ
       head ಗೆ ಜೋಡಿಸಿ circle ಮಾಡು. ಆಮೇಲೆ k ಅನ್ನ k % length
       ಮಾಡಿ ಕಡಿಮೆ ಮಾಡು. ಈಗ (length - k) ನೇ node ಗೆ ಹೋಗಿ, ಅಲ್ಲಿ
       circle ಅನ್ನ ಕತ್ತರಿಸು — ಅದೇ ಹೊಸ tail, ಅದರ ಮುಂದಿನ node ಹೊಸ
       head!"

  Time  : O(n)  →  Why: one pass to find length + link, one
                        pass to find the new tail and cut
  Space : O(1)  →  Why: only a few pointers, no extra storage

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🔍 SECTION 7 — DRY RUN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Input: head = [1,2,3,4,5], k = 2

  Step 1 — find length + make circular:
    length = 5
    circle: 1→2→3→4→5→(back to 1)

  Step 2 — reduce k:
    k = 2 % 5 = 2
    steps_to_new_tail = 5 - 2 = 3

  Step 3 — walk to new tail (3rd node from head, 1-indexed):
    new_tail starts at 1 (node val=1)
    loop runs (3-1)=2 times: 1 → 2 → 3
    new_tail = node(val=3)
    new_head = new_tail.next = node(val=4)

  Step 4 — cut:
    new_tail.next = None  →  3's next becomes None
    result: 4→5→1→2→3→None

  Output: [4,5,1,2,3] ✓ matches expected

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 ⚠️ SECTION 8 — EDGE CASES — ಇವನ್ನ ಮರೆಯಬೇಡ!
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  ✓ Empty list (None)?           →  return None immediately
  ✓ Single node?                 →  always returns itself
                                     (rotating one node does nothing)
  ✓ k == 0?                      →  no rotation, return head as-is
  ✓ k == length (exact multiple)?→  k % length == 0, no-op,
                                     return original head
  ✓ k larger than length
    (e.g. k = 4, length = 3)?    →  reduced via k % length first,
                                     so only the EFFECTIVE
                                     rotation amount matters
  ✓ k = 0 and list non-empty?    →  handled by the mod + the
                                     "steps_to_new_tail == length"
                                     check before walking

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📊 SECTION 9 — COMPLEXITY SUMMARY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                              Time      Space
  Brute (repeated rotation)   O(k * n)   O(1)
  Circular + break             O(n)       O(1)   ← use this ✅

  Time yaake O(n)?  → Exactly two linear passes: one to find
                       length and link the circle, one to find
                       the new tail
  Space yaake O(1)? → Only pointer variables, no extra storage
                       regardless of list size

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🎯 SECTION 10 — PATTERN LEARNED — ಇದರಿಂದ ಕಲಿತದ್ದು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Pattern Name: Modulo-Reduce + Make Circular to Rotate

  Ee pattern yaavaaga use maadabeeku?
  → Any "rotate by k" problem (arrays or lists) where k can be
     arbitrarily larger than the structure's length — ALWAYS
     reduce k via k % length first before doing any real work
  → Linked-list rotation specifically: turning the list into a
     ring sidesteps the need to repeatedly re-walk it; a single
     well-placed cut produces any rotation amount

  Idee pattern beere problemsalli kaanisatte:
  → Rotate Array #189 (same k % length reduction idea, but for
     arrays — reversal trick there instead of a circular link)
  → Rotate List mathe circular buffer / LRU cache designs that
     conceptually wrap around

  Next time intaha problem bandre naanu modalu idannu think maadtene:
  → "Rotate by k ide, k list/array length gintha jaasti aagbahuda
     anta yochisi — haudu antadre, modalu k % length madi
     kadime maadu. Linked list aadre circular madi, right
     jaagadalli cut madi — O(n) alli solve aagutte!"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🗣️ SECTION 11 — INTERVIEWALLI HEGE EXPLAIN MAADABEEKU
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  1. Understand:
     "Rotate a linked list to the right by k places — move the
      last k nodes, as a block, to the front."

  2. Brute force:
     "Repeat 'cut last node, place at front' k times. But k can
      be up to 2*10^9, so first reduce it with k % length — even
      then, repeating is O(k*n) in the worst case."

  3. Optimize:
     "Find the length while linking the tail to the head,
      forming a circle. Reduce k to k % length. Walk to the new
      tail position and cut the ring there — one pass, O(n)."

  4. Code:
     "Two passes: (1) measure length + link tail→head, (2) walk
      (length - k) steps to the new tail, detach, return the
      node after it as the new head."

  5. Complexity:
     "Time O(n) — two linear passes regardless of k. Space O(1)
      — just pointer rewiring."

  Mukhya: whenever k can be huge compared to the structure's
          size, reduce it with modulo FIRST — the actual work is
          always bounded by the structure's own length!
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
# BRUTE FORCE — O(k * n) Time | O(1) Space (repeated rotation)
# ═══════════════════════════════════════════════════════════════════
def rotate_right_brute(head, k):
    """
    Idu modala aaloochane — k % length madi kadime maadi, aamele
    k sala "last node cut madi front ge haaku" anta repeat madu
    """
    if not head or not head.next:
        return head

    length = 1
    curr = head
    while curr.next:
        curr = curr.next
        length += 1

    k = k % length
    if k == 0:
        return head

    for _ in range(k):
        prev = head
        while prev.next.next:
            prev = prev.next
        last = prev.next
        prev.next = None
        last.next = head
        head = last

    return head


# ═══════════════════════════════════════════════════════════════════
# OPTIMAL — O(n) Time | O(1) Space (circular + break)
# ═══════════════════════════════════════════════════════════════════
def rotate_right(head, k):
    """
    Idu final answer — list ge circle madi, k % length reduce
    madi, right jaagadalli cut madi new head/tail set madu
    """
    if not head or not head.next:
        return head

    length = 1
    tail = head
    while tail.next:
        tail = tail.next
        length += 1

    k = k % length
    if k == 0:
        return head

    tail.next = head  # make circular

    steps_to_new_tail = length - k
    new_tail = head
    for _ in range(steps_to_new_tail - 1):
        new_tail = new_tail.next

    new_head = new_tail.next
    new_tail.next = None

    return new_head


# ═══════════════════════════════════════════════════════════════════
# TEST CASES
# ═══════════════════════════════════════════════════════════════════
if __name__ == "__main__":
    # Test 1 — Basic (LeetCode example 1)
    head = build([1, 2, 3, 4, 5])
    assert to_list(rotate_right(head, 2)) == [4, 5, 1, 2, 3]

    # Test 2 — k larger than length (LeetCode example 2)
    head = build([0, 1, 2])
    assert to_list(rotate_right(head, 4)) == [2, 0, 1]

    # Test 3 — k == 0 (no rotation)
    head = build([1, 2, 3])
    assert to_list(rotate_right(head, 0)) == [1, 2, 3]

    # Test 4 — k is an exact multiple of length (no-op)
    head = build([1, 2, 3])
    assert to_list(rotate_right(head, 6)) == [1, 2, 3]

    # Test 5 — single node
    head = build([1])
    assert to_list(rotate_right(head, 5)) == [1]

    # Test 6 — empty list
    assert rotate_right(None, 3) is None

    # Test 7 — two nodes
    head = build([1, 2])
    assert to_list(rotate_right(head, 1)) == [2, 1]

    # Cross-check: brute force must agree on all of the above
    head = build([1, 2, 3, 4, 5])
    assert to_list(rotate_right_brute(head, 2)) == [4, 5, 1, 2, 3]

    head = build([0, 1, 2])
    assert to_list(rotate_right_brute(head, 4)) == [2, 0, 1]

    head = build([1, 2, 3])
    assert to_list(rotate_right_brute(head, 0)) == [1, 2, 3]

    head = build([1, 2, 3])
    assert to_list(rotate_right_brute(head, 6)) == [1, 2, 3]

    head = build([1])
    assert to_list(rotate_right_brute(head, 5)) == [1]

    assert rotate_right_brute(None, 3) is None

    head = build([1, 2])
    assert to_list(rotate_right_brute(head, 1)) == [2, 1]

    print("All tests passed!")
