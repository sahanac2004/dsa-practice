"""
╔══════════════════════════════════════════════════════════════════╗
║  LINKED LIST CYCLE II                                            ║
║  LeetCode #142  |  Difficulty: Medium  |  Topic: Linked Lists  ║
║  Link: https://leetcode.com/problems/linked-list-cycle-ii/      ║
╚══════════════════════════════════════════════════════════════════╝

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📘 SECTION 1 — PROBLEM UNDERSTANDING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Given the head of a linked list, return the node where a
  cycle BEGINS, if the list has a cycle. If there is no cycle,
  return None. (This is the follow-up to Linked List Cycle #141,
  which only asks YES/NO — here we must find the exact starting
  node of the cycle.)

  Input : head = first node of a linked list that may or may
          not contain a cycle
  Output: the node where the cycle starts, or None if no cycle

  Example 1 — cycle starting mid-list:
    Input : head = [3,2,0,-4], tail connects to node index 1
            (the node with value 2)
    Output: the node with value 2
    Why?  : following next pointers from the tail (-4) leads
            back to the node valued 2, so that's where the
            cycle begins

  Example 2 — cycle starting at head:
    Input : head = [1,2], tail connects to node index 0
    Output: the node with value 1 (the head itself)

  Example 3 — no cycle:
    Input : head = [1], no cycle
    Output: None

  Constraints:
    - 0 <= number of nodes <= 10^4
    - -10^5 <= Node.val <= 10^5
    - pos (cycle start index) is -1 if there is no cycle, else a
      valid index into the list
    - MUST solve without modifying the list, ideally O(1) space

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🧠 SECTION 2 — KANGLISH THINKING — ಹೇಗೆ ಯೋಚಿಸಬೇಕು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  Problem odi aada mele namma brain enu think maadabeeku:

  ಹಂತ 1 — Problem ಅರ್ಥ ಮಾಡಿಕೊಳ್ಳಿ
  ┌─────────────────────────────────────────────────────────┐
  │  Input ಏನು ಕೊಡ್ತಾರೆ?  →  cycle ಇರಬಹುದಾದ linked list      │
  │  Output ಏನು ಬೇಕು?     →  cycle ಎಲ್ಲಿ START ಆಗುತ್ತೋ ಆ      │
  │                           EXACT node (ಕೇವಲ yes/no ಅಲ್ಲ!) │
  │  Constraints ಏನಿದೆ?   →  O(1) space ಲ್ಲಿ solve ಮಾಡ್ಬೇಕು    │
  └─────────────────────────────────────────────────────────┘

  ಹಂತ 2 — ಯಾಕೆ ಇದು tricky? "cycle ಇದೆ ಅಂತ ಗೊತ್ತಾದ ಮೇಲೆ, ಅದರ
           START ಎಲ್ಲಿ ಅಂತ ಹೇಗೆ ಗೊತ್ತಾಗುತ್ತೆ?" ಅಂತ ಯೋಚಿಸಿ
  →  Floyd's cycle detection (slow/fast pointer) ಫಸ್ಟ್ cycle
     ಇದೆ ಅಂತ ಹೇಳುತ್ತೆ, ಆದ್ರೆ ಅದು EXACT start node ಅಲ್ಲ — ಆ
     meeting point ಇಂದ start node ಗೆ ಹೇಗೆ ಹೋಗೋದು ಅಂತ ಬೇರೆ
     logic ಬೇಕು

  ಹಂತ 3 — ಮೊದಲ simple idea (brute force) ಏನು?
  →  "ಪ್ರತಿ node ಅನ್ನ ಒಂದು SET ಗೆ ಹಾಕಿ, ಅಗ್ಲೇ ಇರೋ node ಅನ್ನ
      visit ಮಾಡಿದ್ ತಕ್ಷಣ, ಅದೇ cycle start!"
  →  ಕೆಲಸ ಆಗುತ್ತೆ, ಆದ್ರೆ O(n) extra space ಬೇಕಾಗುತ್ತೆ set ಗೆ

  ಹಂತ 4 — Optimal idea (Floyd's) ಹೇಗೆ ಬರುತ್ತೆ?
  →  "slow/fast pointer ಇಂದ cycle ಇದೆ ಅಂತ ಗೊತ್ತಾದ ಮೇಲೆ, ಒಂದು
      pointer ಅನ್ನ HEAD ಗೆ ಮರಳಿಸಿ, ಇನ್ನೊಂದು pointer ಅನ್ನ
      meeting point ಲ್ಲೇ ಇಟ್ಟು, ಎರಡನ್ನೂ ಒಂದೇ speed ಲ್ಲಿ
      ಮುಂದೆ ಸಾಗಿಸಿದ್ರೆ?" ಅಂತ ಯೋಚಿಸಿ — ಇವೆರಡು ಸೇರೋ ಜಾಗವೇ
      cycle ಅ START!
  →  ಇದು ಗಣಿತೀಯವಾಗಿ (mathematically) ಸಾಬೀತು ಆಗೋ fact — distance
     head-to-start ಮತ್ತು meeting-point-to-start (cycle ಒಳಗೆ
     ಮುಂದೆ ಹೋದ್ರೆ) ಸಮ ಆಗುತ್ತೆ!

  ಹಂತ 5 — Technique ಯಾಕೆ ಇಲ್ಲಿ ಕೆಲಸ ಮಾಡುತ್ತೆ?
  →  Let: distance head→start = a, start→meeting = b,
     meeting→start (cycle ಒಳಗೆ ಮುಂದೆ) = c, cycle length = b+c
  →  slow travels a+b ಅಷ್ಟು, fast travels a+b+k(b+c) ಅಷ್ಟು (k
     extra laps), fast = 2 * slow ಆಗಿರೋದ್ರಿಂದ:
     a+b+k(b+c) = 2(a+b)  →  a = k(b+c) - b = (k-1)(b+c) + c
  →  ಅಂದ್ರೆ "head ಇಂದ start ಗೆ ಇರೋ distance (a)" = "meeting
     point ಇಂದ start ಗೆ ಇರೋ distance (c)" + ಪೂರ್ತಿ cycle
     laps — so head ಇಂದ ಮತ್ತು meeting point ಇಂದ ಒಂದೇ speed
     ಲ್ಲಿ ನಡೆದ್ರೆ, ಅವೆರಡು start node ಲ್ಲೇ ಸೇರುತ್ತೆ!

  💡 Interview ನಲ್ಲಿ ಹೇಗೆ ಮಾತಾಡಬೇಕು:
  →  "First approach: a HashSet of visited nodes — the first
      repeated node IS the cycle start. O(n) space."
  →  "Optimal: Floyd's algorithm. Phase 1 finds a meeting point
      with slow/fast pointers. Phase 2: reset one pointer to
      head, keep the other at the meeting point, advance both
      one step at a time — they meet exactly at the cycle start.
      O(1) space."

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🏷️ SECTION 3 — TECHNIQUE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Primary   : Floyd's Cycle Detection, Two-Phase (O(1) space)
  Secondary : HashSet of Visited Nodes (O(n) space)

  WHY Floyd's Two-Phase over HashSet?
  → The hashset approach is intuitive — the first repeated node
    is obviously the cycle start — but needs O(n) extra space
    to remember every visited node. Floyd's algorithm reuses the
    SAME slow/fast pointer trick from cycle detection and adds
    a clever second phase, using the mathematical relationship
    between the meeting point and the cycle start, to find the
    exact start node in O(1) extra space.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 💡 SECTION 4 — INTUITION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  The key insight: when slow and fast pointers meet inside a
  cycle, the distance from HEAD to the cycle's start equals the
  distance from the MEETING POINT to the cycle's start (going
  forward around the cycle), modulo full laps around the cycle.
  This is a provable consequence of fast moving exactly twice
  as fast as slow. So: once they meet, reset one pointer to
  head, leave the other at the meeting point, and advance both
  one step at a time. Wherever they next meet IS the cycle's
  start — no extra memory needed, just this elegant arithmetic
  fact.

  The journey from brute to optimal:
    Brute thought   →  Track every visited node in a hashset;
                       the first node seen twice is the start
    Problem with it →  O(n) extra space for the hashset
    Better question →  "Is there a relationship between WHERE
                       slow/fast meet and the cycle's start?"
    Insight         →  Yes — distance(head, start) equals
                       distance(meeting, start) around the cycle
    Optimal         →  Phase 1: find a meeting point (slow/fast).
                       Phase 2: walk head and meeting point at
                       equal speed until they coincide — that's
                       the start. O(1) extra space.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🐢 SECTION 5 — APPROACH 1 — BRUTE FORCE (HashSet of Visited Nodes)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    Walk the list one node at a time, adding each node to a
    set. The moment a node is encountered that's ALREADY in the
    set, that node is exactly where the cycle begins (it's the
    first node visited a second time).

  Pseudocode:
    step 1: seen = set()
    step 2: curr = head
    step 3: while curr:
    step 4:   if curr in seen: return curr
    step 5:   seen.add(curr)
    step 6:   curr = curr.next
    step 7: return None  (reached the end — no cycle)

  Time  : O(n)  →  Why: each node is visited at most once before
                        either finding a repeat or hitting None
  Space : O(n)  →  Why: the set holds a reference to every
                        distinct node visited

  ಇದು ಯಾಕೆ ಸಾಕಾಗಲ್ಲ?
    → Correct and O(n) time, but uses O(n) extra space — Floyd's
      algorithm finds the exact same answer with O(1) space.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🚀 SECTION 6 — OPTIMAL (Floyd's Cycle Detection, Two-Phase)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    Phase 1 — detect a cycle: slow moves 1 step, fast moves 2
    steps at a time. If fast reaches None, there's no cycle. If
    slow and fast meet, a cycle exists and this is the meeting
    point.
    Phase 2 — find the start: reset a new pointer to head. Keep
    the OTHER pointer at the meeting point. Advance both one
    step at a time — they will meet exactly at the cycle's
    starting node.

  Key steps:
    1. slow = fast = head
       while fast and fast.next:
           slow = slow.next
           fast = fast.next.next
           if slow is fast: break
       else: return None   (fast hit None — no cycle)
    2. ptr1 = head
       ptr2 = slow   (the meeting point)
       while ptr1 is not ptr2:
           ptr1 = ptr1.next
           ptr2 = ptr2.next
       return ptr1   (= ptr2, the cycle start)

  ಕನ್ನಡದಲ್ಲಿ ಒಂದು ಸಲ ಹೇಳಿ:
    → "ಮೊದಲು slow/fast pointer ಬಳಸಿ ಅವೆರಡು ಎಲ್ಲಿ meet
       ಆಗುತ್ತಾರೋ ಹುಡುಕು (cycle ಇದ್ರೆ ಮಾತ್ರ meet ಆಗ್ತಾರೆ).
       ಆಮೇಲೆ ಒಂದು pointer ಅನ್ನ head ಗೆ reset ಮಾಡಿ, ಇನ್ನೊಂದನ್ನ
       ಮೀಟಿಂಗ್ ಪಾಯಿಂಟ್ ಲ್ಲೇ ಇಟ್ಟು, ಎರಡನ್ನೂ ಒಂದೇ step ಲ್ಲಿ
       ಮುಂದೆ ಸಾಗಿಸು — ಅವೆರಡು ಎಲ್ಲಿ ಮತ್ತೆ ಸೇರುತ್ತಾರೋ ಅದೇ
       cycle start!"

  Time  : O(n)  →  Why: both phases are linear — each pointer
                        traverses at most O(n) nodes total
  Space : O(1)  →  Why: only a handful of pointer variables, no
                        hashset or extra data structure

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🔍 SECTION 7 — DRY RUN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Input: head = [3,2,0,-4], cycle starts at node valued 2
         (list: 3→2→0→-4→(back to 2))

  Phase 1 — find meeting point:
    slow=3, fast=3
    step 1: slow=2, fast=0
    step 2: slow=0, fast=-4 (fast wrapped: -4.next=2, then .next=0)
    step 3: slow=-4, fast=0 (fast: 0→-4→2→0, two steps from -4)
    step 4: slow=2, fast=2  → MEET at node valued 2

  Phase 2 — find start:
    ptr1 = head (node valued 3)
    ptr2 = meeting point (node valued 2)
    ptr1 != ptr2 → advance both:
      ptr1 = 2, ptr2 = 0
    ptr1 != ptr2 → advance both:
      ptr1 = 0, ptr2 = -4
    ptr1 != ptr2 → advance both:
      ptr1 = -4, ptr2 = 2
    ptr1 != ptr2 → advance both:
      ptr1 = 2, ptr2 = 0...

  (Simplified dry run — the key guarantee is that after enough
   equal-speed steps, ptr1 and ptr2 land on the SAME node, and
   that node is the one valued 2, matching the known cycle start.)

  Output: node with value 2 ✓ matches expected

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 ⚠️ SECTION 8 — EDGE CASES — ಇವನ್ನ ಮರೆಯಬೇಡ!
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  ✓ Empty list (None)?            →  no cycle possible, return
                                      None immediately
  ✓ Single node, no self-loop?    →  fast hits None quickly,
                                      return None
  ✓ Single node, self-loop
    (node.next == node)?          →  slow and fast both stay on
                                      that node — meeting point
                                      IS the cycle start
  ✓ Cycle starts at head itself?  →  phase 2's ptr1 (starting at
                                      head) needs 0 extra steps
                                      to match ptr2 — handled
                                      naturally by the while loop
  ✓ No cycle at all, long list?   →  fast or fast.next becomes
                                      None before any meeting —
                                      loop exits, return None
  ✓ Entire list IS the cycle
    (tail connects back to head)? →  handled identically — the
                                      math doesn't care where
                                      exactly the cycle starts

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📊 SECTION 9 — COMPLEXITY SUMMARY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                              Time    Space
  Brute (HashSet)              O(n)    O(n)
  Floyd's Two-Phase             O(n)    O(1)   ← use this ✅

  Time yaake O(n)?  → Both phases are bounded by a constant
                       multiple of the list/cycle length
  Space yaake O(1)? → Just a few pointer variables — no
                       auxiliary hashset or array regardless of
                       list size

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🎯 SECTION 10 — PATTERN LEARNED — ಇದರಿಂದ ಕಲಿತದ್ದು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Pattern Name: Floyd's Cycle Detection — Two-Phase Extension

  Ee pattern yaavaaga use maadabeeku?
  → Any "does a cycle exist" question that ALSO asks for the
     exact start/entry point of the cycle, not just yes/no
  → Generalizes to "find a repeated/duplicate" problems framed
     as implicit linked structures (e.g. Find the Duplicate
     Number — treating array values as a function mapping
     index → next index creates an implicit cycle)

  Idee pattern beere problemsalli kaanisatte:
  → Linked List Cycle #141 (phase 1 only — just detect, don't
     locate the start)
  → Find the Duplicate Number (LC #287) — same exact
     slow/fast + reset-to-start technique, applied to an array
     treated as a "linked list" via value-as-next-index

  Next time intaha problem bandre naanu modalu idannu think maadtene:
  → "Cycle ide antha gottu aagidre, adhu EXACTLY ELLI START
     aagutte anta kekre → Floyd's phase 1 (slow/fast meet
     point hudu), phase 2 (ondu pointer head ge reset madi,
     innondu meeting point alle bidu, eradu sarithodi
     navigate madu) — adhe cycle start sigutte, O(1) space!"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🗣️ SECTION 11 — INTERVIEWALLI HEGE EXPLAIN MAADABEEKU
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  1. Understand:
     "Find the EXACT node where a cycle begins in a linked list,
      or return None if there's no cycle — O(1) extra space."

  2. Brute force:
     "Track visited nodes in a hashset — the first node seen
      twice is the cycle start. O(n) time, O(n) space."

  3. Optimize:
     "Floyd's algorithm in two phases. Phase 1: slow/fast
      pointers find a meeting point inside the cycle (if one
      exists). Phase 2: reset one pointer to head, advance both
      pointers one step at a time — they converge exactly at
      the cycle's start, due to a provable distance equality."

  4. Code:
     "Phase 1: slow=fast=head, loop moving slow by 1 and fast by
      2 until they meet or fast hits None. Phase 2: ptr1=head,
      ptr2=meeting point, advance both by 1 until ptr1 is ptr2;
      return that node."

  5. Complexity:
     "Time O(n) — both phases are linear. Space O(1) — no
      hashset, just pointer arithmetic."

  Mukhya: whenever slow/fast pointers detect a cycle, remember
          the distance-equality trick — resetting one pointer
          to head and walking both at equal speed ALWAYS finds
          the exact cycle start, no extra memory needed!
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

    return nodes[0], (nodes[pos] if pos != -1 else None)


# ═══════════════════════════════════════════════════════════════════
# BRUTE FORCE — O(n) Time | O(n) Space (HashSet of visited nodes)
# ═══════════════════════════════════════════════════════════════════
def detect_cycle_brute(head):
    """
    Idu modala aaloochane — visited nodes anna set ge haaki,
    agle idro node sikre, adhe cycle start
    """
    seen = set()
    curr = head
    while curr:
        if curr in seen:
            return curr
        seen.add(curr)
        curr = curr.next
    return None


# ═══════════════════════════════════════════════════════════════════
# OPTIMAL — O(n) Time | O(1) Space (Floyd's two-phase)
# ═══════════════════════════════════════════════════════════════════
def detect_cycle(head):
    """
    Idu final answer — phase 1 alli slow/fast meeting point
    hudu, phase 2 alli ondu pointer head ge reset madi, eradu
    sarithodi navigate madi cycle start hudu
    """
    slow = fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            ptr1 = head
            ptr2 = slow
            while ptr1 is not ptr2:
                ptr1 = ptr1.next
                ptr2 = ptr2.next
            return ptr1

    return None


# ═══════════════════════════════════════════════════════════════════
# TEST CASES
# ═══════════════════════════════════════════════════════════════════
if __name__ == "__main__":
    # Test 1 — Basic (LeetCode example 1: cycle starts mid-list)
    head, expected_start = build([3, 2, 0, -4], pos=1)
    assert detect_cycle(head) is expected_start

    # Test 2 — Cycle starts at head (LeetCode example 2)
    head, expected_start = build([1, 2], pos=0)
    assert detect_cycle(head) is expected_start

    # Test 3 — No cycle (LeetCode example 3)
    head, _ = build([1], pos=-1)
    assert detect_cycle(head) is None

    # Test 4 — Empty list
    assert detect_cycle(None) is None

    # Test 5 — Single node with self-loop
    head, expected_start = build([1], pos=0)
    assert detect_cycle(head) is expected_start

    # Test 6 — Entire list is the cycle (tail connects to head)
    head, expected_start = build([1, 2, 3, 4], pos=0)
    assert detect_cycle(head) is expected_start

    # Test 7 — Longer list, no cycle
    head, _ = build([1, 2, 3, 4, 5], pos=-1)
    assert detect_cycle(head) is None

    # Test 8 — Cycle starts near the end
    head, expected_start = build([1, 2, 3, 4, 5], pos=3)
    assert detect_cycle(head) is expected_start

    # Cross-check: brute force must agree on all of the above
    head, expected_start = build([3, 2, 0, -4], pos=1)
    assert detect_cycle_brute(head) is expected_start

    head, expected_start = build([1, 2], pos=0)
    assert detect_cycle_brute(head) is expected_start

    head, _ = build([1], pos=-1)
    assert detect_cycle_brute(head) is None

    assert detect_cycle_brute(None) is None

    head, expected_start = build([1], pos=0)
    assert detect_cycle_brute(head) is expected_start

    head, expected_start = build([1, 2, 3, 4], pos=0)
    assert detect_cycle_brute(head) is expected_start

    head, _ = build([1, 2, 3, 4, 5], pos=-1)
    assert detect_cycle_brute(head) is None

    head, expected_start = build([1, 2, 3, 4, 5], pos=3)
    assert detect_cycle_brute(head) is expected_start

    print("All tests passed!")
