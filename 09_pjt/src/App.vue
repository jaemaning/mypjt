<template>
  <div id="app">
    <nav class="d-flex justify-content-between">
      <img src="@/assets/clapperboard-g52bdd4164_640.png" width="30" height="30" alt="">
      <div>
        <router-link :to="{name:'home'}">Home</router-link> |
        <router-link :to="{name:'movies'}">Movies</router-link> |
        <router-link :to="{name:'random'}">Random</router-link> |
        <router-link :to="{name:'watchList'}">WatchList</router-link>
      </div>
    </nav>
    <router-view/>

    <!-- <nav class="navbar bg-body-tertiary">
      <div class="container">
        <a class="navbar-brand" href="#">
          <img src="/docs/5.3/assets/brand/bootstrap-logo.svg" alt="Bootstrap" width="30" height="24">
        </a>
      </div>
    </nav> -->
  </div>
</template>

<script>
import axios from 'axios'

const API_KEY = process.env.VUE_APP_TMDB_API_KEY
const AXIOS_URL = `https://api.themoviedb.org/3/discover/movie?include_adult=false&include_video=false&language=ko-KR&page=1&sort_by=vote_average.desc&without_genres=99,10755&vote_count.gte=200&api_key=${API_KEY}`

const WEATHER_API_KEY = process.env.VUE_APP_WEATHER_API_KEY
const WEATHER_AXIOS_URL = `https://api.openweathermap.org/data/2.5/weather?q=Seoul&appid=${WEATHER_API_KEY}`

export default {
  name: 'APP',
  components: {
    
  },
  created() {
    axios({
      method: 'GET',
      url: AXIOS_URL,
    })
    .then((res)=>{
      console.log(res)
      this.$store.commit('pushMovieData', res.data)
    })
    .catch((err)=>{
      console.log(err)
    })

    axios({
      method: 'GET',
      url: WEATHER_AXIOS_URL,
    })
    .then((res)=>{
      this.$store.commit('pushWeatherData', res.data)
    })
    .catch((err)=>{
      console.log(err)
    })

    axios({
      method: 'GET',
      url: 'https://api.themoviedb.org/3/genre/movie/list?api_key=fe0cd3ae385a968eaa140d8955cf4804&language=ko-KR',
    })
    .then((res)=>{
      console.log(res)
      this.$store.commit('pushGenreData', res.data)
    })
    .catch((err)=>{
      console.log(err)
    })
  }
}

</script>

<style>
#app {
  font-family: 'Gowun Dodum', sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  background-image: url("@/assets/cinema-5069314_1920.jpg");
}

nav {
  padding: 10px;
  background-color: rgb(57, 150, 150);
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}
</style>
