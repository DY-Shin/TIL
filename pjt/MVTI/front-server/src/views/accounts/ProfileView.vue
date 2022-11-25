<template>
  <div id="profile">
    <br>
    
    <h3>
      <img src="@/assets/dia.gif" alt="img" width="80px">
      {{ username }}님의 프로필
      <img src="@/assets/dia.gif" alt="img" width="80px">
    </h3>
    <br>
    <div v-if="mvti_pk">
      <h5>당신의 유형은</h5>
      <h5>🎬{{ name }}🎬</h5> 
      <router-link :to="{ name: 'survey1' }"><h5>👉다시 검사하러가기</h5></router-link>
    </div>
    <div v-else>
      <h5>아직 MVTI 검사를 하지 않으셨군요!</h5>
      <router-link :to="{ name: 'survey1' }"><h5>MVTI 검사하고 나에게 맞는 영화 추천받기</h5></router-link>
    </div>
    <br>
    <div v-if="usercomments">
      <div class="fw-bold text-center text-white mt-5">
          <h4>코멘트 {{ usercomments.length }}개</h4>
      </div>
    </div>
    <div v-if="likemovie">
      <div class="fw-bold text-center text-white "></div>
        <h4>좋아요한 영화 {{ likemovie.length }}개</h4>
    </div>
    <br>
    <hr>
    <div class="mt-5">
      <b><h5>
        <!-- <img src="@/assets/heartviolet.gif" alt="img" width="30px"> -->
        {{ username }}님이 좋아한 영화
        <!-- <img src="@/assets/heartviolet.gif" alt="img" width="30px"> -->
      </h5></b>
      <br>
      <UserLike/>
    </div>
    <hr>
    <div class="mt-5">
      <b><h5>
        <!-- <img src="@/assets/heart.gif" alt="img" width="30px"> -->
        {{ username }}님이 남긴 리뷰
        <!-- <img src="@/assets/heart.gif" alt="img" width="30px"> -->
      </h5></b>
      <br>
      <UserComment/>
      <br>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import UserComment from '@/components/UserComment'
import UserLike from '@/components/UserLike'
const API_URL = "http://127.0.0.1:8000"

export default {
  name: 'ProfileView',
  components: {
    UserComment,
    UserLike
  },
  computed: {
    username() {
      return this.$store.state.username
    },
    usercomments() {
      return this.$store.state.usercomments
    },
    mvti_pk() {
      return this.$store.state.resultmvti
    },
    likemovie() {
      return this.$store.state.likemovie
    }
  },
  data () {
    return {
      comment: null,
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
  methods: {
    get_mvti() {
      axios({
        method: 'get',
        url: `${API_URL}/api/v1/movies/mvti/${this.mvti_pk}`
      })
      .then((res) => {
        this.pk = this.mvti_pk
        this.name = res.data.name
        this.genre1 = res.data.genre1
        this.genre2 = res.data.genre2
        this.genre3 = res.data.genre3
        this.genre4 = res.data.genre4
        this.genre5 = res.data.genre5
        // this.put_mvti()
        
        // console.log(this.pk);
        // console.log(this.imgUrl);
      })
      .catch((err) => console.log(err))
    },
  },
  
  created() {
    this.get_mvti()
  },
}
</script>

<style>
  #profile{
    color: white;
  }
</style>