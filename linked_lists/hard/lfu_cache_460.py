"""
╔══════════════════════════════════════════════════════════════════╗
║  LFU CACHE                                                        ║
║  LeetCode #460  |  Difficulty: Hard  |  Topic: Linked Lists   ║
║  Link: https://leetcode.com/problems/lfu-cache/                 ║
╚══════════════════════════════════════════════════════════════════╝

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📘 SECTION 1 — PROBLEM UNDERSTANDING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Design a Least Frequently Used (LFU) cache with a fixed
  `capacity`. Unlike LRU (which evicts by RECENCY), LFU evicts
  by USE COUNT — the key accessed the FEWEST times is evicted
  first. If multiple keys tie on the lowest use count, evict
  the LEAST RECENTLY USED among that tied group.

  Implement the LFUCache class:
    - LFUCache(capacity): initialize with positive size
      `capacity`
    - get(key): return the value if `key` exists, else -1.
      A successful get increments that key's use count by 1.
    - put(key, value): update the value if `key` exists
      (incrementing its use count), otherwise insert the new
      key-value pair. If this exceeds `capacity`, evict the
      LEAST frequently used key (ties broken by least recently
      used). A newly inserted key starts with use count 1.

  BOTH get and put must run in O(1) average time complexity.

  Example:
    LFUCache lfu = new LFUCache(2);
    lfu.put(1, 1);    // cache={1=1}, counts={1:1}
    lfu.put(2, 2);    // cache={1=1, 2=2}, counts={1:1, 2:1}
    lfu.get(1);        // returns 1; counts={1:2, 2:1}
    lfu.put(3, 3);      // key 2 has lowest count (1) -> evict 2
                        // cache={1=1, 3=3}, counts={1:2, 3:1}
    lfu.get(2);          // returns -1 (evicted)
    lfu.get(3);           // returns 3; counts={1:2, 3:2}
    lfu.put(4, 4);         // tie between 1 and 3 (count=2 each)
                           // -> evict LRU of the tied group = 1
                           // cache={3=3, 4=4}
    lfu.get(1);             // returns -1 (evicted)
    lfu.get(3);              // returns 3
    lfu.get(4);               // returns 4

  Constraints:
    - 1 <= capacity <= 10^4
    - 0 <= key, value <= 10^9
    - At most 2 * 10^5 calls to get and put combined

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🧠 SECTION 2 — KANGLISH THINKING — ಹೇಗೆ ಯೋಚಿಸಬೇಕು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  Problem odi aada mele namma brain enu think maadabeeku:

  ಹಂತ 1 — Problem ಅರ್ಥ ಮಾಡಿಕೊಳ್ಳಿ
  ┌─────────────────────────────────────────────────────────┐
  │  Input ಏನು ಕೊಡ್ತಾರೆ?  →  capacity, get(key)/put(key,val)  │
  │                           calls                             │
  │  Output ಏನು ಬೇಕು?     →  get → value/-1; put → add/update, │
  │                           capacity ಮೀರಿದ್ರೆ LEAST          │
  │                           FREQUENTLY used evict (tie →     │
  │                           LRU ಇಂದ decide)                  │
  │  Constraints ಏನಿದೆ?   →  ಎರಡೂ operations O(1) AVERAGE!     │
  └─────────────────────────────────────────────────────────┘

  ಹಂತ 2 — ಯಾಕೆ ಇದು tricky? "LRU ಗಿಂತ ಇದು ಹೆಚ್ಚು complex —
           frequency TRACK ಮಾಡ್ಬೇಕು, ಮತ್ತೆ 'same frequency
           ಒಳಗೆ LRU order' ಅನ್ನೂ TRACK ಮಾಡ್ಬೇಕು, ಇಬ್ಬುದ್ದೂ
           O(1) ಲ್ಲಿ!" ಅಂತ ಯೋಚಿಸಿ
  →  LRU Cache ಲ್ಲಿ ಒಂದೇ doubly linked list ಸಾಕಾಗ್ತಿತ್ತು
     (recency ಮಾತ್ರ track ಮಾಡಬೇಕಿತ್ತು). ಇಲ್ಲಿ TWO DIMENSIONS
     — frequency (ಎಷ್ಟು ಸಲ use ಆಯ್ತು) ಮತ್ತು, ಆ ಫ್ರೀಕ್ವೆನ್ಸಿ
     ಒಳಗೆ recency (ಯಾವಾಗ last use ಆಯ್ತು) — ಎರಡೂ ಗೊತ್ತಿರ್ಬೇಕು

  ಹಂತ 3 — ಮೊದಲ simple idea (brute force) ಏನು?
  →  "ಒಂದು dict (key→value), ಒಂದು dict (key→frequency) ಇಟ್ಟುಕೊಂಡ್ರೆ?
      eviction ಬೇಕಾದಾಗ, ಎಲ್ಲಾ keys ಅನ್ನ SCAN ಮಾಡಿ min frequency
      (ಮತ್ತೆ ties ಒಳಗೆ LRU) ಹುಡುಕ್ಕಿದ್ರೆ?"
  →  ಕೆಲಸ ಆಗುತ್ತೆ, ಆದ್ರೆ eviction ಗೆ O(n) scan ಬೇಕಾಗುತ್ತೆ — O(1)
     average ಗೆ ಇದು ಸಾಕಾಗಲ್ಲ

  ಹಂತ 4 — Optimal idea (HashMap of frequency → doubly linked
           list) ಹೇಗೆ ಬರುತ್ತೆ?
  →  "ಪ್ರತಿ frequency count ಗೂ ಒಂದು ಪ್ರತ್ಯೇಕ doubly linked list
      (ಅದೇ frequency ಇರೋ keys ಗಳ LRU order) ಇಟ್ಟುಕೊಂಡ್ರೆ?" ಅಂತ
      ಯೋಚಿಸಿ: freq_map[f] = doubly linked list ಆ keys ಎಲ್ಲಾ
      ಯಾರ frequency = f. ಜೊತೆಗೆ key_map[key] = node (direct
      lookup ಗೆ), ಮತ್ತೆ `min_freq` ಅನ್ನ ಟ್ರ್ಯಾಕ್ ಮಾಡ್ಕೊಳ್ಳಿ
  →  get(key)/put(key existing): key ಅ node ಅನ್ನ ಅದರ ಪ್ರಸ್ತುತ
     freq_map[f] ಇಂದ remove ಮಾಡಿ, freq_map[f+1] ಗೆ ಸೇರಿಸಿ. ಈ
     move ಅ ಹಳೆ list empty ಆಗಿದ್ರೆ ಮತ್ತೆ ಅದೇ min_freq ಆಗಿದ್ರೆ,
     min_freq++ ಮಾಡಿ
  →  eviction: freq_map[min_freq] ಅ list ಅ TAIL (LRU within that
     frequency) ಅನ್ನ remove ಮಾಡಿ

  ಹಂತ 5 — Technique ಯಾಕೆ ಇಲ್ಲಿ ಕೆಲಸ ಮಾಡುತ್ತೆ?
  →  "ಪ್ರತಿ frequency value ಗೂ ಅದರದ್ದೇ doubly linked list"
     ಅನ್ನೋ idea ಇಂದ, LRU Cache ಅ EXACT same O(1) trick (doubly
     linked list node ಗೆ prev/next ಗೊತ್ತಿರೋದ್ರಿಂದ remove/insert
     O(1)) ಅನ್ನ ಪ್ರತಿ frequency "bucket" ಗೂ ಪ್ರತ್ಯೇಕವಾಗಿ ಅನ್ವಯಿಸ್ಬಹುದು!
     min_freq ಅನ್ನ ಟ್ರ್ಯಾಕ್ ಮಾಡಿದ್ರೆ, "least frequently used" ಎಲ್ಲಿ
     ಅಂತ instant ಆಗಿ ಗೊತ್ತಾಗುತ್ತೆ

  💡 Interview ನಲ್ಲಿ ಹೇಗೆ ಮಾತಾಡಬೇಕು:
  →  "First approach: two HashMaps (value, frequency), scan all
      keys to find min-frequency+LRU on eviction — O(n)."
  →  "Optimal: a HashMap mapping frequency -> doubly linked list
      of keys at that frequency (ordered by recency within the
      bucket), PLUS a HashMap mapping key -> its node, PLUS a
      tracked `min_freq`. Access bumps a key from freq bucket f
      to f+1. Eviction removes the tail of the min_freq bucket."

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🏷️ SECTION 3 — TECHNIQUE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Primary   : HashMap (key -> node) + HashMap (freq -> Doubly
              Linked List) + tracked min_freq (O(1) get/put)
  Secondary : Two HashMaps + Full Scan on Eviction (O(n) evict)

  WHY Frequency-Bucketed Doubly Linked Lists over Scanning?
  → Scanning ALL keys to find the minimum frequency (and, among
    ties, the least recently used) is O(n) per eviction — far
    too slow for the required O(1) average. Grouping keys into
    one doubly linked list PER frequency value turns "find the
    least-frequently-used, LRU-tiebroken key" into "look at the
    TAIL of the bucket for min_freq" — an O(1) lookup, exactly
    the same trick LRU Cache uses, just applied per-frequency
    instead of globally.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 💡 SECTION 4 — INTUITION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  The key insight: LFU needs to answer "which key has been used
  LEAST" instantly, with ties broken by "which of THOSE was used
  LEAST RECENTLY." That's really just LRU Cache's exact
  mechanism — doubly linked list, head = most recent, tail =
  least recent — but applied SEPARATELY to each frequency
  value's group of keys, since only keys with the SAME frequency
  can ever tie. Maintaining a running `min_freq` means the
  "global minimum frequency" bucket is always known instantly;
  its tail is the eviction candidate. Every get/put on an
  existing key just moves that key's node from its current
  frequency bucket to the next one up — one bucket's loss, the
  next bucket's gain at its head (most recent).

  The journey from brute to optimal:
    Brute thought   →  Two HashMaps (value, frequency); on
                       eviction, scan every key to find the
                       minimum frequency, breaking ties by
                       tracking recency separately
    Problem with it →  O(n) per eviction — scanning defeats the
                       O(1) average requirement entirely
    Better question →  "Can keys be pre-grouped by frequency so
                       the minimum-frequency group is always
                       known instantly?"
    Insight         →  A HashMap of frequency -> doubly linked
                       list (LRU-ordered within that frequency)
                       makes BOTH dimensions (frequency AND
                       recency-within-frequency) O(1) accessible
    Optimal         →  key -> node HashMap + freq -> DLL HashMap
                       + tracked min_freq: get/put/evict are all
                       O(1) average

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🐢 SECTION 5 — APPROACH 1 — BRUTE FORCE (HashMaps + Full Scan)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    Keep value[key] and freq[key] dicts, plus a `tick` counter
    recording the "time" of each key's last access in
    last_used[key]. On eviction, scan ALL keys to find the one
    with the smallest freq, breaking ties by the smallest
    last_used (oldest access).

  Pseudocode:
    step 1: value = {}; freq = {}; last_used = {}; tick = 0
    step 2: def get(key):
    step 3:     if key not in value: return -1
    step 4:     freq[key] += 1; tick += 1; last_used[key] = tick
    step 5:     return value[key]
    step 6: def put(key, val):
    step 7:     if key in value:
    step 8:         value[key] = val; get(key)  # bump frequency
    step 9:         return
    step 10:    if len(value) >= capacity:
    step 11:        evict_key = min(value, key=lambda k: (freq[k], last_used[k]))
    step 12:        del value[evict_key]; del freq[evict_key]; del last_used[evict_key]
    step 13:    value[key] = val; freq[key] = 1
    step 14:    tick += 1; last_used[key] = tick

  Time  : O(n)  →  Why: eviction scans every key to find the
                        min-frequency, LRU-tiebroken candidate
  Space : O(n)  →  Why: three dicts, each holding up to n entries

  ಇದು ಯಾಕೆ ಸಾಕಾಗಲ್ಲ?
    → Correct, but the eviction scan is O(n) — the required O(1)
      average complexity demands pre-grouping keys by frequency
      instead of scanning everything on every eviction.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🚀 SECTION 6 — OPTIMAL (Frequency-Bucketed Doubly Linked Lists)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    key_map: key -> node (direct O(1) lookup). freq_map: freq ->
    a small doubly-linked-list structure (with its own head/tail
    sentinels) holding all nodes CURRENTLY at that frequency,
    ordered by recency (head = most recent within that bucket).
    Track `min_freq` — the smallest frequency currently present
    anywhere in the cache.
    _bump(node): remove node from freq_map[node.freq]; if that
    bucket is now empty AND was min_freq, increment min_freq;
    increment node.freq; insert node at the head of
    freq_map[node.freq] (creating that bucket if needed).
    get(key): if absent, -1. Else _bump the node, return its value.
    put(key, value): if key exists, update value and _bump it.
    Else, if at capacity, evict the TAIL of freq_map[min_freq]
    (the global LFU, LRU-tiebroken, candidate) from both maps.
    Insert the new key with freq=1 at the head of freq_map[1],
    and reset min_freq to 1 (a brand new key always has the
    lowest possible frequency).

  Key steps:
    1. key_map = {}; freq_map = {}  (freq -> DLinkedList)
       min_freq = 0; capacity = given
    2. def _bump(node):
           old_list = freq_map[node.freq]
           old_list.remove(node)
           if old_list.is_empty() and min_freq == node.freq:
               min_freq += 1
           node.freq += 1
           freq_map.setdefault(node.freq, DLinkedList()).add_front(node)
    3. def get(key):
           if key not in key_map: return -1
           node = key_map[key]; _bump(node)
           return node.value
    4. def put(key, value):
           if key in key_map:
               key_map[key].value = value; _bump(key_map[key])
               return
           if len(key_map) >= capacity:
               lru_node = freq_map[min_freq].remove_tail()
               del key_map[lru_node.key]
           new_node = Node(key, value, freq=1)
           key_map[key] = new_node
           freq_map.setdefault(1, DLinkedList()).add_front(new_node)
           min_freq = 1

  ಕನ್ನಡದಲ್ಲಿ ಒಂದು ಸಲ ಹೇಳಿ:
    → "ಪ್ರತಿ frequency value ಗೂ ಅದರದ್ದೇ doubly linked list
       (recency order ಲ್ಲಿ). key access ಆದಾಗ, ಆ key ಅ node
       ಅನ್ನ ಅದರ ಪ್ರಸ್ತುತ freq bucket ಇಂದ remove ಮಾಡಿ, freq+1
       ಬಕೆಟ್ ಗೆ head ಬಳಿ ಸೇರಿಸು. ಹಳೆ bucket empty ಆಗಿ, ಅದೇ
       min_freq ಆಗಿದ್ರೆ min_freq++ ಮಾಡು. eviction ಬೇಕಾದಾಗ,
       freq_map[min_freq] ಅ TAIL (ಆ frequency ಒಳಗೆ LRU) ಅನ್ನ
       remove ಮಾಡು. ಹೊಸ key ಅಂದ್ರೆ freq=1 bucket ಗೆ ಹಾಕಿ
       min_freq ಅನ್ನ 1 ಗೆ reset ಮಾಡು!"

  Time  : O(1)  →  Why: HashMap lookups plus doubly linked list
                        remove/insert at head/tail — all constant
                        time, no scanning
  Space : O(capacity)  →  Why: key_map and freq_map together
                        hold at most `capacity` nodes total

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🔍 SECTION 7 — DRY RUN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  LFUCache(2)

  put(1,1): key_map={1:node(f=1)}, freq_map={1:[1]}, min_freq=1
  put(2,2): key_map={1,2}, freq_map={1:[2,1]} (2 is more recent,
            at head), min_freq=1

  get(1): _bump node1: remove from freq_map[1] -> freq_map[1]=[2]
          node1.freq=2 -> freq_map[2]=[1]
          min_freq stays 1 (freq_map[1] still has key 2, not empty)
          returns 1

  put(3,3): at capacity (len=2==2) -> evict tail of
            freq_map[min_freq=1] = freq_map[1]=[2] -> evict key 2
            key_map={1,3} (2 removed)
            new node3: freq=1, freq_map[1]=[3], min_freq=1

  get(2): 2 not in key_map -> return -1

  get(3): _bump node3: freq_map[1] loses 3 -> freq_map[1] empty,
          min_freq WAS 1 and bucket now empty -> min_freq becomes
          2 (since node1 lives at freq 2)
          node3.freq=2 -> freq_map[2] = [3,1] (3 at head, most
          recent within freq=2)
          returns 3

  put(4,4): at capacity -> evict tail of freq_map[min_freq=2] =
            freq_map[2]=[3,1] -> tail is node1 (key=1) -> evict
            key 1
            key_map={3,4}; new node4: freq=1, freq_map[1]=[4],
            min_freq=1

  get(1): 1 not in key_map -> return -1
  get(3): returns 3 (bumped to freq=3 now)
  get(4): returns 4 (bumped to freq=2 now)

  All results match the example ✓

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 ⚠️ SECTION 8 — EDGE CASES — ಇವನ್ನ ಮರೆಯಬೇಡ!
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  ✓ capacity = 1?                  →  every new put (once full)
                                       evicts the single existing
                                       key regardless of its
                                       frequency — the only
                                       bucket IS the min_freq
                                       bucket
  ✓ Updating an EXISTING key's
    value via put?                 →  must bump its frequency
                                       too (not just overwrite
                                       the value) — treated
                                       identically to a get in
                                       terms of frequency effects
  ✓ All keys tied at the same
    frequency on eviction?         →  the doubly linked list's
                                       TAIL within that bucket is
                                       the least-recently-used of
                                       the tied group — handled
                                       automatically by bucket
                                       ordering
  ✓ A new key inserted while
    other keys have higher
    frequencies?                   →  new key always starts at
                                       freq=1, and min_freq is
                                       reset to 1 — a fresh key
                                       is always the global LFU
                                       until accessed
  ✓ get() on a key that was
    never put?                     →  key_map miss -> return -1
                                       immediately, no side
                                       effects on any frequency
                                       bucket

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📊 SECTION 9 — COMPLEXITY SUMMARY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                                        Time (per op)   Space
  Brute (HashMaps + full scan evict)     O(n)            O(n)
  Freq-bucketed doubly linked lists       O(1)            O(capacity) ✅

  Time yaake O(1)?    → HashMap lookups are O(1); each bucket's
                         doubly linked list supports O(1)
                         remove/insert since nodes track their
                         own prev/next
  Space yaake O(capacity)? → key_map and freq_map together never
                         hold more than `capacity` nodes, by
                         eviction design

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🎯 SECTION 10 — PATTERN LEARNED — ಇದರಿಂದ ಕಲಿತದ್ದು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Pattern Name: Frequency-Bucketed Doubly Linked Lists (LFU Generalization of LRU)

  Ee pattern yaavaaga use maadabeeku?
  → Any design problem needing eviction by a PRIMARY criterion
     (frequency) with a SECONDARY tiebreaker (recency) — group
     entries into separate doubly linked lists keyed by the
     primary criterion's value, ordered by the secondary
     criterion within each group; track the "best" primary-
     criterion bucket (e.g. min_freq) as a running variable
  → This is literally "LRU Cache's mechanism, applied once per
     frequency value, plus a running minimum tracker" — a direct
     generalization

  Idee pattern beere problemsalli kaanisatte:
  → LRU Cache #146 (the single-dimension ancestor of this
     problem — ONE doubly linked list instead of one PER
     frequency)
  → Design Browser History #1472 (another doubly-linked-list-
     centric design problem, though simpler — a single moving
     cursor rather than frequency buckets)

  Next time intaha problem bandre naanu modalu idannu think maadtene:
  → "Eviction/priority criteria TWO dimensions ide antadre
     (primary + tiebreaker) → LRU cache ina doubly linked list
     trick anna PRIMARY criterion value prakara SEPARATE
     buckets madi apply madu, 'best bucket' (min_freq tara)
     anna running variable alli track madu — O(1) sigutte!"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🗣️ SECTION 11 — INTERVIEWALLI HEGE EXPLAIN MAADABEEKU
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  1. Understand:
     "Design a cache evicting by LOWEST use frequency, with ties
      broken by least-recently-used. get/put both O(1) average."

  2. Brute force:
     "Dicts for value and frequency per key, plus a tick counter
      for recency. On eviction, scan all keys for the minimum
      (frequency, last_used) pair. O(n) per eviction."

  3. Optimize:
     "key -> node HashMap for O(1) lookup. freq -> doubly linked
      list HashMap, where each bucket holds all keys at that
      exact frequency, ordered by recency. Track min_freq. A
      bump moves a node from its current bucket to the next
      frequency's bucket (at the head). Eviction removes the
      tail of the min_freq bucket."

  4. Code:
     "_bump(node): remove from freq_map[node.freq]; if that
      bucket empties and was min_freq, increment min_freq;
      node.freq += 1; insert at head of (new) freq_map[node.freq].
      get: look up, bump, return value. put: if exists, update +
      bump; else, evict tail of freq_map[min_freq] if at
      capacity, insert new node at freq=1, reset min_freq=1."

  5. Complexity:
     "Time O(1) — HashMap lookups plus constant-time doubly
      linked list operations. Space O(capacity) — bounded by
      eviction."

  Mukhya: LFU is just LRU's doubly-linked-list trick applied
          PER FREQUENCY VALUE, with a running min_freq pointer
          telling you which bucket to evict from — the same
          'node knows its neighbors' insight, one dimension up!
"""


