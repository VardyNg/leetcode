# Find Words That Can Be Formed by Characters

You are given an array of strings `words` and a string `chars`.

A string is good if it can be formed by characters from `chars` (each character can only be used once).

Return the sum of lengths of all good strings in `words`.

- `words[i]` and `chars` consist of lowercase English letters.

#### Attempts:

| # | Time Complexity | Space Complexity | Description | Submission |
| - | ---- | ----- | ----------- | ----------- |
| 1 | O(n x m) | O(n) | Generate hashmap from chars, loop each element in words and compare against the hashmap | https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/submissions/1998898298 |
