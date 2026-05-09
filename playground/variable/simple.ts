console.log(c)

try {
	console.log(a, b)
} catch (e) {
	console.log("a and b are TDZ and can't be accesed before decleration")
	console.error(e);
}

const a = "a";
let b = "b";
var c = "c"

console.log(a, b, c);

