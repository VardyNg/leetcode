function lengthOfLongestSubstring(s: string): number {
	let charSet = new Set<string>();

	let leftPointer = 0
	let maxLength = 0

	for (let rightPointer = 0 ; rightPointer < s.length ; rightPointer++) {
		while (charSet.has(s[rightPointer])) {
			charSet.delete(s[leftPointer])
			leftPointer += 1
		}
		charSet.add(s[rightPointer])
		maxLength = Math.max(maxLength, rightPointer - leftPointer + 1)
	}
	return maxLength;
}

export default lengthOfLongestSubstring;