# ─── Doubly Linked List Node Definition (key, value, frequency) ──
class _Node:
    def __init__(self, key=0, value=0, freq=1):
        self.key = key
        self.value = value
        self.freq = freq
        self.prev = None
        self.next = None


# ─── A small doubly linked list with dummy head/tail sentinels ───
class _DLinkedList:
    def __init__(self):
        self.head = _Node()
        self.tail = _Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def add_front(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node
        self.size += 1

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        self.size -= 1

    def remove_tail(self):
        if self.size == 0:
            return None
        lru = self.tail.prev
        self.remove(lru)
        return lru

    def is_empty(self):
        return self.size == 0


# ═══════════════════════════════════════════════════════════════════
# BRUTE FORCE — O(n) Time per op | O(n) Space (HashMaps + full scan)
# ═══════════════════════════════════════════════════════════════════
class LFUCacheBrute:
    """
    Idu modala aaloochane — value/freq/last_used dicts, eviction
    ge ella keys scan madi min (freq, last_used) hudu
    """

    def __init__(self, capacity):
        self.capacity = capacity
        self.value = {}
        self.freq = {}
        self.last_used = {}
        self.tick = 0

    def get(self, key):
        if key not in self.value:
            return -1
        self.freq[key] += 1
        self.tick += 1
        self.last_used[key] = self.tick
        return self.value[key]

    def put(self, key, value):
        if self.capacity == 0:
            return

        if key in self.value:
            self.value[key] = value
            self.get(key)
            return

        if len(self.value) >= self.capacity:
            evict_key = min(
                self.value, key=lambda k: (self.freq[k], self.last_used[k])
            )
            del self.value[evict_key]
            del self.freq[evict_key]
            del self.last_used[evict_key]

        self.value[key] = value
        self.freq[key] = 1
        self.tick += 1
        self.last_used[key] = self.tick


# ═══════════════════════════════════════════════════════════════════
# OPTIMAL — O(1) Time per op | O(capacity) Space
# (HashMap key->node + HashMap freq->DoublyLinkedList + min_freq)
# ═══════════════════════════════════════════════════════════════════
class LFUCache:
    """
    Idu final answer — key_map (key->node) + freq_map
    (freq->doubly linked list) + min_freq track madi O(1) alli
    get/put/evict
    """

    def __init__(self, capacity):
        self.capacity = capacity
        self.key_map = {}
        self.freq_map = {}
        self.min_freq = 0

    def _bump(self, node):
        old_list = self.freq_map[node.freq]
        old_list.remove(node)

        if old_list.is_empty() and self.min_freq == node.freq:
            self.min_freq += 1

        node.freq += 1
        if node.freq not in self.freq_map:
            self.freq_map[node.freq] = _DLinkedList()
        self.freq_map[node.freq].add_front(node)

    def get(self, key):
        if key not in self.key_map:
            return -1

        node = self.key_map[key]
        self._bump(node)
        return node.value

    def put(self, key, value):
        if self.capacity == 0:
            return

        if key in self.key_map:
            node = self.key_map[key]
            node.value = value
            self._bump(node)
            return

        if len(self.key_map) >= self.capacity:
            lru_node = self.freq_map[self.min_freq].remove_tail()
            del self.key_map[lru_node.key]

        new_node = _Node(key, value, freq=1)
        self.key_map[key] = new_node
        if 1 not in self.freq_map:
            self.freq_map[1] = _DLinkedList()
        self.freq_map[1].add_front(new_node)
        self.min_freq = 1


# ═══════════════════════════════════════════════════════════════════
# TEST CASES
# ═══════════════════════════════════════════════════════════════════
def _run_scenario(cache_cls):
    cache = cache_cls(2)
    cache.put(1, 1)
    cache.put(2, 2)
    assert cache.get(1) == 1
    cache.put(3, 3)                 # evicts key 2 (freq=1, LFU)
    assert cache.get(2) == -1
    assert cache.get(3) == 3
    cache.put(4, 4)                 # tie at freq=2 between 1,3 -> evict 1 (LRU)
    assert cache.get(1) == -1
    assert cache.get(3) == 3
    assert cache.get(4) == 4

    # capacity = 1: every new put evicts the sole existing key
    c1 = cache_cls(1)
    c1.put(1, 10)
    assert c1.get(1) == 10
    c1.put(2, 20)
    assert c1.get(1) == -1
    assert c1.get(2) == 20

    # updating an existing key bumps its frequency
    c2 = cache_cls(2)
    c2.put(1, 1)
    c2.put(2, 2)
    c2.put(1, 100)                   # update -> bumps freq of key 1
    c2.put(3, 3)                     # key 2 still at freq=1 -> evicted
    assert c2.get(2) == -1
    assert c2.get(1) == 100
    assert c2.get(3) == 3

    # get on a never-inserted key
    c3 = cache_cls(2)
    assert c3.get(99) == -1

    # new key always starts as the global LFU
    c4 = cache_cls(2)
    c4.put(1, 1)
    c4.get(1)
    c4.get(1)                        # key 1 now freq=3
    c4.put(2, 2)                     # key 2 freq=1
    c4.put(3, 3)                     # evicts key 2 (freq=1 < key1's freq=3)
    assert c4.get(2) == -1
    assert c4.get(1) == 1
    assert c4.get(3) == 3


if __name__ == "__main__":
    _run_scenario(LFUCache)
    _run_scenario(LFUCacheBrute)

    print("All tests passed!")
