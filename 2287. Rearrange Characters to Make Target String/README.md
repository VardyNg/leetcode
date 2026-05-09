# Rearrange Characters to Make Target String

You are given two 0-indexed strings `s` and `target`. You can take some letters from `s` and rearrange them to form new strings.

Return the maximum number of copies of `target` that can be formed by taking letters from `s` and rearranging them.

Note: Each character from `s` can only be used once across all copies of `target`.

- `s` and `target` consist of lowercase English letters.

#### Attempts:

| # | Time Complexity | Space Complexity | Description | Submission |
| - | ---- | ----- | ----------- | ----------- |
| 1 | O(n) | O(1) | Create Hashmap from s and target, compare them and find the minimal of each character hit | https://leetcode.com/problems/rearrange-characters-to-make-target-string/submissions/1999068162 |
