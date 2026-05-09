function isAnagram(s: string, t: string): boolean {
	
	if (s.length !== t.length) return false

	const hashMap = new Map<string, number>();

	for (const char of s) {
		const count = hashMap.get(char)
		hashMap.set(char, (count || 0) + 1)
	}

	for (const char of t) {
		const count = hashMap.get(char);
		if (!count) return false
		hashMap.set(char, count - 1);
	}

  return true;
}

export default isAnagram;
