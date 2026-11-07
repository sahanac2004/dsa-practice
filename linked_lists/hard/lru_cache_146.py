"""
╔══════════════════════════════════════════════════════════════════╗
║  LRU CACHE                                                        ║
║  LeetCode #146  |  Difficulty: Hard  |  Topic: Linked Lists    ║
║  Link: https://leetcode.com/problems/lru-cache/                 ║
╚══════════════════════════════════════════════════════════════════╝

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📘 SECTION 1 — PROBLEM UNDERSTANDING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Design a data structure that follows the constraints of a
  Least Recently Used (LRU) cache, with a fixed capacity.

  Implement the LRUCache class:
    - LRUCache(capacity): initialize the cache with positive
      size `capacity`
    - get(key): return the value of `key` if it exists,
      otherwise return -1. Accessing a key counts as a "use" —
      it becomes the most recently used.
    - put(key, value): update the value of `key` if it exists,
      otherwise add the key-value pair. If the number of keys
      exceeds `capacity` from this operation, EVICT the least
      recently used key.

  BOTH get and put must run in O(1) average time complexity.

  Example:
    LRUCache cache = new LRUCache(2);
    cache.put(1, 1);           // cache: {1=1}
    cache.put(2, 2);           // cache: {1=1, 2=2}
    cache.get(1);               // returns 1, cache: {2=2, 1=1}
                                 //   (1 is now most recent)
    cache.put(3, 3);            // evicts key 2 (LRU),
                                 //   cache: {1=1, 3=3}
    cache.get(2);                // returns -1 (not found)
    cache.put(4, 4);             // evicts key 1 (LRU),
                                 //   cache: {3=3, 4=4}
    cache.get(1);                 // returns -1 (not found)
    cache.get(3);                  // returns 3
    cache.get(4);                   // returns 4

  Constraints:
    - 1 <= capacity <= 3000
    - 0 <= key, value <= 10^4
    - At most 2 * 10^5 calls to get and put combined

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🧠 SECTION 2 — KANGLISH THINKING — ಹೇಗೆ ಯೋಚಿಸಬೇಕು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  Problem odi aada mele namma brain enu think maadabeeku:

  ಹಂತ 1 — Problem ಅರ್ಥ ಮಾಡಿಕೊಳ್ಳಿ
  ┌─────────────────────────────────────────────────────────┐
  │  Input ಏನು ಕೊಡ್ತಾರೆ?  →  capacity, get(key)/put(key,val)  │
  │                           calls                             │
  │  Output ಏನು ಬೇಕು?     →  get → value ಅಥವಾ -1; put → add/   │
  │                           update, capacity ಮೀರಿದ್ರೆ LRU    │
  │                           key evict                        │
  │  Constraints ಏನಿದೆ?   →  ಎರಡೂ operations O(1) AVERAGE time │
  │                           ಲ್ಲಿ ಆಗ್ಬೇಕು!                    │
  └─────────────────────────────────────────────────────────┘

  ಹಂತ 2 — ಯಾಕೆ ಇದು tricky? "O(1) ಲ್ಲಿ get, PLUS O(1) ಲ್ಲಿ 'least
           recently used' ಅನ್ನ ಕಂಡುಹಿಡಿಯೋದು, PLUS O(1) ಲ್ಲಿ 'most
           recent' ಗೆ move ಮಾಡೋದು — ಇದೆಲ್ಲ ಒಟ್ಟಿಗೆ ಹೇಗೆ?" ಅಂತ
           ಯೋಚಿಸಿ
  →  HashMap ಒಂದೇ ಆದ್ರೆ O(1) lookup ಸಿಗುತ್ತೆ, ಆದ್ರೆ "ಯಾವ key
     least recently used" ಅಂತ ಟ್ರ್ಯಾಕ್ ಮಾಡೋಕೆ ORDER ಬೇಕು —
     plain dict ಲ್ಲಿ order maintain ಮಾಡಿ, "move to most recent"
     ಅನ್ನ O(1) ಲ್ಲಿ ಮಾಡೋದು ಕಷ್ಟ (array/list ಆಗಿದ್ರೆ O(n) ಆಗುತ್ತೆ)

  ಹಂತ 3 — ಮೊದಲ simple idea (brute force) ಏನು?
  →  "ಒಂದು dict (key→value) ಮತ್ತು ಒಂದು LIST (order track ಗೆ)
      ಇಟ್ಟುಕೊಂಡ್ರೆ? access ಆದಾಗ list ಇಂದ remove ಮಾಡಿ ಕೊನೆಗೆ
      ಹಾಕ್ಬೇಕು — ಇದು O(n)!"
  →  ಕೆಲಸ ಆಗುತ್ತೆ, ಆದ್ರೆ list ಒಳಗೆ remove ಮಾಡೋದು O(n) — required
     O(1) average time ಗೆ ಇದು ಸಾಕಾಗಲ್ಲ

  ಹಂತ 4 — Optimal idea (HashMap + Doubly Linked List) ಹೇಗೆ ಬರುತ್ತೆ?
  →  "HashMap ಇಂದ O(1) lookup, DOUBLY linked list ಇಂದ O(1)
      insert/remove/move-to-front ಸಿಗುತ್ತೆ ಅಲ್ವಾ?" ಅಂತ ಯೋಚಿಸಿ:
      HashMap key → node (ಆ node ಯ reference). list ಅ ಒಂದು
      ಕೊನೆ (head ಬಳಿ) = most recently used, ಇನ್ನೊಂದು ಕೊನೆ (tail
      ಬಳಿ) = least recently used
  →  get(key): HashMap ಇಂದ O(1) ಲ್ಲಿ node ಸಿಗುತ್ತೆ, ಆ node ಅನ್ನ
     doubly linked list ಇಂದ O(1) ಲ್ಲಿ remove ಮಾಡಿ, head ಬಳಿ
     O(1) ಲ್ಲಿ ಮತ್ತೆ ಸೇರಿಸ್ಬಹುದು (doubly ಆಗಿರೋದ್ರಿಂದ prev/next
     ಎರಡೂ ಗೊತ್ತು, O(1) removal!)
  →  put(key, val): capacity ಮೀರಿದ್ರೆ tail ಬಳಿ ಇರೋ (LRU) node
     ಅನ್ನ O(1) ಲ್ಲಿ remove ಮಾಡಿ, ಹೊಸ node ಅನ್ನ head ಬಳಿ O(1)
     ಲ್ಲಿ ಸೇರಿಸ್ಬಹುದು

  ಹಂತ 5 — Technique ಯಾಕೆ ಇಲ್ಲಿ ಕೆಲಸ ಮಾಡುತ್ತೆ?
  →  DOUBLY linked list ಅ ಪ್ರತಿ node ಗೂ prev ಮತ್ತು next ಎರಡೂ
     ಗೊತ್ತು — ಹಾಗಾಗಿ "ಈ node ಅನ್ನ ಅದರ ಪ್ರಸ್ತುತ ಜಾಗ ಇಂದ ಪ್ರತ್ಯೇಕ
     ಮಾಡೋದು" (unlink) ಕೇವಲ prev.next ಮತ್ತು next.prev ಅನ್ನ
     ಸರಿಪಡಿಸಿದ್ರೆ ಸಾಕು — list ಅನ್ನ ಪೂರ್ತಿ scan ಮಾಡೋ ಅಗತ್ಯ ಇಲ್ಲ!
     HashMap ಬಳಸಿ "ಈ key ಅ node ಎಲ್ಲಿ" ಅಂತ instant ಆಗಿ ಹುಡುಕ್ಬಹುದು

  💡 Interview ನಲ್ಲಿ ಹೇಗೆ ಮಾತಾಡಬೇಕು:
  →  "First approach: HashMap plus a plain list to track order
      — but removing/reinserting in a list is O(n), too slow"
  →  "Optimal: HashMap (key -> node) plus a doubly linked list
      with dummy head/tail. HashMap gives O(1) lookup, and
      because each node knows its prev AND next, removing it
      from anywhere and re-inserting it at the front is O(1)."

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🏷️ SECTION 3 — TECHNIQUE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Primary   : HashMap + Doubly Linked List with Dummy Head/Tail
              (O(1) get and put)
  Secondary : HashMap + Plain List for Order Tracking (O(n)
              reordering)

  WHY Doubly Linked List over a Plain List?
  → A plain list (or array) can track usage order, but moving
    an accessed key to the "most recent" end requires finding
    it first (O(n) unless you also track its index, and even
    then shifting elements costs O(n)). A DOUBLY linked list
    node knows both its predecessor AND successor, so unlinking
    it from anywhere in the list — and re-inserting it
    elsewhere — is a pure O(1) pointer operation, no scanning
    required. The HashMap maps keys directly to their node
    objects, so there's no searching at all.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 💡 SECTION 4 — INTUITION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  The key insight: this problem needs TWO different superpowers
  at once — "find this key instantly" (a HashMap's specialty)
  and "reorder usage instantly" (a doubly linked list's
  specialty, since removing/inserting a node needs only its
  immediate neighbors, not a scan). Neither alone is enough: a
  HashMap alone has no sense of order; a linked list alone has
  no O(1) lookup. Combined, the HashMap stores key -> node
  references, and the doubly linked list orders those SAME node
  objects by recency — dummy head and tail sentinels remove all
  edge-case checks for "is this the first/last real node."

  The journey from brute to optimal:
    Brute thought   →  HashMap for value lookup, plus a plain
                       Python list recording access order; on
                       each access, remove the key from the list
                       and append it at the end
    Problem with it →  Removing from the MIDDLE of a plain list
                       is O(n) — too slow for frequent access
    Better question →  "Can removing/reinserting a tracked
                       position be made O(1)?"
    Insight         →  A doubly linked list node holds direct
                       references to its neighbors — unlinking
                       and relinking anywhere is O(1), no scan
    Optimal         →  HashMap (key -> node) + doubly linked
                       list with dummy head/tail sentinels — both
                       get and put become O(1)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🐢 SECTION 5 — APPROACH 1 — BRUTE FORCE (HashMap + Plain List Order)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    Keep a dict for key -> value lookups, and a separate plain
    list recording keys in least-to-most-recently-used order.
    On get/put touching a key, remove it from wherever it sits
    in that list (a linear scan) and append it at the end (most
    recent). On put exceeding capacity, pop the list's first
    element (least recently used) and delete it from the dict.

  Pseudocode:
    step 1: cache = {}; order = []  (order[0] = LRU, order[-1] = MRU)
    step 2: def get(key):
    step 3:     if key not in cache: return -1
    step 4:     order.remove(key); order.append(key)
    step 5:     return cache[key]
    step 6: def put(key, value):
    step 7:     if key in cache: order.remove(key)
    step 8:     elif len(cache) >= capacity:
    step 9:         lru_key = order.pop(0); del cache[lru_key]
    step 10:    cache[key] = value; order.append(key)

  Time  : O(n)  →  Why: order.remove(key) does a linear scan to
                        find the key in the list
  Space : O(n)  →  Why: stores n keys in both the dict and the
                        order-tracking list

  ಇದು ಯಾಕೆ ಸಾಕಾಗಲ್ಲ?
    → The problem explicitly requires O(1) AVERAGE time for
      both operations — a linear scan to relocate a key in a
      plain list violates that requirement entirely.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🚀 SECTION 6 — OPTIMAL (HashMap + Doubly Linked List)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    Maintain a doubly linked list with DUMMY head and tail
    sentinel nodes (so the list is never truly empty — no edge
    cases for "removing the only node"). The node right after
    `head` is always the MOST recently used; the node right
    before `tail` is always the LEAST recently used. A HashMap
    maps each key directly to its node object.
    get(key): if present, unlink that node from its current spot
    and reinsert it right after `head` (most recent), return its
    value; else return -1.
    put(key, value): if key exists, update its value and move it
    to most-recent (same as get's reordering). Otherwise, if at
    capacity, remove the node just before `tail` (LRU) from both
    the list and the HashMap; then create a new node, insert it
    right after `head`, and add it to the HashMap.

  Key steps:
    1. class Node: val stores (key, value); has prev, next
    2. head <-> tail dummy sentinels, initially pointing at
       each other
    3. _remove(node): node.prev.next = node.next
                       node.next.prev = node.prev
    4. _insert_front(node): node.prev = head; node.next = head.next
                             head.next.prev = node; head.next = node
    5. get(key):
           if key not in map_: return -1
           node = map_[key]; _remove(node); _insert_front(node)
           return node.value
    6. put(key, value):
           if key in map_: _remove(map_[key])
           elif len(map_) >= capacity:
               lru = tail.prev; _remove(lru); del map_[lru.key]
           new_node = Node(key, value)
           map_[key] = new_node
           _insert_front(new_node)

  ಕನ್ನಡದಲ್ಲಿ ಒಂದು ಸಲ ಹೇಳಿ:
    → "HashMap ಬಳಸಿ key → node reference O(1) ಲ್ಲಿ ಹುಡುಕು.
       doubly linked list ಬಳಸಿ node ಅನ್ನ ಅದರ ಪ್ರಸ್ತುತ ಜಾಗ ಇಂದ
       O(1) ಲ್ಲಿ unlink ಮಾಡಿ, head ಬಳಿ (most recent) O(1) ಲ್ಲಿ
       ಮತ್ತೆ ಸೇರಿಸು. capacity ಮೀರಿದ್ರೆ, tail ಬಳಿ ಇರೋ node
       (LRU) ಅನ್ನ O(1) ಲ್ಲಿ remove ಮಾಡಿ HashMap ಇಂದೂ delete
       ಮಾಡು. dummy head/tail ಇರೋದ್ರಿಂದ 'empty list' edge case
       ಇಲ್ಲ!"

  Time  : O(1)  →  Why: HashMap lookup is O(1); doubly linked
                        list unlink/reinsert needs only
                        pointer updates to immediate neighbors
  Space : O(capacity)  →  Why: the HashMap and linked list each
                        hold at most `capacity` entries at once

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🔍 SECTION 7 — DRY RUN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  cache = LRUCache(2)

  put(1, 1):
    map_ empty, not at capacity -> new_node(1,1), insert at
    front -> list: head <-> [1:1] <-> tail
    map_ = {1: node(1,1)}

  put(2, 2):
    not in map_, not at capacity (len=1 < 2) -> new_node(2,2),
    insert at front -> list: head <-> [2:2] <-> [1:1] <-> tail
    map_ = {1: node(1,1), 2: node(2,2)}

  get(1):
    1 in map_ -> node = node(1,1) -> remove from current spot,
    insert at front
    list: head <-> [1:1] <-> [2:2] <-> tail
    returns 1

  put(3, 3):
    not in map_, AT capacity (len=2 == 2) -> evict LRU = node
    just before tail = node(2,2) -> remove it, del map_[2]
    new_node(3,3), insert at front
    list: head <-> [3:3] <-> [1:1] <-> tail
    map_ = {1: node(1,1), 3: node(3,3)}

  get(2):
    2 not in map_ -> return -1

  put(4, 4):
    not in map_, AT capacity -> evict LRU = node before tail =
    node(1,1) -> remove it, del map_[1]
    new_node(4,4), insert at front
    list: head <-> [4:4] <-> [3:3] <-> tail
    map_ = {3: node(3,3), 4: node(4,4)}

  get(1): 1 not in map_ -> return -1
  get(3): 3 in map_ -> move to front, return 3
  get(4): 4 in map_ -> move to front, return 4

  All results match the example ✓

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 ⚠️ SECTION 8 — EDGE CASES — ಇವನ್ನ ಮರೆಯಬೇಡ!
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  ✓ capacity = 1?                  →  every put after the first
                                       evicts the single existing
                                       key — dummy sentinels
                                       handle this with no
                                       special casing
  ✓ get on a key never put?        →  HashMap miss -> return -1
                                       immediately
  ✓ put on an EXISTING key
    (update, not insert)?          →  must relocate that node to
                                       most-recent AND update its
                                       value — NOT treated as a
                                       fresh insertion (no
                                       eviction should trigger)
  ✓ Repeated get on the SAME key?  →  each call re-moves it to
                                       the front; it never
                                       becomes "stale" just from
                                       being accessed
  ✓ put that exactly fills
    capacity (no eviction yet)?    →  only evict when adding a
                                       BRAND NEW key once already
                                       at capacity — updating an
                                       existing key never evicts

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📊 SECTION 9 — COMPLEXITY SUMMARY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                                  Time (per op)   Space
  Brute (HashMap + plain list)     O(n)            O(n)
  HashMap + doubly linked list      O(1)            O(capacity) ✅

  Time yaake O(1)?    → HashMap gives direct node access; a
                         doubly linked node's prev/next let any
                         unlink+reinsert happen without scanning
  Space yaake O(capacity)? → Both structures hold at most
                         `capacity` entries, by design (eviction
                         keeps it bounded)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🎯 SECTION 10 — PATTERN LEARNED — ಇದರಿಂದ ಕಲಿತದ್ದು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Pattern Name: HashMap + Doubly Linked List (O(1) Access + Order)

  Ee pattern yaavaaga use maadabeeku?
  → ANY design problem needing BOTH instant key lookup AND O(1)
     reordering/eviction by recency or frequency — HashMap alone
     gives lookup but no order; a linked list alone gives order
     but no lookup; TOGETHER (map stores node references) both
     become O(1)
  → Dummy head/tail sentinels are a general trick for ANY doubly
     linked list design — they eliminate every "is this the
     first/last/only node" special case

  Idee pattern beere problemsalli kaanisatte:
  → LFU Cache #460 (same core idea, PLUS a frequency dimension —
     needs a map of frequency -> doubly linked list of nodes at
     that frequency)
  → Design Browser History #1472, Design Linked List #707 (other
     "design a structure with specific O(1)/O(n) operation
     guarantees" problems built on linked-list fundamentals)

  Next time intaha problem bandre naanu modalu idannu think maadtene:
  → "O(1) lookup BEKU, O(1) reorder/evict BEKU anta kekre →
     HashMap ondu alone saladu (order illa), linked list ondu
     alone saladu (lookup illa) — eradu combine madu: map key
     -> node reference, doubly linked list order track madu,
     dummy head/tail haaki edge case thappisu!"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🗣️ SECTION 11 — INTERVIEWALLI HEGE EXPLAIN MAADABEEKU
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  1. Understand:
     "Design a fixed-capacity cache. get/put must both be O(1)
      average time. On exceeding capacity, evict the least
      recently used key."

  2. Brute force:
     "HashMap for value lookup, plus a plain list tracking usage
      order. On access, remove-then-append in the list to mark
      most-recent. O(n) because removing from the middle of a
      list requires a scan."

  3. Optimize:
     "Combine a HashMap (key -> node) with a doubly linked list
      (dummy head/tail sentinels). The node right after head is
      most-recent; right before tail is least-recent. Because
      each node tracks its own prev/next, unlinking it and
      reinserting it at the front is O(1) — no scanning."

  4. Code:
     "_remove(node) patches node.prev.next and node.next.prev.
      _insert_front(node) splices it right after head. get:
      look up in map, remove+reinsert at front, return value.
      put: if key exists, remove old node; elif at capacity,
      evict tail.prev; create new node, map it, insert at front."

  5. Complexity:
     "Time O(1) per operation — HashMap lookup plus constant
      pointer rewiring. Space O(capacity) — both structures stay
      bounded by the cache's size."

  Mukhya: whenever a design problem needs BOTH 'find this
          instantly' and 'reorder/evict instantly,' reach for a
          HashMap mapping keys to linked-list NODE REFERENCES —
          neither structure alone is enough, but together they
          cover both requirements in O(1)!
"""


