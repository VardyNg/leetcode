import isPalindrome from './attempt_1';

describe("test isPalindrome", () => {
  test("Test 1 - 'A man, a plan, a canal: Panama'", () => {
    expect(isPalindrome("A man, a plan, a canal: Panama")).toBe(true);
  });

  test("Test 2 - 'race a car'", () => {
    expect(isPalindrome("race a car")).toBe(false);
  });

  test("Test 3 - empty string with space", () => {
    expect(isPalindrome(" ")).toBe(true);
  });
});
