"""
╔══════════════════════════════════════════════════════════════════╗
║  COPY LIST WITH RANDOM POINTER                                   ║
║  LeetCode #138  |  Difficulty: Medium  |  Topic: Linked Lists   ║
║  Link: https://leetcode.com/problems/                           ║
║        copy-list-with-random-pointer/                           ║
╚══════════════════════════════════════════════════════════════════╝

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📘 SECTION 1 — PROBLEM UNDERSTANDING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  A linked list is given where EACH node has two pointers:
  `next` (the usual one) and `random`, which can point to ANY
  node in the list (or None) — not necessarily a nearby one.

  Construct a DEEP COPY of the list: every new node must be a
  completely separate object, but its `next` and `random`
  pointers must mirror the structure of the original exactly
  (pointing to the CORRESPONDING new nodes, not the old ones).

  Input : head = first node of a linked list with next + random
          pointers
  Output: head of a fully independent deep-copied list with the
          same next/random structure

  Example 1 — basic:
    Input : [[7,null],[13,0],[11,4],[10,2],[1,0]]
            (each pair is [val, index that `random` points to])
    Output: an identical-structured deep copy — same vals, same
            random-pointer pattern, but entirely new node objects

  Example 2 — slightly tricky (random points forward):
    Input : [[1,1],[2,1]]
    Why?  : node 0's random points to node 1, node 1's random
            points to itself (index 1) — both must be mirrored
            correctly in the copy

  Example 3 — all randoms point to the same place:
    Input : [[3,null],[3,0],[3,null]]
    Why?  : duplicate values don't matter — only the STRUCTURE
            (which node's random points to which) must be copied

  Constraints:
    - 0 <= number of nodes <= 1000
    - -10^4 <= Node.val <= 10^4
    - Node.random is None or points to some node in the list

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🧠 SECTION 2 — KANGLISH THINKING — ಹೇಗೆ ಯೋಚಿಸಬೇಕು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  Problem odi aada mele namma brain enu think maadabeeku:

  ಹಂತ 1 — Problem ಅರ್ಥ ಮಾಡಿಕೊಳ್ಳಿ
  ┌─────────────────────────────────────────────────────────┐
  │  Input ಏನು ಕೊಡ್ತಾರೆ?  →  next + random pointers ಇರೋ list │
  │  Output ಏನು ಬೇಕು?     →  ಹೊಸ, ಪೂರ್ತಿ INDEPENDENT deep   │
  │                           copy — ಅದೇ structure            │
  │  Constraints ಏನಿದೆ?   →  random ಯಾವುದೇ node ಗೆ (ಮುಂದೆ,   │
  │                           ಹಿಂದೆ, ತನಗೇ) point ಮಾಡಬಹುದು     │
  └─────────────────────────────────────────────────────────┘

  ಹಂತ 2 — ಯಾಕೆ ಇದು tricky? "random ಅನ್ನ copy ಗೆ ಹೇಗೆ map
           ಮಾಡೋದು?" ಅಂತ ಯೋಚಿಸಿ
  →  random pointer ಯಾವುದೇ node ಗೆ (ಮುಂದೆ ಇರೋ ಅಥವಾ ಹಿಂದೆ
     ಇರೋ) point ಮಾಡಬಹುದು — ಸರಳ single pass ಲ್ಲಿ "copy ಇನ್ನೂ
     ಸೃಷ್ಟಿ ಆಗಿಲ್ಲ" ಅನ್ನೋ ಸಮಸ್ಯೆ ಬರುತ್ತೆ (random forward
     point ಮಾಡಿದ್ರೆ!)

  ಹಂತ 3 — ಮೊದಲ simple idea (HashMap) ಏನು?
  →  "original node → copy node" ಅನ್ನ MAP ಮಾಡಿ ಇಟ್ಟುಕೊಂಡ್ರೆ?
  →  Pass 1: ಪ್ರತಿ original node ಗೂ ಒಂದು copy (val ಮಾತ್ರ) ಸೃಷ್ಟಿಸಿ
     map ಗೆ ಸೇರಿಸಿ
  →  Pass 2: ಪ್ರತಿ copy ಗೂ, map ಬಳಸಿ next ಮತ್ತು random ಅನ್ನ
     ಸರಿಯಾದ COPY nodes ಗೆ point ಮಾಡಿ — map ಇದ್ರೆ "forward
     random" ಸಮಸ್ಯೆ ಇಲ್ಲ, ಯಾಕಂದ್ರೆ ಎಲ್ಲಾ copies ಈಗಾಗಲೇ ಸೃಷ್ಟಿ
     ಆಗಿವೆ!

  ಹಂತ 4 — O(1) EXTRA SPACE (interleaving trick) ಹೇಗೆ?
  →  "HashMap ಬೇಡ ಅಂದ್ರೆ, copy nodes ಅನ್ನ original list ಒಳಗೇ
      INTERLEAVE ಮಾಡಿದ್ರೆ?" ಅಂತ ಯೋಚಿಸಿ: orig1→copy1→orig2→
      copy2→...
  →  ಈಗ "copy ಇಂದ copy ಗೆ random" ಅಂದ್ರೆ "original.random.next"
     ಆಗುತ್ತೆ! (ಯಾಕಂದ್ರೆ ಪ್ರತಿ original ರ ಮುಂದೆನೇ ಅದರ copy
     ಇರುತ್ತೆ)
  →  ಕೊನೆಗೆ ಈ interleaved list ಅನ್ನ ಎರಡು ಭಾಗ (original, copy)
     ಆಗಿ ಬೇರ್ಪಡಿಸಿ

  ಹಂತ 5 — Technique ಯಾಕೆ ಇಲ್ಲಿ ಕೆಲಸ ಮಾಡುತ್ತೆ?
  →  Interleaving ಮಾಡಿದ ಮೇಲೆ, ಪ್ರತಿ copy node ತನ್ನ original
     ರ ಪಕ್ಕದಲ್ಲೇ ಇರುತ್ತೆ — so "original.random ರ COPY" ಅಂದ್ರೆ
     "original.random.next" (ಆ random node ರ ಪಕ್ಕದ copy) ಆಗಿ
     ನೇರವಾಗಿ ಸಿಗುತ್ತೆ, HashMap ಲುಕಪ್ ಬೇಡ!

  💡 Interview ನಲ್ಲಿ ಹೇಗೆ ಮಾತಾಡಬೇಕು:
  →  "First approach: HashMap mapping original→copy, two passes
      — one to create nodes, one to wire next/random"
  →  "O(1) space version: interleave copy nodes right after
      their originals, so a copy's random is just
      original.random.next — then split the interleaved list
      back into two"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🏷️ SECTION 3 — TECHNIQUE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Primary   : Interleaving (O(1) extra space, 3 passes)
  Secondary : HashMap (original → copy), O(n) extra space

  WHY Interleaving over HashMap?
  → The hashmap approach is simpler to reason about but needs
    O(n) extra space to remember the original→copy mapping.
    Interleaving embeds that same mapping INTO the list structure
    itself — "the node right after X" IS X's copy — so no
    separate lookup table is needed at all.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 💡 SECTION 4 — INTUITION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  The key insight: a hashmap's whole job here is answering "given
  an original node, where is its copy?" If we place each copy
  immediately after its original in the list, that question
  answers itself structurally — "original.next" IS the copy. So
  wiring a copy's random pointer becomes "find my original's
  random target, then step one node forward to reach THAT
  node's copy" — i.e. `original.random.next`. No table needed.

  The journey from brute to optimal:
    Brute thought   →  Two passes with a hashmap: first create
                       bare copies and record original→copy,
                       second pass wires next/random using the map
    Problem with it →  O(n) extra space for the hashmap
    Better question →  "Can the LIST ITSELF encode the mapping,
                       instead of a separate table?"
    Insight         →  Interleave copies right after originals;
                       a copy's random is just original.random.next
    Optimal         →  Three O(n) passes (interleave, wire
                       randoms, split apart), O(1) extra space

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🐢 SECTION 5 — APPROACH 1 — BRUTE FORCE (HashMap, two passes)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    Pass 1: walk the original list, creating a bare copy (val
    only) for every node, and record original→copy in a hashmap.
    Pass 2: walk the original list again, using the map to wire
    each copy's `next` and `random` to the correct COPY nodes.

  Pseudocode:
    step 1: old_to_new = {}
    step 2: for node in original list: old_to_new[node] = Node(node.val)
    step 3: for node in original list:
    step 4:   old_to_new[node].next   = old_to_new.get(node.next)
    step 5:   old_to_new[node].random = old_to_new.get(node.random)
    step 6: return old_to_new[head]

  Time  : O(n)  →  Why: two linear passes, O(1) hashmap ops each
  Space : O(n)  →  Why: the hashmap holds an entry per node

  ಇದು ಯಾಕೆ ಸಾಕಾಗಲ್ಲ?
    → Correct and O(n) time, but uses O(n) extra space for the
      mapping table — the interleaving trick gets the same
      result with O(1) extra space.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🚀 SECTION 6 — OPTIMAL (Interleaving, O(1) extra space)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    Three passes over the (temporarily modified) list:
    1. Interleave: for each original node, insert a copy right
       after it (orig1→copy1→orig2→copy2→...).
    2. Wire randoms: for each original, if it has a random
       pointer, set `original.next.random = original.random.next`
       (the copy's random = the copy of the original's random).
    3. Split apart: unweave the interleaved list back into the
       original list (restored) and the new copy list.

  Key steps:
    1. curr = head
       while curr: copy = Node(curr.val); copy.next = curr.next;
                   curr.next = copy; curr = copy.next
    2. curr = head
       while curr: if curr.random: curr.next.random = curr.random.next
                   curr = curr.next.next
    3. curr = head; new_head = head.next
       while curr: copy = curr.next; curr.next = copy.next
                   if copy.next: copy.next = copy.next.next
                   curr = curr.next
       return new_head

  ಕನ್ನಡದಲ್ಲಿ ಒಂದು ಸಲ ಹೇಳಿ:
    → "ಮೊದಲು ಪ್ರತಿ original ರ ಮುಂದೆ ಅದರ copy ಅನ್ನ interleave
       ಮಾಡಿ ಸೇರಿಸು. ಆಮೇಲೆ ಪ್ರತಿ original ಗೆ random ಇದ್ರೆ,
       copy.random = original.random.next (ಆ random node ರ
       ಪಕ್ಕದ copy) ಅಂತ set ಮಾಡು. ಕೊನೆಗೆ interleaved list ಅನ್ನ
       ಎರಡು ಭಾಗ ಆಗಿ ಬೇರ್ಪಡಿಸು — original list restore ಮಾಡಿ,
       copy list ಅನ್ನ ಪ್ರತ್ಯೇಕ ಆಗಿ ಕಟ್ಟು!"

  Time  : O(n)  →  Why: three separate linear passes
  Space : O(1)  →  Why: no hashmap — the interleaved structure
                        itself encodes the original↔copy mapping

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🔍 SECTION 7 — DRY RUN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Input: nodes A(val=1, random=B), B(val=2, random=B)
         (A.next=B, A.random=B, B.next=None, B.random=B — self-loop)

  Step 1 — interleave:
    A → A' → B → B' → None
    (A' is copy of A, B' is copy of B)

  Step 2 — wire randoms:
    A.random = B → A'.random = A.random.next = B.next = B'
    B.random = B → B'.random = B.random.next = B.next = B'
    (so A'.random = B', B'.random = B' — matches original
    structure: A.random=B, B.random=B, mirrored to copies)

  Step 3 — split apart:
    original restored: A → B → None
    copy list:          A' → B' → None
    with A'.random=B', B'.random=B' (self-loop preserved!)

  Output: a deep copy with identical next/random structure ✓

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 ⚠️ SECTION 8 — EDGE CASES — ಇವನ್ನ ಮರೆಯಬೇಡ!
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  ✓ Empty list (None)?             →  None — nothing to copy
  ✓ Single node, random=None?      →  copy with random=None too
  ✓ Single node, random=itself?    →  copy's random points to
                                       ITS OWN copy (self-loop
                                       preserved correctly)
  ✓ All randoms point to None?     →  behaves like a plain deep
                                       copy of next-only pointers
  ✓ Random points backward
    (to an earlier node)?          →  handled identically — the
                                       interleaving trick doesn't
                                       care about direction

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📊 SECTION 9 — COMPLEXITY SUMMARY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                        Time    Space
  Brute (HashMap)        O(n)    O(n)
  Interleaving            O(n)    O(1)   ← use this ✅

  Time yaake O(n)?  → Three linear passes, each O(1) work per node
  Space yaake O(1)? → No hashmap — structure itself encodes the
                       original↔copy mapping during the process

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🎯 SECTION 10 — PATTERN LEARNED — ಇದರಿಂದ ಕಲಿತದ್ದು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Pattern Name: Interleaving to Replace a HashMap

  Ee pattern yaavaaga use maadabeeku?
  → Deep-copy / structure-mirroring problems where a hashmap
     would normally track "original → copy" — if you can
     physically place the copy ADJACENT to its original, the
     adjacency itself replaces the lookup table
  → Any "mirror a graph-like structure built from a linear
     traversal" problem where O(1) space is explicitly asked for

  Idee pattern beere problemsalli kaanisatte:
  → Merge Two Sorted Lists #21 / Sort List #148 (contrast — those
     use a dummy node trick, a different O(1)-space technique)
  → Clone Graph #133 (same underlying idea — HashMap of
     original→copy — but graphs don't have a "linear adjacency"
     to exploit, so the hashmap stays necessary there)

  Next time intaha problem bandre naanu modalu idannu think maadtene:
  → "Deep copy / mirror structure madabekagidre, HashMap beku
     antadre → copy na original pakkadalle place madi, adjacency
     ne mapping replace maaduttadeyanta try maadu — O(1) space!"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🗣️ SECTION 11 — INTERVIEWALLI HEGE EXPLAIN MAADABEEKU
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  1. Understand:
     "Deep-copy a linked list where each node also has a random
      pointer that can point anywhere in the list."

  2. Brute force:
     "HashMap mapping original→copy. First pass creates bare
      copies, second pass wires next/random using the map.
      O(n) time, O(n) space."

  3. Optimize:
     "Interleave each copy right after its original. Now a
      copy's random is just original.random.next — no map
      needed. Then split the interleaved list back into the
      original and the copy."

  4. Code:
     "Three passes: (1) insert copies inline, (2) wire randoms
      using the .next trick, (3) unweave into two separate lists."

  5. Complexity:
     "Time O(n) — three linear passes. Space O(1) — no hashmap,
      the list structure itself carries the mapping."

  Mukhya: a hashmap's job is often just 'remember where I put
          something' — if you can place it RIGHT NEXT to the
          original instead, the hashmap becomes unnecessary!
"""


