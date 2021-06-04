var input = require("fs").readFileSync("./dev/stdin/file.txt", "utf8");
var lines = input.split("\n");

var N = lines.shift();

while (N) {
  N = N.replace("\r", "");
  let lower = false;
  let upper = false;
  let number = false;
  let invalid = false;
  let l = N.split("");

  for (let i = 0; i < l.length; i++) {
    if (
      (l[i] < "0" || l[i] > "9") &&
      (l[i] < "A" || l[i] > "Z") &&
      (l[i] < "a" || l[i] > "z")
    ) {
      invalid = true;
      break;
    }

    if (l[i] >= "0" && l[i] <= "9") {
      number = true;
    }
    if (l[i] >= "a" && l[i] <= "z") {
      lower = true;
    }
    if (l[i] >= "A" && l[i] <= "Z") {
      upper = true;
    }
  }

  if (!invalid && lower && upper && number && N.length >= 6 && N.length <= 32) {
    console.log("Senha valida.");
  } else {
    console.log("Senha invalida.");
  }

  N = lines.shift();
}
