function reverseString(s: string[]): void {
	let beginIndex = 0
	let endIndex = s.length - 1

	while (beginIndex < endIndex) {
		const temp = s[beginIndex]
		s[beginIndex] = s[endIndex]
		s[endIndex] = temp

		beginIndex += 1
		endIndex -= 1
	}
}

export default reverseString;
