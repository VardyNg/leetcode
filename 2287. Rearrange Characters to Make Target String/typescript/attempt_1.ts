function rearrangeCharacters(s: string, target: string): number {
	
	if (s.length < target.length) return 0
	
	const sCounts = new Map<string, number>();
	for (const char of s) {
		sCounts.set(char, ( sCounts.get(char) || 0) + 1)
	}
	
	const targetCounts = new Map<string, number>();
	for (const char of target) {
		targetCounts.set(char, ( targetCounts.get(char) || 0) + 1)
	}
	
	let sum = Math.floor(s.length / target.length)

	for (const item of targetCounts) {
		const hit = sCounts.get(item[0]);

		if (!hit) return 0;

		const minCount = Math.floor(hit / item[1])

		if (minCount === 0) return 0;

		if (minCount < sum) sum = minCount;
	}

	return sum;
}

export default rearrangeCharacters;
