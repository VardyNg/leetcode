# Daily Temperatures

Given an array of integers `temperatures` represents the daily temperatures, return an array `answer` such that `answer[i]` is the number of days you have to wait after the `i`th day to get a warmer temperature.

If there is no future day for which this is possible, keep `answer[i] == 0` instead.

#### Attempts:

| # | Time Complexity | Space Complexity | Description | Submission |
| - | ---- | ----- | ----------- | ----------- |
| 1 | O(n^2) | O(n^2) | Nested loop to scan each element | / |
