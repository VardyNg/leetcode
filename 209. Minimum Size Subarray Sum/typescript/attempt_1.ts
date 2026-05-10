function minSubArrayLen(target: number, nums: number[]): number {
	let leftPointer = 0
	let rightPointer = 0
	let minLength = nums.length;
	let counter = nums[0]
	let found = false

	while (leftPointer < nums.length) {
		
		if (counter < target ) {
			if (rightPointer < nums.length - 1) {
				rightPointer += 1
				counter += nums[rightPointer]
			} else {
				counter -= nums[leftPointer]
				leftPointer += 1	
			}
		} else {
			found = true
			minLength = Math.min(minLength, rightPointer - leftPointer + 1)
			counter -= nums[leftPointer]
			leftPointer += 1
		}
	}
	
	if (!found) return 0

	return minLength;
}

export default minSubArrayLen;
