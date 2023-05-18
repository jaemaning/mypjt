<template>
  <div>
    <div style="color:white; margin-top: 10px;" v-for="(movie,idx) in getMyList" :key="idx"
    @click="cancel(idx)" :class="{canceled : movie.is_wanted}">{{ movie.movie }}</div>
  </div>
</template>

<script>
export default {
  name: 'WatchListItem',
  computed : {
    getMyList() {
      return this.$store.state.myMovieList
    }
  },
  methods : {
    cancel(id) {
      console.log(id)
      this.$store.commit('cancel', id)
    }
  }
}
</script>

<style>
  .canceled {
    text-decoration :line-through;
  }


</style>