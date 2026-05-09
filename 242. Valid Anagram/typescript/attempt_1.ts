function isAnagram(s: string, t: string): boolean {
	
	if (s.length !== t.length) return false

	function stringToMap(s: string): Map<string, number> {
		const tempMap = new Map<string, number>();
		for (const char of s) {
			const count = tempMap.get(char)
			tempMap.set(char, (count || 0) + 1)
		}
		return tempMap;
	}
	
	const sMap = stringToMap(s)
	const tMap = stringToMap(t)

	if (sMap.size !== tMap.size) return false

	for (const sItem of Array.from(sMap)) {
		
		const tValue = tMap.get(sItem[0])

		if (!tValue) return false
		if (tValue !== sItem[1]) return false
	}

  return true;
}

export default isAnagram;
