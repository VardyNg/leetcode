function groupAnagrams(strs: string[]): string[][] {
	const groups = new Map<string, string[]>();

	for (const str of strs) {
		const tempStr = str.split('').sort().join('');
		const hit = groups.get(tempStr) || [];
		hit.push(str)
		groups.set(tempStr, hit)
	}

	return [...groups.values()];
}

export default groupAnagrams;
