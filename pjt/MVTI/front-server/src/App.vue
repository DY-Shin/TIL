<template>
  <div id="app">
    <nav class="navbar navbar-expand-lg bg-dark fixed-top">
      <div class="container-fluid">
        <router-link class="navbar-brand" :to="{ name: 'MovieView' }">
          <img src="@/assets/MVTI.png" alt="#" width="100px">
        </router-link>
        <ul class="navbar-nav">
          <template v-if="isLogin">
            <li class="nav-item">
              <span class="username">환영합니다, 
                <router-link :to="{ name: 'ProfileView', params: { username: username } }">
                  {{ $store.state.username }}
                </router-link>님!
              </span>
            </li>
              <button class="btn btn-primary" @click="Logout">로그아웃</button>
          </template>
          <template v-else>
            <li class="nav-item">
              <router-link :to="{ name: 'LoginView' }">로그인</router-link>
            </li>
            <li class="nav-item">
              <router-link :to="{ name: 'SignupView' }">회원가입</router-link>
            </li>
          </template>
        </ul>
      </div>
    </nav>
    <router-view/>
  </div>
</template>

<script>
export default {
  data() {
    return {
    }
  },
  computed: {
    username() {
      return this.$store.state.username
    },
    isLogin() {
      return this.$store.getters.isLogin
    }
  },
  methods: {
    Logout() {
      this.$store.commit('LOGOUT')
    },
    // 새창 () {
    //   localStorage.setItem('vuex', sessionStorage.getItem('vuex')) // vuex session to local
    // }
  },
  // beforeCreate () {
  //   let localVuex = localStorage.getItem('vuex') // local storage에 vuex 저장여부 확인
  //   if (localVuex) { // 저장되어 있는 경우 session storage로 이동 후 local 제거
  //     localVuex = JSON.parse(localVuex)
  //     // this.$store.commit('setXXX', localVuex.xxx)
  //     localStorage.removeItem('vuex') 
  //   }
  // },
}
</script>

<style>
@font-face {
  font-family:'SeoulNamsanB';
  src: url('@/fonts/SeoulNamsanB.ttf');
  /* font-weight: 400; */
}

#app {
  /* font-family: Avenir, Helvetica, Arial, sans-serif; */
  font-family: 'SeoulNamsanB';
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  background-color: black;
  padding-top: 5.4rem;
  min-height: 969px;
}



nav {
  padding: 30px;
  color: white;
}

nav a {
  font-weight: bold;
  color: white;
}

nav a.router-link-exact-active {
  color: #0080ff;
}

.nav-item {
  margin: 7px;
}
</style>
