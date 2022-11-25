<template>
  <div class="text-start">
    <!-- <table class="table table-sm">
      <thead>
        <tr>
          <th scope="col">#</th>
          <th scope="col">Movie</th>
          <th scope="col">Score</th>
          <th scope="col">Content</th>
          <th scope="col">Username</th>
        </tr>
      </thead> -->
      <!-- <tbody>
        <tr>
          <th scope="row">{{ comment.pk }}</th>
          <th scope="row">
            <router-link :to="{
                    name: 'DetailView',
                    params: { id: comment.movie }
                  }">{{ comment.moviename }}</router-link>
          </th>
          <th scope="row">{{ comment.score }}</th>
          <th scope="row">{{ comment.content }}</th>
          <th scope="row">{{ comment.username }}</th>
        </tr>

      </tbody>
    </table> -->
    <ul class="list-group list-group-horizontal d-flex justify-content-center">
      <li class="list-group-item">💘</li>
      <li class="list-group-item"><router-link :to="{
                    name: 'DetailView',
                    params: { id: comment.movie }
                  }">{{ comment.moviename }}</router-link></li>
      <li class="list-group-item">{{ comment.score }}</li>
      <li class="list-group-item">{{ comment.content }}</li>
      <li class="list-group-item">{{ comment.username }}</li>
    </ul>
  </div>
</template>

<script>
// import axios from 'axios'
// const API_URL = "http://127.0.0.1:8000"

export default {
  name: 'UserCommentItem',
  props: {
    comment: Object,
  },
  data() {
    return {
    }
  },
  computed: {
    username() {
      // console.log(this.$store.state.username)
      return this.$store.state.username
    },
  },
    
  methods:{
    get_all_comments(){
      this.$state.dispatch('get_all_comments')
    },

    getComments(){
      this.$state.dispatch('get_user_comments')
    },
  },
  created(){
    this.get_all_comments()
    this.getComments()
  }
}

</script>

<style>

</style>