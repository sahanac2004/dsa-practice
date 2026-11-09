"""
╔══════════════════════════════════════════════════════════════════╗
║  FLATTEN A MULTILEVEL DOUBLY LINKED LIST                         ║
║  LeetCode #430  |  Difficulty: Hard  |  Topic: Linked Lists   ║
║  Link: https://leetcode.com/problems/                           ║
║        flatten-a-multilevel-doubly-linked-list/                 ║
╚══════════════════════════════════════════════════════════════════╝

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📘 SECTION 1 — PROBLEM UNDERSTANDING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  You are given a doubly linked list where, in addition to the
  usual `next` and `prev` pointers, each node may ALSO have a
  `child` pointer — pointing to a separate doubly linked list
  that lives on a level "below" this one. These child lists may
  themselves have nodes with their own children, several levels
  deep.

  Flatten the list so that all nodes appear in a single-level
  doubly linked list. The flattening order is: whenever a node
  has a child list, that ENTIRE child list (fully flattened
  itself, recursively) gets inserted right between that node
  and whatever came after it, BEFORE continuing with the rest
  of the original level.

  Input : head = multilevel doubly linked list (next, prev,
          child pointers)
  Output: head of a single-level doubly linked list (all child
          pointers now None) with nodes in the correct
          depth-first order

  Example 1 — basic:
    Input : 1 - 2 - 3 - 4 - 5 - 6
                      |
                      7 - 8 - 9 - 10
                           |
                           11 - 12
    Output: [1,2,3,7,8,11,12,9,10,4,5,6]
    Why?  : node 3's child (7-8-9-10) gets inserted right after
            3, before 4. Within THAT child list, node 8's own
            child (11-12) gets inserted right after 8, before 9.

  Example 2 — single level, no children:
    Input : [1,2,3]
    Output: [1,2,3]

  Example 3 — empty list:
    Input : []
    Output: []

  Constraints:
    - 0 <= number of nodes <= 1000
    - 1 <= Node.val <= 10^5

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🧠 SECTION 2 — KANGLISH THINKING — ಹೇಗೆ ಯೋಚಿಸಬೇಕು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  Problem odi aada mele namma brain enu think maadabeeku:

  ಹಂತ 1 — Problem ಅರ್ಥ ಮಾಡಿಕೊಳ್ಳಿ
  ┌─────────────────────────────────────────────────────────┐
  │  Input ಏನು ಕೊಡ್ತಾರೆ?  →  doubly linked list, ಪ್ರತಿ node  │
  │                           ಗೆ child (sub-list) ಇರ್ಬಹುದು     │
  │  Output ಏನು ಬೇಕು?     →  ಎಲ್ಲಾ levels ಅನ್ನ ONE single      │
  │                           level list ಗೆ flatten ಮಾಡಿದ್ದು  │
  │  Constraints ಏನಿದೆ?   →  child ಇರೋ node ಅ ಮುಂದೆ ಅದರ child │
  │                           list ಪೂರ್ತಿ ಬರ್ಬೇಕು (DFS order) │
  └─────────────────────────────────────────────────────────┘

  ಹಂತ 2 — ಯಾಕೆ ಇದು tricky? "ಪ್ರತಿ node ಗೂ child ಇರ್ಬಹುದು, ಆ
           child ಗೂ ಅದ್ರದ್ದೇ child ಇರ್ಬಹುದು — ಅಂದ್ರೆ RECURSIVE
           structure!" ಅಂತ ಯೋಚಿಸಿ
  →  ಇದು ಒಂದು TREE-ತರ structure (linked list ಜೊತೆ child
     pointer ಇರೋ) — DFS ಮಾಡಿ "ಈ node, ಅದ್ರ child (ಪೂರ್ತಿ
     flattened), ಆಮೇಲೆ ಈ node ಅ original next" ಅನ್ನೋ ಕ್ರಮ ಲ್ಲಿ
     ಸೇರಿಸ್ಬೇಕು

  ಹಂತ 3 — ಮೊದಲ simple idea (brute force) ಏನು?
  →  "ಪ್ರತಿ node ಅನ್ನ DFS order ಲ್ಲಿ ಒಂದು ARRAY ಗೆ ಹಾಕಿ (child
      ಇದ್ರೆ ಮೊದಲು child ಅನ್ನ recursively visit ಮಾಡಿ), ಆಮೇಲೆ ಆ
      array ಇಂದ next/prev pointers ಮರು-ಜೋಡಿಸಿದ್ರೆ?"
  →  ಕೆಲಸ ಆಗುತ್ತೆ, ಆದ್ರೆ O(n) extra space ಬೇಕಾಗುತ್ತೆ array ಗೆ

  ಹಂತ 4 — Optimal idea (ಇರೋ nodes ಅನ್ನೇ in-place rewire) ಹೇಗೆ
           ಬರುತ್ತೆ?
  →  "ಪ್ರತಿ node ಗೆ child ಸಿಕ್ಕಾಗ, ಆ child ಅನ್ನ recursively
      flatten ಮಾಡಿ (ಅದ್ರ own tail ಅನ್ನೂ ಕಂಡುಹಿಡಿದು), ಆಮೇಲೆ:
      current node → flattened child → (ಮೊದಲಿದ್ದ) next ಅಂತ
      in-place ಜೋಡಿಸಿದ್ರೆ?" ಅಂತ ಯೋಚಿಸಿ — ಇರೋ nodes ಅನ್ನೇ
      ಮರುಬಳಕೆ, ಎಕ್ಸ್ಟ್ರಾ array ಬೇಡ
  →  recursive function: node ಅನ್ನ flatten ಮಾಡಿ, ಆ ಫ್ಲಾಟ್ಟನ್ಡ್
     chain ಅ TAIL ಅನ್ನ return ಮಾಡುತ್ತೆ — ಇದನ್ನ ಬಳಸಿ ಮುಂದಿನ
     piece ಜೊತೆ ಜೋಡಿಸ್ಬಹುದು

  ಹಂತ 5 — Technique ಯಾಕೆ ಇಲ್ಲಿ ಕೆಲಸ ಮಾಡುತ್ತೆ?
  →  "ಪ್ರತಿ recursive call ತನ್ನ own tail ಅನ್ನ return ಮಾಡುತ್ತೆ"
     ಅನ್ನೋ idea ಇಂದ, caller ಗೆ "ಈ flattened piece ಎಲ್ಲಿ
     ಮುಗಿಯುತ್ತೆ" ಅಂತ instant ಆಗಿ ಗೊತ್ತಾಗುತ್ತೆ — ಮುಂದಿನ piece
     ಅನ್ನ ಅಲ್ಲಿಗೆ ಜೋಡಿಸ್ಬಹುದು, ಮತ್ತೆ ಮುಂದೆ scan ಮಾಡೋ ಅಗತ್ಯ ಇಲ್ಲ

  💡 Interview ನಲ್ಲಿ ಹೇಗೆ ಮಾತಾಡಬೇಕು:
  →  "First approach: DFS traverse into an array first (visit
      a node, then its child fully, then continue), then rebuild
      next/prev pointers from that array — O(n) space"
  →  "Optimal: recursive in-place flatten. For each node, if it
      has a child, recursively flatten the child (which returns
      the child's flattened TAIL), splice child-in-between
      current node and its original next, keep going. O(1) extra
      space beyond the recursion stack."

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🏷️ SECTION 3 — TECHNIQUE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Primary   : Recursive In-Place Flatten (returns the flattened
              tail)
  Secondary : DFS to Array, Then Rebuild Pointers

  WHY Recursive In-Place over Array Rebuild?
  → Collecting DFS order into an array works but needs O(n)
    extra space to hold node references temporarily before
    rewiring. The recursive in-place approach reuses the
    EXISTING node objects directly: whenever a node has a
    child, flatten that child first (recursively), splice it
    in between the node and its original next, and continue —
    each recursive call conveniently returns the TAIL of what it
    flattened, so the caller knows exactly where to attach
    whatever comes next.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 💡 SECTION 4 — INTUITION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  The key insight: this is fundamentally a DEPTH-FIRST SEARCH
  over a tree-like structure that happens to be expressed as a
  linked list with occasional "child" branches. "Flatten
  everything starting from this node" naturally decomposes into
  "process this node; if it has a child, flatten THAT first
  (recursively) and splice it right here; then continue with
  whatever was originally next." The trick that makes splicing
  efficient is having each recursive call return the TAIL node
  of whatever it flattened — that's exactly the node whose
  `next` needs to point to the next piece, no re-scanning
  required to find "where did that child's flattening end."

  The journey from brute to optimal:
    Brute thought   →  DFS the whole structure into a flat
                       array of nodes (visit node, then fully
                       recurse into its child, then continue),
                       then rebuild next/prev pointers from that
                       array
    Problem with it →  O(n) extra space to hold the array of
                       node references
    Better question →  "Can the splicing happen directly on the
                       EXISTING nodes, one piece at a time?"
    Insight         →  A recursive flatten function can return
                       the TAIL of what it just flattened,
                       letting the caller splice the next piece
                       on without any extra bookkeeping
    Optimal         →  Recursive in-place splice: for each node
                       with a child, flatten the child, link
                       node -> flattened child -> original next,
                       recurse onward — O(1) extra space besides
                       the call stack

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🐢 SECTION 5 — APPROACH 1 — BRUTE FORCE (DFS to Array, Rebuild)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    DFS the multilevel structure: visit a node, add it to a
    list; if it has a child, recursively DFS into the child
    BEFORE continuing to this node's own `next`. Once the full
    DFS order is collected, walk the resulting list of nodes and
    rewire next/prev pointers sequentially, clearing every
    child pointer to None.

  Pseudocode:
    step 1: order = []
    step 2: def dfs(node):
    step 3:     while node:
    step 4:         order.append(node)
    step 5:         if node.child: dfs(node.child)
    step 6:         node = node.next
    step 7: dfs(head)
    step 8: for i in range(len(order) - 1):
    step 9:     order[i].next = order[i+1]
    step 10:    order[i+1].prev = order[i]
    step 11:    order[i].child = None
    step 12: if order: order[-1].child = None

  Time  : O(n)  →  Why: every node is visited exactly once
                        during DFS, plus one more linear pass to
                        rewire pointers
  Space : O(n)  →  Why: the `order` array holds a reference to
                        every node

  ಇದು ಯಾಕೆ ಸಾಕಾಗಲ್ಲ?
    → Correct and O(n) time, but uses O(n) extra space for the
      array — the recursive in-place approach splices existing
      nodes directly with no such auxiliary storage.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🚀 SECTION 6 — OPTIMAL (Recursive In-Place Flatten)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    Define a helper that flattens the list starting at a given
    node and returns the TAIL of the flattened result. Walk
    node by node: if the current node has a child, recursively
    flatten that child (getting back its tail), then splice:
    current.next = child_head, child_head.prev = current,
    child's TAIL.next = original_next (reconnecting the rest of
    THIS level), and if original_next exists, its prev points
    back to child's tail. Clear the child pointer. Continue
    walking from where the splice left off, tracking the
    overall tail as you go.

  Key steps:
    1. def flatten_helper(head):
    2.     node = head
    3.     last = head
    4.     while node:
    5.         if node.child:
    6.             next_node = node.next
    7.             child_tail = flatten_helper(node.child)
    8.             node.next = node.child
    9.             node.child.prev = node
    10.            child_tail.next = next_node
    11.            if next_node: next_node.prev = child_tail
    12.            node.child = None
    13.            last = child_tail
    14.            node = next_node
    15.        else:
    16.            last = node
    17.            node = node.next
    18.    return last
    19. flatten_helper(head); return head

  ಕನ್ನಡದಲ್ಲಿ ಒಂದು ಸಲ ಹೇಳಿ:
    → "node ಅನ್ನ walk ಮಾಡ್ತಾ, child ಸಿಕ್ರೆ: ಮೊದಲು ಆ child ಅನ್ನ
       recursively flatten ಮಾಡಿ ಅದ್ರ TAIL ಅನ್ನ ಪಡಿ. ಆಮೇಲೆ
       current → child_head → ... → child_tail → (original
       next) ಅಂತ ಜೋಡಿಸಿ, child pointer ಅನ್ನ None ಮಾಡಿ, ಅಲ್ಲಿಂದ
       ಮುಂದೆ continue ಮಾಡು. ಕೊನೆಗೆ overall TAIL ಅನ್ನ return
       ಮಾಡು!"

  Time  : O(n)  →  Why: every node is visited and spliced
                        exactly once, across all recursive calls
                        combined
  Space : O(d)  →  Why: recursion depth equals the maximum
                        "nesting depth" of child lists (not the
                        total node count) — no auxiliary array

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🔍 SECTION 7 — DRY RUN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Input (simplified): 1 - 2 - 3 - 4
                           |
                           5 - 6

  flatten_helper(head=1):
    node=1, no child -> last=1, node=2
    node=2, no child -> last=2, node=3
    node=3, HAS child (5):
        next_node = 4 (3's original next)
        child_tail = flatten_helper(5)
            node=5, no child -> last=5, node=6
            node=6, no child -> last=6, node=None
            return 6
        child_tail = 6
        3.next = 5; 5.prev = 3
        6.next = 4 (reconnect to what was after 3)
        4.prev = 6
        3.child = None
        last = 6; node = 4 (continue from here)
    node=4, no child -> last=4, node=None
    return 4 (overall tail)

  Final chain: 1 -> 2 -> 3 -> 5 -> 6 -> 4
  Output: [1,2,3,5,6,4] ✓ matches expected DFS order

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 ⚠️ SECTION 8 — EDGE CASES — ಇವನ್ನ ಮರೆಯಬೇಡ!
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  ✓ Empty list (None)?            →  return None immediately,
                                      nothing to flatten
  ✓ Single node, no child?        →  no-op, returned as-is
  ✓ No node has a child at all?   →  behaves exactly like a
                                      plain single-level list,
                                      unchanged
  ✓ Child list exists but the
    node WITH a child is the
    very last node at its level?  →  next_node is None — the
                                      splice correctly sets
                                      child_tail.next = None,
                                      no dangling reference
  ✓ Multiple levels of nesting
    (child's child has a child)?  →  handled naturally by
                                      recursion — each level
                                      flattens its own children
                                      before returning its tail
  ✓ A node has a child that is
    itself just ONE node?         →  child_tail = that single
                                      node; splice still works
                                      identically (head == tail
                                      for a 1-node child list)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📊 SECTION 9 — COMPLEXITY SUMMARY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                              Time    Space
  Brute (DFS to array)         O(n)    O(n)
  Recursive in-place splice     O(n)    O(d)   ← use this ✅
                                               (d = max nesting
                                                depth, not n)

  Time yaake O(n)?  → Across all recursive calls combined, each
                       node is visited and spliced exactly once
  Space yaake O(d)?  → Recursion depth tracks how deeply nested
                       the child lists go, independent of total
                       node count

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🎯 SECTION 10 — PATTERN LEARNED — ಇದರಿಂದ ಕಲಿತದ್ದು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Pattern Name: Recursive Flatten Returning Tail (DFS Splice)

  Ee pattern yaavaaga use maadabeeku?
  → Any "flatten a nested/tree-like linked structure into a
     single level, in DFS order" problem — a recursive helper
     that returns the TAIL of whatever it flattened lets the
     caller splice the next piece on directly, with zero
     re-scanning
  → General technique for any "merge a recursively-structured
     chain back into a flat one" task

  Idee pattern beere problemsalli kaanisatte:
  → Flatten Binary Tree to Linked List (LC #114) — nearly
     identical idea: recursively flatten each subtree, splice
     the flattened left subtree between a node and its right
  → Copy List with Random Pointer #138 (contrast — a different
     "extra pointer on a linked list" problem, but solved via
     interleaving rather than recursive splicing)

  Next time intaha problem bandre naanu modalu idannu think maadtene:
  → "Nested / tree-like linked structure anna ONE flat level ge
     flatten madabekagidre → recursive helper banayi, adhu
     flatten madida piece ina TAIL anna return madali — caller
     ge mundina piece anna EXACTLY alle splice madoke sigutte,
     re-scan bedave illa!"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🗣️ SECTION 11 — INTERVIEWALLI HEGE EXPLAIN MAADABEEKU
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  1. Understand:
     "A doubly linked list where nodes may have a `child`
      pointer to a nested list, possibly many levels deep.
      Flatten everything into one level in DFS order (a node's
      child list gets fully inserted right after it, before
      continuing to the node's original next)."

  2. Brute force:
     "DFS the whole structure into an array of node references
      (visit a node, recurse fully into its child, then
      continue), then rebuild next/prev pointers from that
      array. O(n) time, O(n) space."

  3. Optimize:
     "Recursive helper: walk nodes; whenever one has a child,
      recursively flatten the child FIRST (which returns the
      child's tail), then splice node -> child_head ->
      ... -> child_tail -> original_next directly on the
      existing nodes, and continue. The helper returns the
      overall tail."

  4. Code:
     "flatten_helper(head): track `last`. On a child, recurse on
      it, get child_tail, rewire four pointers (node.next,
      child.prev, child_tail.next, next_node.prev), clear
      node.child, continue from next_node. On no child, just
      advance. Return last."

  5. Complexity:
     "Time O(n) — each node spliced once overall. Space O(d) —
      recursion depth tracks nesting depth, not total nodes."

  Mukhya: a recursive 'flatten and return the tail' helper is
          the standard trick for ANY nested linked-structure
          flattening problem — it lets you splice pieces
          together directly without ever re-scanning to find
          where one piece ends!
"""