# ─── Node Definition (next + random) ──────────────────────────────
class Node:
    def __init__(self, x, next=None, random=None):
        self.val    = x
        self.next   = next
        self.random = random


# ─── Helper: build list from [val, random_index] pairs ───────────
def build(pairs):
    if not pairs:
        return None

    nodes = [Node(val) for val, _ in pairs]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    for i, (_, random_index) in enumerate(pairs):
        if random_index is not None:
            nodes[i].random = nodes[random_index]

    return nodes[0]


# ─── Helper: serialize list to [val, random_index] pairs ─────────
def serialize(head):
    nodes = []
    curr = head
    while curr:
        nodes.append(curr)
        curr = curr.next

    index_of = {id(n): i for i, n in enumerate(nodes)}
    result = []
    for n in nodes:
        random_index = index_of[id(n.random)] if n.random else None
        result.append([n.val, random_index])

    return result


# ─── Helper: collect node identities (to verify a TRUE deep copy) ─
def node_ids(head):
    ids = []
    curr = head
    while curr:
        ids.append(id(curr))
        curr = curr.next
    return ids


# ═══════════════════════════════════════════════════════════════════
# BRUTE FORCE — O(n) Time | O(n) Space (HashMap, two passes)
# ═══════════════════════════════════════════════════════════════════
def copy_random_list_brute(head):
    """
    Idu modala aaloochane — old_to_new hashmap bhalasi, pass1
    copies create madu, pass2 next/random wire madu
    """
    if not head:
        return None

    old_to_new = {}
    curr = head
    while curr:
        old_to_new[curr] = Node(curr.val)
        curr = curr.next

    curr = head
    while curr:
        old_to_new[curr].next = old_to_new.get(curr.next)
        old_to_new[curr].random = old_to_new.get(curr.random)
        curr = curr.next

    return old_to_new[head]


