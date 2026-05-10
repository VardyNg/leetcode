import finalString from './attempt_2';

describe("test finalString", () => {
  test("Test 1 - 'string'", () => {
    expect(finalString("string")).toBe("rtsng");
  });

  test("Test 2 - 'poiinter'", () => {
    expect(finalString("poiinter")).toBe("ponter");
  });
});
