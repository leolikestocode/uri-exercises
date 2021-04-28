var input = require("fs").readFileSync("./dev/stdin/file.txt", "utf8");
var lines = input.split("\n");

var N = lines.shift();

while (N) {
  [d, vf, vg] = N.split(" ");

  const dist = Math.sqrt(144 + d * d);
  const tf = 12 / vf;
  const tg = dist / vg;

  console.log(tg <= tf ? "S" : "N");

  N = lines.shift();
}
