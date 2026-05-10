import maxProfit from './attempt_1';

describe("test maxProfit", () => {
  test("Test 1 - [7,1,5,3,6,4]", () => {
    expect(maxProfit([7, 1, 5, 3, 6, 4])).toBe(5);
  });

  test("Test 2 - [7,6,4,3,1] no profit", () => {
    expect(maxProfit([7, 6, 4, 3, 1])).toBe(0);
  });
});
