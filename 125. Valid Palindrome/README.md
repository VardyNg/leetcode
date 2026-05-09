# Valid Palindrome

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward.

Alphanumeric characters include letters and numbers.

Given a string `s`, return `true` if it is a palindrome, or `false` otherwise.

#### Attempts:

| # | Time Complexity | Space Complexity | Description | Submission |
| - | ---- | ----- | ----------- | ----------- |
| 1 | O(n) | O(n) | Two-pointers: first remove non-alphanumberic values and convert to lower case, then being and end pointers moving toward each other and compare value at the indices | https://leetcode.com/problems/valid-palindrome/submissions/1999187526 |
| 2 | O(n) | O(1) | Two pointers: check if pointing a aplhanumeric vaue, if not, move it until found one. Then compare two values after converting to lower case | https://leetcode.com/problems/valid-palindrome/submissions/1999194044 |