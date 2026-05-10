import MinStack from './attempt_1';

describe("test MinStack", () => {
  test("Test 1 - push, push, push, getMin, pop, top, getMin", () => {
    const minStack = new MinStack();
    minStack.push(-2);
    minStack.push(0);
    minStack.push(-3);
    expect(minStack.getMin()).toBe(-3);
    minStack.pop();
    expect(minStack.top()).toBe(0);
    expect(minStack.getMin()).toBe(-2);
  });

  test("Test 2 - push, push, push, getMin, top, pop, getMin", () => {
    const minStack = new MinStack();
    minStack.push(-2);
    minStack.push(0);
    minStack.push(-1);
    expect(minStack.getMin()).toBe(-2);
    expect(minStack.top()).toBe(-1);
    minStack.pop();
    expect(minStack.getMin()).toBe(-2);
  });
});
