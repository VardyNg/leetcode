import isValid from './attempt_1';

describe("test isValid", () => {
  test("Test 1 - '()'", () => {
    expect(isValid("()")).toBe(true);
  });

  test("Test 2 - '()[]{}'", () => {
    expect(isValid("()[]{}")).toBe(true);
  });

  test("Test 3 - '(]'", () => {
    expect(isValid("(]")).toBe(false);
  });

  test("Test 4 - '([)]'", () => {
    expect(isValid("([)]")).toBe(false);
  });

  test("Test 5 - '{[]}'", () => {
    expect(isValid("{[]}")).toBe(true);
  });
});
