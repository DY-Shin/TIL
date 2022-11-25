import Vue from 'vue'
import VueRouter from 'vue-router'
import MovieView from '@/views/movies/MovieView'
import DetailView from '@/views/movies/DetailView'
import SignupView from '@/views/accounts/SignupView'
import LoginView from '@/views/accounts/LoginView'
import ProfileView from '@/views/accounts/ProfileView'
import survey1View from '@/views/mvti/survey/survey1View'
import survey2View from '@/views/mvti/survey/survey2View'
import survey3View from '@/views/mvti/survey/survey3View'
import survey4View from '@/views/mvti/survey/survey4View'
import survey5View from '@/views/mvti/survey/survey5View'
import survey6View from '@/views/mvti/survey/survey6View'
import survey7View from '@/views/mvti/survey/survey7View'
import survey8View from '@/views/mvti/survey/survey8View'
import survey9View from '@/views/mvti/survey/survey9View'
import MvtiResult from '@/views/mvti/MvtiResult'


Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'MovieView',
    component: MovieView
  },

  
  {
    path: '/signup',
    name: 'SignupView',
    component: SignupView,
  },
  
  {
    path: '/login',
    name: 'LoginView',
    component: LoginView,
  },

  {
    path: '/user/:username',
    name: 'ProfileView',
    component: ProfileView,
  },
  
  {
    path: '/survey1',
    name: 'survey1',
    component: survey1View,
  },
  {
    path: '/survey2',
    name: 'survey2',
    component: survey2View,
  },
  {
    path: '/survey3',
    name: 'survey3',
    component: survey3View,
  },
  {
    path: '/survey4',
    name: 'survey4',
    component: survey4View,
  },
  {
    path: '/survey5',
    name: 'survey5',
    component: survey5View,
  },
  {
    path: '/survey6',
    name: 'survey6',
    component: survey6View,
  },
  {
    path: '/survey7',
    name: 'survey7',
    component: survey7View,
  },
  {
    path: '/survey8',
    name: 'survey8',
    component: survey8View,
  },
  {
    path: '/survey9',
    name: 'survey9',
    component: survey9View,
  },
  {
    path: '/MvtiResult',
    name: 'MvtiResult',
    component: MvtiResult,
  },
  {
    path: '/:id',
    name: 'DetailView',
    component: DetailView,
  },
  
  ]
      
const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router