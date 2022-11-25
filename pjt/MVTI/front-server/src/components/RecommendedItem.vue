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
          <h4><b>{{ movie.title }}</b></h4>
        </div>
      </div>
    </router-link>
  </swiper-slide>

</template>

<script>
import axios from 'axios'
import { swiperSlide } from 'vue-awesome-swiper'
const API_URL = "http://127.0.0.1:8000"

export default {
  name: 'RecommnededItem',
  props: {
    movie: Object,
  },
  components: {
    swiperSlide,
  },
  data() {
    return{
      imgUrl: null,
    }
  },
  created() {
    this.getMovieUrl()
  },
  methods: {
    getMovieUrl() {
      axios({
        method: 'get',
        url: `${API_URL}/api/v1/movies/${this.movie.id}/`,
      })
        .then((res) => {
          this.imgUrl = `https://themoviedb.org/t/p/w300_and_h450_bestv2${res.data?.poster_path}`
          // console.log(this.imgUrl)
        })
        .catch(err => console.log(err))
    }
  }
}
</script>

<style scoped>
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