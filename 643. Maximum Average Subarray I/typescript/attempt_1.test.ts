import findMaxAverage from './attempt_1';

describe("test findMaxAverage", () => {
  test("Test 1 - [1,12,-5,-6,50,3], k=4", () => {
    expect(findMaxAverage([1, 12, -5, -6, 50, 3], 4)).toBeCloseTo(12.75);
  });

  test("Test 2 - [5], k=1", () => {
    expect(findMaxAverage([5], 1)).toBeCloseTo(5.0);
  });
});
