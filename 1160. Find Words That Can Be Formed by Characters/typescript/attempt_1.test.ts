import countCharacters from './attempt_1';

describe("test countCharacters", () => {
  test("Test 1 - cat and hat can be formed", () => {
    expect(countCharacters(["cat", "bt", "hat", "tree"], "atach")).toBe(6);
  });

  test("Test 2 - hello and world can be formed", () => {
    expect(countCharacters(["hello", "world", "leetcode"], "welldonehoneyr")).toBe(10);
  });
});
