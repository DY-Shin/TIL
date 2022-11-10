<template>
  <div>
    <h1>중요 할일</h1>
    <ul v-for="todo in list" :key="todo.id">
      <div v-if="todo.isImportant">
        <label :class="{'is-important': todo.isImportant}">
          <span class="ms-2 clickable">{{ todo.content }}</span>
        </label>
      </div>
    </ul>
  </div>
</template>

<script>
export default {
  name: 'ImportantTodoPage',
  computed: {
    list() {
      return this.$store.state.list
    }
  }
}
</script>

<style>

</style>