import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '../views/HomeView.vue'
import LoginView from '../views/LoginView.vue'
import SignupView from '../views/SignupView.vue'
import GameView from '../views/GameView'
import MovieDetailView from '../views/MovieDetailView'
import MypageView from '../views/MypageView'
import YourpageView from '../views/YourpageView'
import SearchListView from '../views/SearchListView'
import RecommendView from '../views/RecommendView'
import NotFound404 from '../views/NotFound404'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/movies',
    name: 'movies',
    component: () => import(/* webpackChunkName: "about" */ '../views/MoviesView.vue')
  },
  {
    path: '/login',
    name: 'login',
    component: LoginView
  },
  {
    path: '/signup',
    name: 'signup',
    component: SignupView
  },
  {
    path: '/game',
    name: 'game',
    component: GameView
  },
  {
    path: '/movies/:pk',
    name: 'movie',
    component: MovieDetailView
  },
  {
    path: '/mypage',
    name: 'mypage',
    component: MypageView
  },
  {
    path: '/yourpage/:pk',
    name: 'yourpage',
    component: YourpageView
  },
  {
    path: '/searchlist/:data',
    name: 'searchlist',
    component: SearchListView
  },
  {
    path: '/recommend/:index',
    name: 'recommend',
    component: RecommendView
  },


  {
    path: "/404",
    name: 'NotFound404',
    component: NotFound404

  },
  {
    path : "*",
    redirect : "/404"
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
