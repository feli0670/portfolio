let x = 11;
let y = 11;
let a = 1;
let b = 0;
let Rect = [];

function setup() {
  createCanvas(windowWidth, windowHeight);
}

function draw() {
  background("white");
  fill("red");
  stroke("black");
  circle(x, y, 20);
  x = x + a;
  y = y + b;

  //tegner
  for (let i = 0; i < Rect.length; i++) {
    rect(Rect[i][0], Rect[i][1], 50);
  }
}
  function keyPressed() {
    if (keyCode == 82) {
      //gemmer 
      Rect.push([mouseX, mouseY]);
    }

  if (keyCode === LEFT_ARROW && a >= 0) {
    b = 0;
    a--;
  } else if (keyCode === RIGHT_ARROW && a <= 0) {
    b = 0;
    a++;
  } else if (keyCode === DOWN_ARROW && b <= 0) {
    a = 0;
    b++;
  } else if (keyCode === UP_ARROW && b >= 0) {
    a = 0;
    b--;
  }
}
