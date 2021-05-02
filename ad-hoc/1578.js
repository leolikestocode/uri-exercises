var input = require("fs").readFileSync("./dev/stdin/file.txt", "utf8");
var lines = input.split("\n");

var N = lines.shift();
let matriz = 4;

for (let i = 0; i < N; i++) {
  var M = lines.shift();
  var K = [];
  const arr = [];
  for (let j = 0; j < M; j++) {
    K.push(
      lines
        .shift()
        .replace("\r", "")
        .split(" ")
        .map((v, index) => {
          const d = BigInt(v * v);
          if ((arr[index] || 0) < String(d).length) {
            arr[index] = String(d).length;
          }
          return d;
        })
        .join(" ")
    );
  }
  console.log(`Quadrado da matriz #${matriz}:`);
  K.forEach((k) => {
    k.split(" ").forEach((el, ind) => {
      process.stdout.write(
        `${ind !== 0 ? " " : ""}${" ".repeat(
          arr[ind] - String(el).length
        )}${el}`
      );
    });
    console.log("");
  });
  console.log("");
  matriz++;
}
