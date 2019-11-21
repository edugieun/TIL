<template>
  <div class="home">
    <h1>Todo with Django</h1>
    <TodoInput @createTodo="createTodo"/>
    <TodoList :todos="todos"/>
  </div>
</template>

<script>
// @ is an alias to /src
import router from '../router'
import TodoList from '@/components/TodoList'
import axios from 'axios'
// import jwtDecode from 'jwt-decode'
import TodoInput from '@/components/TodoInput'
import { mapGetters } from 'vuex'

export default {
  name: 'home',
  components: {
    TodoList,
    TodoInput,
  },
  data() {
    return {
      todos: [],
    }
  },
  methods: {
    // 로그인 여부 확인
    checkLoggedIn() {
      // this.$session.start()
      // if (!this.$session.has('jwt')) {
      if (!this.isLoggedIn) {
        router.push('/login')
      }
    },
    getTodos() {
      // this.$session.start()
      // const token = this.$session.get('jwt')
      // const requestHeader = {
      //   headers: {
      //     Authorization: 'JWT ' + token
      //   }
      // }
      // const user_id = jwtDecode(token).user_id
      // axios.get(`http://127.0.0.1:8000/api/v1/users/${user_id}/`, requestHeader)
      axios.get(`http://127.0.0.1:8000/api/v1/users/${this.userId}/`, this.requestHeader)
      .then(res => {
        this.todos = res.data.todo_set
      })
      .catch(err => {
        console.log(err)
      })
    },
    createTodo(title) {
      // this.$session.start()
      // const token = this.$session.get('jwt')
      // const requestHeader = {
      //   headers: {
      //     Authorization: 'JWT ' + token
      //   }
      // }
      // const user_id = jwtDecode(token).user_id
      const requestForm = new FormData()
      // requestForm.append('user', user_id)
      requestForm.append('user', this.userId)
      requestForm.append('title', title)

      axios.post('http://127.0.0.1:8000/api/v1/todos/', requestForm, this.requestHeader)
      .then(res => {
        this.todos.push(res.data)
      })
      .catch(arr => {
        console.log(arr)
      })
    }
  },
  computed: {
    // ...은 스프레트 문법 => 각각의 getters를 가져온다.
    // mapGetters는 함수의 인자로 들어가는 배열에는 getters에서 정의한 함수들 중에서 가지고 오고 싶은 getter들을 작성한다.
    ...mapGetters([
      'isLoggedIn',
      'requestHeader',
      'userId'
    ])
  },
  // DOM에 Vue instance가 mount 될 때마다 checkLoggedIn이 실행되어, 로그인 여부를 체크
  mounted() {
    this.checkLoggedIn()
    this.getTodos()
  }
}
</script>