# ─── Doubly Linked List Node Definition (with child pointer) ─────
class Node:
    def __init__(self, val, prev=None, next=None, child=None):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


# ─── Helper: build a flat list of nodes (no children) ────────────
def build_flat(values):
    nodes = [Node(v) for v in values]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
        nodes[i + 1].prev = nodes[i]
    return nodes[0] if nodes else None


# ─── Helper: convert a flat list back to a Python list ───────────
def to_list(head):
    result = []
    curr = head
    while curr:
        result.append(curr.val)
        curr = curr.next
    return result


# ═══════════════════════════════════════════════════════════════════
# BRUTE FORCE — O(n) Time | O(n) Space (DFS to array, rebuild)
# ═══════════════════════════════════════════════════════════════════
def flatten_brute(head):
    """
    Idu modala aaloochane — DFS madi order array ge haaki,
    aamele next/prev pointers array indha rebuild madu
    """
    order = []

    def dfs(node):
        while node:
            order.append(node)
            if node.child:
                dfs(node.child)
                node.child = None
            node = node.next

    dfs(head)

    for i in range(len(order) - 1):
        order[i].next = order[i + 1]
        order[i + 1].prev = order[i]

    if order:
        order[-1].next = None
        return order[0]

    return None


# ═══════════════════════════════════════════════════════════════════
# OPTIMAL — O(n) Time | O(d) Space (recursive in-place flatten)
# ═══════════════════════════════════════════════════════════════════
def _flatten_helper(head):
    node = head
    last = head

    while node:
        if node.child:
            next_node = node.next
            child_tail = _flatten_helper(node.child)

            node.next = node.child
            node.child.prev = node
            child_tail.next = next_node
            if next_node:
                next_node.prev = child_tail

            node.child = None
            last = child_tail
            node = next_node
        else:
            last = node
            node = node.next

    return last


