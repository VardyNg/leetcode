function isValid(s: string): boolean {

	let stack: string[] = [];
	const pairs: Record<string, string> = {
		"(": ")",
		"[": "]",
		"{": "}",
	}
	
	for (const char of s) {
		if (char in pairs) {
			stack.push(pairs[char]);
		} else if (stack[stack.length - 1] === char) {
			stack.pop()
		} else {
			return false
		}
	}

	return stack.length === 0
}

export default isValid;
