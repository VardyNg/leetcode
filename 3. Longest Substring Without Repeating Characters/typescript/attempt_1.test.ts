import lengthOfLongestSubstring from './attempt_1';

describe("test lengthOfLongestSubstring", () => {
  test("Test 1 - 'abcabcbb'", () => {
    expect(lengthOfLongestSubstring("abcabcbb")).toBe(3);
  });

  test("Test 2 - 'bbbbb'", () => {
    expect(lengthOfLongestSubstring("bbbbb")).toBe(1);
  });

  test("Test 3 - 'pwwkew'", () => {
    expect(lengthOfLongestSubstring("pwwkew")).toBe(3);
  });

  test("Test 4 - empty string", () => {
    expect(lengthOfLongestSubstring("")).toBe(0);
  });

	test("Test 5 - whole string is the longest substring", () => {
		expect(lengthOfLongestSubstring('abcdefghijk')).toBe(11)
	})

	test("Test 6 - 'aab", () => {
		expect(lengthOfLongestSubstring('aab')).toBe(2)
	})
});
