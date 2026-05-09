import groupAnagrams from './attempt_2';

describe("test groupAnagrams", () => {
  test("Test 1 - mixed anagrams", () => {
    const result = groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]);
    const sorted = result.map(group => group.sort()).sort((a, b) => a[0].localeCompare(b[0]));
    expect(sorted).toEqual([
      ["ate", "eat", "tea"],
      ["bat"],
      ["nat", "tan"],
    ]);
  });

  test("Test 2 - empty string", () => {
    expect(groupAnagrams([""])).toEqual([[""]]);
  });

  test("Test 3 - single character", () => {
    expect(groupAnagrams(["a"])).toEqual([["a"]]);
  });
});
