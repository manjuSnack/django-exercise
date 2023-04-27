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
