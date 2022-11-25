<template>
  <div class="carousel-item">
    <router-link
      :to="{
        name: 'DetailView',
        params: { id: movie.id }
      }"  
    >
      <img :src="imgUrl" class="d-block w-70 mx-auto" alt="...">
      <div class="carousel-caption d-none d-md-block w-70 mx-auto">
        <div id="title" class="d-inline-flex">
          <h2><b>{{ this.movie.title }}</b></h2>
        </div>
        <!-- <br>
        <p>{{ this.movie.overview }}</p> -->
      </div>
    </router-link>
  </div>
</template>

<script>
import axios from 'axios'
const API_URL = "http://127.0.0.1:8000"

export default {
  name: 'CarouselItem',
  props: {
    movie: Object,
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
          this.imgUrl = `https://image.tmdb.org/t/p/original${res.data.backdrop_path}`
          // console.log(this.imgUrl)
        })
        .catch(err => console.log(err))
    }
  }
}
</script>

<style>
/* #title{
  -webkit-text-stroke-width: 0.2px;
  -webkit-text-stroke-color: black;
} */
.carousel-inner {
  width: auto;
  height: 800px; /* 이미지 높이 변경 */
}

.carousel-item {
  width: auto;
  height: 100%;
}

.d-block {
  display: block;
  width: auto;
  height: 100%;
}
</style>