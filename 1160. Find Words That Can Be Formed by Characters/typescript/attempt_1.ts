function countCharacters(words: string[], chars: string): number {
	const charsLength = chars.length;
	let sum = 0;

	const counts = new Map<string, number>();

	for (const char of chars) {
		counts.set(char, ( counts.get(char) || 0 ) + 1 )
	}

	for (const word of words) {
		const wordLength = word.length;
		if (wordLength > charsLength) continue

		const tempCount = new Map(counts);

		let isGood = true;
		for (const char of word) {
			const hit = tempCount.get(char);
			if (!hit) {
				isGood = false
				break;
			}
			tempCount.set(char, hit - 1)
		}

		if (!isGood) continue;

		sum += wordLength
	}

	return sum;
}

export default countCharacters;
