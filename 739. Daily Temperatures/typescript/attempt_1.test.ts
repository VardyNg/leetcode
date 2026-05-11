import dailyTemperatures from './attempt_1';

describe("test dailyTemperatures", () => {
  test("Test 1 - [73,74,75,71,69,72,76,73]", () => {
    expect(dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73])).toEqual([1, 1, 4, 2, 1, 1, 0, 0]);
  });

  test("Test 2 - [30,40,50,60]", () => {
    expect(dailyTemperatures([30, 40, 50, 60])).toEqual([1, 1, 1, 0]);
  });

  test("Test 3 - [30,60,90]", () => {
    expect(dailyTemperatures([30, 60, 90])).toEqual([1, 1, 0]);
  });
});
