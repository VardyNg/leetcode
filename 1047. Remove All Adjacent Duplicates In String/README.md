# Remove All Adjacent Duplicates In String

You are given a string `s` consisting of lowercase English letters. A duplicate removal consists of choosing two adjacent and equal letters and removing them.

We repeatedly make duplicate removals on `s` until we no longer can.

Return the final string after all such duplicate removals have been made.

#### Attempts:

| # | Time Complexity | Space Complexity | Description | Submission |
| - | ---- | ----- | ----------- | ----------- |
| 1 | O(n) | O(n) | Use a stack, read each character and push/pop the stack conditionally, and reconstruct the final string | https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/submissions/2000034350 |
