"""
╔══════════════════════════════════════════════════════════════════╗
║  REVERSE NODES IN K-GROUP                                        ║
║  LeetCode #25  |  Difficulty: Hard  |  Topic: Linked Lists     ║
║  Link: https://leetcode.com/problems/                           ║
║        reverse-nodes-in-k-group/                                 ║
╚══════════════════════════════════════════════════════════════════╝

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📘 SECTION 1 — PROBLEM UNDERSTANDING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Given the head of a linked list, reverse the nodes of the
  list in GROUPS of k, and return the modified list. If the
  number of nodes is NOT a multiple of k, the nodes left over
  at the end (fewer than k of them) should remain AS-IS, not
  reversed.

  You may NOT alter the values in the nodes — only the nodes
  themselves may be rewired (next pointers change, values don't).

  Input : head = singly linked list, k = group size
  Output: head of the list with every full group of k nodes
          reversed, leftover tail group (if any) untouched

  Example 1 — basic, exact multiple:
    Input : head = [1,2,3,4,5], k = 2
    Output: [2,1,4,3,5]
    Why?  : groups of 2: (1,2)->(2,1), (3,4)->(4,3), leftover
            (5) alone — stays as-is since it's < k nodes

  Example 2 — k = 3:
    Input : head = [1,2,3,4,5], k = 3
    Output: [3,2,1,4,5]
    Why?  : first group of 3 (1,2,3) reverses to (3,2,1);
            leftover (4,5) has only 2 nodes (< k=3) — stays as-is

  Constraints:
    - 1 <= number of nodes <= 5000
    - 0 <= Node.val <= 1000
    - 1 <= k <= number of nodes
    - Follow-up: can you solve it in O(1) extra memory (not
      counting recursion stack)?

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🧠 SECTION 2 — KANGLISH THINKING — ಹೇಗೆ ಯೋಚಿಸಬೇಕು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  Problem odi aada mele namma brain enu think maadabeeku:

  ಹಂತ 1 — Problem ಅರ್ಥ ಮಾಡಿಕೊಳ್ಳಿ
  ┌─────────────────────────────────────────────────────────┐
  │  Input ಏನು ಕೊಡ್ತಾರೆ?  →  linked list ಮತ್ತು k (group size) │
  │  Output ಏನು ಬೇಕು?     →  ಪ್ರತಿ k-size group reverse,       │
  │                           leftover (< k nodes) as-is       │
  │  Constraints ಏನಿದೆ?   →  values ಬದಲಾಯಿಸ್ಬಾರ್ದು, nodes      │
  │                           ಅನ್ನೇ rewire ಮಾಡ್ಬೇಕು             │
  └─────────────────────────────────────────────────────────┘

  ಹಂತ 2 — ಯಾಕೆ ಇದು tricky? "ಪ್ರತಿ group ಅನ್ನ reverse ಮಾಡಿ, ಆಮೇಲೆ
           ಮುಂದಿನ group ಜೊತೆ ಹೇಗೆ ಜೋಡಿಸೋದು, ಮತ್ತೆ leftover
           ಅನ್ನ ಹೇಗೆ identify ಮಾಡೋದು?" ಅಂತ ಯೋಚಿಸಿ
  →  Reverse Linked List #206 ಅ 3-pointer trick ಗೊತ್ತು, ಆದ್ರೆ
     ಇಲ್ಲಿ "ಪ್ರತಿ k nodes ಗೂ ಪ್ರತ್ಯೇಕ reversal" ಮಾಡ್ಬೇಕು, ಮತ್ತೆ
     "ಈ group ಗೆ k ಇಡೀ nodes ಇದ್ಯಾ, ಇಲ್ಲಾ leftover ಆ" ಅಂತ
     ಮೊದಲೇ ಗೊತ್ತಾಗ್ಬೇಕು (check ಮಾಡ್ಬೇಕು)

  ಹಂತ 3 — ಮೊದಲ simple idea (brute force) ಏನು?
  →  "ಎಲ್ಲಾ values ಅನ್ನ array ಗೆ ಹಾಕಿ, ಪ್ರತಿ k-size chunk ಅನ್ನ
      reverse ಮಾಡಿ (ಪೂರ್ತಿ k ಇರೋ chunks ಮಾತ್ರ), ಮತ್ತೆ list
      ಕಟ್ಟಿದ್ರೆ?"
  →  ಕೆಲಸ ಆಗುತ್ತೆ, ಆದ್ರೆ O(n) extra space ಬೇಕಾಗುತ್ತೆ array ಗೆ

  ಹಂತ 4 — Optimal idea (recursion) ಹೇಗೆ ಬರುತ್ತೆ?
  →  "ಮೊದಲು ಈ group ಗೆ k nodes ಇದ್ಯಾ ಅಂತ check ಮಾಡಿ (ಇಲ್ದಿದ್ರೆ
      as-is return ಮಾಡಿ). ಇದ್ರೆ, ಈ group ಅನ್ನ reverse ಮಾಡಿ,
      ಮುಂದಿನ group ಗೆ recursive call ಮಾಡಿ, ಆ call ಅ result ಅನ್ನ
      ಈ group ಅ (reversed) ಕೊನೆ ಗೆ ಜೋಡಿಸಿದ್ರೆ?" ಅಂತ ಯೋಚಿಸಿ —
      ಪ್ರತಿ group ಪ್ರತ್ಯೇಕವಾಗಿ handle ಆಗುತ್ತೆ, ಮುಂದಿನ groups
      recursion ಅ ಜವಾಬ್ದಾರಿ!

  ಹಂತ 5 — Technique ಯಾಕೆ ಇಲ್ಲಿ ಕೆಲಸ ಮಾಡುತ್ತೆ?
  →  "ಈ group reverse ಮಾಡಿ, ಮುಂದಿನ ಭಾಗ ಅನ್ನ recursively ಅದೇ
     function ಗೆ ಬಿಟ್ಟು ಬಿಡು" ಅನ್ನೋ idea — ಪ್ರತಿ recursion level
     ಕೇವಲ "ಇದೇ group ಅನ್ನ reverse ಮಾಡಿ, ಮುಂದಿನ group ಅ result
     ಗೆ ಜೋಡಿಸೋದು" ಅಷ್ಟೇ ಕೆಲಸ ಮಾಡುತ್ತೆ — base case "k nodes
     ಇಲ್ಲ" ಆದಾಗ ಆ ಭಾಗ ಅನ್ನ as-is ಬಿಟ್ಟು ಬಿಡುತ್ತೆ

  💡 Interview ನಲ್ಲಿ ಹೇಗೆ ಮಾತಾಡಬೇಕು:
  →  "First approach: extract values to an array, reverse each
      full k-sized chunk, rebuild — O(n) time, O(n) space"
  →  "Optimal: recursively — check if k nodes remain; if not,
      return as-is. If yes, reverse this group of k using the
      standard 3-pointer technique, recursively process the
      rest, then connect this group's (now-tail) node to
      whatever the recursive call returns."

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🏷️ SECTION 3 — TECHNIQUE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Primary   : Recursive Group Reversal (check-then-reverse-then-recurse)
  Secondary : Extract to Array + Reverse Full Chunks + Rebuild

  WHY Recursion over Array Extraction?
  → Extracting to an array works but needs O(n) extra space to
    hold values temporarily. Recursion instead treats "reverse
    the WHOLE list in groups of k" as "reverse ONE group of k,
    then recursively solve the exact same problem for everything
    after it" — a clean self-similar reduction that reuses the
    same 3-pointer reversal trick from Reverse Linked List #206,
    just bounded to k nodes, repeated group by group.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 💡 SECTION 4 — INTUITION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  The key insight: "reverse the list in groups of k" is really
  just "reverse the first k nodes, then solve the exact same
  problem again on everything after them." That's a textbook
  recursive reduction. First, check whether k nodes even exist
  from here — if not, this is the leftover tail, return it
  untouched (base case). Otherwise, reverse exactly k nodes
  using the standard 3-pointer technique. After reversing, the
  group's ORIGINAL first node is now its TAIL — connect that
  tail's `next` to whatever the recursive call on the remaining
  list returns. The recursive call's return value becomes the
  "rest of the answer," automatically handling all subsequent
  groups (and the final leftover) the exact same way.

  The journey from brute to optimal:
    Brute thought   →  Extract all values to an array, reverse
                       each full chunk of k values, leave any
                       remainder chunk alone, rebuild the list
    Problem with it →  O(n) extra space for the array
    Better question →  "Can 'reverse in groups of k' be
                       expressed as a smaller version of itself?"
    Insight         →  Reverse one group, then recursively solve
                       the IDENTICAL problem on what remains —
                       connecting the pieces at each level
    Optimal         →  Recursive: check k-nodes-exist (base
                       case), reverse k nodes in place, recurse
                       on the rest, connect — O(n) time, O(n/k)
                       recursion depth (not counting that,
                       O(1) extra pointer space per level)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🐢 SECTION 5 — APPROACH 1 — BRUTE FORCE (Array Chunk Reverse + Rebuild)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    Walk the list once, collecting all values into an array.
    Walk the array in chunks of size k; if a chunk has EXACTLY k
    elements, reverse that chunk in place within the array;
    otherwise (fewer than k remain), leave it untouched. Rebuild
    a fresh linked list from the modified array.

  Pseudocode:
    step 1: values = [all node values, in order]
    step 2: for i in range(0, len(values), k):
    step 3:     if i + k <= len(values):
    step 4:         values[i:i+k] = reversed(values[i:i+k])
    step 5: build and return a new linked list from values

  Time  : O(n)  →  Why: a constant number of linear scans over
                        the values
  Space : O(n)  →  Why: stores all values in an intermediate
                        array before rebuilding

  ಇದು ಯಾಕೆ ಸಾಕಾಗಲ್ಲ?
    → Correct and O(n) time, but uses O(n) extra space — the
      recursive approach reuses the original nodes directly,
      with only pointer rewiring (plus the recursion stack).

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🚀 SECTION 6 — OPTIMAL (Recursive Group Reversal)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    Base case: walk k steps ahead from `head`. If fewer than k
    nodes exist (hit None before completing k steps), return
    head as-is (leftover group, untouched).
    Recursive case: reverse exactly k nodes using the standard
    3-pointer technique (prev, curr, next_node). After the
    reversal loop, `head` (the group's original first node) is
    now the group's TAIL — set head.next to the result of
    recursively calling this same function on `curr` (the node
    right after this group). Return `prev` (the new head of
    this now-reversed group).

  Key steps:
    1. def reverse_k_group(head, k):
    2.     node = head
    3.     for _ in range(k):
    4.         if not node: return head   # fewer than k left
    5.         node = node.next
    6.     prev, curr = None, head
    7.     for _ in range(k):
    8.         next_node = curr.next
    9.         curr.next = prev
    10.        prev = curr
    11.        curr = next_node
    12.    head.next = reverse_k_group(curr, k)
    13.    return prev

  ಕನ್ನಡದಲ್ಲಿ ಒಂದು ಸಲ ಹೇಳಿ:
    → "ಮೊದಲು k steps ಮುಂದೆ ಹೋಗಿ ಈ group ಗೆ k nodes ಇದ್ಯಾ ಅಂತ
       check ಮಾಡು — ಇಲ್ದಿದ್ರೆ head ಅನ್ನೇ as-is return ಮಾಡು.
       ಇದ್ರೆ, standard 3-pointer reversal ಬಳಸಿ k nodes reverse
       ಮಾಡು. ಈಗ (ಮೊದಲಿನ) head ಅನ್ನೇ (reversed group ಅ TAIL)
       ಅದರ next ಅನ್ನ ಮುಂದಿನ group ಗೆ recursive call ಮಾಡಿ ಬಂದ
       result ಗೆ ಜೋಡಿಸು. ಹೊಸ head (prev) ಅನ್ನ return ಮಾಡು!"

  Time  : O(n)  →  Why: each node is visited a constant number
                        of times across the k-check and reversal
                        loops, across all recursive calls combined
  Space : O(n/k) →  Why: recursion depth equals the number of
                        groups (n/k levels of call stack); each
                        level itself uses O(1) extra pointers

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🔍 SECTION 7 — DRY RUN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Input: head = [1,2,3,4,5], k = 2

  Call reverse_k_group(head=1, k=2):
    Check k nodes exist: node=1 -> node=2 -> node=3 (2 steps
    done, node=3 exists) -> k nodes DO exist, proceed

    Reversal loop (k=2 iterations), head=1, prev=None, curr=1:
      iter 1: next_node=2, 1.next=None, prev=1, curr=2
      iter 2: next_node=3, 2.next=1, prev=2, curr=3

    After loop: prev=node(2) [new head of this group],
                curr=node(3) [next group's start]
                head (original, node 1) is now the group's TAIL

    head.next = reverse_k_group(curr=3, k=2)  <- recurse!

    Inner call reverse_k_group(head=3, k=2):
      Check k nodes exist: node=3 -> node=4 -> node=5 (2 steps
      done, node=5 exists) -> k nodes DO exist, proceed

      Reversal loop, head=3, prev=None, curr=3:
        iter 1: next_node=4, 3.next=None, prev=3, curr=4
        iter 2: next_node=5, 4.next=3, prev=4, curr=5

      After loop: prev=node(4), curr=node(5)
      head(3).next = reverse_k_group(curr=5, k=2)  <- recurse!

      Innermost call reverse_k_group(head=5, k=2):
        Check k nodes exist: node=5 -> node=None (only 1 step
        possible before hitting None) -> k nodes DO NOT exist
        -> return head (= node 5) AS-IS

      Back in middle call: head(3).next = node(5)
      Chain so far: 4 -> 3 -> 5
      return prev = node(4)

    Back in outer call: head(1).next = node(4)
    Chain: 2 -> 1 -> 4 -> 3 -> 5
    return prev = node(2)

  Output: [2,1,4,3,5] ✓ matches expected

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 ⚠️ SECTION 8 — EDGE CASES — ಇವನ್ನ ಮರೆಯಬೇಡ!
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  ✓ k = 1?                        →  every "group" is a single
                                      node — reversing it is a
                                      no-op, list unchanged
  ✓ k = total length (reverse
    the entire list as one group)? →  the whole list IS exactly
                                      one full group — behaves
                                      identically to Reverse
                                      Linked List #206
  ✓ Length is an exact multiple
    of k?                          →  every group gets reversed;
                                      the final recursive call's
                                      base case sees node=None
                                      cleanly (0 leftover)
  ✓ Length is NOT a multiple of k
    (leftover group at the end)?   →  that final group's base
                                      case check fails to find k
                                      nodes, so it's returned
                                      completely untouched
  ✓ Single node, any k >= 1?      →  k=1 is a no-op; k>1 means
                                      fewer than k nodes exist,
                                      so the single node is
                                      returned as-is

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📊 SECTION 9 — COMPLEXITY SUMMARY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                              Time    Space
  Brute (array chunk reverse)  O(n)    O(n)
  Recursive group reversal      O(n)    O(n/k)   ← use this ✅

  Time yaake O(n)?   → Across all recursive calls combined,
                        each node is touched a constant number
                        of times (once in a k-check, once in a
                        reversal loop)
  Space yaake O(n/k)? → Recursion depth equals the number of
                        groups; each stack frame itself uses
                        only O(1) extra pointers

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🎯 SECTION 10 — PATTERN LEARNED — ಇದರಿಂದ ಕಲಿತದ್ದು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Pattern Name: Bounded Reversal + Recursive Self-Reduction

  Ee pattern yaavaaga use maadabeeku?
  → Any "repeat the same transformation on fixed-size chunks of
     a linked list" problem — reverse-in-groups, process-in-
     batches, etc. — recursion naturally expresses "do this
     chunk, then recursively do the identical thing to the rest"
  → Always pair a "does enough remain?" base-case check with the
     bounded in-place operation, so the leftover tail is
     automatically handled correctly

  Idee pattern beere problemsalli kaanisatte:
  → Reverse Linked List #206 (the base 3-pointer reversal
     technique, here just bounded to k nodes and repeated)
  → Reverse Linked List II #92 (a SINGLE bounded reversal with
     explicit before/after reconnection — contrast with this
     problem's recursive, repeated-groups version)
  → Swap Nodes in Pairs #24 (the k=2 special case of this exact
     recursive pattern)

  Next time intaha problem bandre naanu modalu idannu think maadtene:
  → "List na FIXED-SIZE chunks alli repeat aagi process
     madabekagidre (reverse, group-wise transform) → recursion
     use madu: 'ee chunk madi mugisi, remaining ge SAME problem
     anna recursively bidu' anta think madu — base case 'chunk
     size satisfy aagatva' anta check madokke mathra nenapittukko!"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🗣️ SECTION 11 — INTERVIEWALLI HEGE EXPLAIN MAADABEEKU
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  1. Understand:
     "Reverse the linked list in groups of k nodes. Any leftover
      group with fewer than k nodes at the end stays as-is."

  2. Brute force:
     "Extract values to an array, reverse each full k-sized
      chunk, leave a remainder chunk alone, rebuild. O(n) time,
      O(n) space."

  3. Optimize:
     "Recursively: check if k nodes exist from here — if not,
      return as-is (base case). Otherwise, reverse exactly k
      nodes with the standard 3-pointer technique, recursively
      solve the identical problem on the rest, then connect this
      group's original head (now its tail) to that result."

  4. Code:
     "Base case loop: walk k steps, return head early if None is
      hit. Reversal loop: standard prev/curr/next_node dance for
      k iterations. head.next = recursive call on curr. Return
      prev."

  5. Complexity:
     "Time O(n) — each node processed a constant number of times
      overall. Space O(n/k) for the recursion stack (one frame
      per group)."

  Mukhya: 'repeat this transformation on fixed-size chunks' is
          almost always a clean recursive self-reduction — solve
          ONE chunk, then recursively hand off the identical
          problem on what remains, with a 'not enough left'
          check as the base case!
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
# BRUTE FORCE — O(n) Time | O(n) Space (array chunk reverse + rebuild)
# ═══════════════════════════════════════════════════════════════════
def reverse_k_group_brute(head, k):
    """
    Idu modala aaloochane — values array ge haaki, prathi full
    k-size chunk reverse madi, leftover anna bidu, hosa list build madu
    """
    values = to_list(head)
    n = len(values)

    for i in range(0, n, k):
        if i + k <= n:
            values[i:i + k] = reversed(values[i:i + k])

    return build(values)


# ═══════════════════════════════════════════════════════════════════
# OPTIMAL — O(n) Time | O(n/k) Space (recursive group reversal)
# ═══════════════════════════════════════════════════════════════════
def reverse_k_group(head, k):
    """
    Idu final answer — k nodes idya anta check madu (base case),
    idre k nodes reverse madi, remaining ge recursively bidu,
    kodage connect madu
    """
    node = head
    for _ in range(k):
        if not node:
            return head
        node = node.next

    prev, curr = None, head
    for _ in range(k):
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node

    head.next = reverse_k_group(curr, k)

    return prev


# ═══════════════════════════════════════════════════════════════════
# TEST CASES
# ═══════════════════════════════════════════════════════════════════
if __name__ == "__main__":
    # Test 1 — Basic (LeetCode example 1)
    head = build([1, 2, 3, 4, 5])
    assert to_list(reverse_k_group(head, 2)) == [2, 1, 4, 3, 5]

    # Test 2 — LeetCode example 2
    head = build([1, 2, 3, 4, 5])
    assert to_list(reverse_k_group(head, 3)) == [3, 2, 1, 4, 5]

    # Test 3 — k = 1 (no-op)
    head = build([1, 2, 3, 4, 5])
    assert to_list(reverse_k_group(head, 1)) == [1, 2, 3, 4, 5]

    # Test 4 — k = length (reverse the whole list)
    head = build([1, 2, 3, 4, 5])
    assert to_list(reverse_k_group(head, 5)) == [5, 4, 3, 2, 1]

    # Test 5 — Length is an exact multiple of k
    head = build([1, 2, 3, 4, 5, 6])
    assert to_list(reverse_k_group(head, 3)) == [3, 2, 1, 6, 5, 4]

    # Test 6 — Single node
    head = build([1])
    assert to_list(reverse_k_group(head, 1)) == [1]

    # Test 7 — Single node, k larger than length
    head = build([1])
    assert to_list(reverse_k_group(head, 2)) == [1]

    # Test 8 — Two full groups of k=2
    head = build([1, 2, 3, 4])
    assert to_list(reverse_k_group(head, 2)) == [2, 1, 4, 3]

    # Cross-check: brute force must agree on all of the above
    head = build([1, 2, 3, 4, 5])
    assert to_list(reverse_k_group_brute(head, 2)) == [2, 1, 4, 3, 5]

    head = build([1, 2, 3, 4, 5])
    assert to_list(reverse_k_group_brute(head, 3)) == [3, 2, 1, 4, 5]

    head = build([1, 2, 3, 4, 5])
    assert to_list(reverse_k_group_brute(head, 1)) == [1, 2, 3, 4, 5]

    head = build([1, 2, 3, 4, 5])
    assert to_list(reverse_k_group_brute(head, 5)) == [5, 4, 3, 2, 1]

    head = build([1, 2, 3, 4, 5, 6])
    assert to_list(reverse_k_group_brute(head, 3)) == [3, 2, 1, 6, 5, 4]

    head = build([1])
    assert to_list(reverse_k_group_brute(head, 1)) == [1]

    head = build([1])
    assert to_list(reverse_k_group_brute(head, 2)) == [1]

    head = build([1, 2, 3, 4])
    assert to_list(reverse_k_group_brute(head, 2)) == [2, 1, 4, 3]

    print("All tests passed!")
