"""
╔══════════════════════════════════════════════════════════════════╗
║  JUMP GAME II                                                     ║
║  LeetCode #45  |  Difficulty: Medium  |  Topic: Arrays / Greedy   ║
║  Link: https://leetcode.com/problems/jump-game-ii/                 ║
╚══════════════════════════════════════════════════════════════════╝

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📘 SECTION 1 — PROBLEM UNDERSTANDING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Same setup as Jump Game (#55) — nums[i] is the max jump length from
  index i — but now find the MINIMUM number of jumps needed to reach
  the last index. It's guaranteed the last index is always reachable.

  Input : nums = [2, 3, 1, 1, 4]
  Output: 2

  Example 1 — basic:
    Input : nums = [2, 3, 1, 1, 4]
    Output: 2
    Why?  : jump from index 0 to index 1 (1 jump), then from index 1
             (value 3) straight to the last index (1 more jump) — total 2

  Example 2 — slightly tricky (needs multiple small jumps):
    Input : nums = [1, 1, 1, 1]
    Output: 3
    Why?  : every jump is exactly length 1, so reaching index 3 from
             index 0 forces exactly 3 individual jumps — no shortcuts
             available since nums[i]=1 everywhere

  Constraints:
    - 1 <= nums.length <= 10^4
    - 0 <= nums[i] <= 1000
    - It's guaranteed you can reach nums[n-1]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🧠 SECTION 2 — KANGLISH THINKING — ಹೇಗೆ ಯೋಚಿಸಬೇಕು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  ಮೊದಲು problem odidaga ನಮ್ಮ brain ಏನು think ಮಾಡಬೇಕು:

  ಹಂತ 1 — Problem ಅರ್ಥ ಮಾಡಿಕೊಳ್ಳಿ (What are they asking?)
  ┌─────────────────────────────────────────────────────────┐
  │  Input ಏನು ಕೊಡ್ತಾರೆ?  →  ಪ್ರತಿ index ಗೂ max jump length     │
  │  Output ಏನು ಬೇಕು?     →  last index reach ಆಗೋಕೆ minimum    │
  │                          jumps ಎಷ್ಟು ಬೇಕು                  │
  │  Constraints ಏನಿದೆ?   →  n<=10^4, last index reachable ಅಂತ │
  │                          guarantee ಇದೆ (Jump Game #55 ಗಿಂತ  │
  │                          ಬೇರೆ — "ಆಗುತ್ತಾ" ಅಲ್ಲ, "ಎಷ್ಟು" ಬೇಕು)│
  └─────────────────────────────────────────────────────────┘

  ಹಂತ 2 — ನನಗೆ ಗೊತ್ತಿರೋ simple way ಏನು? (Brute force thought)
  →  BFS ಥರ ಯೋಚಿಸಿ — level 0 ಇಂದ level 1 reach ಆಗೋ ಎಲ್ಲಾ indices, ಆಮೇಲೆ
     level 2... ಅಂತ, last index ಯಾವ level ನಲ್ಲಿ ಸಿಗುತ್ತೆ ಅಂತ ನೋಡೋದು.
     ಅಥವಾ recursion ಇಂದ ಪ್ರತಿ jump length try ಮಾಡಿ min ತಗೋಳೋದು.
  →  ಆದರೆ ಇದು slow ಯಾಕೆ? → Naive recursion exponential O(2^n). Naive
     BFS ಸಹ ಪ್ರತಿ level ಗೂ ಎಲ್ಲಾ neighbors re-check ಮಾಡಿದ್ರೆ O(n²) ಆಗ್ಬೋದು.

  ಹಂತ 3 — Better way ಹೇಗೆ ಯೋಚಿಸುವುದು? (Optimization thought)
  →  "Jump Game #55 ನಲ್ಲಿ 'farthest reachable' track ಮಾಡಿದ್ವಿ. ಇಲ್ಲಿ
     ಸಹ ಅದೇ idea use ಮಾಡ್ಬಹುದಾ, ಆದ್ರೆ 'level' (jump count) ಸಹ track
     ಮಾಡ್ತಾ?"
  →  ಅಹಾ moment: ಇದು implicit BFS! "current jump ನ boundary" (current
     jump ಇಂದ reach ಆಗೋ farthest index) ಮುಟ್ಟಿದ ತಕ್ಷಣ, ಜಂಪ್ count
     increment ಮಾಡಿ, ಆ boundary ಅನ್ನ "next jump ನ farthest" ಗೆ ಸೆಟ್
     ಮಾಡ್ಬೇಕು. ಪ್ರತಿ index ಗೂ farthest track ಮಾಡ್ತಾ ಹೋಗಿ, current
     boundary ಮುಟ್ಟಿದಾಗ ಮಾತ್ರ jump++ ಮಾಡಿ boundary ಅನ್ನ farthest ಗೆ
     update ಮಾಡಿದ್ರೆ, ಇಡೀ array ಒಂದೇ pass ನಲ್ಲಿ min jumps ಸಿಗುತ್ತೆ!
  →  ಇದರಿಂದ ನಾವು Greedy → Implicit BFS (Track Current Boundary +
     Farthest) use ಮಾಡಬಹುದು!

  ಹಂತ 4 — Technique ಯಾಕೆ ಇಲ್ಲಿ ಕೆಲಸ ಮಾಡುತ್ತೆ?
  →  BFS level ಗಳೇ "minimum jumps" ಗೆ ಸಮಾನ — ಪ್ರತಿ level ಎಷ್ಟು
     indices reach ಮಾಡುತ್ತೋ ಅಷ್ಟೂ ಒಂದೇ jump count ಒಳಗೆ ಬರುತ್ತೆ.
  →  "current boundary" ಅನ್ನ track ಮಾಡಿದ್ರೆ, explicit queue ಬೇಡ —
     ಒಂದೇ linear scan ಸಾಕು.
  →  Greedy ಇಲ್ಲಿ correct ಆಗುತ್ತೆ ಯಾಕಂದ್ರೆ ನಾವು ಯಾವಾಗ್ಲೂ "farthest"
     ಅನ್ನೇ ಮುಂದಿನ boundary ಆಗಿ ಆರಿಸ್ತೀವಿ — ಇದೇ optimal choice.

  💡 Interview ನಲ್ಲಿ ಹೇಗೆ ಮಾತಾಡಬೇಕು (Think out loud):
  →  "This is really an implicit BFS — each 'jump' is like a BFS
      level, and I want the fewest levels to reach the last index."
  →  "The brute force tries every jump length recursively — O(2^n),
      too slow."
  →  "I track two things while scanning: the farthest index reachable
      overall, and the boundary of the current jump. When I reach
      that boundary, I know I must take another jump, so I increment
      the count and move the boundary out to the farthest I've seen."

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🏷️ SECTION 3 — TECHNIQUE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Primary   : Greedy → Implicit BFS (Current Boundary + Farthest)
  Secondary : None

  WHY this technique?
  → Minimum jumps to reach a target is structurally identical to
    minimum BFS levels — but doing real BFS with a queue is
    unnecessary overhead here
  → Tracking "farthest reachable" and "current jump's boundary"
    separately lets one linear scan simulate BFS levels implicitly
  → Greedy works because always extending to the farthest possible
    point within the current jump never hurts future jumps

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 💡 SECTION 4 — INTUITION (How to think — English)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Key observation: think of indices reachable within k jumps as "BFS
  level k". While scanning left to right within the current level
  (bounded by current_end), we compute the farthest index reachable
  within k+1 jumps. The moment the scan index reaches current_end
  (the edge of the current level), we've exhausted this level, so we
  commit to another jump and push current_end out to farthest.

  The journey from brute to optimal:
    Brute thought   →  recursively try every jump length from every index
    Problem with it →  exponential time, unusable for n up to 10^4
    Better question →  "isn't this the same shape as BFS shortest
                        path, just on an implicit graph?"
    Insight         →  simulate BFS levels with two pointers — farthest
                        reachable, and the current level's boundary —
                        instead of an actual queue
    Optimal         →  single greedy pass, O(n) time, O(1) space

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🐢 SECTION 5 — APPROACH 1 — BRUTE FORCE (Recursive, Try Every Jump)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    From index i, try every jump length from 1 to nums[i], recursing
    and taking the minimum jump count among all choices that
    eventually reach the last index.

  Pseudocode:
    step 1: def min_jumps(i):
    step 2:   if i >= n-1: return 0
    step 3:   best = infinity
    step 4:   for step in range(1, nums[i]+1):
    step 5:     best = min(best, 1 + min_jumps(i + step))
    step 6:   return best
    step 7: return min_jumps(0)

  Time  : O(2^n)  →  Why: exponential branching at every index
  Space : O(n)    →  Why: recursion depth up to n

  ಇದು ಯಾಕೆ ಸಾಕಾಗಲ್ಲ? (Why is this not enough?)
    → n=10^4 ಗೆ exponential ಖಂಡಿತ TLE. Greedy implicit-BFS ಇಂದ O(n)
      ಗೆ ಇಳಿಸ್ಬೋದು.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🚶 SECTION 6 — APPROACH 2 — BETTER (skip — brute jumps straight to optimal)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  ಇಲ್ಲಿ intermediate approach ಇಲ್ಲ — greedy implicit-BFS insight ಸಿಕ್ಕ
  ತಕ್ಷಣ ನೇರವಾಗಿ optimal ಗೆ ಹೋಗಬಹುದು (DP memoization O(n²) ಆಗುತ್ತೆ,
  greedy ಇಂದ ಇನ್ನೂ fast).

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🚀 SECTION 7 — APPROACH 3 — OPTIMAL   (Greedy — Current Boundary + Farthest)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    Scan left to right (excluding the last index, since we stop once
    we can reach it). Maintain farthest (best reach seen so far) and
    current_end (the farthest reachable using the jumps taken so
    far). When i reaches current_end, this jump's "budget" is used
    up, so increment jumps and set current_end = farthest.

  Key steps:
    1. jumps = 0, current_end = 0, farthest = 0
    2. for i in range(n - 1):
         farthest = max(farthest, i + nums[i])
         if i == current_end:
             jumps += 1
             current_end = farthest
    3. Return jumps

  ಕನ್ನಡದಲ್ಲಿ ಒಂದು ಸಲ ಹೇಳಿ (Say it once in Kanglish so it sticks):
    → "jumps=0, current_end=0, farthest=0 ಇಂದ start ಮಾಡು. ಪ್ರತಿ index
        i (last index ಬಿಟ್ಟು) ಗೂ farthest = max(farthest, i+nums[i])
        update ಮಾಡು. i == current_end ಆದ್ರೆ (ಈ jump ನ boundary
        ಮುಟ್ಟಿದ್ವಿ), jumps++ ಮಾಡಿ current_end = farthest ಗೆ set ಮಾಡು!"

  Time  : O(n)  →  Why: single left-to-right pass, no revisits
  Space : O(1)  →  Why: only jumps, current_end, farthest tracked

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🔍 SECTION 8 — DRY RUN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Input: nums = [2, 3, 1, 1, 4]  (n=5, loop runs i=0..3)

  jumps=0, current_end=0, farthest=0

  i=0 (nums[i]=2): farthest=max(0,0+2)=2
                   i==current_end(0)? Yes → jumps=1, current_end=2
  i=1 (nums[i]=3): farthest=max(2,1+3)=4
                   i==current_end(2)? No (i=1)
  i=2 (nums[i]=1): farthest=max(4,2+1)=4
                   i==current_end(2)? Yes → jumps=2, current_end=4
  i=3 (nums[i]=1): farthest=max(4,3+1)=4
                   i==current_end(4)? No (i=3)
  loop ends (i only goes to n-2=3)

  Output: 2   matches expected

  ಇನ್ನೊಂದು example — tricky case (every jump length is 1):
  Input: nums = [1, 1, 1, 1]  (n=4, loop runs i=0..2)

  jumps=0, current_end=0, farthest=0

  i=0 (nums[i]=1): farthest=max(0,0+1)=1
                   i==current_end(0)? Yes → jumps=1, current_end=1
  i=1 (nums[i]=1): farthest=max(1,1+1)=2
                   i==current_end(1)? Yes → jumps=2, current_end=2
  i=2 (nums[i]=1): farthest=max(2,2+1)=3
                   i==current_end(2)? Yes → jumps=3, current_end=3
  loop ends (i only goes to n-2=2)

  Output: 3   matches expected

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 ⚠️ SECTION 9 — EDGE CASES — ಇವನ್ನ ಮರೆಯಬೇಡ!
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  ✓ Single element array?      →  already at the last index, 0 jumps
                                   needed (loop range(n-1) is empty)
  ✓ Two elements?               →  exactly one jump needed, loop runs
                                   once and correctly counts it
  ✓ First element covers everything (nums[0] >= n-1)? →  one jump
                                   suffices, current_end reaches
                                   farthest = n-1 immediately at i=0
  ✓ All jump lengths are 1?     →  forces exactly n-1 jumps, no
                                   shortcuts possible (see dry run above)
  ✓ Large jump values (nums[i] > n)? →  farthest just caps naturally
                                   since the array itself is only length n

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📊 SECTION 10 — COMPLEXITY SUMMARY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                Time      Space
  Brute Force   O(2^n)    O(n)
  Optimal       O(n)      O(1)    ← use this 

  Time ಯಾಕೆ ಅಷ್ಟು?  → ಒಂದೇ pass ನಲ್ಲಿ ಪ್ರತಿ index (last index ಬಿಟ್ಟು)
                        ಒಂದೇ ಸಲ visit ಆಗುತ್ತೆ.
  Space ಯಾಕೆ ಅಷ್ಟು? → jumps, current_end, farthest — 3 variables
                        ಬಿಟ್ಟು ಬೇರೆ extra structure ಬೇಡ.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🎯 SECTION 11 — PATTERN LEARNED — ಇದರಿಂದ ಕಲಿತದ್ದು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Pattern Name: Greedy Implicit BFS — Level Boundary Tracking

  ಈ pattern ಯಾವಾಗ use ಮಾಡಬೇಕು?
  → "Minimum steps/jumps to reach target" ಕೇಳಿದಾಗ, ಆದ್ರೆ explicit
    graph/queue build ಮಾಡೋದು unnecessary overhead ಆಗಿದ್ದಾಗ
  → Problem ಸ್ವತಃ BFS-shaped ಆಗಿದ್ದು (levels = steps), ಆದ್ರೆ array
    index ಗಳೇ implicit graph nodes ಆಗಿದ್ದಾಗ
  → "current level ನ boundary" ಮತ್ತು "next level ನ farthest" ಅಂತ
    ಎರಡು separate values track ಮಾಡ್ಬಹುದು ಅಂತ ಗೊತ್ತಾದಾಗ

  ಇದೇ pattern ಬೇರೆ problems ನಲ್ಲಿ ಕಾಣಿಸುತ್ತೆ:
  → Jump Game (#55) — same farthest-reach idea, simpler reachability-only version
  → Video Stitching — same "min intervals to cover a range" greedy family
  → Minimum Number of Taps to Open to Water a Garden — same boundary-jump pattern

  Next time ಇಂತಹ problem ಬಂದ್ರೆ ನಾನು ಮೊದಲು ಇದನ್ನ think ಮಾಡ್ತೇನೆ:
  → "Minimum jumps/steps ಕೇಳಿದ ತಕ್ಷಣ, ಇದು implicit BFS ಅಂತ ಗುರುತಿಸಿ,
      queue ಬೇಡ — current level boundary + next level farthest ಅಂತ
      ಎರಡು variables ಇಂದ single pass ನಲ್ಲಿ solve ಮಾಡು."

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🗣️ SECTION 12 — INTERVIEWALLI HEGE EXPLAIN MAADABEEKU
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  1. Understand:
     "I need the minimum number of jumps to reach the last index,
      given the max jump length from each index — and it's guaranteed
      the end is reachable."

  2. Brute force:
     "A recursive approach tries every jump length from every index
      and takes the minimum — exponential time, too slow for n=10^4."

  3. Optimize:
     "This is really an implicit BFS — jumps are like BFS levels. I
      track the farthest index reachable overall, and the boundary of
      the current jump. When my scan reaches that boundary, I know
      I've exhausted the current jump's reach and must take another."

  4. Code:
     "I will use two variables — current_end (this jump's limit) and
      farthest (best reach seen so far) — incrementing jumps and
      pushing current_end to farthest exactly when i hits current_end."

  5. Complexity:
     "Time O(n) — single pass excluding the last index. Space O(1) —
      three running variables only."

  ಮುಖ್ಯ: ಸುಮ್ಮನೆ ಕೂತು code ಬರೆಯಬೇಡ!
         Interviewer ಗೆ ನಿನ್ನ thinking process ಕಾಣಬೇಕು.
"""


