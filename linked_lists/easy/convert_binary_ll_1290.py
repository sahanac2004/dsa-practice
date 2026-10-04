"""
╔══════════════════════════════════════════════════════════════════╗
║  CONVERT BINARY NUMBER IN A LINKED LIST TO INTEGER               ║
║  LeetCode #1290  |  Difficulty: Easy  |  Topic: Linked Lists    ║
║  Link: https://leetcode.com/problems/convert-binary-number-in-a-║
║        linked-list-to-integer/                                   ║
╚══════════════════════════════════════════════════════════════════╝

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📘 SECTION 1 — PROBLEM UNDERSTANDING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Given the head of a singly linked list where each node value
  is 0 or 1, the list represents a binary number (MSB first).
  Return its decimal value.

  Input : head = linked list of 0s and 1s (most significant bit first)
  Output: decimal integer value

  Example 1 — basic:
    Input : 1 → 0 → 1
    Output: 5
    Why?  : Binary 101 = 1×4 + 0×2 + 1×1 = 5

  Example 2 — slightly tricky (all zeros):
    Input : 0
    Output: 0
    Why?  : Binary 0 = 0

  Constraints:
    - List has between 1 and 30 nodes
    - Each node.val is 0 or 1
    - The number represented fits in a 32-bit integer

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🧠 SECTION 2 — KANGLISH THINKING — ಹೇಗೆ ಯೋಚಿಸಬೇಕು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  Problem odi aada mele namma brain enu think maadabeeku:

  ಹಂತ 1 — Problem ಅರ್ಥ ಮಾಡಿಕೊಳ್ಳಿ
  ┌─────────────────────────────────────────────────────────┐
  │  Input ಏನು ಕೊಡ್ತಾರೆ?  →  binary bits linked list      │
  │                           (MSB first)                   │
  │  Output ಏನು ಬೇಕು?     →  decimal integer value        │
  │  Constraints ಏನಿದೆ?   →  max 30 nodes, fits 32-bit    │
  └─────────────────────────────────────────────────────────┘

  ಹಂತ 2 — ನನಗೆ ಗೊತ್ತಿರೋ simple way ಏನು?
  →  All bits collect ಮಾಡಿ string ಮಾಡಿ int(s, 2) ಮಾಡೋಣ
  →  ಅಥವಾ bits collect ಮಾಡಿ positional value sum ಮಾಡೋಣ

  ಹಂತ 3 — Better way ಹೇಗೆ ಯೋಚಿಸುವುದು?
  →  "Bit shift trick! ಒಂದೇ pass ಲ್ಲಿ ಮಾಡಬಹudaa?"
  →  YES! result = result * 2 + node.val
     ಪ್ರತಿ step ಲ್ಲಿ result ಅನ್ನು left shift (×2) ಮಾಡಿ
     current bit add ಮಾಡು!
  →  1→0→1:
     result = 0*2 + 1 = 1
     result = 1*2 + 0 = 2
     result = 2*2 + 1 = 5 ✓

  ಹಂತ 4 — Technique ಯಾಕೆ ಇಲ್ಲಿ ಕೆಲಸ ಮಾಡುತ್ತೆ?
  →  Left shift by 1 = multiply by 2 = make room for next bit
  →  Same as how we convert binary to decimal mentally!
  →  Single pass, O(1) space — perfect

  💡 Interview ನಲ್ಲಿ ಹೇಗೆ ಮಾತಾಡಬೇಕು:
  →  "Use bit shift: result = result * 2 + node.val each step"
  →  "Same technique as reading binary number left to right"
  →  "O(n) time, O(1) space — single pass"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🏷️ SECTION 3 — TECHNIQUE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Primary   : Bit Shift — result = result * 2 + bit
  Secondary : Collect bits → join → int(s, 2)

  WHY Bit Shift?
  → Natural way to build binary number left to right
  → Each step: shift existing bits left (×2), add new bit
  → O(1) space — no string or array needed
  → Same trick used in all binary conversion problems

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 💡 SECTION 4 — INTUITION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Converting binary to decimal left to right:
  Start with result = 0.
  For each bit: result = result * 2 + bit
  This is exactly like sliding a window of bits.

  Binary 1→0→1:
    See 1: result = 0 * 2 + 1 = 1   (binary so far: 1)
    See 0: result = 1 * 2 + 0 = 2   (binary so far: 10)
    See 1: result = 2 * 2 + 1 = 5   (binary so far: 101)

  Or alternatively: OR shift
    result = (result << 1) | node.val  (bit shift version)

  The journey from brute to optimal:
    Brute thought   →  Collect all bits, reverse, compute positionally
    Problem with it →  Extra array + reverse needed
    Better question →  "Can I compute while traversing?"
    Insight         →  result * 2 + bit builds the number in one pass!
    Optimal         →  O(n) time, O(1) space — single traversal

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🐢 SECTION 5 — APPROACH 1 — BRUTE FORCE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    Collect all bits into a string.
    Convert binary string to int using Python's int(s, 2).

  Pseudocode:
    step 1: bits = ""
    step 2: while curr: bits += str(curr.val); curr = curr.next
    step 3: return int(bits, 2)

  Time  : O(n)   →  Why: one traversal
  Space : O(n)   →  Why: bits string

  ಇದು ಯಾಕೆ ಸಾಕಾಗಲ್ಲ?
    → Valid adu, but O(n) space — O(1) possible!
    → int(bits, 2) is a Python shortcut — interviewer might
      want you to show you understand the math

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🚀 SECTION 6 — APPROACH 2 — OPTIMAL (Bit Shift)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    Single pass. At each node: result = result * 2 + node.val
    Equivalent to left-shifting result and ORing the new bit.

  Key steps:
    1. result = 0, curr = head
    2. While curr:
       a. result = result * 2 + curr.val
          (or: result = (result << 1) | curr.val)
       b. curr = curr.next
    3. return result

  ಕನ್ನಡದಲ್ಲಿ ಒಂದು ಸಲ ಹೇಳಿ:
    → "result = 0 ಇಂದ start maadu. ಪ್ರತಿ node ಗೆ:
       result = result * 2 + node.val.
       ×2 = left shift = ಹೊಸ bit ಗೆ room ಮಾಡು.
       + node.val = new bit add maadu.
       Single pass, O(1) space!"

  Time  : O(n)   →  Why: single traversal
  Space : O(1)   →  Why: only result and curr

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🔍 SECTION 7 — DRY RUN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Input: 1 → 0 → 1
  result=0

  node=1: result = 0*2 + 1 = 1
  node=0: result = 1*2 + 0 = 2
  node=1: result = 2*2 + 1 = 5

  Output: 5 ✓  (binary 101 = 5)

  ಇನ್ನೊಂದು — single zero:
  Input: 0
  node=0: result = 0*2 + 0 = 0
  Output: 0 ✓

  ಇನ್ನೊಂದು — all ones:
  Input: 1 → 1 → 1 → 1
  result=0
  node=1: result=1
  node=1: result=3
  node=1: result=7
  node=1: result=15
  Output: 15 ✓ (binary 1111 = 15)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 ⚠️ SECTION 8 — EDGE CASES — ಇವನ್ನ ಮರೆಯಬೇಡ!
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  ✓ Single node 0?    →  return 0
  ✓ Single node 1?    →  return 1
  ✓ All zeros?        →  0→0→0 → 0
  ✓ All ones?         →  1→1→1→1 → 15
  ✓ Leading zero?     →  0→1→0 → 2 (binary 010 = 2)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📊 SECTION 9 — COMPLEXITY SUMMARY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                  Time    Space
  Brute (string)  O(n)    O(n)
  Optimal         O(n)    O(1)   ← use this ✅

  Time yaake O(n)?  → Visit each node exactly once
  Space yaake O(1)? → Only result integer and curr pointer

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🎯 SECTION 10 — PATTERN LEARNED — ಇದರಿಂದ ಕಲಿತದ್ದು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Pattern Name: Bit Shift Accumulation

  Universal binary → decimal trick:
  ┌────────────────────────────────────┐
  │  result = 0                        │
  │  for each bit (MSB first):         │
  │      result = result * 2 + bit     │
  │  (or: result = (result<<1) | bit)  │
  └────────────────────────────────────┘

  Ee pattern yaavaaga use maadabeeku?
  → Convert binary sequence to integer
  → Bits given MSB first (natural reading order)
  → Single pass without storing all bits

  Idee pattern beere problemsalli kaanisatte:
  → Number of 1 Bits #191 (bit manipulation)
  → Reverse Bits #190 (bit manipulation)
  → Single Number #136 (XOR trick)

  Next time intaha problem bandre naanu modalu idannu think maadtene:
  → "Binary bits MSB first, decimal value beeka?
     → result = result*2 + bit! Single pass O(1) space!"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🗣️ SECTION 11 — INTERVIEWALLI HEGE EXPLAIN MAADABEEKU
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  1. Understand:
     "Linked list of 0s and 1s represents binary number MSB first.
      Return its decimal value."

  2. Brute force:
     "Collect bits into string, use int(s, 2). O(n) space."

  3. Optimize:
     "Use bit shift accumulation: result = result*2 + node.val.
      At each step, shift existing bits left (make room) and
      add the new bit. Single pass, O(1) space."

  4. Code:
     "result=0, traverse: result = result*2 + curr.val.
      Equivalently: result = (result << 1) | curr.val."

  5. Complexity:
     "Time O(n). Space O(1)."

  Mukhya: summane kuutu code bareyabeda!
          result*2 = left shift = make room for next bit!
          Show both forms: *2+bit and <<1|bit
"""


