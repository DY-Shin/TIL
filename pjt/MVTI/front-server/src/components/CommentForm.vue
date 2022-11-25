<template>
  <div>
    <p>{{ username }}님, 평점을 남겨보세요!</p>
    <!-- <fieldset class="rating">
      <input type="radio" id="star5" name="rating" value="5" v-model="movieScore"/><label class = "full" for="star5" title="Awesome - 5 stars"></label>
      <input type="radio" id="star4half" name="rating" value="4.5" v-model="movieScore"/><label class="half" for="star4half" title="Pretty good - 4.5 stars"></label>
      <input type="radio" id="star4" name="rating" value="4" v-model="movieScore"/><label class = "full" for="star4" title="Pretty good - 4 stars"></label>
      <input type="radio" id="star3half" name="rating" value="3.5" v-model="movieScore"/><label class="half" for="star3half" title="Meh - 3.5 stars"></label>
      <input type="radio" id="star3" name="rating" value="3" v-model="movieScore"/><label class = "full" for="star3" title="Meh - 3 stars"></label>
      <input type="radio" id="star2half" name="rating" value="2.5" v-model="movieScore"/><label class="half" for="star2half" title="Kinda bad - 2.5 stars"></label>
      <input type="radio" id="star2" name="rating" value="2" v-model="movieScore"/><label class = "full" for="star2" title="Kinda bad - 2 stars"></label>
      <input type="radio" id="star1half" name="rating" value="1.5" v-model="movieScore"/><label class="half" for="star1half" title="Meh - 1.5 stars"></label>
      <input type="radio" id="star1" name="rating" value="1" v-model="movieScore"/><label class = "full" for="star1" title="Sucks big time - 1 star"></label>
      <input type="radio" id="starhalf" name="rating" value="0.5" v-model="movieScore"/><label class="half" for="starhalf" title="Sucks big time - 0.5 stars"></label>
    </fieldset> -->
    <!-- <h2>Glowing Stars</h2> -->
    <div style="background:#000; padding-bottom:10px;" class="d-flex justify-content-center">
      <star-rating :increment="0.5" v-model="movieScore"></star-rating>
    </div>
    <br>
    <div>
      <input 
        type="text" 
        id="comment"
        v-model.trim="commentContent"
        @keyup.enter="createComment">
      <button type="submit" class="btn btn-primary ms-2" @click="createComment">Submit</button>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import StarRating from 'vue-star-rating'

const API_URL = "http://127.0.0.1:8000"

export default {
  name: 'CommentForm',
  data() {
    return {
      movieScore: 0,
      commentContent: null,
    }
  },
  components: {
    StarRating
  },
  computed: {
    username() {
      return this.$store.state.username
    },
  },
  methods: {
    createComment() {
      const content = this.commentContent
      const movie_id = this.$route.params.id
      const username = this.username
      const score = this.movieScore

      // console.log(username)
      // console.log(score)
      
      if (!content) {
        alert('내용을 입력해주세요')
        // return
        // console.log()
      } else {
        axios({
        method: 'post',
        url: `${API_URL}/api/v1/movies/${this.$route.params.id}/comments/`,
        data: {
          content,
          movie_id,
          username,
          score,
        },
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
      .then(() => {
        // console.log(res)
        this.$store.dispatch('get_comments', movie_id)
      })
      .catch((err) => {
        console.log(err)
      })
        
      }
      this.commentContent = null
      // this.score = null
      // console.log(this.$route.params)     
    }
  },
}
</script>

<style>

body {
  font-family: 'Raleway', sans-serif;
}

.custom-text {
  font-weight: bold;
  font-size: 1.9em;
  border: 1px solid #cfcfcf;
  padding-left: 10px;
  padding-right: 10px;
  border-radius: 5px;
  color: #999;
  background: #fff;
}
</style>