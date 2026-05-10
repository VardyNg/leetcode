function isValid(s: string): boolean {

	let queue: string[] = [];
	const pairs: Record<string, string> = {
		"(": ")",
		"[": "]",
		"{": "}",
	}
	
	for (const char of s) {
		if (Object.keys(pairs).includes(char)) {
			queue.push(pairs[char]);
		} else if (queue[queue.length - 1] === char) {
			queue.pop()
		} else {
			return false
		}
	}

	return queue.length === 0
}

export default isValid;
