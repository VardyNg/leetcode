function search(nums: number[], target: number): number {
	let l = 0;
	let r = nums.length - 1;

	while (r >= l) {
		const mid = Math.floor((r + l) / 2);
		if (nums[mid] === target) return mid;
		if (nums[mid] < target) l = mid + 1
		if (nums[mid] > target) r = mid - 1
	}

	return -1
}

export default search;
