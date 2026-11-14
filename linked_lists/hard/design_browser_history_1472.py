"""
╔══════════════════════════════════════════════════════════════════╗
║  DESIGN BROWSER HISTORY                                           ║
║  LeetCode #1472  |  Difficulty: Medium  |  Topic: Linked Lists   ║
║  (Grouped here with Hard per the curriculum checklist)          ║
║  Link: https://leetcode.com/problems/                           ║
║        design-browser-history/                                   ║
╚══════════════════════════════════════════════════════════════════╝

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📘 SECTION 1 — PROBLEM UNDERSTANDING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Design a browser's history system, starting on `homepage`.

  Implement the BrowserHistory class:
    - BrowserHistory(homepage): initializes with `homepage` as
      the current page
    - visit(url): visits `url` from the CURRENT page. This
      clears up ALL the forward history (anything you could
      have gone "forward" to before is now gone).
    - back(steps): move `steps` back in history. If there
      aren't that many pages to go back, land on the EARLIEST
      page possible. Return the URL after moving.
    - forward(steps): move `steps` forward in history. If there
      aren't that many pages to go forward, land on the MOST
      RECENT page possible. Return the URL after moving.

  Input : a homepage string, followed by a sequence of visit /
          back / forward calls
  Output: for back/forward calls, the URL landed on

  Example:
    BrowserHistory browserHistory = new BrowserHistory("leetcode.com");
    browserHistory.visit("google.com");       // leetcode.com -> google.com
    browserHistory.visit("facebook.com");     // google.com -> facebook.com
    browserHistory.visit("youtube.com");      // facebook.com -> youtube.com
    browserHistory.back(1);                   // facebook.com -> returns "facebook.com"
    browserHistory.back(1);                   // google.com -> returns "google.com"
    browserHistory.forward(1);                 // facebook.com -> returns "facebook.com"
    browserHistory.visit("linkedin.com");      // clears forward history from facebook.com
                                                // facebook.com -> linkedin.com
    browserHistory.forward(2);                  // no forward history, stay at
                                                 // linkedin.com, returns "linkedin.com"
    browserHistory.back(2);                      // linkedin.com -> google.com,
                                                  // returns "google.com"
    browserHistory.back(7);                       // more steps than available,
                                                   // lands on leetcode.com,
                                                   // returns "leetcode.com"

  Constraints:
    - 1 <= homepage.length, url.length <= 20
    - 1 <= steps <= 100
    - At most 5000 calls total to visit, back, and forward

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🧠 SECTION 2 — KANGLISH THINKING — ಹೇಗೆ ಯೋಚಿಸಬೇಕು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  Problem odi aada mele namma brain enu think maadabeeku:

  ಹಂತ 1 — Problem ಅರ್ಥ ಮಾಡಿಕೊಳ್ಳಿ
  ┌─────────────────────────────────────────────────────────┐
  │  Input ಏನು ಕೊಡ್ತಾರೆ?  →  homepage, visit/back/forward     │
  │                           calls                             │
  │  Output ಏನು ಬೇಕು?     →  back/forward → landed-on URL;    │
  │                           visit → forward history CLEAR    │
  │  Constraints ಏನಿದೆ?   →  steps ಮೀರಿದ್ರೆ earliest/latest    │
  │                           page ಗೆ clamp ಆಗ್ಬೇಕು              │
  └─────────────────────────────────────────────────────────┘

  ಹಂತ 2 — ಯಾಕೆ ಇದು tricky? "visit ಮಾಡಿದ ಮೇಲೆ forward history
           ಪೂರ್ತಿ ಅಳಿಸಿ ಹೋಗ್ಬೇಕು — ಇದ್ಕೆ sarathi structure ಏನು
           ಬೇಕು?" ಅಂತ ಯೋಚಿಸಿ
  →  ಇದು EXACTLY ಒಂದು DOUBLY linked list ತರ! current page ಅ
     prev side = back history, next side = forward history.
     ಹೊಸ visit ಅಂದ್ರೆ current ಅ next (forward history) ಅನ್ನ
     ಪೂರ್ತಿ ಕತ್ತರಿಸಿ, ಹೊಸ node ಸೇರಿಸೋದು!

  ಹಂತ 3 — ಮೊದಲ simple idea (brute force) ಏನು?
  →  "ಒಂದು ARRAY (history) ಮತ್ತು ಒಂದು 'current index' pointer
      ಇಟ್ಟುಕೊಂಡ್ರೆ? visit ಮಾಡಿದಾಗ current index ಗಿಂತ ಮುಂದಿರೋ
      ಎಲ್ಲಾ elements ಅನ್ನ TRUNCATE ಮಾಡಿ, ಹೊಸ url ಸೇರಿಸಿ, back/
      forward ಅಂದ್ರೆ ಕೇವಲ index ಅನ್ನ clamp ಮಾಡಿ ಬದಲಾಯಿಸಿದ್ರೆ?"
  →  ಇದು ಕೂಡ ಸುಲಭ ಮತ್ತು ಸರಿಯಾಗಿ ಕೆಲಸ ಮಾಡುತ್ತೆ! ಆದ್ರೆ visit ಗೆ
     truncate (ಬಹುಶಃ O(n) worst case list slicing) ಬೇಕಾಗ್ಬಹುದು

  ಹಂತ 4 — Optimal idea (Doubly Linked List) ಹೇಗೆ ಬರುತ್ತೆ?
  →  "ಪ್ರತಿ page ಅನ್ನ ಒಂದು DOUBLY linked list node ಅಂತ ಮಾಡಿ,
      current ಅನ್ನ track ಮಾಡಿದ್ರೆ?" ಅಂತ ಯೋಚಿಸಿ: visit(url) →
      current.next = new_node (ಹಳೆ forward history automatic
      ಆಗಿ 'orphan' ಆಗುತ್ತೆ, garbage collected!), current = new_node.
      back(steps)/forward(steps): current ಅನ್ನ prev/next
      direction ಲ್ಲಿ steps ಅಷ್ಟು ಅಥವಾ ಸಾಧ್ಯ ಆಗೋವಷ್ಟು ಮುಂದೆ/ಹಿಂದೆ
      ಸಾಗಿಸಿ

  ಹಂತ 5 — Technique ಯಾಕೆ ಇಲ್ಲಿ ಕೆಲಸ ಮಾಡುತ್ತೆ?
  →  "visit ಮಾಡಿದಾಗ current.next = new_node" ಅಂತ ಬರೀ ONE
     pointer ಬದಲಾಯಿಸಿದ್ರೆ, ಹಳೆ forward chain ಗೆ ಯಾರೂ reference
     ಇಲ್ಲ ಆಗೋದ್ರಿಂದ ಅದನ್ನ "clear" ಮಾಡಿದ ಹಾಗೇ ಆಯ್ತು — explicit
     delete/truncate ಬೇಡ! back/forward ಕೇವಲ current.prev ಅಥವಾ
     current.next ಅನ್ನ follow ಮಾಡಿದ್ರೆ ಸಾಕು, ಪ್ರತಿ step O(1)

  💡 Interview ನಲ್ಲಿ ಹೇಗೆ ಮಾತಾಡಬೇಕು:
  →  "First approach: array + current index, truncating forward
      entries on a new visit — simple, but truncation can be
      O(n) in the worst case."
  →  "Optimal: model history as a doubly linked list where
      `current` is a pointer into it. visit() creates a new node
      after current and REPOINTS current.next, automatically
      discarding the old forward chain. back/forward just walk
      `current` along prev/next pointers, clamping at the ends."

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🏷️ SECTION 3 — TECHNIQUE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Primary   : Doubly Linked List with a "current" Pointer
  Secondary : Array + Current Index (with truncation on visit)

  WHY Doubly Linked List over Array + Index?
  → The array approach is perfectly valid and simple, but
    discarding forward history on a new visit means slicing
    the array (or at least conceptually truncating it), and a
    naive implementation may do O(n) work or waste memory
    keeping old entries around. A doubly linked list discards
    old forward history for FREE — just repoint current.next to
    a new node, and the old chain becomes unreachable. Walking
    back/forward is a direct O(1)-per-step pointer following,
    identical in spirit to walking any doubly linked list.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 💡 SECTION 4 — INTUITION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  The key insight: a browser's history is LITERALLY a doubly
  linked list in disguise — "back" means "go to prev," "forward"
  means "go to next," and "visit a new page" means "cut off
  everything after here, and attach one new page." A doubly
  linked list node naturally supports both directions (prev AND
  next), so walking back/forward costs just one pointer hop per
  step. And because `current.next = new_node` simply REPLACES
  whatever the old next pointer was, any previously-forward
  pages become unreachable automatically — no explicit cleanup
  needed, Python's garbage collector takes care of it.

  The journey from brute to optimal:
    Brute thought   →  Keep a Python list of visited URLs plus
                       a current index; visit() truncates
                       everything after the index before
                       appending; back/forward just clamp and
                       move the index
    Problem with it →  Truncating a list (or managing array
                       bounds carefully) adds overhead and
                       conceptual complexity that a linked
                       structure sidesteps entirely
    Better question →  "Isn't 'go back/forward, cut off forward
                       history on a new action' EXACTLY what a
                       doubly linked list with a moving pointer
                       already does?"
    Insight         →  Model each page as a node with prev/next;
                       `current` is just a pointer that moves
                       along the chain; visiting repoints
                       current.next, discarding the old forward
                       chain implicitly
    Optimal         →  Doubly linked list + `current` pointer:
                       visit is O(1), back/forward are O(steps)
                       each (bounded by how far you can actually
                       move)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🐢 SECTION 5 — APPROACH 1 — BRUTE FORCE (Array + Current Index)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    Keep a Python list `history` of visited URLs and an integer
    `current` index into it. visit(url): truncate history to
    keep only entries up to and including the current index,
    then append the new url and advance current. back(steps):
    move current back by steps, clamped at 0. forward(steps):
    move current forward by steps, clamped at the last index.

  Pseudocode:
    step 1: history = [homepage]; current = 0
    step 2: def visit(url):
    step 3:     history = history[:current+1]
    step 4:     history.append(url); current += 1
    step 5: def back(steps):
    step 6:     current = max(0, current - steps)
    step 7:     return history[current]
    step 8: def forward(steps):
    step 9:     current = min(len(history)-1, current + steps)
    step 10:    return history[current]

  Time  : O(n)  →  Why: visit() may need to truncate/copy part
                        of the history list in the worst case
  Space : O(n)  →  Why: stores every visited URL in the history
                        list (bounded by total visit calls)

  ಇದು ಯಾಕೆ ಸಾಕಾಗಲ್ಲ?
    → It's actually a reasonably efficient and common real-world
      solution, but truncating a Python list (history[:current+1])
      recreates a new list each time, which is O(k) where k is
      the truncated length — the linked-list approach avoids
      that recreation entirely by just repointing one pointer.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🚀 SECTION 6 — OPTIMAL (Doubly Linked List with Current Pointer)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    Each visited page is a doubly linked list node (prev, next,
    url). Maintain a `current` pointer into this chain.
    visit(url): create a new node, link current.next to it and
    its prev back to current — this REPLACES whatever current's
    old `next` pointed to, discarding the old forward chain.
    Advance current to the new node.
    back(steps): move current backward via .prev, up to `steps`
    times or until there's no more prev (clamping at the
    earliest page).
    forward(steps): move current forward via .next, similarly
    clamped at the most recent page.

  Key steps:
    1. class Node: url, prev=None, next=None
    2. __init__(homepage): current = Node(homepage)
    3. visit(url):
           new_node = Node(url)
           new_node.prev = current
           current.next = new_node
           current = new_node
    4. back(steps):
           while steps > 0 and current.prev:
               current = current.prev
               steps -= 1
           return current.url
    5. forward(steps):
           while steps > 0 and current.next:
               current = current.next
               steps -= 1
           return current.url

  ಕನ್ನಡದಲ್ಲಿ ಒಂದು ಸಲ ಹೇಳಿ:
    → "ಪ್ರತಿ page ಒಂದು doubly linked list node. visit ಮಾಡಿದಾಗ,
       ಹೊಸ node ಅನ್ನ current ಅ ಮುಂದೆ ಜೋಡಿಸಿ, current ಅನ್ನ ಅದಕ್ಕೆ
       ಮುಂದೆ ಸಾಗಿಸು — ಹಳೆ forward chain ಗೆ ಯಾರೂ reference
       ಇಲ್ಲ ಆಗೋದ್ರಿಂದ automatic ಆಗಿ 'ಮುಗಿಯುತ್ತೆ'. back/forward
       ಅಂದ್ರೆ current ಅನ್ನ prev/next ಇಂದ steps ಅಷ್ಟು (ಅಥವಾ
       ಸಾಧ್ಯ ಆಗೋವಷ್ಟು) ಸಾಗಿಸಿ, ಅದರ url return ಮಾಡು!"

  Time  : O(1)   →  Why: visit() does a constant number of
                         pointer updates
         O(steps) →  Why: back/forward walk at most `steps`
                         pointer hops (or fewer, if clamped)
  Space : O(1) per operation →  Why: each visit allocates exactly
                         one new node; no bulk copying ever happens

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🔍 SECTION 7 — DRY RUN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  BrowserHistory("leetcode.com")
    current = Node("leetcode.com")  [chain: leetcode.com]

  visit("google.com"):
    new_node = Node("google.com"); new_node.prev = current
    current.next = new_node; current = new_node
    chain: leetcode.com <-> google.com (current is google.com)

  visit("facebook.com"):
    chain: leetcode.com <-> google.com <-> facebook.com
    (current is facebook.com)

  visit("youtube.com"):
    chain: leetcode.com <-> google.com <-> facebook.com <-> youtube.com
    (current is youtube.com)

  back(1):
    current = current.prev = facebook.com; steps exhausted
    return "facebook.com" ✓

  back(1):
    current = current.prev = google.com; steps exhausted
    return "google.com" ✓

  forward(1):
    current = current.next = facebook.com; steps exhausted
    return "facebook.com" ✓

  visit("linkedin.com"):
    new_node = Node("linkedin.com"); new_node.prev = current (facebook.com)
    current.next = new_node  <- this OVERWRITES facebook.com's old
                                 next (which was youtube.com) —
                                 youtube.com is now unreachable!
    current = new_node
    chain (reachable from current backward): leetcode.com <->
    google.com <-> facebook.com <-> linkedin.com

  forward(2):
    current.next is None (linkedin.com is the last node) ->
    loop doesn't execute, stay at linkedin.com
    return "linkedin.com" ✓

  back(2):
    current = facebook.com (1 step), current = google.com (2 steps)
    return "google.com" ✓

  back(7):
    current = leetcode.com (1 step), current.prev is None -> stop
    return "leetcode.com" ✓

  All results match the example ✓

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 ⚠️ SECTION 8 — EDGE CASES — ಇವನ್ನ ಮರೆಯಬೇಡ!
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  ✓ back/forward called with no
    history in that direction?    →  the while loop condition
                                      (current.prev / current.next
                                      being None) stops movement
                                      immediately, no crash
  ✓ steps larger than available
    history in that direction?    →  loop naturally clamps at
                                      the earliest/latest node —
                                      no need to pre-compute how
                                      many steps are "valid"
  ✓ visit() called right after
    a back() (mid-history)?       →  current.next gets
                                      OVERWRITTEN with the new
                                      node, silently discarding
                                      whatever forward chain
                                      existed — exactly the
                                      required behavior
  ✓ Very first call is back()
    or forward() with no visits
    yet?                          →  current.prev and
                                      current.next are both None
                                      from init — stays on
                                      homepage, returns it
  ✓ Many consecutive visits with
    no back/forward in between?   →  each visit just extends the
                                      chain forward one node at a
                                      time — no special handling
                                      needed

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📊 SECTION 9 — COMPLEXITY SUMMARY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                                      visit     back/forward
  Brute (array + current index)       O(n)      O(1)
  Doubly linked list + pointer         O(1)      O(steps)  ← use
                                                             this ✅

  visit yaake O(1) (linked list)?  → Only a constant number of
                                      pointer updates, no copying
  back/forward yaake O(steps)?     → Walks at most `steps`
                                      pointer hops, naturally
                                      clamped by None checks

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🎯 SECTION 10 — PATTERN LEARNED — ಇದರಿಂದ ಕಲಿತದ್ದು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Pattern Name: Doubly Linked List as a "Moving Cursor" History

  Ee pattern yaavaaga use maadabeeku?
  → Any "undo/redo," "back/forward," or "linear history with a
     current position" design problem — model it as a doubly
     linked list where a `current` pointer moves along prev/next,
     and taking a NEW action simply repoints current.next,
     implicitly discarding any old "redo" chain
  → Classic real-world analogues: browser history, text editor
     undo/redo stacks, media player playlist navigation

  Idee pattern beere problemsalli kaanisatte:
  → LRU Cache #146 (same "HashMap/structure + doubly linked list"
     design family, though LRU's list tracks RECENCY rather than
     a single moving cursor)
  → Flatten a Multilevel Doubly Linked List #430 (another
     doubly-linked-list-centric design/manipulation problem)

  Next time intaha problem bandre naanu modalu idannu think maadtene:
  → "Back/forward, undo/redo, ya 'current position in a linear
     history' design madabekagidre → doubly linked list + ondu
     'current' pointer use madu. Hosa action thogondre,
     current.next anna simply REPOINT madu — hazhe forward/redo
     chain automatic aagi discard aagutte, explicit cleanup
     bedave illa!"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🗣️ SECTION 11 — INTERVIEWALLI HEGE EXPLAIN MAADABEEKU
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  1. Understand:
     "Model a browser's back/forward history. visit() clears any
      forward history. back/forward move a 'current' position,
      clamping at the earliest/latest page if steps exceed what's
      available."

  2. Brute force:
     "A Python list of URLs plus a current index. visit()
      truncates everything after the current index, then
      appends. back/forward clamp and move the index. Simple,
      but truncation isn't free."

  3. Optimize:
     "Model each page as a doubly linked list node with a moving
      `current` pointer. visit() creates a new node right after
      current and repoints current.next to it — any old forward
      chain becomes unreachable automatically. back/forward just
      walk current along .prev/.next, stopping early if there's
      nowhere further to go."

  4. Code:
     "Node has url, prev, next. visit: new_node.prev=current;
      current.next=new_node; current=new_node. back/forward:
      loop up to `steps` times, following .prev or .next while
      it exists; return current.url."

  5. Complexity:
     "visit is O(1) — constant pointer work. back/forward are
      O(steps) — bounded by how far there is to actually move."

  Mukhya: ANY 'linear history with a movable current position,
          and new actions erase redo/forward history' design
          problem is a doubly linked list with a moving cursor —
          repointing current.next on a new action is all it
          takes to 'clear' the old forward chain!
"""


