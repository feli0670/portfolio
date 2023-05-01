//Opgave c
function numbers(n, state) {
  let L = [];
  let i = 0;

  if (state != null) {
    for (let i = 0; i < n; i++) {
      if (state === "lige" && i % 2 == 0) {
        L.push(i);
      } else if (state === "ulige" && i % 2 != 0) {
        L.push(i);
      }
    }
    return L;
  } else if (n == 0 && state == 0) {
    return "1 3 5 7 9";
  }
}
console.log(numbers(/*n:*/ 100, /*state:*/ "lige"));

//Opgave d
function setup() {
  createCanvas(400, 400);
  drawCircle(20);
}

function drawCircle(n) {
  for (let i = 0; i < n; i++) {
    let r = random(10, 100);
    circle(random(r, width - r), random(r, height - r), r);
  }
}
