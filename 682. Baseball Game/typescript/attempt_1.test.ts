import calPoints from './attempt_1';

describe("test calPoints", () => {
  test("Test 1 - ['5','2','C','D','+']", () => {
    expect(calPoints(["5", "2", "C", "D", "+"])).toBe(30);
  });

  test("Test 2 - ['5','-2','4','C','D','9','+','+']", () => {
    expect(calPoints(["5", "-2", "4", "C", "D", "9", "+", "+"])).toBe(27);
  });

  test("Test 3 - ['1','C']", () => {
    expect(calPoints(["1", "C"])).toBe(0);
  });
});
