<template>
  <div style="height: 100vh;">
    <div class='container mt-4'>
      <h1 class="mb-5">{{ weather }} 한 날씨엔 이런 영화 어때요 ?</h1>
      <button @click="get_random" class="btn btn-success mb-2">PICK</button>
      <div class="card" style="width: 18rem; margin:auto;background-color: darkslategray;">
        <img v-if="imageURL" class="card-img-top" :src="'https://image.tmdb.org/t/p/original/'+imageURL" alt="Card image cap">
        <div class="card-body">
          <h5>{{ random_movie?.title }}</h5>
        </div>
      </div>
    </div>
  </div>
</template>

<script>

export default {
  name: 'RandomView',
  data () {
    return {
      imageURL : null
    }
    
  },
  
  computed : {
    weather() {
      return this.$store.state.weatherData
    },
    random_movie() {
      return this.$store.state.random_movie
    },
    all_movies () {
      return this.$store.state.moviesData
    }

  },
  methods : {
    getImageURL(){
        this.imageURL = this.random_movie?.poster_path
    },
    get_random() {
      this.$store.commit('random_pick')
      this.imageURL = this.random_movie?.poster_path
      // this.genre_weather[this.weather].forEach(num => {
      //   this.all_movies.forEach(movie => {
      //     if (movie.genre_ids.includes(num)) {
      //       this.filter_movies.push(movie)
      //     }
      //   })
      // })
      // // console.log("filter", filter_movies)

      // // 날씨 연관 시키고 싶었음
      // // console.log(this.weatherList.indexOf(this.weather))
      // // this.all_movies.forEach(element => {
      // //   if (element.genre_ids.includes(this.weatherList.indexOf(this.weather))){
      // //     this.myMoviesList.push(element)
      // //   }
      // // })
      // this.random_movie = _.sample(this.filter_movies)
      // console.log(this.random_movie)
      
    },
    // random_pick() {
    //   this.$store.commit('random_pick')
    // }
  },

  created () {
    this.$store.commit('random_pick')
    this.getImageURL()
    // this.all_movies = this.$store.state.moviesData
    // if (this.all_movies) {
    // this.genre_weather[this.weather].forEach(num => {
    //     this.all_movies.forEach(movie => {
    //       if (movie.genre_ids.includes(num)) {
    //         this.filter_movies.push(movie)
    //       }
    //     })
    //   })
    // this.random_movie = _.sample(this.filter_movies)
    // // this.random_movie = _.sample(this.all_movies)
    // console.log(this.random_movie)
    // }
  }
}
</script>

<style>
.container {
  color: white;
}

.img {
  width: 100%;
}

</style>