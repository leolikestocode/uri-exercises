var input = require("fs").readFileSync("./dev/stdin/file.txt", "utf8");
var lines = input.split("\n");

var N = lines.shift();

while (N !== "0 0") {
  const [a, b] = N.split(" ");
  const arrA = String(a).replace(/\D/g, "").split("").reverse();
  const arrB = String(b).replace(/\D/g, "").split("").reverse();
  let count = 0;
  let carry = 0;

  for (let i = 0; i <= arrA.length; i++) {
    const parseA = parseInt(arrA[i]) || 0;
    const parseB = parseInt(arrB[i]) || 0;
    if (parseA + parseB + carry > 9) {
      carry = 1;
      count++;
    } else {
      carry = 0;
    }
  }

  if (count === 0) {
    console.log("No carry operation.");
  } else if (count === 1) {
    console.log("1 carry operation.");
  } else {
    console.log(`${count} carry operations.`);
  }

  N = lines.shift();
}
