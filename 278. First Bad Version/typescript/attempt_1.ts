// The isBadVersion API is defined elsewhere.
// declare function isBadVersion(version: number): boolean;

function solution(isBadVersion: (version: number) => boolean) {
  return function (n: number): number {
		let l = 1
		let r = n

		while ( l < r ) {
			const mid = Math.floor((r + l) / 2)
			if (isBadVersion(mid)) {
				r = mid
			} else {
				l = mid + 1
			}

		}

		return l
  };
}

export default solution;