# ═══════════════════════════════════════════════════════════════════
# BRUTE FORCE — O(2^n) Time | O(n) Space  (Recursive, Try Every Jump)
# ═══════════════════════════════════════════════════════════════════
def jump_brute(nums):
    """ಇದು ಮೊದಲ ಆಲೋಚನೆ — ಪ್ರತಿ jump length ಅನ್ನ recursively try ಮಾಡಿ min ತಗೊಳ್ಳೋದು"""
    n = len(nums)

    def min_jumps(i):
        if i >= n - 1:
            return 0
        best = float("inf")
        for step in range(1, nums[i] + 1):
            best = min(best, 1 + min_jumps(i + step))
        return best

    return min_jumps(0)


# ═══════════════════════════════════════════════════════════════════
# OPTIMAL — O(n) Time | O(1) Space  (Greedy — Current Boundary + Farthest)
# ═══════════════════════════════════════════════════════════════════
def jump(nums):
    """ಇದು final answer — implicit BFS ಥರ current jump boundary ಮತ್ತು farthest track ಮಾಡು"""
    n = len(nums)
    jumps = 0
    current_end = 0
    farthest = 0

    for i in range(n - 1):
        farthest = max(farthest, i + nums[i])
        if i == current_end:
            jumps += 1
            current_end = farthest

    return jumps


# ═══════════════════════════════════════════════════════════════════
# TEST CASES
# ═══════════════════════════════════════════════════════════════════
if __name__ == "__main__":
    import sys
    sys.stdout.reconfigure(encoding="utf-8")   # Windows cp1252 can't print emoji otherwise

    # Test 1 — Basic example
    assert jump([2, 3, 1, 1, 4]) == 2

    # Test 2 — Edge case: single element, no jumps needed
    assert jump([0]) == 0

    # Test 3 — Edge case: all same elements (all 1s, forces max jumps)
    assert jump([1, 1, 1, 1]) == 3

    # Test 4 — Tricky: first jump covers the whole array in one go
    assert jump([5, 1, 1, 1, 1]) == 1

    print("All tests passed! ")
