function minSubArrayLen(target: number, nums: number[]): number {
	let leftPointer = 0
	let min = Infinity
	let sum = 0
	for (let rightPointer = 0 ; rightPointer < nums.length ; rightPointer++) {
		sum += nums[rightPointer]

		while (sum >= target) {
			min = Math.min(min, rightPointer - leftPointer + 1)
			sum -= nums[leftPointer]
			leftPointer += 1
		}
	}

	return min === Infinity ? 0 : min
}

export default minSubArrayLen;
