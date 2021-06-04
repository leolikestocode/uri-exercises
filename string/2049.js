var input = require("fs").readFileSync("./dev/stdin/file.txt", "utf8");
var lines = input.split("\n");

var n = lines.shift().replace("\r", "");
let i = 0;
while (n) {
  if (n == "0") {
    break;
  }
  m = lines.shift().replace("\r", "");

  if (i !== 0) {
    console.log("");
  }

  console.log(`Instancia ${++i}`);
  console.log(m.indexOf(n) !== -1 ? "verdadeira" : "falsa");

  n = lines.shift().replace("\r", "");
}
