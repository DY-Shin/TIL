import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import createPersistedState from 'vuex-persistedstate'
import router from '@/router'
import _ from 'lodash'

Vue.use(Vuex)

const API_URL = "http://127.0.0.1:8000"

export default new Vuex.Store({
  state: {
    movies: [],
    recMovies: [],
    token: null,
    username: null,
    userpk: null,
    comments: null,
    allcomments: null,
    usercomments: null,
    mvtiscore1: [
      {'name': 'group1', 'score' : 0},
      {'name': 'group2', 'score' : 0},
      {'name': 'group3', 'score' : 0},
      {'name': 'group4', 'score' : 0},
      {'name': 'group5', 'score' : 0},
      {'name': 'group6', 'score' : 0},
      
    ],
    resultscore: [],
    resultname: [],
    resultmvti: null,
    likemovie: []
  },
  plugins: [
    createPersistedState(),
  ],
  getters: {
    isLogin(state) {
      return state.token ? true : false
    },
  },
  mutations: {
    GET_MOVIES(state, movies){
      state.movies = movies
    },

    SAVE_TOKEN(state, payload1) {
      state.token = payload1.token
      state.username = payload1.username
      state.userpk = payload1.userpk
      // router.push({name: 'MovieView' })
      // console.log(payload1.username)
    },

    LOGOUT(state){
      state.token = !state.token
      router.push({name: 'LoginView'})
    },


    // 댓글 가져오기
    GET_COMMENTS(state, data) {
      // console.log(data)
      state.comments = data
    },

    GET_ALL_COMMENTS(state, data) {
      state.allcomments = data
    },

    GET_USER_COMMENTS(state) {
      state.usercomments = state.allcomments.filter((comment) => {
        // console.log(state.usercomments);
        if (comment.username === state.username) {
          return comment
        }
      })
    },

    // 유형 검사
    TOGROUP1(state) {
      state.mvtiscore1[0].score += 1
      console.log(state.mvtiscore1)
    },
    TOGROUP2(state) {
      state.mvtiscore1[1].score += 1
      console.log(state.mvtiscore1)
    },
    TOGROUP3(state) {
      state.mvtiscore1[2].score += 1
      console.log(state.mvtiscore1)
    },
    TOGROUP4(state) {
      state.mvtiscore1[3].score += 1
      console.log(state.mvtiscore1)
    },
    TOGROUP5(state) {
      state.mvtiscore1[4].score += 1
      console.log(state.mvtiscore1)
    },
    TOGROUP6(state) {
      state.mvtiscore1[5].score += 1
      console.log(state.mvtiscore1)
    },

    GET_RESULT(state) {
      state.resultscore = _.sortBy(state.mvtiscore1, ['score']).reverse()
      state.resultscore = state.resultscore.splice(0, 3)
      state.resultscore = _.sortBy(state.resultscore, ['name'])
      // console.log(state.sortresult);
      for(let i=0; state.resultname.length < 3; i++){
        state.resultname.push(state.resultscore[i]['name']);
     }
      console.log(state.resultname);
      console.log(JSON.stringify(state.resultname))
      if (JSON.stringify(state.resultname) === '["group1","group2","group3"]') {
        state.resultmvti = 1
      } else if (JSON.stringify(state.resultname) === '["group1","group2","group4"]') {
        state.resultmvti = 2
      } else if (JSON.stringify(state.resultname) === '["group1","group4","group6"]') {
        state.resultmvti = 3
      } else if (JSON.stringify(state.resultname) === '["group1","group3","group6"]') {
        state.resultmvti = 4
      } else if (JSON.stringify(state.resultname) === '["group2","group3","group5"]') {
        state.resultmvti = 5
      } else if (JSON.stringify(state.resultname) === '["group2","group4","group5"]') {
        state.resultmvti = 6
      } else if (JSON.stringify(state.resultname) === '["group3","group5","group6"]') {
        state.resultmvti = 7
      } else if (JSON.stringify(state.resultname) === '["group4","group5","group6"]') {
        state.resultmvti = 8
      }
      console.log(state.resultmvti);
    },

    RESET_MVTI (state) {
      state.mvtiscore1[0].score = 0
      state.mvtiscore1[1].score = 0
      state.mvtiscore1[2].score = 0
      state.mvtiscore1[3].score = 0
      state.mvtiscore1[4].score = 0
      state.mvtiscore1[5].score = 0
      state.resultscore = []
      state.resultname = []

    },
    GETUSER (state, data) {
      state.userpk = data.pk
    },
    GETLIKE (state, data) {
      state.likemovie = data
      // console.log(state.likemovie);
    },
    GET_REC_MOVIES(state, recMovies) {
      state.recMovies = recMovies
    }
  },
  actions: {
    getUser(context) {
      axios({
        method: 'get',
        url: `${API_URL}/accounts/user/`,
        headers: {
          Authorization: `Token ${context.state.token}`
        }
      })
        .then((res) => {
          console.log(res)
          console.log('================================');
          context.commit('GETUSER', res.data)
        })
        .catch((err) => {
          console.log(err)
        })
    },
    getMovies(context){
      axios({
        method: 'get',
        url: `${API_URL}/api/v1/movies/`,
      })
        .then(res=> {
          // console.log(res, context)
          context.commit('GET_MOVIES', res.data)
        })
        .catch(err => console.log(err))
    },

    signUp(context, payload) {
      axios({
        method: 'post',
        url: `${API_URL}/accounts/signup/`,
        data: {
          userpk: payload.userpk,
          username: payload.username,
          email: payload.email,
          password1: payload.password1,
          password2: payload.password2,
        }
      })
        .then((res) => {
          console.log(payload)
          const payload1 = {
            token : res.data.key,
            username : payload.username,
            userpk : payload.userpk
          }
          context.commit('SAVE_TOKEN', payload1)
        })
        .catch(err => {
          console.log(err)
          alert('다시 시도해주세요!')})
      },

    logIn(context, payload) {
      axios({
        method: 'post',
        url: `${API_URL}/accounts/login/`,
        data: {
          username: payload.username,
          password: payload.password,
        }
      })
      .then((res) => {
        // console.log(res)
        const payload1 = {
          token : res.data.key,
          username : payload.username
        }
        context.commit('SAVE_TOKEN', payload1)
        router.push({name: 'MovieView' })
        context.dispatch('getUser')
        console.log();
      })
      .catch((err) => {
        console.log(err)
        alert('다시 시도해주세요!')
      })
    },

    get_comments(context, movieId) {
      console.log(movieId);
      axios({
        method: 'get',
        url: `${API_URL}/api/v1/movies/${movieId}/comments/`,
      })
      .then((res) => {
        // console.log(res);
        context.commit('GET_COMMENTS', res.data)
        
      })
      .catch(err => console.log(err))
    },

    get_all_comments(context) {
      axios({
        method: 'get',
        url: `${API_URL}/api/v1/comments/`,
      })
      .then((res) => {
        context.commit('GET_ALL_COMMENTS', res.data)
        context.commit('GET_USER_COMMENTS')
        // console.log(res)
      })
      .catch(err => console.log(err))
    },

    get_user_comments(context) {
      context.commit('GET_USER_COMMENTS')
    },

    get_result(context) {
      context.commit('GET_RESULT')
    },

    // likeMovie(context) {
    //   axios({
    //     method: 'get',
    //     url: `${API_URL}/api/v1/comments/`,
    //   })
    //   .then((res) => {
    //     context.commit('LIKE_MOVIE', res.data)
    //     // console.log(res)
    //   })
    //   .catch(err => console.log(err))
    // },

    reset_mvti(context) {
      context.commit('RESET_MVTI')
    },

    getlike(context) {
      axios({
        method: 'get',
        url: `${API_URL}/api/v1/movies/like/${context.state.userpk}/`,
        headers: {
          Authorization: `Token ${context.state.token}`
        }
      })
        .then((res) => {
          // console.log(res);
          context.commit('GETLIKE', res.data)
        })
        .catch((err) => {
          console.log(err)
        })
    },

    getRecMovies(context) {
      axios({
        method: 'get',
        url: `${API_URL}/api/v1/movies/recommendation/${this.state.resultmvti}/`,
      })
        .then(res=> {
          // console.log(res, context)
          context.commit('GET_REC_MOVIES', res.data)
        })
        .catch(err => console.log(err))
    }
  },
  modules: {
  }
})