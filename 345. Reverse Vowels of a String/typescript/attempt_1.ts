function reverseVowels(s: string): string {
	function isVowel(t: string): boolean {
		switch(t.toLowerCase()) {
			case "a":
			case "e":
			case "i":
			case "o":
			case "u":
				return true
			default: 
				return false
		}
	}

	let beginIndex = 0
	let endIndex = s.length - 1
	let sArr = s.split('');
	while (beginIndex < endIndex) {
		if(!isVowel(sArr[beginIndex])) {
			beginIndex += 1
			continue
		}

		if(!isVowel(sArr[endIndex])) {
			endIndex -= 1
			continue
		}
		
		const temp = sArr[beginIndex]
		sArr[beginIndex] = sArr[endIndex]
		sArr[endIndex] = temp

		beginIndex += 1
		endIndex -= 1
	}

	return sArr.join('')
}

export default reverseVowels;
