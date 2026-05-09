# Ransom Note

Given two strings `ransomNote` and `magazine`, return `true` if `ransomNote` can be constructed by using the letters from `magazine` and `false` otherwise.

Each letter in `magazine` can only be used once in `ransomNote`.

- `ransomNote` and `magazine` consist of lowercase English letters.

#### Attempts:

| # | Time Complexity | Space Complexity | Description | Submission |
| - | ---- | ----- | ----------- | ----------- |
| 1 | O(n) | O(1) | Create hashmap from magazine, then loop characters in ransomNote against the hasdmap| https://leetcode.com/problems/ransom-note/submissions/1998861929 |
