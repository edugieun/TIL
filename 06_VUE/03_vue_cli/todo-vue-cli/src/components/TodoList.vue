<template>
  <div class="todo-list">
    <h2>{{ category }}</h2>
    <input type="text" v-model="newTodo" @keyup.enter="addTodo">
    <button @click="addTodo">+</button>
    <li v-for="todo in todos" v-bind:key="todo.id">
      <span>{{ todo.content }}</span>
      <button @click="removeTodo(todo.id)">x</button>
    </li>
  </div>
</template>

<script>
  export default {
    props: {
      // 문자열인 동시에 반드시 필요로 하는 데이터이다.
      category: {
        String,
        required: true,
        // 유효성 검사
        validator: function (value) {
          if (value.length < 5) {
            return true
          } else {
            return false
          }
        }
      }
    },

    data: function () {
      return {
        todos: [],
        newTodo: '',
      }
    },

    methods: {
      addTodo: function () {
        if (this.newTodo.length !== 0) {
          this.todos.push({
            id: Date.now(),
            content: this.newTodo,
            completed: false,
          })
          this.newTodo = ''
        }
      },
      removeTodo: function (todoId) {
        this.todos = this.todos
          .filter(todo => {
            return todo.id !== todoId
          })
      },
    }
  }
</script>

<style>
  .todo-list {
    display: inline-block;
    width: 33%;
  }
</style>