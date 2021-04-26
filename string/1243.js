var input = require("fs").readFileSync("./dev/stdin/file.txt", "utf8");
var lines = input.split("\n");

var N = lines.shift();
// not finished - with cases to test
while (N) {
  N = N.toLocaleLowerCase();
  const words = N.trim()
    .replace(/[(0-9|.)]/g, "")
    .split(" ")
    .filter((item) => item);
  const noSpace = N.replace(/[^a-z]/g, "");

  // console.log(`words`, words.length, words);

  if (noSpace.length / words.length <= 3) {
    console.log("250", words, noSpace);
  } else if (noSpace.length / words.length >= 6) {
    console.log("1000", words, noSpace);
  } else {
    console.log("500", words, noSpace);
  }

  N = lines.shift();
}
