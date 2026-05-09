function isPalindrome(s: string): boolean {
	let beginPointer = 0
	let endPointer = s.length - 1

	function isAlphanumeric(char: string): boolean {
		return /[a-z0-9]/i.test(char);
	}


	while (beginPointer < endPointer) {
		if (!isAlphanumeric(s[beginPointer])) {
			beginPointer += 1;
			continue
		}
		
		if (!isAlphanumeric(s[endPointer])) {
			endPointer -= 1;
			continue
		}

		if (s[beginPointer].toLowerCase() !== s[endPointer].toLowerCase()) {
			return false
		}
		
		beginPointer += 1;
		endPointer -= 1;
	}

	return true
}

export default isPalindrome;
