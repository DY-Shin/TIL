<template>
  <div id="result" class="mt-auto">
    <br>
    <h3>축하드립니다! ❰{{ name }}❱ 유형이시군요!</h3>
    <router-link :to="{ name: 'MovieView'}">
      <button class="btn btn-outline-primary" type="button">{{ username }}님의 취향 영화 보러가기</button>
    </router-link>
    <div id="image" class="d-flex justify-content-center mt-3">
      <span v-if="mvti_pk === 1">
        <img src="@/assets/mvti1.jpg" alt="img">
      </span>
      <span v-if="mvti_pk === 2">
        <img src="@/assets/mvti2.jpg" alt="img">
      </span>
      <span v-if="mvti_pk === 3">
        <img src="@/assets/mvti3.jpg" alt="img">
      </span>
      <span v-if="mvti_pk === 4">
        <img src="@/assets/mvti4.jpg" alt="img">
      </span>
      <span v-if="mvti_pk === 5">
        <img src="@/assets/mvti5.jpg" alt="img">
      </span>
      <span v-if="mvti_pk === 6">
        <img src="@/assets/mvti6.jpg" alt="img">
      </span>
      <span v-if="mvti_pk === 7">
        <img src="@/assets/mvti7.jpg" alt="img">
      </span>
      <span v-if="mvti_pk === 8">
        <img src="@/assets/mvti8.jpg" alt="img">
      </span>
    </div>
    
    <!-- 영화 목록 좌르륵 -->

  </div>
</template>

<script>
import axios from 'axios'
const API_URL = "http://127.0.0.1:8000"

export default {
  name: 'MvtiResult',
  computed: {
    username() {
      return this.$store.state.username
    },
    mvti_pk() {
      return this.$store.state.resultmvti
    },
    imgUrl(){
      return `@/assets/mvti${this.pk}.jpg`
    },
    userpk() {
      return this.$store.state.userpk
    }
    
  },
  data() {
    return {
      name: null,
      genre1: null,
      genre2: null,
      genre3: null,
      genre4: null,
      genre5: null,
      pk: null,
      id: null,
      
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
        this.put_mvti()
        
        // console.log(this.pk);
        // console.log(this.imgUrl);
      })
      .catch((err) => console.log(err))
    },
    getUser() {
      axios({
        method: 'get',
        url: `${API_URL}/accounts/user/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
        .then((res) => {
          this.id = res.data.pk
          console.log(this.id)
        })
        .catch((err) => {
          console.log(err)
        })
    },
    put_mvti() {
      // this.userid = this.id
      console.log(this.id);
      axios({
        method: 'post',
        url: `${API_URL}/userinfo/${this.id}/mvti/${this.mvti_pk}/`
      })
      .then(() => {
        this.mvti = this.mvti_pk
        this.$store.dispatch('reset_mvti')
      })
      .catch((err) => console.log(err))
    }
  },
  created() {
    this.getUser()
    this.get_mvti()
  }
  
}
</script>

<style>
#image img {
  width: 700px;
}
#result{
  color: white;
}
</style>