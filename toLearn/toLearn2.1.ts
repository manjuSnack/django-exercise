// #2.1 __init__
// TypeScript → python

// 아래는 TypeScript로 작성된 예제.
class Person {
  constructor(private firstName: string, private lastName: string) {}
}

class Entrepreneur extends Person {
  constructor(
    firstName: string,
    lastName: string,
    private shares: number,
    private company: string
  ) {
    super(firstName, lastName);
  }
}

class Actor extends Person {
  constructor(
    firstName: string,
    lastName: string,
    private oscars: number,
    private age: number
  ) {
    super(firstName, lastName);
  }
}

// constructor : class가 생성될 때 호출되는 함수
