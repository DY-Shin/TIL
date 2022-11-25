<template>
  <!-- <div v-if="profile.comments.length > 0">
    <ul class="list-group list-group-flush list-group-numbered mx-5">
      <li class="
                list-group-item
                d-flex
                justify-content-between
                align-items-start
                bg-transparent
                text-white
                border-bottom
                my-1" v-for="(comment, index) in commentsPerPage[commentCurrentPage - 1]" :key="index"
        @dblclick="onClickReview(comment.review.pk)">
        <div class="ms-2 me-auto">
          <h5 class="fw-bold">
            {{ comment.review.movie.title }}
          </h5>
          <div class="text-start">
            {{ comment.content.length > 30 ? comment.content.slice(0, 20) + '...' : comment.content }}
          </div>
        </div>
      </li>
    </ul>
  
  
  </div> -->
  
  <div v-if="comments.length > 0">
    <UserCommentItem
      v-for="comment in comments"
      :key="comment.id"
      :comment="comment"
    />
  </div>
  <div v-else class="fw-bold text-center text-white mx-5">
    <h4>댓글이 없네요..</h4>
  </div>
</template>

<script>
import UserCommentItem from '@/components/UserCommentItem.vue'
// import axios from 'axios'
// const API_URL = "http://127.0.0.1:8000"

export default {
  name: 'UserComment',
  components: {
    UserCommentItem
  },
  computed: {
    comments() {
      return this.$store.state.usercomments
    }
  },
  data() {
    return {
      // comment : [],
      // commentUser: this.comment.username,
      // currentUser: this.$store.state.username
    }
  },
  methods:{
    // getArticles(){
    //     this.$store.state.comments.forEach(comment => {
    //       if (this.currentUser === this.commentUser){
    //         // console.log(article)
    //         this.comments.push(comment)
    //       }
    //     })
    //   },

    getComments(){
        this.$store.dispatch('get_all_comments')
    }
  },
  created(){
    this.getComments()
  }
  
}
</script>

<style>

</style>