function canConstruct(ransomNote: string, magazine: string): boolean {
	if (ransomNote.length > magazine.length) return false;

	const hashMap = new Map<string, number>();

	for (const char of magazine) {
		hashMap.set(char, ( hashMap.get(char) || 0 ) + 1)
	}

	for (const char of ransomNote) {
		const hit = hashMap.get(char)
		if (!hit) return false
		if (hit == 0) return false // can remove this, as !hit already check hit == 0
		hashMap.set(char, hit - 1)
	}

	return true
}

export default canConstruct;
