import search from './attempt_2';

describe("test search", () => {
  test("Test 1 - [-1,0,3,5,9,12], target=9", () => {
    expect(search([-1, 0, 3, 5, 9, 12], 9)).toBe(4);
  });

  test("Test 2 - [-1,0,3,5,9,12], target=2", () => {
    expect(search([-1, 0, 3, 5, 9, 12], 2)).toBe(-1);
  });
});
