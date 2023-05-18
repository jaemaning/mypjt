<template>
  <div class="container mt-4">
    <div class="row row-cols-1 row-cols-md-3 g-4 d-flex">
      <MovieCard class="col mx-auto" v-for="(movie, idx) in getMovies" :key="idx" :get-movie="movie"/>
    </div>
  </div>
</template>

<script>
import MovieCard from '@/components/MovieCard.vue';

export default {
  name: 'MovieView',
  components: {
    MovieCard
  },
  computed: {
    getMovies() {
      return this.$store.state.moviesData
    }
  },
}
</script>

<style>

</style>