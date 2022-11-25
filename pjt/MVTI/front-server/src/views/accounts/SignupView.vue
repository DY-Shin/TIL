<template>
  <div>
    <img src="@/assets/MVTI.png" alt="#" width="300px">
    <h1>회원가입</h1>
    <form @submit.prevent="signup">
      <div class="col-4">
        <div class="mb-3">
          <label for="username" class="form-label">아이디</label>
          <input type="text" class="form-control" id="username" v-model="username" aria-describedby="emailHelp"><br>
          <div>
            <label for="email" class="form-label">이메일</label>
            <input type="text" class="form-control" id="email" v-model="email">
            <p class="validation-text" v-if="!isEmailValid && email">
                  <!-- 이메일 형식 및 입력란 공백 확인 -->
              <span class="warning">
                올바른 이메일 형식을 입력해 주세요.
              </span>
            </p>
          </div>
        </div>
  
        <div class="mb-3">
          <label for="password1" class="form-label">비밀번호</label>
          <input type="password" class="form-control" id="password1" v-model="password1">
          <p class="validation-text" v-if="!isPasswordValid && password1">
                <!-- 비밀번호 형식 및 입력란 공백 확인 -->
            <span class="warning">
              비밀번호는 총 8자 이상, 문자와 숫자를 1자 이상 포함해야 합니다.
            </span>
          </p>
        </div>
  
        <div class="mb-3">
          <label for="password2" class="form-label">비밀번호 확인</label>
          <input type="password" class="form-control" id="password2" v-model="password2">
        </div>
        <!-- <div class="mb-3 form-check">
          <input type="checkbox" class="form-check-input" id="exampleCheck1">
          <label class="form-check-label" for="exampleCheck1">Check me out</label>
        </div> -->
        <button type="submit" class="btn btn-primary">회원가입</button>
      </div>
    </form>
  </div>
</template>

<script>
import router from '@/router'
import { validateEmail } from '@/utils/validation';
import { validatePassword } from '@/utils/validation';
// import axios from 'axios'

export default {
  name: 'SingupView',
  data() {
    return {
      userpk: null,
      username: null,
      email: null,
      password1: null,
      password2: null,
    }
  },
  computed: {
    isEmailValid() {
      return validateEmail(this.email);
    },
    isPasswordValid() {
      return validatePassword(this.password1)
    }
  },
  methods: {
    signup() {
      const userpk = this.id
      const username = this.username
      const email = this.email
      const password1 = this.password1
      const password2 = this.password2
      console.log(this.id);

      const payload = {
        userpk,
        username,
        email,
        password1,
        password2
      }
      this.$store.dispatch('signUp', payload)
      router.push({name: 'MovieView' })
    }
  }
}
</script>

<style>
.warning {
  color: rgb(25, 106, 255);
}
</style>