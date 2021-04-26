var input = require("fs").readFileSync("./dev/stdin/file.txt", "utf8");
var lines = input.split("\n");

var N = lines.shift();
while (N) {
  N = N.replace(/(o|O)/g, "0")
    .replace(/l/g, "1")
    .replace(/[^0-9]/g, "");

  N = parseInt(N);

  if (N && N <= 2147483647) {
    console.log(N);
  } else {
    console.log("error");
  }

  N = lines.shift();
}