# ─── Doubly Linked List Node Definition ───────────────────────────
class _Node:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


# ═══════════════════════════════════════════════════════════════════
# BRUTE FORCE — O(n) Time per op | O(n) Space (HashMap + plain list)
# ═══════════════════════════════════════════════════════════════════
class LRUCacheBrute:
    """
    Idu modala aaloochane — dict value lookup ge, plain list
    order track madokke; access aadaga list.remove + append
    (O(n) scan)
    """

    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.order = []

    def get(self, key):
        if key not in self.cache:
            return -1
        self.order.remove(key)
        self.order.append(key)
        return self.cache[key]

    def put(self, key, value):
        if key in self.cache:
            self.order.remove(key)
        elif len(self.cache) >= self.capacity:
            lru_key = self.order.pop(0)
            del self.cache[lru_key]

        self.cache[key] = value
        self.order.append(key)


# ═══════════════════════════════════════════════════════════════════
# OPTIMAL — O(1) Time per op | O(capacity) Space
# (HashMap + Doubly Linked List with dummy head/tail)
# ═══════════════════════════════════════════════════════════════════
class LRUCache:
    """
    Idu final answer — HashMap (key -> node) + doubly linked
    list (dummy head/tail), node unlink/reinsert O(1) alli
    """

    def __init__(self, capacity):
        self.capacity = capacity
        self.map_ = {}
        self.head = _Node()
        self.tail = _Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def _insert_front(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def get(self, key):
        if key not in self.map_:
            return -1

        node = self.map_[key]
        self._remove(node)
        self._insert_front(node)
        return node.value

    def put(self, key, value):
        if key in self.map_:
            self._remove(self.map_[key])
        elif len(self.map_) >= self.capacity:
            lru = self.tail.prev
            self._remove(lru)
            del self.map_[lru.key]

        new_node = _Node(key, value)
        self.map_[key] = new_node
        self._insert_front(new_node)


# ═══════════════════════════════════════════════════════════════════
# TEST CASES
# ═══════════════════════════════════════════════════════════════════
def _run_scenario(cache_cls):
    cache = cache_cls(2)
    cache.put(1, 1)
    cache.put(2, 2)
    assert cache.get(1) == 1
    cache.put(3, 3)                 # evicts key 2
    assert cache.get(2) == -1
    cache.put(4, 4)                 # evicts key 1
    assert cache.get(1) == -1
    assert cache.get(3) == 3
    assert cache.get(4) == 4

    # capacity = 1: every new put evicts the previous key
    cache1 = cache_cls(1)
    cache1.put(1, 10)
    assert cache1.get(1) == 10
    cache1.put(2, 20)
    assert cache1.get(1) == -1
    assert cache1.get(2) == 20

    # updating an existing key should NOT trigger eviction
    cache2 = cache_cls(2)
    cache2.put(1, 1)
    cache2.put(2, 2)
    cache2.put(1, 100)              # update, not insert
    assert cache2.get(1) == 100
    assert cache2.get(2) == 2       # still present, no eviction

    # get on a never-inserted key
    cache3 = cache_cls(2)
    assert cache3.get(99) == -1

    # repeated get on the same key keeps it fresh
    cache4 = cache_cls(2)
    cache4.put(1, 1)
    cache4.put(2, 2)
    cache4.get(1)
    cache4.get(1)
    cache4.put(3, 3)                 # should evict 2, not 1
    assert cache4.get(1) == 1
    assert cache4.get(2) == -1
    assert cache4.get(3) == 3


if __name__ == "__main__":
    _run_scenario(LRUCache)
    _run_scenario(LRUCacheBrute)

    print("All tests passed!")
