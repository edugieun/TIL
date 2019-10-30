const numbers = [1, 2, 3, 4,]
console.log(numbers[0])
console.log(numbers[-1]) // undefined : 정확한 양의 정수 index만 가능
console.log(numbers.length)

console.log(numbers.reverse()) // 원본을 뒤집음
console.log(numbers)
console.log(numbers.reverse())
console.log(numbers)

// push - 값을 집어넣는 동시에 return 값은 배열의 길이를 리턴한다.
console.log(numbers.push('a'))
console.log(numbers)

// pop - 배열의 마지막 요소 제거 후 그 요소를 return
console.log(numbers.pop())
console.log(numbers)

// unshift - 배열의 가장 앞에 요소를 추가하고 return 은 배열의 길이
console.log(numbers.unshift('a'))
console.log(numbers)

// shift - 배열의 첫 요소 제거 후 그 요소를 return
console.log(numbers.shift())
console.log(numbers)

// includes - 배열에 값이 있는지 확인. boolean return
console.log(numbers.includes(1))
console.log(numbers.includes(0))

console.log(numbers.push('a', 'a'))
console.log(numbers)
console.log(numbers.indexOf('a')) // 중복이 존재한다면 처음 찾은 요소의 index를 return
console.log(numbers.indexOf('b')) // 찾고자 하는 요소가 없으면 -1 을 return

// join - 배열의 요소를 join 함수의 인자를 기준으로 이어서 문자열로 return
console.log(numbers.join()) // '1,2,3,4,a,a' 배열을 문자열로 만든다. / 아무것도 넣지 않으면, ',' 쉼표를 기준으로 가져옴
console.log(numbers.join('')) // '1234aa'
console.log(numbers.join('-')) // '1-2-3-4-a-a'
console.log(numbers)