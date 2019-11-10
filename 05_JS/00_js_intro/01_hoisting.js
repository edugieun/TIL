console.log(a)
var a = 10
console.log(a)

// // JS가 이해한 코드
// // 선언만 위로 끌어 올린다.(hoisting)
var a // 선언 + 초기화(undefined)
console.log(a)
a = 10
console.log(a)

// let은 안된다. referencess error
console.log(b)
let b = 10
console.log(b)
// 마찬가지로 아래와 같은 과정을 거친다
// 아래 코드는 let의 호이스팅 과정의 이해를 돕기 위한 것으로 동작은 정상적으로 하나,
// 실제 호이스팅의 내부 처리 과정에서는 'let b' 부분이 메모리에 저장되지 않기 때문에 에러가 난다.
let b // 선언 + TDZ => 초기화가 안된 상태(메모리에 저장되지 않은 상태)
console.log(b)
b = 10 // 할당 불가 (초기화가 아직 안됨)
console.log(b)


// if (x !== 1) {
//   console.log(y) // undefined
//   var y = 3
//   if (y === 3) {
//     var x = 1
//   }
//   console.log(y) // 3
// }

// if (x === 1) {
//   console.log(y) // 3
// }