# ─── Node Definition ──────────────────────────────────────────────
class ListNode:
    def __init__(self, val=0, next=None):
        self.val  = val
        self.next = next


# ─── Helpers ──────────────────────────────────────────────────────
def build(vals):
    dummy = ListNode(0)
    curr  = dummy
    for v in vals:
        curr.next = ListNode(v)
        curr = curr.next
    return dummy.next


# ═══════════════════════════════════════════════════════════════════
# BRUTE FORCE — O(n) Time | O(n) Space
# ═══════════════════════════════════════════════════════════════════
def get_decimal_value_brute(head):
    """Idu modala aaloochane — collect bits as string, convert"""
    bits = ""
    curr = head
    while curr:
        bits += str(curr.val)
        curr  = curr.next
    return int(bits, 2)


# ═══════════════════════════════════════════════════════════════════
# OPTIMAL — O(n) Time | O(1) Space
# ═══════════════════════════════════════════════════════════════════
def get_decimal_value(head):
    """
    Idu final answer — bit shift accumulation
    result = result * 2 + bit  at each step
    Equivalent: result = (result << 1) | bit
    """
    result = 0
    curr   = head

    while curr:
        result = (result << 1) | curr.val   # left shift + OR new bit
        curr   = curr.next

    return result


# ═══════════════════════════════════════════════════════════════════
# TEST CASES
# ═══════════════════════════════════════════════════════════════════
if __name__ == "__main__":
    # Test 1 — Basic: 101 = 5
    assert get_decimal_value(build([1, 0, 1])) == 5

    # Test 2 — Single zero
    assert get_decimal_value(build([0])) == 0

    # Test 3 — Single one
    assert get_decimal_value(build([1])) == 1

    # Test 4 — All zeros
    assert get_decimal_value(build([0, 0, 0])) == 0

    # Test 5 — All ones: 1111 = 15
    assert get_decimal_value(build([1, 1, 1, 1])) == 15

    # Test 6 — Leading zero: 010 = 2
    assert get_decimal_value(build([0, 1, 0])) == 2

    # Test 7 — Larger number: 11101 = 29
    assert get_decimal_value(build([1, 1, 1, 0, 1])) == 29

    # Test 8 — Brute force matches optimal
    assert get_decimal_value_brute(build([1, 0, 1])) == 5
    assert get_decimal_value_brute(build([1, 1, 1, 1])) == 15

    print("All tests passed!")
