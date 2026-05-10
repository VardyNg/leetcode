# Min Stack

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the `MinStack` class:
- `MinStack()` initializes the stack object.
- `push(val)` pushes the element `val` onto the stack.
- `pop()` removes the element on the top of the stack.
- `top()` gets the top element of the stack.
- `getMin()` retrieves the minimum element in the stack.

You must implement a solution with O(1) time complexity for each function.

#### Attempts:

| # | Time Complexity | Space Complexity | Description | Submission |
| - | ---- | ----- | ----------- | ----------- |
| 1 | O(1) | O(n) | Use two stacks: minStack + stack, use minStack to keep track the latest minimal value, presist across push and pop| |
