import Vue from 'vue'
import Vuex from 'vuex'
import _ from 'lodash'
import createPersistedState from 'vuex-persistedstate'

Vue.use(Vuex)

export default new Vuex.Store({
  plugins: [
    createPersistedState(),
  ],
  state: {
    moviesData: null,
    myMovieList : [],
    weatherData: null,
    genresData : null,
    genre_weather : {
      Clouds : [16, 10402, 10770],
      Rain : [27, 53, 878],
      Mist : [10752, 10751, 37],
      Clear : [35, 28, 18],
      Haze : [12, 80, 14],
      Snow : [99, 36, 9648, 10749]
      },
    filter_movies : [],
    random_movie : null,
  },
  getters: {
  },
  mutations: {
    pushMovieData(state, data) {
      state.moviesData = data.results
      console.log(state.moviesData)
    },
    addMyList(state, movie) {
      state.myMovieList.push({movie: movie, is_wanted:false})
    },
    cancel(state, id) {
      console.log(id)
      state.myMovieList[id].is_wanted = !state.myMovieList[id].is_wanted
    },
    pushWeatherData(state, data) {
      state.weatherData = data.weather[0].main
      console.log(state.weatherData)
    },
    pushGenreData(state, data) {
      state.genresData = data.genres
      console.log(state.genresData)
    },
    random_pick(state) {
      state.genre_weather[state.weatherData].forEach(num => {
          state.moviesData.forEach(movie => {
            if (movie.genre_ids.includes(num)) {
              state.filter_movies.push(movie)
            }
          })
        })
      state.random_movie = _.sample(state.filter_movies)
      console.log("random", state.random_movie)
    }
  },
  actions: {

  },
  modules: {
  }
})
