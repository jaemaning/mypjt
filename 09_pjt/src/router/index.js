import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '../views/HomeView.vue'
import MovieView from '../views/MovieView'
import RandomView from '../views/RandomView'
import WatchListView from '../views/WatchListView'

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
    component: MovieView
  },
  {
    path: '/random',
    name: 'random',
    component: RandomView
    // component: () => import('../views/RandomView.vue')
  },
  {
    path: '/watch-list',
    name: 'watchList',
    component: WatchListView
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
