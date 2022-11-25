<template>
  <div>
    <h3><b>Comment List</b></h3>
    <CommentForm/>
    <ul>
      <CommentListItem
        v-for="comment in comments"
        :key="comment.id"
        :comment="comment"
      />
    </ul>

  </div>
</template>

<script>
import CommentForm from '@/components/CommentForm.vue'
import CommentListItem from '@/components/CommentListItem.vue'

export default {
  name: 'CommentList',
  components: {
    CommentForm,
    CommentListItem
  },
  computed: {
    comments() {
      return this.$store.state.comments
    }
  },
  methods: {
    
  }
}
</script>

<style>

</style>