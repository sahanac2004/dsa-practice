"""
╔══════════════════════════════════════════════════════════════════╗
║  LINKED LIST CYCLE                                                ║
║  LeetCode #141  |  Difficulty: Easy  |  Topic: Linked Lists     ║
║  Link: https://leetcode.com/problems/linked-list-cycle/         ║
╚══════════════════════════════════════════════════════════════════╝

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📘 SECTION 1 — PROBLEM UNDERSTANDING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Given the head of a linked list, determine if the list has a
  cycle in it — i.e. some node's `next` pointer eventually leads
  back to a node already visited, instead of terminating at
  None. Return True if a cycle exists, False otherwise. (This is
  the simpler yes/no version — the follow-up, Linked List Cycle
  II #142, asks you to find the EXACT node where the cycle
  starts.)

  Input : head = first node of a linked list that may or may
          not contain a cycle
  Output: True if a cycle exists, False otherwise

  Example 1 — cycle exists:
    Input : head = [3,2,0,-4], tail connects to node index 1
    Output: True
    Why?  : following next pointers from -4 loops back to the
            node valued 2, so it never reaches None

  Example 2 — cycle at head:
    Input : head = [1,2], tail connects to node index 0
    Output: True

  Example 3 — no cycle:
    Input : head = [1]
    Output: False

  Constraints:
    - 0 <= number of nodes <= 10^4
    - -10^5 <= Node.val <= 10^5
    - pos is -1 if there is no cycle, else a valid index
    - MUST solve in O(1) extra space (follow-up requirement)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🧠 SECTION 2 — KANGLISH THINKING — ಹೇಗೆ ಯೋಚಿಸಬೇಕು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  Problem odi aada mele namma brain enu think maadabeeku:

  ಹಂತ 1 — Problem ಅರ್ಥ ಮಾಡಿಕೊಳ್ಳಿ
  ┌─────────────────────────────────────────────────────────┐
  │  Input ಏನು ಕೊಡ್ತಾರೆ?  →  cycle ಇರಬಹುದಾದ linked list      │
  │  Output ಏನು ಬೇಕು?     →  cycle ಇದ್ಯಾ (True/False) ಅಷ್ಟೇ   │
  │                           — ಎಲ್ಲಿ start ಆಗುತ್ತೆ ಅಂತ ಬೇಡ   │
  │  Constraints ಏನಿದೆ?   →  O(1) space ಲ್ಲಿ solve ಮಾಡ್ಬೇಕು    │
  └─────────────────────────────────────────────────────────┘

  ಹಂತ 2 — ಯಾಕೆ ಇದು tricky? "cycle ಇದ್ರೆ normal traversal
           ಮುಗಿಯೋಲ್ಲ!" ಅಂತ ಯೋಚಿಸಿ
  →  ಸಾಧಾರಣ `while curr: curr = curr.next` ಮಾಡಿದ್ರೆ, cycle
     ಇದ್ರೆ ಅದು INFINITE LOOP ಆಗಿ ಹೋಗುತ್ತೆ — ಯಾವತ್ತೂ None ಸಿಗಲ್ಲ
  →  ಹಾಗಾದ್ರೆ "ಈ node ಅನ್ನ ಮೊದಲೇ ನೋಡಿದ್ದೀನಾ" ಅಂತ ಹೇಗೆ ಗೊತ್ತಾಗುತ್ತೆ,
     extra memory ಇಲ್ಲದೇ?

  ಹಂತ 3 — ಮೊದಲ simple idea (brute force) ಏನು?
  →  "ಪ್ರತಿ node ಅನ್ನ ಒಂದು SET ಗೆ ಹಾಕಿ, ಅಗ್ಲೇ ಇರೋ node ಮತ್ತೆ
      ಸಿಕ್ರೆ cycle ಇದೆ ಅಂತ ಹೇಳಿದ್ರೆ?"
  →  ಕೆಲಸ ಆಗುತ್ತೆ, ಆದ್ರೆ O(n) extra space ಬೇಕಾಗುತ್ತೆ set ಗೆ —
     follow-up O(1) space ಕೇಳುತ್ತೆ!

  ಹಂತ 4 — Optimal idea (Floyd's) ಹೇಗೆ ಬರುತ್ತೆ?
  →  "ಎರಡು pointer, ಒಂದು SLOW (1 step), ಒಂದು FAST (2 step) —
      cycle ಇದ್ರೆ fast ಯಾವತ್ತಾದ್ರೂ slow ಅನ್ನ 'lap' ಮಾಡಿ catch
      ಮಾಡುತ್ತೆ (ಒಂದೇ ground ಮೇಲೆ ಓಡ್ತಿದ್ದಾರಲ್ಲ, ಹಾಗಾಗಿ ಸಿಗ್ತಾರೆ)!
      cycle ಇಲ್ದಿದ್ರೆ fast ಸುಮ್ಮನೆ None ಗೆ ಹೋಗಿ ಮುಗಿಯುತ್ತೆ"

  ಹಂತ 5 — Technique ಯಾಕೆ ಇಲ್ಲಿ ಕೆಲಸ ಮಾಡುತ್ತೆ?
  →  Think ಮಾಡಿ: ಒಂದು circular track ಮೇಲೆ ಇಬ್ಬರು ಓಡ್ತಿದ್ದಾರೆ,
     ಒಬ್ಬ ಡಬಲ್ ಸ್ಪೀಡ್ ಲ್ಲಿ — ಅವರ ಮಧ್ಯೆ gap ಪ್ರತಿ step ಗೂ 1
     ಕಡಿಮೆ ಆಗ್ತಾ ಹೋಗುತ್ತೆ (relative speed = 1), ಆದ್ದರಿಂದ
     ಖಂಡಿತ ಒಂದಲ್ಲ ಒಂದು ದಿನ gap = 0 ಆಗಿ ಸಿಗ್ತಾರೆ (cycle ಒಳಗೆ
     ಇದ್ರೆ ಮಾತ್ರ — straight line ಆದ್ರೆ fast ಮೊದಲೇ None ಗೆ ಹೋಗುತ್ತೆ)

  💡 Interview ನಲ್ಲಿ ಹೇಗೆ ಮಾತಾಡಬೇಕು:
  →  "First approach: a HashSet of visited nodes — if we ever
      revisit a node, there's a cycle. O(n) space."
  →  "Optimal: Floyd's slow/fast pointers. If there's a cycle,
      fast eventually laps slow and they meet. If fast hits
      None, there's no cycle. O(1) space."

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🏷️ SECTION 3 — TECHNIQUE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Primary   : Floyd's Cycle Detection — Slow/Fast Pointers (O(1) space)
  Secondary : HashSet of Visited Nodes (O(n) space)

  WHY Slow/Fast over HashSet?
  → The hashset approach is the natural first thought — track
    what's been seen, flag a repeat. But it needs O(n) extra
    space. Two pointers moving at different speeds (1 step vs 2
    steps) achieve the same detection with ZERO extra memory: if
    a cycle exists, the gap between them shrinks by 1 every
    iteration and they are guaranteed to collide; if no cycle
    exists, the fast pointer simply reaches the end first.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 💡 SECTION 4 — INTUITION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  The key insight: picture two runners on a track, one running
  twice as fast as the other. On a straight path (no cycle), the
  faster runner simply finishes first and there's no "meeting."
  But on a LOOP, the faster runner eventually catches up to and
  laps the slower one from behind — they're guaranteed to occupy
  the same spot at some point, because the gap between them
  closes by exactly one step every iteration. So: if the fast
  pointer ever lands on the same node as the slow pointer,
  there's a cycle. If the fast pointer instead falls off the end
  (hits None), there's no cycle.

  The journey from brute to optimal:
    Brute thought   →  Remember every node visited in a hashset;
                       a repeat means a cycle
    Problem with it →  O(n) extra space for the hashset
    Better question →  "Can two pointers moving at different
                       speeds detect a loop without remembering
                       anything?"
    Insight         →  Yes — a faster pointer must eventually lap
                       a slower one if and only if they're on a
                       cycle
    Optimal         →  One O(n) pass with slow (1 step) and fast
                       (2 steps) pointers, O(1) extra space

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🐢 SECTION 5 — APPROACH 1 — BRUTE FORCE (HashSet of Visited Nodes)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    Walk the list one node at a time, adding each node to a
    set. If a node is ever encountered that's already in the
    set, a cycle exists. If the traversal reaches None first,
    there's no cycle.

  Pseudocode:
    step 1: seen = set()
    step 2: curr = head
    step 3: while curr:
    step 4:   if curr in seen: return True
    step 5:   seen.add(curr)
    step 6:   curr = curr.next
    step 7: return False

  Time  : O(n)  →  Why: each node is visited at most once before
                        either finding a repeat or hitting None
  Space : O(n)  →  Why: the set holds a reference to every
                        distinct node visited

  ಇದು ಯಾಕೆ ಸಾಕಾಗಲ್ಲ?
    → Correct and O(n) time, but uses O(n) extra space — Floyd's
      algorithm detects the exact same thing with O(1) space.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🚀 SECTION 6 — OPTIMAL (Floyd's Cycle Detection, Slow/Fast Pointers)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    Use two pointers starting at head: slow moves one step at a
    time, fast moves two steps at a time. If fast (or fast.next)
    reaches None, there's no cycle — return False. If slow and
    fast ever point to the same node, a cycle exists — return
    True.

  Key steps:
    1. slow = fast = head
    2. while fast and fast.next:
    3.     slow = slow.next
    4.     fast = fast.next.next
    5.     if slow is fast: return True
    6. return False

  ಕನ್ನಡದಲ್ಲಿ ಒಂದು ಸಲ ಹೇಳಿ:
    → "slow pointer ಅನ್ನ 1 step, fast pointer ಅನ್ನ 2 step ಅಂತ
       ಒಟ್ಟಿಗೆ ಮುಂದೆ ಸಾಗಿಸು. ಎಲ್ಲಾದ್ರೂ ಇಬ್ಬರೂ ಒಂದೇ node ಗೆ
       ಸಿಕ್ಕಿದ್ರೆ cycle ಇದೆ ಅಂತ ಹೇಳು. fast ಯಾವಾಗಲಾದ್ರೂ None
       ಗೆ ಹೋದ್ರೆ cycle ಇಲ್ಲ ಅಂತ ಹೇಳು!"

  Time  : O(n)  →  Why: in the worst case, fast travels at most
                        twice around the cycle before meeting
                        slow
  Space : O(1)  →  Why: only two pointer variables, no hashset
                        or extra data structure

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🔍 SECTION 7 — DRY RUN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Input: head = [3,2,0,-4], tail (-4) connects back to node
         valued 2 (list: 3→2→0→-4→(back to 2))

  Start: slow = 3, fast = 3

  Iteration 1:
    slow = slow.next = 2
    fast = fast.next.next = 0
    slow (2) is fast (0)? No

  Iteration 2:
    slow = slow.next = 0
    fast = fast.next.next = 2  (fast: 0 → -4 → 2)
    slow (0) is fast (2)? No

  Iteration 3:
    slow = slow.next = -4
    fast = fast.next.next = 0  (fast: 2 → 0 → -4, then 2 steps
                                 more lands back on 0)
    slow (-4) is fast (0)? No

  Iteration 4:
    slow = slow.next = 2
    fast = fast.next.next = 2
    slow (2) is fast (2)? YES → return True

  Output: True ✓ matches expected

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 ⚠️ SECTION 8 — EDGE CASES — ಇವನ್ನ ಮರೆಯಬೇಡ!
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  ✓ Empty list (None)?            →  loop condition fails
                                      immediately, return False
  ✓ Single node, no self-loop?    →  fast.next is None right
                                      away, return False
  ✓ Single node, self-loop
    (node.next == node)?          →  fast catches slow on the
                                      very first iteration,
                                      return True
  ✓ Two nodes, cycle at head?     →  fast laps around quickly
                                      and meets slow, return True
  ✓ Long list, no cycle at all?   →  fast reaches None (or
                                      fast.next is None) after
                                      traversing the full list,
                                      return False
  ✓ Entire list is one big cycle
    (tail points back to head)?   →  handled identically — slow
                                      and fast always eventually
                                      meet somewhere in the loop

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📊 SECTION 9 — COMPLEXITY SUMMARY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                              Time    Space
  Brute (HashSet)              O(n)    O(n)
  Floyd's Slow/Fast             O(n)    O(1)   ← use this ✅

  Time yaake O(n)?  → Fast travels at most 2x the cycle length
                       plus the tail length before meeting slow
                       or hitting None
  Space yaake O(1)? → Just two pointer variables — no hashset
                       or extra storage regardless of list size

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🎯 SECTION 10 — PATTERN LEARNED — ಇದರಿಂದ ಕಲಿತದ್ದು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Pattern Name: Floyd's Cycle Detection (Tortoise and Hare)

  Ee pattern yaavaaga use maadabeeku?
  → Any "does this structure loop back on itself" question on a
     linked list, or any implicit sequence defined by a "next"
     function (array-as-graph, repeated function application)
  → Base case for the two-phase extension that finds the EXACT
     cycle start (see Linked List Cycle II #142)

  Idee pattern beere problemsalli kaanisatte:
  → Linked List Cycle II #142 (same slow/fast core, PLUS a
     second phase to locate the exact start node)
  → Happy Number (LC #202) — repeatedly applying digit-square-sum
     is an implicit "linked list," and slow/fast detects whether
     it cycles instead of reaching 1
  → Find the Duplicate Number (LC #287) — array values as
     "next pointers" form an implicit cycle to detect

  Next time intaha problem bandre naanu modalu idannu think maadtene:
  → "List/sequence loop aaguttilla antha confirm madabekagidre,
     HashSet bedi — slow (1 step) fast (2 step) pointer odhsi,
     avaru sigidre cycle ide, fast None ge hogidre cycle illa —
     O(1) space!"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🗣️ SECTION 11 — INTERVIEWALLI HEGE EXPLAIN MAADABEEKU
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  1. Understand:
     "Determine whether a linked list has a cycle — just
      True/False, O(1) extra space required."

  2. Brute force:
     "Track visited nodes in a hashset — a repeated node means
      a cycle. O(n) time, O(n) space."

  3. Optimize:
     "Floyd's slow/fast pointers: slow moves 1 step, fast moves
      2 steps. If they ever meet, there's a cycle. If fast falls
      off the end, there isn't."

  4. Code:
     "slow = fast = head. While fast and fast.next exist: advance
      slow by 1, fast by 2; if slow is fast, return True. If the
      loop exits, return False."

  5. Complexity:
     "Time O(n) — fast traverses at most a small constant
      multiple of the list. Space O(1) — only two pointers."

  Mukhya: whenever a structure is traversed via 'next' pointers
          and might loop back on itself, slow/fast pointers
          detect that in O(1) space — no need to remember
          anything you've already visited!
"""


