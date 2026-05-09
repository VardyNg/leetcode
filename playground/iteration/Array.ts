const arr: number[] = [1,4,5,1,2,3]
console.log(arr);

for (const num of arr) { // return value
	console.log(num)
	console.log(typeof num)
}

for (const num in arr) { // return index
	console.log(num)
	console.log(typeof num)
}