# ─── Doubly Linked List Node Definition ───────────────────────────
class _Node:
    def __init__(self, url):
        self.url = url
        self.prev = None
        self.next = None


# ═══════════════════════════════════════════════════════════════════
# BRUTE FORCE — visit O(n) | back/forward O(1) (array + current index)
# ═══════════════════════════════════════════════════════════════════
class BrowserHistoryBrute:
    """
    Idu modala aaloochane — history array + current index,
    visit aadaga forward entries truncate madi append madu
    """

    def __init__(self, homepage):
        self.history = [homepage]
        self.current = 0

    def visit(self, url):
        self.history = self.history[:self.current + 1]
        self.history.append(url)
        self.current += 1

    def back(self, steps):
        self.current = max(0, self.current - steps)
        return self.history[self.current]

    def forward(self, steps):
        self.current = min(len(self.history) - 1, self.current + steps)
        return self.history[self.current]


# ═══════════════════════════════════════════════════════════════════
# OPTIMAL — visit O(1) | back/forward O(steps)
# (doubly linked list with a moving current pointer)
# ═══════════════════════════════════════════════════════════════════
class BrowserHistory:
    """
    Idu final answer — doubly linked list + current pointer,
    visit madaga current.next anna repoint madi forward chain
    discard madu
    """

    def __init__(self, homepage):
        self.current = _Node(homepage)

    def visit(self, url):
        new_node = _Node(url)
        new_node.prev = self.current
        self.current.next = new_node
        self.current = new_node

    def back(self, steps):
        while steps > 0 and self.current.prev:
            self.current = self.current.prev
            steps -= 1
        return self.current.url

    def forward(self, steps):
        while steps > 0 and self.current.next:
            self.current = self.current.next
            steps -= 1
        return self.current.url


