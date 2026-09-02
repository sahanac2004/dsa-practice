# strings — Problems

Files are organized by difficulty subfolder: `easy/`, `medium/`, `hard/`.

## 🟢 Easy

| # | Problem | Technique | LC Link | File |
|---|---------|-----------|---------|------|
| 1 | Roman to Integer | hashmap/simulation | [LC #13](https://leetcode.com/problems/roman-to-integer/) | [easy/roman_to_integer_13.py](easy/roman_to_integer_13.py) |
| 2 | Longest Common Prefix | strings/vertical-scan | [LC #14](https://leetcode.com/problems/longest-common-prefix/) | [easy/longest_common_prefix_14.py](easy/longest_common_prefix_14.py) |
| 3 | Find the Index of the First Occurrence (strStr) | KMP/pattern-matching | [LC #28](https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/) | [easy/kmp_pattern_matching_28.py](easy/kmp_pattern_matching_28.py) |
| 4 | Isomorphic Strings | hashmap | [LC #205](https://leetcode.com/problems/isomorphic-strings/) | [easy/isomorphic_strings_205.py](easy/isomorphic_strings_205.py) |
| 5 | Valid Anagram | hashmap/frequency | [LC #242](https://leetcode.com/problems/valid-anagram/) | [easy/valid_anagram_242.py](easy/valid_anagram_242.py) |
| 6 | Reverse Words in a String III | two-pointers | [LC #557](https://leetcode.com/problems/reverse-words-in-a-string-iii/) | [easy/reverse_every_word_in_string_557.py](easy/reverse_every_word_in_string_557.py) |
| 7 | Rotate String (Check String Rotation) | string-concatenation trick | [LC #796](https://leetcode.com/problems/rotate-string/) | [easy/check_string_rotation_796.py](easy/check_string_rotation_796.py) |
| 8 | Remove Outermost Parentheses | stack/counter | [LC #1021](https://leetcode.com/problems/remove-outermost-parentheses/) | [easy/remove_outermost_parentheses_1021.py](easy/remove_outermost_parentheses_1021.py) |
| 9 | Maximum Nesting Depth of the Parentheses | stack/counter | [LC #1614](https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/) | [easy/maximum_nesting_depth_parentheses_1614.py](easy/maximum_nesting_depth_parentheses_1614.py) |
| 10 | Largest Odd Number in String | traversal | [LC #1903](https://leetcode.com/problems/largest-odd-number-in-string/) | [easy/largest_odd_number_in_string_1903.p](easy/largest_odd_number_in_string_1903.p) |

## 🟡 Medium

| # | Problem | Technique | LC Link | File |
|---|---------|-----------|---------|------|
| 11 | Longest Substring Without Repeating Characters | sliding-window/hashmap | [LC #3](https://leetcode.com/problems/longest-substring-without-repeating-characters/) | [medium/longest_no_repeat_3.py](medium/longest_no_repeat_3.py) |
| 12 | Longest Palindromic Substring | expand-around-center | [LC #5](https://leetcode.com/problems/longest-palindromic-substring/) | [medium/longest_palindromic_substring_5.py](medium/longest_palindromic_substring_5.py) |
| 13 | String to Integer (atoi) | simulation | [LC #8](https://leetcode.com/problems/string-to-integer-atoi/) | [medium/string_to_integer_atoi_8.py](medium/string_to_integer_atoi_8.py) |
| 14 | Longest Substring with At Least K Repeating Characters | divide-and-conquer/sliding-window | [LC #395](https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters/) | [medium/longest_substring_at_least_k_repeating_395.py](medium/longest_substring_at_least_k_repeating_395.py) |
| 15 | Longest Repeating Character Replacement | sliding-window/frequency | [LC #424](https://leetcode.com/problems/longest-repeating-character-replacement/) | [medium/longest_repeating_replace_424.py](medium/longest_repeating_replace_424.py) |
| 16 | Sort Characters By Frequency | hashmap/bucket-sort | [LC #451](https://leetcode.com/problems/sort-characters-by-frequency/) | [medium/sort_characters_by_frequency_451.py](medium/sort_characters_by_frequency_451.py) |
| 17 | Permutation in String | sliding-window/frequency | [LC #567](https://leetcode.com/problems/permutation-in-string/) | [medium/permutation_in_string_567.py](medium/permutation_in_string_567.py) |
| 18 | Palindromic Substrings | expand-around-center | [LC #647](https://leetcode.com/problems/palindromic-substrings/) | [medium/count_palindromic_substrings_647.py](medium/count_palindromic_substrings_647.py) |
| 19 | Score of Parentheses | stack | [LC #856](https://leetcode.com/problems/score-of-parentheses/) | [medium/score_of_parentheses_856.py](medium/score_of_parentheses_856.py) |
| 20 | Sum of Beauty of All Substrings | hashmap/frequency | [LC #1781](https://leetcode.com/problems/sum-of-beauty-of-all-substrings/) | [medium/sum_beauty_all_substrings_1781.py](medium/sum_beauty_all_substrings_1781.py) |

## 🔴 Hard

| # | Problem | Technique | LC Link | File |
|---|---------|-----------|---------|------|
| 21 | Minimum Window Substring | sliding-window/need-have | [LC #76](https://leetcode.com/problems/minimum-window-substring/) | [hard/min_window_substring_76.py](hard/min_window_substring_76.py) |
| 22 | Shortest Palindrome | KMP/failure-function | [LC #214](https://leetcode.com/problems/shortest-palindrome/) | [hard/shortest_palindrome_214.py](hard/shortest_palindrome_214.py) |
| 23 | Longest Palindromic Subsequence | dp/lcs | [LC #516](https://leetcode.com/problems/longest-palindromic-subsequence/) | [hard/longest_palindromic_subsequence_516.py](hard/longest_palindromic_subsequence_516.py) |
| 24 | Minimum Insertion Steps to Make a String Palindrome | dp/lcs | [LC #1312](https://leetcode.com/problems/minimum-insertion-steps-to-make-a-string-palindrome/) | [hard/min_insertions_make_palindrome_1312.py](hard/min_insertions_make_palindrome_1312.py) |
| 25 | Longest Happy Prefix | KMP/failure-function | [LC #1392](https://leetcode.com/problems/longest-happy-prefix/) | [hard/longest_happy_prefix_1392.py](hard/longest_happy_prefix_1392.py) |
| 26 | Rabin-Karp Algorithm (Pattern Matching via Rolling Hash) | string-hashing | [cp-algorithms](https://cp-algorithms.com/string/rabin-karp.html) | [hard/rabin_karp_algorithm.py](hard/rabin_karp_algorithm.py) |
| 27 | Z-Function / Pattern Matching | z-algorithm | [cp-algorithms](https://cp-algorithms.com/string/z-function.html) | [hard/z_function_pattern_matching.py](hard/z_function_pattern_matching.py) |
| 28 | Minimum Characters to Add at Front to Make Palindrome | KMP/hashing | [GeeksforGeeks](https://www.geeksforgeeks.org/dsa/minimum-characters-added-front-make-string-palindrome/) | [hard/min_chars_add_front_palindrome.py](hard/min_chars_add_front_palindrome.py) |
