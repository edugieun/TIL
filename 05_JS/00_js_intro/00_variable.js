// // let 변수

// let x = 1

// if (x === 1) {
//   let x = 2
//   console.log(x) //  x: 2
// }

// console.log(x) // x: 1

// const (상수)

// const 선언시에 초기값을 생략하면 오류 발생
// const MY_FAV

// const MY_FAV = 7
// console.log('my favorite number is: ' + MY_FAV)
// 상수를 재할당, 재선언하려는 시도는 모두 오류 발생.
// MY_FAV = 20 // 재할당 불가
// const MY_FAV = 20 // 재선언 불가
// let MY_FAV = 20 // 재선언 불가
// var MY_FAV = 20 // 재선언 불가

// const MY_FAV = 7
// if (MY_FAV === 7) {
//   // 블록 유효 범위로 지정된 MY_FAV 변수를 만드므로 재선언 가능하다.
//   // 즉, 전역이 아닌 범위안이므로 이름 공간에서 충돌이 나지 않는다.
//   // const일지라도 역시 블록 범위 안이므로 충돌이 나지 않는다.
//   const MY_FAV = 20
//   console.log(MY_FAV)
// }
// console.log(MY_FAV)

// var(변수)
// function varTest() {
//   // let일 경우와 var일 경우 비교
//   let x = 1
//   // var x = 1
//   if (true) {
//     let x = 2 // 상위 블록과 다른 변순
//     // var x = 2 // 상위 블록과 같은 변수
//     console.log(x) // 2
//   }
//   console.log(x) 
// }
// varTest()

// let 과 var
// var a = 1
// let b = 2
// if (a === 1) {
//   var a = 11
//   let b = 22

//   console.log(a) // 11 
//   console.log(b) // 22
// }
// console.log(a) // 11
// console.log(b) // 2

// 식별자 작성 스타일
// 1. 카멜 케이스(camelCase) - 객체, 변수, 함수 (=== lower-camel-case)
let dog
let variableName
// 배열은 복수형 변수명 사용
const dogs = []
// 정규 표현식을 'r' 로 시작
const rDecs = /.*/
console.log(rDecs)
// 함수
function getPropertyName() {
  return 1
}
// boolean을 반환하는 변수나 함수 - 'is'로 시작
let isAvailable = false

// 2. 파스칼 케이스(PascalCase) - 클래스, 생성자 (=== upper-camel-case)
class User {
  constructor(options) {
    this.name = option.name
  }
}

// 3. 대문자 스네이크 케이스(SNAKE_CASE) - 상수
// 이 표현은 변수와 변수의 속성이 변하지 않는다는 것을 프로그래머에게 알려준다.
const API_KEY = 'vjfkdlsj43dl'