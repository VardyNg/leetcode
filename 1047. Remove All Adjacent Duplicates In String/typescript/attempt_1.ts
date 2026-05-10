function removeDuplicates(s: string): string {
	let stack: string[] = [];
	
	for (const char of s) {
		if (stack.length == 0 || stack[stack.length - 1] !== char) {
			stack.push(char)
		} else {
			stack.pop();
		}
	}

	return stack.join('')
}

export default removeDuplicates;
