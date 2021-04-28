var input = require("fs").readFileSync("./dev/stdin/file.txt", "utf8");
var lines = input.split("\n");

var n = lines.shift();

while (n) {
  let l = 1,
    c = 1;

  while (l % n != 0) {
    l = (10 * l + 1) % n;
    c++;
  }

  console.log(c);

  n = lines.shift();
}
