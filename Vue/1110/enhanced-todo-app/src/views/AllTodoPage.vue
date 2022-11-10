<template>
  <div>
    <h1>모든 할일</h1>
    <form @submit.prevent="createTodo">
      <input type="submit" class="btn" value="+">
      <!-- <i class="bi bi-plus-lg"></i> -->
      <input type="text" v-model.trim="content">
    </form>
    <hr>
    <ul class="ul">
      <TodoListItem 
        v-for="todo in list.slice().reverse()"
        :key="todo.id"
        :todo=todo
      />
    </ul>
  </div>
</template>

<script>
import TodoListItem from '@/components/TodoListItem'

export default {
  name: 'AllTodoPage',
  components: {
    TodoListItem,
  },
  data() {
    return {
      content: null,
    }
  },
  computed: {
    list() {
      return this.$store.state.list
    }
  },
  methods: {
    createTodo() {
      const content = this.content
      if (this.content) {
        this.$store.dispatch('createTodo', content)
      }
      this.content = null
    }
  }
}
</script>

<style>
  .ul {
  list-style: none;
  padding: 0;
  }
</style>
