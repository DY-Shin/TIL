<template>
  <swiper-slide role="tab">
    <router-link 
      :to="{ 
            name: 'DetailView',
            params: { id: movie.id }
          }"
    >
      <div id="card">
        <img :src="imgUrl" alt="img">
        <div id="card-body">
          <!-- <h5>{{ movie.id }}</h5> -->
          <h4>{{ movie.title }}</h4>
        </div>
      </div>
    </router-link>
  </swiper-slide>
</template>

<script>
// import axios from 'axios'
// const API_URL = "http://127.0.0.1:8000"
import { swiperSlide } from 'vue-awesome-swiper'

export default {
  name: 'UserLikeItem',
  props: {
    movie: Object
  },
  components: {
    swiperSlide,
  },
  data() {
    return{
      imgUrl: `https://themoviedb.org/t/p/w300_and_h450_bestv2${this.movie.poster_path}`,
    }
  },
  methods: {
    getLike() {
      this.$store.dispatch('getlike')
    }
  },
  created() {
    this.getLike()
  }
}
</script>

<style>
#card-body {
  margin-top: 10px;
  margin-bottom: 30px;
  word-break: keep-all;
  min-height: 60px;
  }

a {
  /* color: black !important; */
  text-decoration: none !important;
}
#card {
  /* background-color: rgba( 255, 255, 255, 0.7 ); */
  color: white !important;
}
</style>