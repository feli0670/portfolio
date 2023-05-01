class Animal{
  constructor(name) {
    this.animalName = name
  }
  
  displayName() {
    console.log(this.animalName)
  }
}

class Vertebrate extends Animal{
  constructor(name){
    super(name)
    this.animalType = 'Vertebrate'
    this.numberOfVertebrate = 60000
    this.look = ['Fur or hair','Gills and scale']
  }
}

class Mamal extends Vertebrate{
  constructor(name) {
    super(name)
    this.animalClass = 'Mamal'
    this.numberOfMamal = 5400
    this.lookMamal = this.look[0]
  }
}

class Fish extends Vertebrate{
  constructor(name) {
    super(name)
    this.animalClass = 'Fish'
    this.numberOfFish = 29000
    this.look = [1]
  }
}

class Salmon extends Fish{
  constructor(name) {
    super(name)

  }

}


var dyr = new Salmon('jo')
dyr.displayName() 