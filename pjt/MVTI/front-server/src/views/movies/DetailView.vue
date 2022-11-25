<template>
  <div 
    :style="{ backgroundImage : `url(${backImgUrl})`}"
    style="background-size: cover; overflow: auto; background-attachment: fixed;"
  >
    <div class="d-flex flex-row justify-content-evenly flex-wrap">
      <!-- <h1>Detail</h1> -->
      <div class="col-12 col-lg-3">
        <div class="card mt-5" style="width: 20rem; margin: 0 auto;">
          <img :src="movieImgUrl" alt="movie_img">
        </div>
      </div>
      <div class="col-12 col-lg-7">
        <div class="card mt-5 text-start" id="body">
          <div class="card-body">
            <div class="card-header d-flex justify-content-between">
              <h1><b>{{ movie?.title }}</b></h1>
              <div v-if="!isLike">
                <h1>
                  <i class="bi bi-heart" @click="like" style="color:crimson;"></i>                
                </h1>
              </div>
              <div v-else>
                <h1>
                  <i class="bi bi-heart-fill" @click="like" style="color:crimson;"></i>
                </h1>
              </div>
            </div>
            <h5><b>{{ movie?.released_date }} | ⭐{{ movie?.vote_avg }}</b></h5>
            <!-- <p>{{ movie?.genres }}</p> -->
            <h3><b>개요</b></h3>
            <p><b>{{ movie?.overview }}</b></p>
            <h3><b>티저 영상</b></h3>
            <iframe :src="videoUrl" frameborder="0" width="640" height="360"></iframe>
          </div>
        </div>
        <div id="actorCard" class="text-align-center mt-3">
          <br>
          <h5><b>출연진</b></h5>
          <hr>
          <swiper 
            ref="filterSwiper" 
            :options="swiperOption" 
            role="tablist"
          >
            <ActorsList
              v-for="(actor, idx) in actorsData"
              :key="idx"
              :actor="actor"
            />
            <div class="swiper-button-prev" slot="button-prev"></div>
            <div class="swiper-button-next" slot="button-next"></div>
          </swiper>
        </div>
      </div>
    </div>
    <template v-if="isLogin">
      <div id="comment" style="width: 30rem; margin: 0 auto; background-color: black; color: white; justify-content-center" class="mt-5">
        <CommentList/>
      </div>
    </template>
  </div>
</template>

<script>
import axios from 'axios'
import CommentList from '@/components/CommentList.vue'
import ActorsList from '@/components/ActorsList.vue'
import { swiper } from 'vue-awesome-swiper'
import 'swiper/dist/css/swiper.min.css'

const API_URL = "http://127.0.0.1:8000"

export default {
  name: 'DetailView',
  components: {
    CommentList,
    ActorsList,
    swiper,
  },
  data() {
    return{
      movie: null,
      movieImgUrl: null,
      backImgUrl: null,
      videoUrl: null,
      actorsData: null,
      swiperOption: {
        slidesPerView: 7,
        slidesPerGroup: 3,
        spaceBetween: 6, // swiper-slide 사이의 간격 지정
        slidesOffsetBefore: 0, // slidesOffsetBefore는 첫번째 슬라이드의 시작점에 대한 변경할 때 사용
        slidesOffsetAfter: 0, // slidesOffsetAfter는 마지막 슬라이드 시작점 + 마지막 슬라이드 너비에 해당하는 위치의 변경이 필요할 때 사용
        freeMode: true, // freeMode를 사용시 스크롤하는 느낌으로 구현 가능
        centerInsufficientSlides: true, // 컨텐츠의 수량에 따라 중앙정렬 여부를 결정함
        navigation: {
          nextEl: ".swiper-button-next",
          prevEl: ".swiper-button-prev",
        },
      },
      isLike: null,
    }
  },
  computed: {
    isLogin() {
      return this.$store.getters.isLogin
    },
  },
  created() {
    this.getMovieDetail()
    this.getComments()
    this.get_like()
  },
  methods: {
    getMovieDetail() {
      axios({
        method: 'get',
        url: `${API_URL}/api/v1/movies/${this.$route.params.id}/`,
      })
      .then((res) => {
        // console.log(res)
        this.movie = res.data
        this.movieImgUrl = `https://themoviedb.org/t/p/w600_and_h900_bestv2${this.movie?.poster_path}`
        this.backImgUrl = `https://image.tmdb.org/t/p/original${this.movie?.backdrop_path}`
        this.videoUrl = `https://www.youtube.com/embed/${this.movie?.youtube_url}`
        this.actorsData = this.movie?.actors_data
        // console.log(this.actorsData)
      })
      .catch(err => console.log(err))
    },

    // 영화에 달린 코멘트 가져오기
    getComments(){
      const movieId = this.$route.params.id
      this.$store.dispatch('get_comments', movieId)
    },

    // 영화 좋아요
    like() {
      const movie_id = this.$route.params.id
      const bi = document.querySelector('.bi')
      axios({
        method: 'post',
        url: `${API_URL}/api/v1/movies/${this.$route.params.id}/like/${this.$store.state.userpk}/`,
        data: {
          movie_id
        },
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
        .then(() => {
          // console.log(res.data)
          // this.isLike = res.data
          this.$store.commit('GETLIKE', this.movie)
          if(this.isLike.likes) {
            bi.classList.remove('bi-heart')
            bi.classList.add('bi-heart-fill')
            this.isLike = !this.isLike
            // console.log('좋아요')
          }
          else {
            bi.classList.remove('bi-heart-fill')
            bi.classList.add('bi-heart')
            this.isLike = !this.isLike
            // console.log('취소')
          }
        })
        .catch((err) => {
          console.log(err);
        })
    },
    get_like() {
      const movie_id = this.$route.params.id
      axios({
        method: 'get',
        url: `${API_URL}/api/v1/movies/${this.$route.params.id}/like/${this.$store.state.userpk}/`,
        data: {
          movie_id
        },
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
        .then((res) => {
          // console.log(res.data.likes)
          this.isLike = res.data.likes
        })
        .catch((err) => {
          console.log(err);
        })
    }
  },
}
</script>

<style>
  #body {
    background-color: rgba( 255, 255, 255, 0.7 );
    color: black;
    background-size: cover;
  }
  #comment {
    background-color: white;
    border-radius: 20px;
  }
  #actorCard{
    background-color: rgba( 255, 255, 255, 0.7 );
    color: black;
  }
  .bi{
    cursor: pointer;
  }
</style>

<style lang="scss" scoped>
  .swiper-container {
    .swiper-wrapper {
      .swiper-slide {
        width: 'auto'; // auto 값을 지정해야 슬라이드의 width값이 텍스트 길이 기준으로 바뀜
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
        // cursor: pointer;
      }
    }
  }
</style>
