function findMaxAverage(nums: number[], k: number): number {
	let startIndex = 0;

	let sum = 0;
	let maxAvg = 0;

	for (let i = startIndex ; i < k ; i++) {
		sum += nums[i]
	}
	maxAvg = sum / k

	while (startIndex + k - 1 < nums.length - 1) {
		sum = sum - nums[startIndex] + nums[startIndex + k - 1 + 1]
		startIndex += 1
		maxAvg = Math.max(maxAvg, sum / k)
	}

	return maxAvg
}

export default findMaxAverage;
