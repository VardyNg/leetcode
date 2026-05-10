import removeDuplicates from './attempt_1';

describe("test removeDuplicates", () => {
  test("Test 1 - 'abbaca'", () => {
    expect(removeDuplicates("abbaca")).toBe("ca");
  });

  test("Test 2 - 'azxxzy'", () => {
    expect(removeDuplicates("azxxzy")).toBe("ay");
  });

  test("Test 3 - 'a'", () => {
    expect(removeDuplicates("a")).toBe("a");
  });
});
