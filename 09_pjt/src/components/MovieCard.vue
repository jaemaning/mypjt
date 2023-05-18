<template>
  <div class="mx-auto d-flex justify-content-center">
    <div class="card" style="width: 18rem; border: none;">
    <img class="card-img-top" :src="srcURL" alt="Card image cap">
    <div class="card-body" style="background-color: darkslategray;">
      <h4>{{ getMovie.title }}</h4>
      <p class="card-text">{{ getMovie.overview }}</p>
    </div>
  </div>

    
  </div>
</template>

<script>
const imgURL = 'https://image.tmdb.org/t/p/original'

export default {
  name: 'MovieCard',
  data () {
    return {
      srcURL : imgURL + this.getMovie.poster_path
    }
  },
  props: {
    getMovie: Object
  }
}
</script>

<style>

.card {
  border: solid darkslategray;
  color: white;
}


</style>