# ─── Linked List Node Definition (with optional self-reference) ──
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# ─── Helper: build a list, optionally wiring a cycle at pos ───────
def build(values, pos=-1):
    if not values:
        return None

    nodes = [ListNode(v) for v in values]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]

    if pos != -1:
        nodes[-1].next = nodes[pos]

    return nodes[0]


# ═══════════════════════════════════════════════════════════════════
# BRUTE FORCE — O(n) Time | O(n) Space (HashSet of visited nodes)
# ═══════════════════════════════════════════════════════════════════
def has_cycle_brute(head):
    """
    Idu modala aaloochane — visited nodes anna set ge haaki,
    agle idro node sikre, cycle ide anta helu
    """
    seen = set()
    curr = head
    while curr:
        if curr in seen:
            return True
        seen.add(curr)
        curr = curr.next
    return False


# ═══════════════════════════════════════════════════════════════════
# OPTIMAL — O(n) Time | O(1) Space (Floyd's slow/fast pointers)
# ═══════════════════════════════════════════════════════════════════
def has_cycle(head):
    """
    Idu final answer — slow (1 step) fast (2 step) pointer
    odhsi, avaru ondaagi sikidre cycle ide, fast None ge
    hogidre cycle illa
    """
    slow = fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            return True

    return False


# ═══════════════════════════════════════════════════════════════════
# TEST CASES
# ═══════════════════════════════════════════════════════════════════
if __name__ == "__main__":
    # Test 1 — Basic (LeetCode example 1: cycle mid-list)
    head = build([3, 2, 0, -4], pos=1)
    assert has_cycle(head) is True

    # Test 2 — Cycle at head (LeetCode example 2)
    head = build([1, 2], pos=0)
    assert has_cycle(head) is True

    # Test 3 — No cycle (LeetCode example 3)
    head = build([1], pos=-1)
    assert has_cycle(head) is False

    # Test 4 — Empty list
    assert has_cycle(None) is False

    # Test 5 — Single node with self-loop
    head = build([1], pos=0)
    assert has_cycle(head) is True

    # Test 6 — Entire list is the cycle (tail connects to head)
    head = build([1, 2, 3, 4], pos=0)
    assert has_cycle(head) is True

    # Test 7 — Longer list, no cycle
    head = build([1, 2, 3, 4, 5], pos=-1)
    assert has_cycle(head) is False

    # Test 8 — Cycle starts near the end
    head = build([1, 2, 3, 4, 5], pos=3)
    assert has_cycle(head) is True

    # Cross-check: brute force must agree on all of the above
    head = build([3, 2, 0, -4], pos=1)
    assert has_cycle_brute(head) is True

    head = build([1, 2], pos=0)
    assert has_cycle_brute(head) is True

    head = build([1], pos=-1)
    assert has_cycle_brute(head) is False

    assert has_cycle_brute(None) is False

    head = build([1], pos=0)
    assert has_cycle_brute(head) is True

    head = build([1, 2, 3, 4], pos=0)
    assert has_cycle_brute(head) is True

    head = build([1, 2, 3, 4, 5], pos=-1)
    assert has_cycle_brute(head) is False

    head = build([1, 2, 3, 4, 5], pos=3)
    assert has_cycle_brute(head) is True

    print("All tests passed!")
