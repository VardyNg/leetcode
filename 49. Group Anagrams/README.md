# Group Anagrams

Given an array of strings `strs`, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

- `strs[i]` consists of lowercase English letters.

#### Attempts:

| # | Time Complexity | Space Complexity | Description | Submission |
| - | ---- | ----- | ----------- | ----------- |
| 1 | O(n x m) | O(n x m) | Generate hashmap for each string in strs, convert to the static key and appen in the array | https://leetcode.com/problems/group-anagrams/submissions/1999098314 |
