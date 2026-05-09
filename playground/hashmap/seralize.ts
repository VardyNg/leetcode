function mapToKey(map: Map<string, number>) {
	const entires = [...map.entries()];
	entires.sort(([a], [b] ) => a.localeCompare(b));

	const parts = []
	for (const [key, val] of entires) {
		parts.push(`${key}:${val}`)
	}

	return parts.join(',')
}

const child1 = new Map<string, number>();
child1.set('a', 1)
child1.set('b', 1)

const child2 = new Map<string, number>();
child2.set('a', 1)
child2.set('b', 2)

const parentMap = new Map<string, number>();

parentMap.set(mapToKey(child1), 0)
parentMap.set(mapToKey(child2), 1)

console.log(parentMap)

const child3 = new Map<string, number>();
child3.set('b', 2)
child3.set('a', 1)

console.log(parentMap.get(mapToKey(child3)));