import reverseVowels from './attempt_1';

describe("test reverseVowels", () => {
  test("Test 1 - 'hello'", () => {
    expect(reverseVowels("hello")).toBe("holle");
  });

  test("Test 2 - 'leetcode'", () => {
    expect(reverseVowels("leetcode")).toBe("leotcede");
  });

  test("Test 3 - 'aA'", () => {
    expect(reverseVowels("aA")).toBe("Aa");
  });
});
