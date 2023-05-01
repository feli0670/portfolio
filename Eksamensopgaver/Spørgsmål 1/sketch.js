let x = 11;
let y = 11;
let a = 1;
let b = 0;

let cirkler = []; //array, hvor længden af det vil komme til at afhænge af 'i'
let antal; //variabel

function setup() {
  createCanvas(windowWidth, windowHeight); //programmets flade
  antal = random(5, 15); //variablen tildeles en værdi

  //for-løkken som genererer cirklerne
  for (let i = 0; i < antal; i++) {
    //for-løkke som kører et antal gange baseret på 'antal' (en tilfældig værdi mellem 5 og 15)
    cirkler[i] = new cirkel(); //cirkler generes, antallet afhænger af hvor mange gange løkken køres
  }
}

function draw() {
  background("black"); //baggrund
  fill("red"); //udfyldning
  x += a;
  y += b;
  circle(x, y, 20);
  if (x < 20 / 2 || x > width - 20 / 2) {
    a *= -1;
  }
  if (y < 20 / 2 || x > width - 20 / 2) {
    b *= -1;
  }

  //for-løkke der søger for at vise cirklerne og sørge for de er i bevægelse
  for (let i = 0; i < antal; i++) {
    //for-løkke som kører et antal gange baseret på 'antal' (en tilfældig værdi mellem 5 og 15)
    cirkler[i].vis(); //metoden 'vis' i klassen 'cirkel' bliver kaldet for 'i' cirkel
    cirkler[i].bevæg(); //metoden 'bevæg' i klassen 'cirkel' bliver kaldet for 'i' cirkel
  }
}

//klasse til cirklerne
class cirkel {
  //klassens opbygning og parametre
  constructor() {
    this.d = 20; //cirklernes diameter
    this.x = random(this.d / 2, width - this.d / 2); //cirkel x-position
    this.y = random(this.d / 2, height - this.d / 2); //cirkel y-position
    this.xspeed = random(1, 5); //x-hastighed
    this.yspeed = random(1, 5); //y-hastighed
  }

  //metode til kontrol og styring af cirklernes bevægelser
  bevæg() {
    this.x += this.xspeed; //x-hastigheden bliver lagt til cirklens x-position, så cirklen vil bevæge sig
    this.y += this.yspeed; //y-hastigheden bliver lagt til cirklens x-position, så cirklen vil bevæge sig

    //følgende to if-statements sørger for at cirklerne ikke bevæger sig uden for programmets flade
    if (this.x < this.d / 2 || this.x > width - this.d / 2) {
      //kode i statementet køre sålænge en af udtrykkende er sande
      this.xspeed *= -1; //cirklens x-hastighed skifter fortegn og derfor retning
    }
    if (this.y < this.d / 2 || this.y > height - this.d / 2) {
      //kode i statementet køre sålænge en af udtrykkende er sande
      this.yspeed *= -1; //cirklens y-hastighed skifter fortegn og derfor retning
    }
  }

  //metode til som viser cirklen på programmets flade
  vis() {
    circle(this.x, this.y, this.d); //cirkel på baggrund af forskellige parametre
  }
}
