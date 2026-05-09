function isPalindrome(s: string): boolean {
	s = s.replace(/[^a-z0-9]/gi, "")
	s = s.split('').map((char) => char = char.toLowerCase()).join('')

	if (s.length === 1) return true

	let beginPointer = 0
	let endPointer = s.length - 1

	while (beginPointer < endPointer) {
		if (s[beginPointer] !== s[endPointer]) return false

		beginPointer += 1;
		endPointer -= 1;
	}

	return true
}

export default isPalindrome;
