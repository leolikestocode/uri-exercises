var input = require("fs").readFileSync("./dev/stdin/file.txt", "utf8");
var lines = input.split("\n");

var N = lines.shift();

for (let i = 0; i < parseInt(N); i++) {
  const str = lines.shift();
  let finalStr = "";
  str.split(" ").forEach((item) => {
    if (item) finalStr += item[0];
  });
  console.log(finalStr);
}
