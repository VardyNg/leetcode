import canConstruct from './attempt_1';

describe("test canConstruct", () => {
  test("Test 1 - cannot construct", () => {
    expect(canConstruct("a", "b")).toBe(false);
  });

  test("Test 2 - cannot construct", () => {
    expect(canConstruct("aa", "ab")).toBe(false);
  });

  test("Test 3 - can construct", () => {
    expect(canConstruct("aa", "aab")).toBe(true);
  });
});
