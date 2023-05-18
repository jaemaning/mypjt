<template>
  <div class="home" style="height: 100vh;">
    <div class="pt-4">
      <h1 class="teamjang">
        Hello I'm Jaeman Kim
      </h1>
      <h1 class="teamone">
        Hello I'm Minkuk Kim
      </h1>
    </div>
  </div>
</template>

<script>

export default {
  name: 'HomeView',
  components: {
    
  }
}
</script>

<style scoped>
  img {
    width: 100vw;
    height: 100vh;
  }

  .home {
    background-image: url("@/assets/giphy.gif");
  }

  .teamjang {
    color: white;
  }

  .teamone {
    color: black;
  }
</style>
