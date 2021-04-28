var input = require("fs").readFileSync("./dev/stdin/file.txt", "utf8");
var lines = input.split("\n");

var n = lines.shift();

for (let i = 0; i < parseInt(n); i++) {
  var m = lines.shift().split(" ");
  let sum = 0;
  let high = 0;
  for (let j = 1; j <= m[0]; j++) sum += parseInt(m[j]);

  for (let j = 1; j <= m[0]; j++) {
    if (sum / m[0] < m[j]) high++;
  }

  console.log(((high * 100) / m[0]).toFixed(3) + "%");
}
