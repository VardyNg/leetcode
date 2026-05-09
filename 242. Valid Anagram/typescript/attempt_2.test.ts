import isAnagram from './attempt_1';

describe("test isAnagram", () => {
  test("Test 1 - valid anagram", () => {
    expect(isAnagram("anagram", "nagaram")).toBe(true);
  });

  test("Test 2 - not an anagram", () => {
    expect(isAnagram("rat", "car")).toBe(false);
  });
  test("Test 3 - not an anagram", () => {
    expect(isAnagram("aacc", "ccac")).toBe(false);
  });
});
