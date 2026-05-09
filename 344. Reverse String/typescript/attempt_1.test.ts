import reverseString from './attempt_1';

describe("test reverseString", () => {
  test("Test 1 - ['h','e','l','l','o']", () => {
    const s = ["h", "e", "l", "l", "o"];
    reverseString(s);
    expect(s).toEqual(["o", "l", "l", "e", "h"]);
  });

  test("Test 2 - ['H','a','n','n','a','h']", () => {
    const s = ["H", "a", "n", "n", "a", "h"];
    reverseString(s);
    expect(s).toEqual(["h", "a", "n", "n", "a", "H"]);
  });
});
