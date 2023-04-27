// Functional Programming
// imperative code (명령형 코드) 예시

function spaceToHeart(text) {
  let result = "";
  for (let i = 0; i < text.length; i++) {
    if (text[i] === " ") {
      result += "❤";
    } else {
      result += text[i];
    }
  }
  return result;
}

// declarative code (선언형 코드) 예시
function spaceToHeart(text) {
  return text.replaceAll(" ", "❤");
}

console.log(spaceToHeart("I love you")); // I❤love❤you

// ---
// imperative code (명령형 코드) 예시
const arr = [1, 2, 3, 4, 5, 6, 7, 8, 9];

function removeOdd(items) {
  const result = [];
  for (let i = 0; i < items.length; i++) {
    if (items[i] % 2 === 0) {
      result.push(items[i]);
    }
  }
  return result;
}

// declarative code (선언형 코드) 예시
function checkForOdd(item) {
  return item % 2 === 0;
}

function removeOdd(items) {
  return items.filter(checkForOdd);
}

console.log(removeOdd(arr)); // [ 2, 4, 6, 8 ]

// Imperative와 declarative의 차이점
// 명령형(imperative) 코드와 선언형(declarative) 코드의 차이점

// 명령형(imperative) 코드
// :  그 결과값에 '어떻게' 도달하느냐에 관한 것

// 선언형(declarative) 코드
// : 대표적으로 CSS가 이에 해당 된다. 원하는 '결과값'을 선언하는 것. JavaScript에서는 .replaceAll( ), .filter( )와 같은 함수를 일컫는다.
// 대부분 선언형 코드의 내부에는 명령형 코드로 작성되어 있다.
