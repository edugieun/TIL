function doSomething(subject, callback) {
  console.log(`이제 ${subject} 과목평가 준비를 시작해볼까?`)
  callback()
}

// 무명함수 사용
doSomething('django', function () {
  console.log('며칠 안 남았는다?')
})

// 기명함수 사용
function alertFinish() {
  console.log('며칠 안 남았는다?')
}

doSomething('django', alertFinish)