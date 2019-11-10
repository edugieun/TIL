// const me = {
//   name: 'ssafy', // key 가 한 단어 일때는 '' 없이 써도 된다.
//   'phone number': '01012345678', // kety가 여러 단어 일 경우는 '' 를 사용
//   appleProducts: {
//     ipad: '2018pro',
//     iphone: '7',
//     macbook: '2019pro',
//   }
// }

// console.log(me.name) // ssafy / 키가 한 단어 일 경우 그냥 '.'으로 호출 가능
// console.log(me['name']) // ssafy
// console.log(me['phone number']) // 키가 여러 단어일 경우 반드시 대괄호 [' '] 로 호출
// console.log(me.appleProducts)
// console.log(me.appleProducts.ipad)

// // Oject Literal (객체 표현법)
// // ES5 시절 사용법
// var books = ['Learning JS', 'Eloquent JS']
// var comics = {
//   'DC': ['Joker', 'Aquaman'],
//   'Marvel': ['Captain Marvel', 'Avengers'],
// }
// var magazines = null

// var bookShop = {
//   books: books,
//   comics: comics,
//   magazines: magazines,
// }
// console.log(bookShop)
// console.log(typeof(bookShop))
// console.log(bookShop.books[0])

// // ES6+ 부터
// // object의 key와 value가 같다면, 마치 배열처럼 한번만 작성 가능
// let bookShop2 = {
//   books,
//   comics,
//   magazines,
// }
// console.log(bookShop2)

////////////////////////

// JSON
const jsonData = JSON.stringify({ // JSON -> String
  coffee: 'Americano',
  iceCream: 'Mint Choco',
})
console.log(jsonData) // {"coffee":"Americano","iceCream":"Mint Choco"}
console.log(typeof(jsonData)) // string

const parseData = JSON.parse(jsonData)
console.log(parseData) // { coffee: 'Americano', iceCream: 'Mint Choco',} // 트레일링 콤마는 객체에서만 쓸 수 있고, JSON에서는 사용 불가
console.log(typeof(parseData)) // object