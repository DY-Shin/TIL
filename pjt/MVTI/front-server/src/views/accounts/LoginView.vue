<template>
  <div>
    <img src="@/assets/MVTI.png" alt="#" width="300px">
    <h1>로그인</h1>
    <form @submit.prevent="logIn">
      <div class="col-4">

        <div class="mb-3">
          <label for="username" class="form-label">아이디</label>
          <input type="text" class="form-control" id="username" v-model="username" aria-describedby="emailHelp">
        </div>
        <div class="mb-3">
          <label for="password" class="form-label">비밀번호</label>
          <input type="password" class="form-control" id="password" v-model="password">
        </div>
        <!-- <div class="mb-3 form-check">
          <input type="checkbox" class="form-check-input" id="exampleCheck1">
          <label class="form-check-label" for="exampleCheck1">Check me out</label>
        </div> -->
        <button type="submit" class="btn btn-primary">로그인</button>
      </div>
    </form>
    <span>회원이 아니신가요? <router-link :to="{ name: 'SignupView' }">회원가입하기</router-link></span>
  </div>
</template>

<script>
// import router from '@/router'
// import validateEmail from ''
// import axios from 'axios'
// const API_URL = "http://127.0.0.1:8000"

export default {
  name: 'LogInView',
  data() {
    return {
      username: null,
      password: null,
      error: null,
    }
  },
  methods: {

    logIn() {
      const username = this.username
      const password = this.password

      const payload = {
        username,
        password
      }
      this.$store.dispatch('logIn', payload)
    },
    
  }
}
</script>

<style>
form {
  /* width: 500px; */
  display: flex;
  justify-content: center;
  text-align: start;
}
</style>