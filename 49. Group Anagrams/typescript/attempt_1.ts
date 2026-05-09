function groupAnagrams(strs: string[]): string[][] {
	const groups = new Map<string, string[]>();

	function mapToKey(map: Map<string, number>): string {
		const entries = [...map.entries()];
		entries.sort(([a], [b]) => a.localeCompare(b))

		const parts: string[] = [];

		for (const [key, value] of entries) {
			parts.push(`${key}:${value}`)
		}

		return parts.join(',');
	}

	for (const str of strs) {
		const strMap = new Map<string, number>();
		for (const char of str) {
			strMap.set(char, (strMap.get(char) || 0) + 1)
		}

		const hit = groups.get(mapToKey(strMap)) || []
		hit.push(str)
		groups.set(mapToKey(strMap), hit)
	}

	return [...groups.values()]
}

export default groupAnagrams;
