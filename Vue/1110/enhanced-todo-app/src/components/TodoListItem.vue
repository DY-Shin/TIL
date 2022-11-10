<template>
  <div class="todo-list-item">
    <div class="todo-list-item_main">
      <label :class="{'is-completed': todo.isCompleted}">
        <input type="checkbox" @click="updateTodoStatus" class="me-3 d-none">
        <i class="bi bi-circle h4 clickable"></i>
        <span class="ms-2 clickable">{{ todo.content }}</span>
      </label>
      <button class="btn ms-auto" @click="updateImportance">
        <i class="bi bi-star-fill fc-yellow"></i>
      </button>
    </div>
   </div>
</template>

<script>
export default {
  name: 'TodoListItem',
  props: {
    todo: Object,
  },
  methods: {
    updateTodoStatus() {
      this.$store.dispatch('updateTodoStatus', this.todo)
    },
    updateImportance() {
      this.$store.dispatch('updateImportance', this.todo)
    },
  }
}
</script>

<style>
  .todo-list-item{
    position: relative;
  }

  .todo-list-item_main{
    margin: 1rem 0;
    padding: 1rem;
    display: flex;
    align-items: center;
    border: 1px solid #D1D5DB;
    border-radius: 0.5rem;
    cursor: pointer;
  }

  label{
    display: inline-block;
  }

  .is-completed {
    text-decoration: line-through;
  }

  .fc-yellow {
    color: #FBBF24;
  }
</style>