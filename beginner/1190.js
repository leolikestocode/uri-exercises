var input = require("fs").readFileSync("./dev/stdin/file.txt", "utf8");
var lines = input.split("\n");

var n = lines.shift().replace("\r", "");
var s = 0;

for (let i = 0; i < 12; i++) {
  for (let j = 0; j < 12; j++) {
    var m = parseFloat(lines.shift());
    if (j > 6 && j + i >= 12 && j > i) {
      console.log(`j, i`, j, i);
      s += m;
    }
  }
}

if (n === "S") console.log(s.toFixed(1));
if (n === "M") console.log((s / 30).toFixed(1));
