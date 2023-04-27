// # Object
const player = {
  name: "Bill Gates",
  health: 85,
  skill: "Programmer",
};

// # Objects
const playerOne = {
  name: "Bill Gates",
  health: 85,
  skill: "Programmer",
};

const playerTwo = {
  name: "Elon Musk",
  health: 90,
  skill: "Legend",
};

const playerThree = {
  name: "Warren Buffett",
  health: 100,
  skill: "Investor",
};

// 위의 문제점 2가지
// 1. 오타
// 2. property에 무언가 추가할 경우 일일히 모두 수정해야 한다.
// 이를 해결하기 위해 Class가 등장했다.
// Class : 설계도와 같다.

// # JavaScript
// # Class
// # Python에서의 Class는 oop.py 참고
class Player {
  constructor(name, health, skill) {
    this.name = name;
    this.health = health;
    this.skill = skill;
    this.xp = 0;
  }
  sayHello() {
    return `Hi, my name is ${this.name} and my skill is ${this.skill}`;
  }
  takeHit() {
    this.health = this.health - 5;
  }
}

const bill = new Player("Bill Gates", 85, "Programmer");
const elon = new Player("Elon Musk", 90, "Legend");
const warren = new Player("Warren Buffett", 100, "Investor");
console.log(elon.skill);
console.log(elon.takeHit());

// constructor() { ... } : Method
// this : Python에 self와 같다. Class 내 인스턴스 변수와 인스턴스 메서드를 참조한다.

// # Inheritance (상속)
class Human {
  constructor(name) {
    this.name = name;
    this.arms = 2;
    this.legs = 2;
  }
}

class Baby extends Human {
  constructor(name) {
    // this.name = name;
    // this.arms = 2;
    // this.legs = 2;
    super(name); // 부모 Class에 접근
    this.cute = true;
  }
  cry() {
    return `waa waa`;
  }
}

class Teenager extends Human {
  constructor(name) {
    // this.name = name;
    // this.arms = 2;
    // this.legs = 2;
    super(name);
    this.emotional = true;
  }
  curse() {
    return `#$18%@&!`;
  }
}
