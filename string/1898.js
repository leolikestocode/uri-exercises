var input = require("fs").readFileSync("./dev/stdin/file.txt", "utf8");
var lines = input.split("\n");

var n = lines.shift().replace(/[^0-9.]+/g, "");
var m = lines.shift().replace(/[^0-9.]+/g, "");

var cpf = n.substring(0, 11);
var sum = n.substring(11, n.length);

mDot = m.split("").findIndex((item) => item === ".");
sumDot = sum.split("").findIndex((item) => item === ".");

if (mDot !== -1) {
  m = m.substring(0, mDot + 3);
}

if (sumDot !== -1) {
  sum = sum.substring(0, sumDot + 3);
}

console.log(`cpf ${cpf}`);
console.log((parseFloat(m) + parseFloat(sum)).toFixed(2));
