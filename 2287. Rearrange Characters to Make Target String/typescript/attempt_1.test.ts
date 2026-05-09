import rearrangeCharacters from './attempt_1';

describe("test rearrangeCharacters", () => {
  test("Test 1 - can form 2 copies of 'code'", () => {
    // For the first copy of "code", take the letters at indices 4, 5, 6, and 7.
    // For the second copy of "code", take the letters at indices 17, 18, 19, and 20.
    expect(rearrangeCharacters("ilovecodingonleetcode", "code")).toBe(2);
  });

  test("Test 2 - can form 1 copy of 'abc'", () => {
    // We can make one copy of "abc" by taking the letters at indices 0, 1, and 2.
    // We cannot reuse the letter 'c' at index 2, so we cannot make a second copy.
    expect(rearrangeCharacters("abcba", "abc")).toBe(1);
  });

  test("Test 3 - can form 1 copy of 'aaaaa'", () => {
    // We can make one copy of "aaaaa" by taking the letters at indices 0, 3, 6, 9, and 12.
    expect(rearrangeCharacters("abbaccaddaeea", "aaaaa")).toBe(1);
  });
});
