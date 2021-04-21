var input = require("fs").readFileSync("/dev/stdin", "utf8");
var lines = input.split("\n");
var N = lines.shift();

while (N != "0 0") {
  const [flaw, numbers] = N.split(" ");
  const regexRule = new RegExp(flaw, "g");
  console.log(
    String(BigInt(numbers.replace(regexRule, "") || 0)).replace("n", "")
  );

  N = lines.shift();
}
