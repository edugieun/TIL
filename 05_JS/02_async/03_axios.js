// 1. axios 설치해서 사용하기
const axios = require('axios')
axios.get('http://jsonplaceholder.typicode.com/posts')
  .then(response => {
    console.log(response)
  })
  .catch(err => {
    console.log(err)
  })