# ═══════════════════════════════════════════════════════════════════
# TEST CASES
# ═══════════════════════════════════════════════════════════════════
def _run_scenario(cls):
    bh = cls("leetcode.com")
    bh.visit("google.com")
    bh.visit("facebook.com")
    bh.visit("youtube.com")
    assert bh.back(1) == "facebook.com"
    assert bh.back(1) == "google.com"
    assert bh.forward(1) == "facebook.com"
    bh.visit("linkedin.com")
    assert bh.forward(2) == "linkedin.com"
    assert bh.back(2) == "google.com"
    assert bh.back(7) == "leetcode.com"

    # back/forward with no history in that direction yet
    bh2 = cls("home.com")
    assert bh2.back(5) == "home.com"
    assert bh2.forward(5) == "home.com"

    # visit after a back, mid-history, clears forward chain
    bh3 = cls("a.com")
    bh3.visit("b.com")
    bh3.visit("c.com")
    bh3.back(1)                     # now at b.com
    bh3.visit("d.com")              # clears c.com from forward history
    assert bh3.forward(5) == "d.com"
    assert bh3.back(1) == "b.com"
    assert bh3.back(1) == "a.com"

    # many consecutive visits, no back/forward
    bh4 = cls("x.com")
    bh4.visit("y.com")
    bh4.visit("z.com")
    assert bh4.back(2) == "x.com"
    assert bh4.forward(2) == "z.com"


if __name__ == "__main__":
    _run_scenario(BrowserHistory)
    _run_scenario(BrowserHistoryBrute)

    print("All tests passed!")
