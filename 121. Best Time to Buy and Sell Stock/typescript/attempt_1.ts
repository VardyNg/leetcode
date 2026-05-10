function maxProfit(prices: number[]): number {
	if (prices.length <= 1) return 0

	let start = 0
	let end = 1
	let profit = 0
	while (end <= prices.length - 1) {
		
		if (prices[start] > prices[end]) {
			start = end
			end = end + 1
			continue
		}
		
		profit = Math.max(prices[end] - prices[start], profit)
		end = end + 1
	}
	return profit;
}

export default maxProfit;
