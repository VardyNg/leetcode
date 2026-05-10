# Baseball Game

You are keeping score for a baseball game with strange rules. The game consists of several rounds, where the scores of past rounds may affect future rounds' scores.

At the beginning of the game, you start with an empty record. You are given a list of strings `ops`, where `ops[i]` is the ith operation you must apply to the record and is one of the following:

- An integer `x` — Record a new score of `x`.
- `"+"` — Record a new score that is the sum of the previous two scores.
- `"D"` — Record a new score that is double the previous score.
- `"C"` — Invalidate the previous score, removing it from the record.

Return the sum of all the scores on the record after applying all the operations.

#### Attempts:

| # | Time Complexity | Space Complexity | Description | Submission |
| - | ---- | ----- | ----------- | ----------- |
| 1 | O(n) | O(n) | Construct array to hold the complied numbers, loop and calculate run-sum | https://leetcode.com/problems/baseball-game/submissions/2000027574 |
