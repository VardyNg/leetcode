function search(nums: number[], target: number): number {

	function binarySearch(l: number, r: number) {

		const mid = Math.floor((r + l) / 2)

		if (nums[mid] === target) {
			return mid
		} else if (r === l) {
			return -1
		} else if (nums[mid] > target) {
			return binarySearch(l, mid - 1)
		} else if (nums[mid] < target) {
			return binarySearch(mid + 1, r)
		}

		return -1
	}

	return binarySearch(0, nums.length - 1)
}

export default search;
