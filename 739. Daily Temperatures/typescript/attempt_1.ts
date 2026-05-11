function dailyTemperatures(temperatures: number[]): number[] {
	let res: number[] = []

	for (let i = 0 ; i < temperatures.length ; i++) {
		let day = 0;
		for ( let j = i + 1; j < temperatures.length ; j++) {
			if (temperatures[j] > temperatures[i]) {
				day = j - i
				break
			}
		}
		res.push(day)
	}

	return res
}

export default dailyTemperatures;
