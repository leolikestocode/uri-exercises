var input = require("fs").readFileSync("./dev/stdin/file.txt", "utf8");
var lines = input.split("\n");

var N = lines.shift();

function toObject(arr) {
  var rv = {};
  for (var i = 0; i < arr.length; ++i) rv[arr[i]] = 0;
  return rv;
}

for (let i = 0; i < N; i++) {
  const M = lines.shift();
  const letterLower = M.toLocaleLowerCase().replace(/[^a-z]|/g, "");
  const objLetters = toObject([..."abcdefghijklmnopqrstuvwxyz"]);
  let final = "";
  let maior = -1;

  letterLower.split("").forEach((item) => {
    objLetters[item] += 1;
  });

  Object.entries(objLetters).forEach(([key, value]) => {
    if (value === maior) {
      final += key;
    }
    if (value > maior) {
      maior = value;
      final = key;
    }
  });

  console.log(final);
}