# ═══════════════════════════════════════════════════════════════════
# OPTIMAL — O(n) Time | O(1) Space (interleaving)
# ═══════════════════════════════════════════════════════════════════
def copy_random_list(head):
    """
    Idu final answer — copy na original pakkadalle interleave
    madi, random wire madi, kadege eradu lists bidrish madu
    """
    if not head:
        return None

    # Step 1: interleave — orig1 -> copy1 -> orig2 -> copy2 -> ...
    curr = head
    while curr:
        copy = Node(curr.val)
        copy.next = curr.next
        curr.next = copy
        curr = copy.next

    # Step 2: wire random pointers for the copies
    curr = head
    while curr:
        if curr.random:
            curr.next.random = curr.random.next
        curr = curr.next.next

    # Step 3: split the interleaved list back into original + copy
    curr = head
    new_head = head.next
    while curr:
        copy = curr.next
        curr.next = copy.next
        if copy.next:
            copy.next = copy.next.next
        curr = curr.next

    return new_head


# ═══════════════════════════════════════════════════════════════════
# TEST CASES
# ═══════════════════════════════════════════════════════════════════
if __name__ == "__main__":
    # Test 1 — Basic (LeetCode example)
    original = build([[7, None], [13, 0], [11, 4], [10, 2], [1, 0]])
    copy = copy_random_list(original)
    assert serialize(copy) == [[7, None], [13, 0], [11, 4], [10, 2], [1, 0]]
    assert not set(node_ids(original)) & set(node_ids(copy))  # true deep copy

    # Test 2 — Random points forward / to self
    original = build([[1, 1], [2, 1]])
    copy = copy_random_list(original)
    assert serialize(copy) == [[1, 1], [2, 1]]

    # Test 3 — Mixed None and self-pointing randoms
    original = build([[3, None], [3, 0], [3, None]])
    copy = copy_random_list(original)
    assert serialize(copy) == [[3, None], [3, 0], [3, None]]

    # Test 4 — Empty list
    assert copy_random_list(None) is None

    # Test 5 — Single node with self-loop random
    original = build([[5, 0]])
    copy = copy_random_list(original)
    assert serialize(copy) == [[5, 0]]
    assert copy.random is copy  # self-loop preserved, pointing to the COPY

    # Cross-check: brute force must agree on all of the above
    original = build([[7, None], [13, 0], [11, 4], [10, 2], [1, 0]])
    copy = copy_random_list_brute(original)
    assert serialize(copy) == [[7, None], [13, 0], [11, 4], [10, 2], [1, 0]]

    original = build([[1, 1], [2, 1]])
    assert serialize(copy_random_list_brute(original)) == [[1, 1], [2, 1]]

    original = build([[3, None], [3, 0], [3, None]])
    assert serialize(copy_random_list_brute(original)) == [[3, None], [3, 0], [3, None]]

    assert copy_random_list_brute(None) is None

    original = build([[5, 0]])
    copy = copy_random_list_brute(original)
    assert serialize(copy) == [[5, 0]]
    assert copy.random is copy

    print("All tests passed!")
