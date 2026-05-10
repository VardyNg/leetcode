function finalString(s: string): string {
	const temp: string[] = []

	let isReverse = false

	for (const char of s) {
		if (char === 'i') {
			isReverse = !isReverse
		} else if(isReverse) {
			temp.unshift(char)
		} else {
			temp.push(char)
		}
	}

	if (isReverse) {
		temp.reverse()
	}
	return temp.join('')
}

export default finalString;
