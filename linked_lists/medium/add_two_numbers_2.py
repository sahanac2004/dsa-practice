"""
╔══════════════════════════════════════════════════════════════════╗
║  ADD TWO NUMBERS                                                 ║
║  LeetCode #2  |  Difficulty: Medium  |  Topic: Linked Lists     ║
║  Link: https://leetcode.com/problems/add-two-numbers/           ║
║  NeetCode: https://neetcode.io/problems/add-two-numbers-linked-list
╚══════════════════════════════════════════════════════════════════╝

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📘 SECTION 1 — PROBLEM UNDERSTANDING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Two non-empty linked lists represent two non-negative integers.
  Digits are stored in REVERSE ORDER (LSB first).
  Each node contains a single digit.
  Add the two numbers and return the sum as a linked list
  (also in reverse order).

  Input : l1, l2 = two linked lists (digits in reverse order)
  Output: linked list representing their sum (reverse order)

  Example 1 — basic:
    Input : l1=2→4→3,  l2=5→6→4
    Output: 7→0→8
    Why?  : 342 + 465 = 807 → reversed = 7→0→8

  Example 2 — different lengths + final carry:
    Input : l1=9→9→9→9→9→9→9, l2=9→9→9→9
    Output: 8→9→9→9→0→0→0→1
    Why?  : 9999999 + 9999 = 10009998 → reversed

  Constraints:
    - Number of nodes: 1 to 100
    - 0 <= Node.val <= 9
    - No leading zeros (except number 0 itself)
    - Digits stored in reverse order (LSB at head)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🧠 SECTION 2 — KANGLISH THINKING — ಹೇಗೆ ಯೋಚಿಸಬೇಕು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  Problem odi aada mele namma brain enu think maadabeeku:

  ಹಂತ 1 — Problem ಅರ್ಥ ಮಾಡಿಕೊಳ್ಳಿ
  ┌─────────────────────────────────────────────────────────┐
  │  Input ಏನು ಕೊಡ್ತಾರೆ?  →  2 linked lists (digits       │
  │                           reversed order ಲ್ಲಿ)         │
  │  Output ಏನು ಬೇಕು?     →  sum ಅನ್ನು same reversed       │
  │                           format ಲ್ಲಿ linked list       │
  │  Constraints ಏನಿದೆ?   →  carry handle maadabeeku,     │
  │                           different lengths OK          │
  └─────────────────────────────────────────────────────────┘

  ಹಂತ 2 — ನನಗೆ ಗೊತ್ತಿರೋ simple way ಏನು?
  →  Numbers extract ಮಾಡಿ add ಮಾಡಿ result ಅನ್ನು
     linked list ಆಗಿ convert ಮಾಡೋಣ
  →  ಆದರೆ ಇದು slow ಯಾಕೆ?
     Large numbers ಆದ್ರೆ integer overflow possible!
     (100 digits = beyond 64-bit int in C++/Java)

  ಹಂತ 3 — Better way ಹೇಗೆ ಯೋಚಿಸುವುದು?
  →  "Grade school addition ಹೇಗೆ ಮಾಡ್ತೇವೆ?"
  →  Right to left ಹೋಗಿ digit by digit add ಮಾಡಿ
     carry track ಮಾಡ್ತೇವೆ!
  →  Reversed list iddodarina digit by digit
     left to right traverse = LSB first add — perfect!
  →  Dummy node use ಮಾಡಿ result build ಮಾಡೋಣ!

  ಹಂತ 4 — Technique ಯಾಕೆ ಇಲ್ಲಿ ಕೆಲಸ ಮಾಡುತ್ತೆ?
  →  Lists already reversed → LSB at head → perfect for addition!
  →  carry = total // 10
  →  new_digit = total % 10
  →  Loop until BOTH lists exhausted AND carry = 0!
     (3 conditions — most common bug is missing carry!)

  💡 Interview ನಲ್ಲಿ ಹೇಗೆ ಮಾತಾಡಬೇಕು:
  →  "Simulate grade school addition digit by digit"
  →  "Since lists are reversed, head = LSB → add left to right"
  →  "Track carry, handle different lengths, final carry check"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🏷️ SECTION 3 — TECHNIQUE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Primary   : Dummy Node + Carry Simulation
  Secondary : —

  WHY Dummy Node?
  → Building result list from scratch — dummy avoids null head checks
  → Same trick as Merge Two Sorted Lists!

  WHY Carry Simulation instead of extract-add-convert?
  → No integer overflow for 100-digit numbers
  → Lists already reversed → LSB first → natural for addition

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 💡 SECTION 4 — INTUITION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Think of it as adding two numbers column by column (right to left).
  Since the lists are in REVERSE order, head is already the
  rightmost (units) digit — perfect for column-by-column addition!

  At each step:
    val1 = l1.val if l1 else 0    (0 if list exhausted)
    val2 = l2.val if l2 else 0
    total = val1 + val2 + carry
    carry = total // 10            (carry to next position)
    digit = total % 10             (current position digit)
    Append digit to result

  Continue until BOTH lists are exhausted AND carry == 0!
  The carry==0 check is the most common missed bug here.
  Example: [5] + [5] = [0, 1] — the 1 comes from carry alone!

  The journey from brute to optimal:
    Brute thought   →  Extract numbers, add, convert back
    Problem with it →  100-digit numbers overflow 64-bit integers
    Better question →  "Can I add digit by digit like school math?"
    Insight         →  YES! Lists already reversed → LSB first!
    Optimal         →  Dummy node + carry simulation O(max(m,n))

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🐢 SECTION 5 — APPROACH 1 — BRUTE FORCE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    Extract numbers from both lists (using positional values).
    Add them. Convert result back to linked list (reversed digits).

  Time  : O(m + n)      →  traverse both + build result
  Space : O(max(m,n))   →  result list

  ಇದು ಯಾಕೆ ಸಾಕಾಗಲ್ಲ?
    → Python handles big integers fine, but in C++/Java 100-digit
      numbers overflow 64-bit int — not interview-safe!
    → Always simulate digit by digit in interviews.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🚀 SECTION 6 — APPROACH 2 — OPTIMAL (Carry Simulation)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Idea:
    Simulate grade school addition. Use dummy node to build result.
    At each step get digits from l1 and l2 (0 if exhausted).
    Compute sum + carry, get new digit and new carry.
    Append digit to result, advance both pointers.

  Key steps:
    1. dummy = ListNode(0), curr = dummy, carry = 0
    2. While l1 OR l2 OR carry:
       a. v1 = l1.val if l1 else 0
       b. v2 = l2.val if l2 else 0
       c. total = v1 + v2 + carry
       d. carry = total // 10
       e. curr.next = ListNode(total % 10)
       f. curr = curr.next
       g. if l1: l1 = l1.next
       h. if l2: l2 = l2.next
    3. return dummy.next

  ಕನ್ನಡದಲ್ಲಿ ಒಂದು ಸಲ ಹೇಳಿ:
    → "dummy node create maadu, carry=0.
       l1 OR l2 OR carry — 3 conditions iddre loop!
       v1 = l1.val (or 0), v2 = l2.val (or 0).
       total = v1+v2+carry. carry = total//10.
       New node total%10 append maadu. curr advance.
       l1,l2 advance. dummy.next return maadu!"

  Time  : O(max(m, n))  →  traverse longer list + possible carry
  Space : O(max(m, n))  →  result list has at most max(m,n)+1 nodes

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🔍 SECTION 7 — DRY RUN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Input: l1=2→4→3, l2=5→6→4, carry=0  (342 + 465)

  Step 1: v1=2, v2=5, total=7,  carry=0, digit=7  →  [7]
          l1=4→3, l2=6→4

  Step 2: v1=4, v2=6, total=10, carry=1, digit=0  →  [7→0]
          l1=3,   l2=4

  Step 3: v1=3, v2=4, total=8,  carry=0, digit=8  →  [7→0→8]
          l1=None, l2=None

  carry=0, l1=None, l2=None → exit loop
  Output: 7→0→8  ✓  (807)

  ಇನ್ನೊಂದು — final carry edge case:
  l1=9→9, l2=1  (99 + 1 = 100)

  Step 1: v1=9, v2=1, total=10, carry=1, digit=0  →  [0]
          l1=9, l2=None

  Step 2: v1=9, v2=0, total=10, carry=1, digit=0  →  [0→0]
          l1=None, l2=None

  Step 3: l1=None, l2=None, carry=1 → STILL IN LOOP!
          v1=0, v2=0, total=1, carry=0, digit=1   →  [0→0→1]

  Output: 0→0→1  ✓  (100 reversed)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 ⚠️ SECTION 8 — EDGE CASES — ಇವನ್ನ ಮರೆಯಬೇಡ!
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  ✓ Different lengths?    →  Use 0 when shorter list exhausted
  ✓ Final carry only?     →  9→9 + 1 = 0→0→1 (carry creates extra!)
  ✓ Single digits carry?  →  [5] + [5] = [0, 1]
  ✓ One list is [0]?      →  [0] + any = any
  ✓ Both [0]?             →  [0] + [0] = [0]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📊 SECTION 9 — COMPLEXITY SUMMARY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                  Time           Space
  Brute Force     O(m+n)         O(max(m,n))
  Optimal         O(max(m,n))    O(max(m,n))   ← use this ✅

  Time yaake O(max(m,n))?
    → Traverse the longer list; one extra step if final carry
  Space yaake O(max(m,n))?
    → Result list has at most max(m,n)+1 nodes

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🎯 SECTION 10 — PATTERN LEARNED — ಇದರಿಂದ ಕಲಿತದ್ದು
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Pattern Name: Dummy Node + Carry Simulation

  Carry simulation template — memorise idannu:
  ┌────────────────────────────────────────────────┐
  │  carry = 0                                     │
  │  while l1 or l2 or carry:   ← 3 conditions!  │
  │      v1 = l1.val if l1 else 0                  │
  │      v2 = l2.val if l2 else 0                  │
  │      total = v1 + v2 + carry                   │
  │      carry = total // 10                       │
  │      curr.next = ListNode(total % 10)          │
  │      curr = curr.next                          │
  │      if l1: l1 = l1.next                       │
  │      if l2: l2 = l2.next                       │
  └────────────────────────────────────────────────┘

  Idee pattern beere problemsalli kaanisatte:
  → Add Two Numbers II #445 (MSB first — reverse lists first!)
  → Add Binary #67 (same carry logic, binary)
  → Multiply Strings #43 (digit-by-digit multiply)
  → Plus One #66 (already solved in arrays — same carry idea!)

  Next time intaha problem bandre naanu modalu idannu think maadtene:
  → "Digits linked list add maadabekittu?
     → Dummy node + carry! v1+v2+carry = total.
     carry = total//10, digit = total%10.
     Loop condition: l1 OR l2 OR carry — 3, not 2!"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🗣️ SECTION 11 — INTERVIEWALLI HEGE EXPLAIN MAADABEEKU
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  1. Understand:
     "Add two numbers stored as reversed linked lists.
      Return their sum as a reversed linked list."

  2. Brute force:
     "Extract integers, add, convert back. Works in Python but
      overflows in C++/Java for 100-digit numbers."

  3. Optimize:
     "Simulate grade school addition digit by digit.
      Since lists are reversed, head = LSB — perfect for addition!
      Use carry variable. Handle different lengths with 0 padding.
      Loop while l1 OR l2 OR carry — the carry check is critical!
      Final carry like 99+1=100 creates an extra node."

  4. Code:
     "Dummy node, carry=0. Loop: v1/v2 from lists (0 if None).
      total=v1+v2+carry. Append total%10 node. carry=total//10.
      Advance l1, l2 if not None. Return dummy.next."

  5. Complexity:
     "Time O(max(m,n)). Space O(max(m,n)) for result list."

  Mukhya: summane kuutu code bareyabeda!
          "while l1 or l2 or carry" — 3 conditions, not 2!
          Final carry creates extra node — common interview trap!
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

def to_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


# ═══════════════════════════════════════════════════════════════════
# BRUTE FORCE — O(m+n) Time | O(max(m,n)) Space
# ═══════════════════════════════════════════════════════════════════
def add_two_numbers_brute(l1, l2):
    """Idu modala aaloochane — extract numbers, add, convert back"""
    def to_num(node):
        num, place = 0, 1
        while node:
            num   += node.val * place
            place *= 10
            node   = node.next
        return num

    total = to_num(l1) + to_num(l2)
    if total == 0:
        return ListNode(0)

    dummy = ListNode(0)
    curr  = dummy
    while total > 0:
        curr.next = ListNode(total % 10)
        curr      = curr.next
        total   //= 10
    return dummy.next


# ═══════════════════════════════════════════════════════════════════
# OPTIMAL — O(max(m,n)) Time | O(max(m,n)) Space
# ═══════════════════════════════════════════════════════════════════
def add_two_numbers(l1, l2):
    """
    Idu final answer — dummy node + carry simulation
    Grade school addition digit by digit
    KEY: loop while l1 OR l2 OR carry (3 conditions!)
    """
    dummy = ListNode(0)
    curr  = dummy
    carry = 0

    while l1 or l2 or carry:
        v1 = l1.val if l1 else 0    # 0 if list exhausted
        v2 = l2.val if l2 else 0

        total = v1 + v2 + carry
        carry = total // 10          # carry to next position
        digit = total % 10           # current position digit

        curr.next = ListNode(digit)
        curr      = curr.next

        if l1: l1 = l1.next
        if l2: l2 = l2.next

    return dummy.next


# ═══════════════════════════════════════════════════════════════════
# TEST CASES
# ═══════════════════════════════════════════════════════════════════
if __name__ == "__main__":
    # Test 1 — Basic: 342 + 465 = 807
    assert to_list(add_two_numbers(
        build([2,4,3]), build([5,6,4]))) == [7,0,8]

    # Test 2 — Final carry: 99 + 1 = 100 → [0,0,1]
    assert to_list(add_two_numbers(
        build([9,9]), build([1]))) == [0,0,1]

    # Test 3 — Different lengths: 9999999 + 9999 = 10009998
    assert to_list(add_two_numbers(
        build([9,9,9,9,9,9,9]), build([9,9,9,9]))) == [8,9,9,9,0,0,0,1]

    # Test 4 — Both zeros
    assert to_list(add_two_numbers(
        build([0]), build([0]))) == [0]

    # Test 5 — Single digits with carry: 5 + 5 = 10 → [0,1]
    assert to_list(add_two_numbers(
        build([5]), build([5]))) == [0,1]

    # Test 6 — One list longer: 1 + 99 = 100 → [0,0,1]
    assert to_list(add_two_numbers(
        build([1]), build([9,9]))) == [0,0,1]

    # Test 7 — Brute force matches optimal
    assert to_list(add_two_numbers_brute(
        build([2,4,3]), build([5,6,4]))) == [7,0,8]
    assert to_list(add_two_numbers_brute(
        build([9,9]), build([1]))) == [0,0,1]

    print("All tests passed!")
