<template>
  <div class="movie-list text-center">
    <div id="carouselExampleCaptions" class="carousel slide" data-bs-ride="carousel">
      <div class="carousel-inner">
        <div v-if="isLogin" class="carousel-item active">
          <router-link :to="{ name: 'survey1' }">
            <img src="@/assets/banner.jpg" class="d-block w-70 mx-auto" alt="...">
          </router-link>
        </div>
        <div v-else class="carousel-item active">
          <router-link :to="{ name: 'LoginView' }">
            <img src="@/assets/banner.jpg" class="d-block w-70 mx-auto" alt="...">
          </router-link>
        </div>
        <CarouselItem
          v-for="movie in sampleMovies"
          :key="movie.id"
          :movie="movie"
        />
      </div>
      <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide="prev">
        <span class="carousel-control-prev-icon" aria-hidden="true"></span>
        <span class="visually-hidden">Previous</span>
      </button>
      <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide="next">
        <span class="carousel-control-next-icon" aria-hidden="true"></span>
        <span class="visually-hidden">Next</span>
      </button>
    </div>
    <br>
    <br>
    <div v-if="isLogin && mvti_id">
      <h1>❰{{ name }}❱ 유형인 당신을 위한 추천 영화</h1>
      <swiper 
        ref="filterSwiper" 
        :options="swiperOption" 
        role="tablist"
      >
        <RecommendedItem
          v-for="movie in recMovies"
          :key="movie.id"
          :movie="movie"
        />
        <div class="swiper-button-prev" slot="button-prev"></div>
        <div class="swiper-button-next" slot="button-next"></div>
      </swiper>
    </div>
    <h1>Movie List</h1>
    <swiper 
      ref="filterSwiper" 
      :options="swiperOption" 
      role="tablist"
    >
      <MovieListItem
        v-for="movie in movies"
        :key="movie.id"
        :movie="movie"
      />
      <div class="swiper-button-prev" slot="button-prev"></div>
      <div class="swiper-button-next" slot="button-next"></div>
    </swiper>
  </div>
</template>
<script>
import MovieListItem from '@/components/MovieListItem'
import RecommendedItem from '@/components/RecommendedItem'
import CarouselItem from '@/components/CarouselItem'
import _ from 'lodash'
import { swiper } from 'vue-awesome-swiper'
import 'swiper/dist/css/swiper.min.css'
import axios from 'axios'
const API_URL = "http://127.0.0.1:8000"

export default {
  name: 'MovieList',
  components: {
    MovieListItem,
    swiper,
    CarouselItem,
    RecommendedItem,
  },
  data () {
    return {
      name: null,
      swiperOption: {
        slidesPerView: 'auto',
        slidesPerGroup: 4,
        spaceBetween: 6, // swiper-slide 사이의 간격 지정
        slidesOffsetBefore: 0, // slidesOffsetBefore는 첫번째 슬라이드의 시작점에 대한 변경할 때 사용
        slidesOffsetAfter: 0, // slidesOffsetAfter는 마지막 슬라이드 시작점 + 마지막 슬라이드 너비에 해당하는 위치의 변경이 필요할 때 사용
        freeMode: true, // freeMode를 사용시 스크롤하는 느낌으로 구현 가능
        centerInsufficientSlides: true, // 컨텐츠의 수량에 따라 중앙정렬 여부를 결정함
        navigation: {
          nextEl: ".swiper-button-next",
          prevEl: ".swiper-button-prev",
        },
      }
    }
  },
  computed: {
    movies() {
      return this.$store.state.movies
    },
    sampleMovies(){
      return _.sampleSize(this.$store.state.movies, 5)
    },
    isLogin(){
      return this.$store.getters.isLogin
    },
    mvti_id(){
      return this.$store.state.resultmvti
    },
    recMovies(){
      return this.$store.state.recMovies
    }
  },
  methods: {
    get_mvti() {
      axios({
        method: 'get',
        url: `${API_URL}/api/v1/movies/mvti/${this.$store.state.resultmvti}`
      })
      .then((res) => {
        this.name = res.data.name
      })
      .catch((err) => console.log(err))
    },
  },
  created() {
    this.get_mvti()
  },
}
</script>
<style lang="scss" scoped>
.movie-list {
  text-align: start;
  color: white;
  background-color: black;
}

.swiper-container {
  .swiper-wrapper {
    .swiper-slide {
      width: 300px; // auto 값을 지정해야 슬라이드의 width값이 텍스트 길이 기준으로 바뀜
      min-width: 56px; // min-width를 지정하지 않을 경우 텍스트가 1개 내지는 2개가 들어갈 때 탭 모양이 상이할 수 있으므로 넣어준다.
      padding: 0px;
      font-size: 14px;
      line-height: 36px;
      text-align: center;
      color: #84868c;
      border: 0;
      border-radius: 18px;
      // background: #f3f4f7;
      appearance: none;
      cursor: pointer;
    }
  }
}
</style>