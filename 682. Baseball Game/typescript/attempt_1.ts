function calPoints(operations: string[]): number {
	const stack: number[] = [];
	let sum = 0;
	for (const op of operations) {
		switch(op) {
			case 'C':
				if (stack.length > 0) {
					sum -= stack[stack.length - 1]
					stack.pop();
				}
				break;
			case '+':
				if (stack.length >= 2) {
					const res = stack[stack.length - 1] + stack[stack.length - 2]
					sum += res
					stack.push(res)
				}
				break;
			case 'D':
				if (stack.length > 0) {
					const res = stack[stack.length - 1] * 2
					sum += res
					stack.push(res)
				}
			break
			default:
				const res = parseInt(op) 
				sum += res
				stack.push(res)
		}

	}

	return sum;
}

export default calPoints;