def flatten(head):
    """
    Idu final answer — recursive helper node walk madi, child
    sikre adhanna flatten madi splice madu, overall tail track
    madtha mundhe hogu
    """
    if not head:
        return None

    _flatten_helper(head)
    return head


# ═══════════════════════════════════════════════════════════════════
# TEST CASES
# ═══════════════════════════════════════════════════════════════════
if __name__ == "__main__":
    # Test 1 — Basic (LeetCode example 1)
    #   1 - 2 - 3 - 4 - 5 - 6
    #           |
    #           7 - 8 - 9 - 10
    #               |
    #               11 - 12
    n1, n2, n3, n4, n5, n6 = (Node(v) for v in [1, 2, 3, 4, 5, 6])
    n7, n8, n9, n10 = (Node(v) for v in [7, 8, 9, 10])
    n11, n12 = Node(11), Node(12)

    for a, b in [(n1, n2), (n2, n3), (n3, n4), (n4, n5), (n5, n6)]:
        a.next = b
        b.prev = a
    for a, b in [(n7, n8), (n8, n9), (n9, n10)]:
        a.next = b
        b.prev = a
    for a, b in [(n11, n12)]:
        a.next = b
        b.prev = a

    n3.child = n7
    n8.child = n11

    assert to_list(flatten(n1)) == [1, 2, 3, 7, 8, 11, 12, 9, 10, 4, 5, 6]

    # Test 2 — Single level, no children (LeetCode example 2)
    head = build_flat([1, 2, 3])
    assert to_list(flatten(head)) == [1, 2, 3]

    # Test 3 — Empty list (LeetCode example 3)
    assert flatten(None) is None

    # Test 4 — Single node, no child
    head = build_flat([1])
    assert to_list(flatten(head)) == [1]

    # Test 5 — Child at the very last node of the top level
    top = build_flat([1, 2, 3])
    child = build_flat([4, 5])
    nodes = []
    curr = top
    while curr:
        nodes.append(curr)
        curr = curr.next
    nodes[-1].child = child
    assert to_list(flatten(top)) == [1, 2, 3, 4, 5]

    # Test 6 — Child that itself has a single-node child (3 levels deep)
    a = build_flat([1, 2])
    b = Node(3)
    c = Node(4)
    curr = a
    while curr.next:
        curr = curr.next
    curr.child = b
    b.child = c
    assert to_list(flatten(a)) == [1, 2, 3, 4]

    # Cross-check: brute force must agree on all of the above
    n1, n2, n3, n4, n5, n6 = (Node(v) for v in [1, 2, 3, 4, 5, 6])
    n7, n8, n9, n10 = (Node(v) for v in [7, 8, 9, 10])
    n11, n12 = Node(11), Node(12)

    for a, b in [(n1, n2), (n2, n3), (n3, n4), (n4, n5), (n5, n6)]:
        a.next = b
        b.prev = a
    for a, b in [(n7, n8), (n8, n9), (n9, n10)]:
        a.next = b
        b.prev = a
    n11.next = n12
    n12.prev = n11

    n3.child = n7
    n8.child = n11

    assert to_list(flatten_brute(n1)) == [1, 2, 3, 7, 8, 11, 12, 9, 10, 4, 5, 6]

    head = build_flat([1, 2, 3])
    assert to_list(flatten_brute(head)) == [1, 2, 3]

    assert flatten_brute(None) is None

    head = build_flat([1])
    assert to_list(flatten_brute(head)) == [1]

    print("All tests passed!")
