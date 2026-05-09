const hashmap = new Map<string, number>();

console.log(hashmap);

hashmap.set('a', 1);
hashmap.set('b', 2);
console.log(hashmap);

console.log(hashmap.has('a'));

console.log(hashmap.entries());
console.log(hashmap.keys());
console.log(hashmap.values());


hashmap.delete('a')
