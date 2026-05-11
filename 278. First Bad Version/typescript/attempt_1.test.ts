import solution from './attempt_1';

describe("test firstBadVersion", () => {
  test("Test 1 - n=5, bad=4", () => {
    const isBadVersion = (version: number) => version >= 4;
    const firstBadVersion = solution(isBadVersion);
    expect(firstBadVersion(5)).toBe(4);
  });

  test("Test 2 - n=1, bad=1", () => {
    const isBadVersion = (version: number) => version >= 1;
    const firstBadVersion = solution(isBadVersion);
    expect(firstBadVersion(1)).toBe(1);
  });

  test("Test 3 - n=10, bad=7", () => {
    const isBadVersion = (version: number) => version >= 7;
    const firstBadVersion = solution(isBadVersion);
    expect(firstBadVersion(10)).toBe(7);
  });

  test("Test 4 - n=3, bad=2", () => {
    const isBadVersion = (version: number) => version >= 2;
    const firstBadVersion = solution(isBadVersion);
    expect(firstBadVersion(3)).toBe(2);
  });
});
