<template>
  <div>
    <h1>보고싶은 영화</h1>
    <input type="text" v-model="inputData" @keyup.enter="addMovie">
    <button @click="addMovie">Add</button>
  </div>
</template>

<script>
export default {
  name: 'WatchListForm',
  data () {
    return {
      inputData : '',

    }
  },
  methods : {

    addMovie() {
      if (this.inputData.length !== 0) {
        this.$store.commit('addMyList', this.inputData)
      }
      else {
        alert('제목을 입력해라.')
      }
      this.inputData = ''
    }
  }
}
</script>

<style>

h1 {
  color: white;
}

</style>