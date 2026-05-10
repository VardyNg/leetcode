function finalString(s: string): string {
	const sArr = s.split('')

	function convert(index: number, input: string[]): string[] {
		if (index >= input.length) {
			return input;
		}

		if (input[index] !== 'i') {
			return convert(index + 1, input)
		}

		const temp: string[] = []
		for (let i = index - 1 ; i >= 0 ; i-- ) {
			temp.push(input[i])
		}
		temp.push(...input.slice(index + 1))

		return convert(index, temp)
	}

	return convert(0, sArr).join('')
}

export default finalString;
